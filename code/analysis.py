import glob 
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from utils_analysis import ttest
from utils_analysis import count_morphemes
from utils_analysis import create_pointplot, create_boxplot

# DEFINE LANGUAGE AND CONDITION OF EXPERIMENT ('english' OR 'french'; 'pseudo' OR 'real')
language, condition = 'english', 'pseudo'

# READ IN TRIALLISTS
df_roots = pd.read_csv(f'../experimental_design/{language}_{condition}/r.csv')

path = f'../subject_data/{language}_{condition}'
csv_files = glob.glob(path + '/*.csv')
df_pilot = pd.concat((pd.read_csv(file) for file in csv_files), ignore_index = True)[5:-1]

# ADD WORDLENGTH AND NUMBER OF MORPHEMES
df_pilot['wordlength'] = df_pilot['first'].str.len()
df_pilot['num_morphemes'] = df_pilot['condition'].apply(count_morphemes)

# ADD TYPE ('TARGET' OR 'CONTROL') 
root_list, permuted_root_list = [list(df_roots[col]) for col in ['Root', 'PermutedRoot']]
df_pilot['type'] = df_pilot['root'].apply(lambda x: 'target' if x in root_list else 'control' if x in permuted_root_list else None)

# CALCULATE ERROR RATE
df_pilot['error_rate'] = 1 - df_pilot['correct']
n = len(df_pilot)


# REMOVE OUTLIERS
z_score = ['encoding_time', 'rt']
for var in z_score:
    df_pilot = df_pilot[abs(stats.zscore(df_pilot[var])) <= 3]

# FILTER OUT PARTICIPANTS WITH <0.5 ACCURACY
df_accuracy = df_pilot.groupby('ID')['correct'].mean().reset_index()
df_accuracy = df_accuracy[df_accuracy['correct'] >= 0.5]
df_pilot_outliers = pd.merge(df_pilot, df_accuracy[['ID']], on='ID')

num_outliers = n - len(df_pilot_outliers)
print(f'Number of outliers removed: {num_outliers}')

# FILTER DATAFRAME (ONLY USE CORRECT TRIALS)
df_correct = df_pilot_outliers.query('correct == True')

# PLOTS
for plot_info in [('type', 'error_rate', df_pilot_outliers, 'Type', 'Error Rate'), 
                  ('type', 'rt', df_correct, 'Type', 'Reaction Time'), 
                  ('type', 'encoding_time', df_correct, 'Type', 'Encoding Time')]:
    create_boxplot(*plot_info)

for plot_info in [('wordlength', 'rt', 'Number of Characters', 'Reaction Time', (0, 4000)), 
                  ('num_morphemes', 'rt', 'Number of Morphemes', 'Reaction Time', (0, 4000)), 
                  ('wordlength', 'encoding_time', 'Number of Characters', 'Encoding Time', (0, 4000)), 
                  ('num_morphemes', 'encoding_time', 'Number of Morphemes', 'Encoding Time', (0, 4000)), 
                  ('wordlength', 'error_rate', 'Number of Characters', 'Error Rate', None), 
                  ('num_morphemes', 'error_rate', 'Number of Morphemes', 'Error Rate', None)]:
    create_pointplot(df_pilot_outliers, *plot_info)

# ENCODING TIME, RT, AND ERROR-RATE AS A FUNCTION OF TYPE (TARGET VS CONTROL)
# MEDIAN, MEAN, AND SD
for variable in ['encoding_time', 'rt']:
    df_grouped = df_correct.groupby('type')['encoding_time'].agg(['median', 'mean', 'std'])
    print(df_grouped)

# ERROR RATE
df_grouped = df_pilot_outliers.groupby('type')['error_rate'].agg(['median', 'mean', 'std'])
print(df_grouped)

# ENCODING TIME, RT, AND ERROR-RATE AS A FUNCTION OF WORDLENGTH AND NUMBER OF MORPHEMES (MEANS & MEDIANS)
for variable in ['encoding_time', 'rt']:
    for grouping_variable in ['wordlength', 'num_morphemes']:
        df_grouped = df_correct.groupby(grouping_variable)[variable].agg(['median', 'mean', 'std'])
        print(f' {variable} as a function of {grouping_variable}: {df_grouped}')


# ERROR RATE AS A FUNCTION OF NUMBER OF CHARACTERS AND NUMBER OF MORPHEMES (MEANS & MEDIANS)
for grouping_variable in ['wordlength', 'num_morphemes']:
    df_grouped = df_pilot_outliers.groupby(grouping_variable)['error_rate'].agg(['median', 'mean', 'std'])
    print(f'Error rate as a function of {grouping_variable}: {df_grouped}')


# T-TEST (EQUAL WORDLENGTH, DIFFERENT NUMBER OF MORPHEMES)
ttest_args = [(8, 2, 3), (10, 3, 4), (9, 2, 4)] # wl, n_morph1, n_morph2
for args in ttest_args:
    ttest(df_pilot_outliers, wl=args[0], n_morph1=args[1], n_morph2=args[2])


# CHECK PREREQUISITS FOR REGRESSION MODELS
# CHECK FOR NORMALITY OF RESIDUALS USING A QQ PLOT 
sm.qqplot(df_correct['rt'], line='s')
sm.qqplot(df_correct['encoding_time'], line='s')
sm.qqplot(df_pilot_outliers['error_rate'], line='s')

# CHECK FOR HONOGENEITY OF VARIANCE USING LEVENE'S TEST
stat, p = stats.levene(df_correct[df_correct['type']=='target']['rt'], df_correct[df_correct['type']=='control']['rt'])
print("Levene's test for RT: statistic =", stat, ", p-value =", p)

stat, p = stats.levene(df_correct[df_correct['type']=='target']['encoding_time'], df_correct[df_correct['type']=='control']['encoding_time'])
print("Levene's test for encoding time: statistic =", stat, ", p-value =", p) # significant!!

stat, p = stats.levene(df_pilot_outliers[df_pilot_outliers['type']=='target']['error_rate'], df_pilot_outliers[df_pilot_outliers['type']=='control']['error_rate'])
print("Levene's test for error rate: statistic =", stat, ", p-value =", p)

# CREATE REGRESSION MODELS
model_rt = ols('rt ~ type', data=df_correct).fit()
model_encoding_time = ols('encoding_time ~ type', data=df_correct).fit()
model_error_rate = ols('error_rate ~ type', data=df_pilot_outliers).fit()

# PRINT SUMMARY OF THE MODELS
print(model_rt.summary())
print(model_encoding_time.summary())
print(model_error_rate.summary())

