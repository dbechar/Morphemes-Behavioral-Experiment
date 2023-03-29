import pandas as pd
from statsmodels.formula.api import ols
from utils_analysis import load_df, remove_outliers
from utils_analysis import create_pointplot, create_boxplot
from utils_analysis import ttest

# DEFINE LANGUAGE AND CONDITION OF EXPERIMENT ('english' OR 'french'; 'pseudo' OR 'real')
language, condition = 'english', 'pseudo'

# READ IN TRIALLISTS
df = load_df (language, condition)

# REMOVE OUTLIERS
df_filtered = remove_outliers(df)

# PLOT 
for plot_info in [(df_filtered.query('correct == True'),'wordlength', 'rt', 'Number of Characters', 'Reaction Time', (0, 6000)), 
                  (df_filtered.query('correct == True'),'num_morphemes', 'rt', 'Number of Morphemes', 'Reaction Time', (0, 6000)), 
                  (df_filtered.query('correct == True'), 'wordlength', 'encoding_time', 'Number of Characters', 'Encoding Time', (0,7000)), 
                  (df_filtered.query('correct == True'), 'num_morphemes', 'encoding_time', 'Number of Morphemes', 'Encoding Time', (0, 7000)), 
                  (df_filtered, 'wordlength', 'error_rate', 'Number of Characters', 'Error Rate', (0, 0.9)), 
                  (df_filtered, 'num_morphemes', 'error_rate', 'Number of Morphemes', 'Error Rate', (0, 0.9))]:
    create_pointplot(*plot_info)
    
# ENCODING TIME, RT, AND ERROR-RATE AS A FUNCTION OF WORDLENGTH AND NUMBER OF MORPHEMES (MEANS & MEDIANS)
for variable in ['encoding_time', 'rt']:
    for grouping_variable in ['wordlength', 'num_morphemes']:
        df_grouped = df_filtered.query('correct == True').groupby(grouping_variable)[variable].agg(['median', 'mean', 'std'])
        print(f' {variable} as a function of {grouping_variable}: {df_grouped}')


# ERROR RATE AS A FUNCTION OF NUMBER OF CHARACTERS AND NUMBER OF MORPHEMES (MEANS & MEDIANS)
for grouping_variable in ['wordlength', 'num_morphemes']:
    df_grouped = df_filtered.groupby(grouping_variable)['error_rate'].agg(['median', 'mean', 'std'])
    print(f'Error rate as a function of {grouping_variable}: {df_grouped}')


# T-TEST (RT ~ EQUAL WORDLENGTH, DIFFERENT NUMBER OF MORPHEMES)
word_lencon = df_filtered.query('correct == True').groupby("num_morphemes")["wordlength"].value_counts()
print (word_lencon)

# DATAFRAME WITH MEAN ERRORRATE PER PARTICIPANT
mean_error_rate = df_filtered.groupby(['ID', 'wordlength', 'num_morphemes'])['error_rate'].mean()
df_mean_error_rate = pd.DataFrame({'ID': mean_error_rate.index.get_level_values('ID'), 
                                   'mean_error_rate': mean_error_rate.values,
                                   'wordlength': mean_error_rate.index.get_level_values ('wordlength'),
                                   'num_morphemes': mean_error_rate.index.get_level_values ('num_morphemes')
                                   })


ttest_args = [(11, 2, 5), (12,3,5), (10,3,4)] # wl, n_morph1, n_morph2
for args in ttest_args:
    for var in ['rt', 'encoding_time']:
        ttest(df_filtered.query('correct == True'), wl=args[0], n_morph1=args[1], n_morph2=args[2], variable = var)
        df_plot = df_filtered.query('correct == True')[(df_filtered.query('correct == True')['wordlength'] == args[0]) & ((df_filtered.query('correct == True')['num_morphemes'] == args[1]) | (df_filtered.query('correct == True')['num_morphemes'] == args[2]))]
        create_boxplot (x = 'num_morphemes', y = var, data = df_plot, xlabel = f'Number of Morphemes (Wordlength:{args[0]})', ylabel = f'{var.capitalize()}', ylim = (0,4000))
""" 
for args in ttest_args: 
        ttest(df_filtered, wl=args[0], n_morph1=args[1], n_morph2=args[2], variable = 'error_rate')
        df_plot = df_mean_error_rate[(df_mean_error_rate['wordlength'] == args[0]) & ((df_mean_error_rate['num_morphemes'] == args[1]) | (df_mean_error_rate['num_morphemes'] == args[2]))]
        create_boxplot (x = 'num_morphemes', y = 'mean_error_rate', data = df_plot, xlabel = f'Number of Morphemes (Wordlength:{args[0]})', ylabel = 'Mean Error Rate', ylim = (0, 1))
"""       

# CREATE REGRESSION MODELS 
mod_rt = ols('rt ~ wordlength * target_type', data=df_filtered.query('correct == True')).fit()
mod_encoding_time = ols('encoding_time ~ wordlength * target_type', data=df_filtered.query('correct == True')).fit()
#mod_error_rate = ols('error_rate ~ wordlength * target_type', data=df_filtered).fit()

# PRINT SUMMARY OF THE MODELS
#print(mod_rt.summary())
#print(mod_encoding_time.summary())
#print(mod_error_rate.summary())