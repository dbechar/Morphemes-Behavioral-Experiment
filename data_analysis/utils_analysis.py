import glob 
import pandas as pd
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def load_df (language, condition):
    # READ IN TRIALLISTS
    path = f'../subject_data/{language}_{condition}'
    csv_files = glob.glob(path + '/*.csv')
    df = pd.concat((pd.read_csv(file) for file in csv_files), ignore_index = True)
    df = df.dropna(subset = ['condition'])
    # ADD NUMBER OF MORPHEMES
    df['num_morphemes'] = df['condition'].apply(count_morphemes)
    # CALCULATE ERROR RATE
    df['error_rate'] = 1 - df['correct']
    df['wordlength'] = df['wordlength'].astype(int)
    return df

def remove_outliers (df):
    df_filtered = df[(abs(stats.zscore(df[['encoding_time', 'rt']])) <= 3).all(axis=1)]
    df_filtered = df.groupby('ID').filter(lambda x: x['correct'].mean() >= 0.5)
    rt_mean = df_filtered.query('correct == True')['rt'].mean()
    rt_std = df_filtered.query('correct == True')['rt'].std()
    df_filtered = df_filtered.groupby('ID').filter(lambda x: x['correct'].mean() >= 0.5 and x['rt'].mean() >= rt_mean - 3*rt_std)
    print(f'Number of outliers removed: {len(df) - len(df_filtered)}')
    return df_filtered


def count_morphemes(condition):
    return len(condition.replace('_long', ''))

def create_boxplot(x, y, data, xlabel, ylabel, ylim, xticks = None, hue=None):
    ax = sns.boxplot(x=x, y=y, data=data, hue=hue, palette=['r', 'g'])
    sns.despine()
    ax.set_ylim(ylim)
    ax.set_xlabel(xlabel, fontdict={'size': 14, 'weight': 'bold'})
    ax.set_ylabel(ylabel, fontdict={'size': 14, 'weight': 'bold'})
    if xticks != None: 
        ax.set_xticklabels(xticks, fontsize = 10)
    plt.show()
    

def create_pointplot(data, x_var, y_var, x_label, y_label, y_lim, xticks=None, order=None, models=None):
    plot = sns.pointplot(data=data, x=x_var, y=y_var, hue='target_type', hue_order=['target', 'control'], 
                         palette=['g', 'r'], order=order, errorbar='se')
    
    if models is not None:
        for i, model in enumerate(models):
            x_range = data[x_var].unique()
            y_range = model.params[0] + model.params[1] * x_range
            
            sns.lineplot(x=x_range, y=y_range, color='k', ax=plot, label=f'Model {i+1}')
    
    plot.set_xlabel(x_label, fontdict={'size': 14, 'weight': 'bold'})
    plot.set_ylabel(y_label, fontdict={'size': 14, 'weight': 'bold'})
    plot.set(ylim=y_lim)
    
    if xticks is not None:
        plot.set_xticklabels(xticks, fontsize=10)
    
    green_patch = mpatches.Patch(color='g', label='Label1')
    red_patch = mpatches.Patch(color='r', label='Label2')
    plot.legend(title='Type', labels=['Target', 'Control'], handles=[green_patch, red_patch])   
    
    plt.show()


def ttest (df, wl, n_morph1, n_morph2, variable):
    # Filter data for the given word length and numbers of morphemes
    df_n_morph1 = df.loc[(df['wordlength'] == wl) & (df['num_morphemes'] == n_morph1)].copy()
    df_n_morph2 = df.loc[(df['wordlength'] == wl) & (df['num_morphemes'] == n_morph2)].copy()

    # Calculate error-rates for each group
    df_n_morph1[variable] = pd.to_numeric(df_n_morph1[variable])
    df_n_morph2[variable] = pd.to_numeric(df_n_morph2[variable])

    # Perform t-test
    t, p = stats.ttest_ind(df_n_morph1[variable], df_n_morph2[variable])
    
    print(f"T-test results for {variable} with wordlength {wl} and number of morphemes {n_morph1} vs. {n_morph2}: t = {t:.4f}, p = {p:.4f}")
    

def error_position(df):
    df_error = df.copy().query('is_error == 1')
    
    for index, error_row in df_error.iterrows():
        if error_row['error_to_which_morpheme'] == 'p':
            prefix_index = 1 if int(error_row['i_morpheme']) == 0 else 0
            prefix_str = error_row['prefixes'].split('_')[prefix_index-1]
            if len(prefix_str) < 3:
                df_error.drop(index, inplace=True)
                continue
                
            if int(error_row['i_morpheme']) == 0 and int(error_row['i_within_morpheme']) == 0:
                position = 'word_boundary' if error_row['i_within_morpheme'] == 0 else 'morpheme_boundary'
            else:
                position = 'morpheme_boundary' if error_row['i_within_morpheme'] == 0 or error_row['i_within_morpheme'] == len(prefix_str)-1 else 'within_morpheme'
                
        elif error_row['error_to_which_morpheme'] == 'r':
            count_prefix = error_row['condition'].count('p')
            count_suffix = error_row['condition'].count('s')
            
            if count_prefix == 0:
                if error_row['i_within_morpheme'] == 0:
                    position = 'word_boundary'
                elif error_row['i_within_morpheme'] == len(error_row['root'])-1:
                    position = 'word_boundary' if count_suffix == 0 else 'morpheme_boundary'
                else:
                    position = 'within_morpheme'
            else:
                if error_row['i_within_morpheme'] == 0:
                    position = 'morpheme_boundary'
                elif error_row['i_within_morpheme'] == len(error_row['root'])-1:
                    position = 'morpheme_boundary' if count_suffix != 0 else 'word_boundary'
                else:
                    position = 'within_morpheme'
        
        elif error_row['error_to_which_morpheme'] == 's':
            suffix_str = error_row['suffixes'].split('_')[int(error_row['i_morpheme'])]
            if len(suffix_str) < 3:
                df_error.drop(index, inplace=True)
                continue
            
            if error_row['condition'].count('s') == error_row['i_morpheme'] + 1:
                position = 'word_boundary' if error_row['i_within_morpheme'] == len(suffix_str)-1 else ('morpheme_boundary'if error_row['i_within_morpheme'] == 0 else 'within_morpheme')
            else: 
                position = 'morpheme_boundary' if error_row['i_within_morpheme'] == 0 or error_row['i_within_morpheme'] == len(suffix_str)-1 else 'within_morpheme'
                    

        df_error.loc[index, 'error_position'] = position
        
    return df_error

