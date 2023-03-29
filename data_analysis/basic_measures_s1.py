# BACIC MEASURES FIGURE + T-TEST (S1)
import glob 
import pandas as pd
import scipy.stats as stats
from utils_analysis import count_morphemes
from utils_analysis import create_boxplot

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

# REMOVE OUTLIERS
df_filtered = df[(abs(stats.zscore(df[['encoding_time', 'rt']])) <= 3).all(axis=1)]
df_filtered = df.groupby('ID').filter(lambda x: x['correct'].mean() >= 0.5)
rt_mean = df_filtered.query('correct == True')['rt'].mean()
rt_std = df_filtered.query('correct == True')['rt'].std()
df_filtered = df_filtered.groupby('ID').filter(lambda x: x['correct'].mean() >= 0.5 and x['rt'].mean() >= rt_mean - 3*rt_std)

print(f'Number of outliers removed: {len(df) - len(df_filtered)}')


# DATAFRAME WITH MEAN ERRORRATE PER PARTICIPANT
mean_error_rate = df_filtered.groupby(['ID', 'target_type'])['error_rate'].mean()
df_mean_error_rate = pd.DataFrame({'ID': mean_error_rate.index.get_level_values('ID'), 
                                   'target_type': mean_error_rate.index.get_level_values('target_type'), 
                                   'mean_error_rate': mean_error_rate.values})

# PLOTS
for plot_info in [('target_type', 'mean_error_rate', df_mean_error_rate, 'Type', 'Mean Error Rate', (0, 0.2), ['Control', 'Target']), 
                  ('target_type', 'rt', df_filtered.query('correct == True'),'Type', 'Reaction Time', (0, 5000), ['Control', 'Target']), 
                  ('target_type', 'encoding_time', df_filtered.query('correct == True'), 'Type', 'Encoding Time', (0,5000), ['Control', 'Target'])]:
    create_boxplot(*plot_info)


# ENCODING TIME, RT, AND ERROR-RATE AS A FUNCTION OF TYPE (TARGET VS CONTROL)
# MEDIAN, MEAN, AND SD
for variable in ['encoding_time', 'rt']:
    print(f"{variable}: {df_filtered.query('correct == True').groupby('target_type')[variable].agg(['median', 'mean', 'std'])}")

print(f"Error Rate: {df_filtered.groupby('target_type')['error_rate'].agg(['median', 'mean', 'std'])}")


# Perform t-tests to determine significant differences between target and control trials
for variable in ['rt', 'encoding_time']:
    target = df_filtered.query("target_type == 'target' and correct == True")[variable]
    control = df_filtered.query("target_type == 'control' and correct == True")[variable]
    t, p = stats.ttest_ind(target, control)
    print(f"{variable.capitalize()}: t = {t:.2f}, p = {p:.4f}")

target_er = df_filtered.groupby(['ID', 'target_type'])['error_rate'].mean().reset_index().query("target_type == 'target'")['error_rate']
control_er = df_filtered.groupby(['ID', 'target_type'])['error_rate'].mean().reset_index().query("target_type == 'control'")['error_rate']
t, p = stats.ttest_ind(target_er, control_er)
print(f"Error Rate: t = {t:.2f}, p = {p:.4f}")
