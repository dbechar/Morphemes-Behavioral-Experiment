import pandas as pd
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


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
    
def create_pointplot(data, x_var, y_var, x_label, y_label, y_lim, xticks = None, order=None):
    plot = sns.pointplot(data=data, x=x_var, y=y_var, hue='target_type', hue_order = ['target', 'control'], 
                         palette=['g', 'r'], order=order, errorbar=('se'))
    plot.set_xlabel(x_label, fontdict={'size': 14, 'weight': 'bold'})
    plot.set_ylabel(y_label, fontdict={'size': 14, 'weight': 'bold'})
    plot.set(ylim=y_lim)
    if xticks != None:
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
    

def error_position (df):
    df_error = df.copy().query('is_error == 1')
    
    """
    # Drop rows with prefix or suffix less than 3 characters
    for index, error_row in df_error.iterrows():
        if error_row['error_to_which_morpheme'] == 'p':
            prefix_num = int(error_row['i_morpheme'])
            if prefix_num == 0:
                prefix_index = 1
            else:
                prefix_index = 0
            prefix_str = error_row['prefixes'].split('_')[prefix_index-1]
            if len(prefix_str) < 3:
                df_error.drop(index, inplace=True)
        elif error_row['error_to_which_morpheme'] == 's':
            suffix_num = int(error_row['i_morpheme'])
            suffix_str = error_row['suffixes'].split('_')[suffix_num]
            if len(suffix_str) < 3:
                df_error.drop(index, inplace=True)
    """
    # Determine position of error
    for index, error_row in df_error.iterrows():
        if error_row['error_to_which_morpheme'] == 'p':
            prefix_num = int(error_row['i_morpheme'])
            if prefix_num == 0:
                prefix_index = 1
            else:
                prefix_index = 0
                
            if int(error_row['i_morpheme']) == 0 and int(error_row['i_within_morpheme']) == 0: 
                if error_row['i_within_morpheme'] == 0:
                    position = 'word_boundary'
                elif error_row['i_within_morpheme'] == len(error_row['prefixes'].split('_')[prefix_index-1])-1:
                    position = 'morpheme_boundary'
                else:
                    position = 'within_morpheme'
            else:
                if error_row['i_within_morpheme'] == 0:
                    position = 'morpheme_boundary'
                elif error_row['i_within_morpheme'] == len(error_row['prefixes'].split('_')[prefix_index-1])-1:
                    position = 'morpheme_boundary'
                else:
                    position = 'within_morpheme'
        
        elif error_row['error_to_which_morpheme'] == 'r':
            
            count_prefix = 0
            count_suffix = 0
            for char in error_row['condition']:
                if char == 'p':
                    count_prefix += 1
                for char in error_row ['condition']:
                    if char == 's':
                        count_suffix +=1
            
            if count_prefix != 0: 
              if error_row['i_within_morpheme'] == 0:
                  position = 'morpheme_boundary'
                  
              elif error_row['i_within_morpheme'] == len(error_row['root'])-1:
                  if count_suffix == 0: 
                      position = 'word_boundary'
                  else: 
                      position = 'morpheme_boundary'
              else:
                  position = 'within_morpheme'
            
            else: 
                if error_row['i_within_morpheme'] == 0:
                    position = 'word_boundary'
                elif error_row['i_within_morpheme'] == len(error_row['root'])-1:
                    if count_suffix == 0: 
                        position = 'word_boundary'
                    else: 
                        position = 'morpheme_boundary' 
                else:
                    position = 'within_morpheme'
            

        elif error_row['error_to_which_morpheme'] == 's':
            count = 0
            for char in error_row['condition']:
                if char == 's':
                    count += 1
            if count == error_row['i_morpheme'] + 1: 
                if error_row['i_within_morpheme'] == 0:
                    position = 'morpheme_boundary' 
                elif error_row['i_within_morpheme'] == len(error_row['suffixes'].split('_')[int(error_row['i_morpheme'])])-1: 
                    position = 'word_boundary'
                else:
                    position = 'within_morpheme'
            else: 
                if error_row['i_within_morpheme'] == 0:
                    position = 'morpheme_boundary'
                elif error_row['i_within_morpheme'] == len(error_row['suffixes'].split('_')[int(error_row['i_morpheme'])])-1:
                    position = 'morpheme_boundary'
                else:
                    position = 'within_morpheme'
        
        df_error.loc[index, 'error_position'] = position
        
    return df_error
