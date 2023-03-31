import pandas as pd
import scipy.stats as stats
from utils_analysis import create_boxplot
from utils_analysis import load_df, remove_outliers

# DEFINE LANGUAGE AND CONDITION OF EXPERIMENT ('english' OR 'french'; 'pseudo' OR 'real')
language, condition = 'english', 'pseudo'

# READ IN TRIALLISTS
df = load_df (language, condition)
print (df['ID'].nunique()) # number of participants

# REMOVE OUTLIERS
df_filtered = remove_outliers(df)

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
