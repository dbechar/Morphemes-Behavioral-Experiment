import glob 
import pandas as pd
import seaborn as sns

# DEFINE LANGUAGE OF EXPERIMENT ("english" OR "french")
language = 'english'
condition = 'pseudo'

# READ IN TRIALLISTS
df_roots = pd.read_csv(f'../experimental_design/{language}_{condition}/r.csv')
path = f'../subject_data/{language}_{condition}'
csv_files = glob.glob(path + '/*.csv')
df_list = (pd.read_csv(file) for file in csv_files)

subjectdata = pd.concat (df_list, ignore_index = True)
subjectdata['wordlength'] = subjectdata['first'].str.len()
subjectdata = subjectdata[5:-1]

# ADD NUMBER OF MORPHEMES
def count_morphemes(condition):
    return len(condition.replace('_long', ''))

subjectdata['number_of_morphemes'] = subjectdata['condition'].apply(count_morphemes)

# ADD TYPE ('TARGET' OR 'CONTROL')
root_list, permuted_root_list = list(df_roots['Root']), list(df_roots['PermutedRoot'])
subjectdata['type'] = subjectdata['root'].apply(lambda x: 'target' if x in root_list else 'control' if x in permuted_root_list else None)

# FILTER DATAFRAME (ONLY USE CORRECT TRIALS)
df_correct = subjectdata.copy().loc[subjectdata['correct'] == True]
false_count = subjectdata['correct'].value_counts()[False]


# ENCODING TIME AS A FUNCTION OF WORDLENGTH
# CALCULATE MEAN AND MEDIAN
et_wl_stats = df_correct.groupby('wordlength')['encoding_time'].agg(['median', 'mean'])
print(et_wl_stats)
# PLOT
sns.pointplot(data = df_correct, x = 'wordlength', y = 'encoding_time', hue= 'type')


# ENCODING TIME AS A FUNCTION OF NUMBER OF MORPHEMES
df_correct_target = df_correct.loc[df_correct['type'] == 'target']
et_nom_stats = df_correct_target.groupby('number_of_morphemes')['encoding_time'].agg(['median', 'mean'])
print (et_nom_stats)
# PLOT
sns.pointplot (data = df_correct_target, x = 'number_of_morphemes', y = 'encoding_time')


# REACTION TIME AS A FUNCTION OF WORDLENGTH
rt_wl_stats = df_correct.groupby('wordlength')['rt'].agg(['median', 'mean'])
print(rt_wl_stats)
# PLOT

# REACTION TIME AS A FUNCTION OF NUMBER OF MORPHEMES
rt_nom_stats = df_correct.groupby('number_of_morphemes')['rt'].agg(['median', 'mean'])
print(rt_nom_stats)
# PLOT


# ERROR-RATE AS A FUCNTION OF WORDLENGTH
er_wl = subjectdata.groupby('wordlength')['correct'].mean()
print (er_wl)
# PLOT 


# ERROR-RATE AS A FUNCTION OF NUMBER OF MORPHEMES
er_nom = subjectdata.groupby('number_of_morphemes')['correct'].mean()
print (er_nom)
# PLOT 


# T-TEST (EQUAL WORDLENGTH, DIFFERENT NUMBER OF MORPHEMES)