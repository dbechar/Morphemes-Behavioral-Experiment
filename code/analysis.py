import glob 
import pandas as pd
import scipy.stats as stats
import statsmodels.formula.api as smf
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

# FILTER DATAFRAME (ONLY USE CORRECT TRIALS)
df_correct = df_pilot.query('correct == True')

# REMOVE OUTLIERS
z_score_columns = ['encoding_time', 'rt']
for col in z_score_columns:
    df_pilot = df_pilot[abs(stats.zscore(df_pilot[col])) <= 3]

# FILTER OUT PARTICIPANTS WITH <0.5 ACCURACY
df_accuracy = df_pilot.groupby('ID')['correct'].mean().reset_index()
df_accuracy = df_accuracy[df_accuracy['correct'] >= 0.5]
df_pilot_filtered = pd.merge(df_pilot, df_accuracy[['ID']], on='ID')

num_outliers_removed = n - len(df_pilot)
print(f'Number of outliers removed: {num_outliers_removed}')

# PLOTS
for plot_info in [('type', 'error_rate', df_pilot_filtered, 'Type', 'Error Rate'), 
                  ('type', 'rt', df_correct, 'Type', 'Reaction Time'), 
                  ('type', 'encoding_time', df_correct, 'Type', 'Encoding Time')]:
    create_boxplot(*plot_info)

for plot_info in [('wordlength', 'rt', 'Number of Characters', 'Reaction Time', (0, 4000)), 
                  ('num_morphemes', 'rt', 'Number of Morphemes', 'Reaction Time', (0, 4000)), 
                  ('wordlength', 'encoding_time', 'Number of Characters', 'Encoding Time', (0, 4000)), 
                  ('num_morphemes', 'encoding_time', 'Number of Morphemes', 'Encoding Time', (0, 4000)), 
                  ('wordlength', 'error_rate', 'Number of Characters', 'Error Rate', None), 
                  ('num_morphemes', 'error_rate', 'Number of Morphemes', 'Error Rate', None)]:
    create_pointplot(df_pilot_filtered, *plot_info)

# ENCODING TIME, RT, AND ERROR-RATE AS A FUNCTION OF WORDLENGTH AND NUMBER OF MORPHEMES (MEANS & MEDIANS)
for variable in ['encoding_time', 'rt']:
    for grouping_variable in ['wordlength', 'num_morphemes']:
        df_grouped = df_correct.groupby(grouping_variable)[variable].agg(['median', 'mean'])
        print(df_grouped)


# ERROR RATE AS A FUNCTION OF NUMBER OF CHARACTERS AND NUMBER OF MORPHEMES (MEANS & MEDIANS)
for grouping_variable in ['wordlength', 'num_morphemes']:
    df_grouped = df_pilot.groupby(grouping_variable)['error_rate'].agg(['median', 'mean'])
    print(df_grouped)


# T-TEST (EQUAL WORDLENGTH, DIFFERENT NUMBER OF MORPHEMES)
ttest_args = [(8, 2, 3), (10, 3, 4), (9, 2, 4)] # wl, n_morph1, n_morph2

for args in ttest_args:
    ttest(df_pilot, wl=args[0], n_morph1=args[1], n_morph2=args[2])
    

# REGRESSION MODELS
# CHECK PREREQUISITS


# CREATE MODEL
model = smf.ols(formula = 'rt ~ num_morphemes + wordlength + C(trial_type)', data=df_correct).fit()
print(model.summary())