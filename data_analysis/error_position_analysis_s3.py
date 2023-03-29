# ERROR POSITION ANALYSIS
# Change error-position analysis: word boundary, morpheme boundary (that is not at word boundary), else.
# Another plot for error analysis: split based on whether the error is in an affix or root

# PERFORMANCE VS WORDLENGTH/NUMBER OF MORPHEMES (S2)
import glob 
import pandas as pd
import scipy.stats as stats
from utils_analysis import count_morphemes
from utils_analysis import create_pointplot
from utils_analysis import error_position

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

# POSITION OF ERROR WITHIN MORPHEME
# ONLY USE TRIALS WITH ERROR IN AFFIX THAT IS LONGER THAN 2 LETTERS
df_error = error_position(df_filtered)

# PLOTS 
for plot_info in [('error_position', 'error_rate', 'Error Position Within Word', 'Error Rate', 
                   None, ['Within Morpheme', 'Morpheme Boundary', ' Word Boundary']), 
                  ('error_position', 'rt', 'Error Position Within Word', 'Reaction Time',
                  (0, 1500), ['Within Morpheme', 'Morpheme Boundary', ' Word Boundary'])]:
    create_pointplot(df_error, *plot_info,  order = ['within_morpheme', 'morpheme_boundary','word_boundary'])