from utils_analysis import load_df, remove_outliers
from utils_analysis import create_pointplot
from utils_analysis import error_position

# DEFINE LANGUAGE AND CONDITION OF EXPERIMENT ('english' OR 'french'; 'pseudo' OR 'real')
language, condition = 'english', 'pseudo'

# READ IN TRIALLISTS
df = load_df (language, condition)

# REMOVE OUTLIERS
df_filtered = remove_outliers(df)

# POSITION OF ERROR WITHIN MORPHEME
# ONLY USE TRIALS WITH ERROR IN AFFIX THAT IS LONGER THAN 2 LETTERS
df_error = error_position(df_filtered)

# PLOTS 
for plot_info in [('error_position', 'error_rate', 'Error Position Within Word', 'Error Rate', 
                   None, ['Within Morpheme', 'Morpheme Boundary', ' Word Boundary']), 
                  ('error_position', 'rt', 'Error Position Within Word', 'Reaction Time',
                  (0, 1500), ['Within Morpheme', 'Morpheme Boundary', ' Word Boundary'])]:
    create_pointplot(df_error, *plot_info,  order = ['within_morpheme', 'morpheme_boundary','word_boundary'])
    
