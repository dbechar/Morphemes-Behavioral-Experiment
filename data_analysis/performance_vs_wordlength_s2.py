# PERFORMANCE VS WORDLENGTH/NUMBER OF MORPHEMES (S2)
import glob 
import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols
from utils_analysis import count_morphemes
from utils_analysis import create_pointplot, create_boxplot
from utils_analysis import ttest

# DEFINE LANGUAGE AND CONDITION OF EXPERIMENT ('english' OR 'french'; 'pseudo' OR 'real')
language, condition = 'english', 'pseudo'

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

# REMOVE OUTLIERS
df_filtered = df[(abs(stats.zscore(df[['encoding_time', 'rt']])) <= 3).all(axis=1)]
df_filtered = df.groupby('ID').filter(lambda x: x['correct'].mean() >= 0.5)
rt_mean = df_filtered.query('correct == True')['rt'].mean()
rt_std = df_filtered.query('correct == True')['rt'].std()
df_filtered = df_filtered.groupby('ID').filter(lambda x: x['correct'].mean() >= 0.5 and x['rt'].mean() >= rt_mean - 3*rt_std)

print(f'Number of outliers removed: {len(df) - len(df_filtered)}')

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

ttest_rt = [(12, 3, 5), (14, 4, 6), (12,2,4)] # wl, n_morph1, n_morph2
for args in ttest_rt:
    ttest(df_filtered, wl=args[0], n_morph1=args[1], n_morph2=args[2], variable = 'rt')
    df_plot = df_filtered.query('correct == True')[(df_filtered.query('correct == True')['wordlength'] == args[0]) & ((df_filtered.query('correct == True')['num_morphemes'] == args[1]) | (df_filtered.query('correct == True')['num_morphemes'] == args[2]))]
    create_boxplot (x = 'num_morphemes', y = 'rt', data = df_plot, xlabel = f'Number of Morphemes (Wordlength:{args[0]})', ylabel = 'Reaction Time', ylim = (0,3000))

ttest_et = [(10, 2, 4), (10, 3, 4), (7,2,3)]
for args in ttest_et: 
    ttest(df_filtered, wl=args[0], n_morph1=args[1], n_morph2=args[2], variable = 'encoding_time')
    df_plot = df_filtered.query('correct == True')[(df_filtered.query('correct == True')['wordlength'] == args[0]) & ((df_filtered.query('correct == True')['num_morphemes'] == args[1]) | (df_filtered.query('correct == True')['num_morphemes'] == args[2]))]
    create_boxplot (x = 'num_morphemes', y = 'encoding_time', data = df_plot, xlabel = f'Number of Morphemes (Wordlength:{args[0]})', ylabel = 'Encoding Time', ylim = (0,3000))



# CREATE REGRESSION MODELS 
mod_rt = ols('rt ~ wordlength * target_type', data=df_filtered.query('correct == True')).fit()
mod_encoding_time = ols('encoding_time ~ wordlength * target_type', data=df_filtered.query('correct == True')).fit()
#mod_error_rate = ols('error_rate ~ wordlength * target_type', data=df_filtered).fit()

# PRINT SUMMARY OF THE MODELS
#print(mod_rt.summary())
#print(mod_encoding_time.summary())
#print(mod_error_rate.summary())