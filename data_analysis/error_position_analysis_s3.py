from utils_analysis import load_df, remove_outliers
from utils_analysis import create_pointplot
from utils_analysis import error_position, error_position_letter
import seaborn as sns
import matplotlib.pyplot as plt



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
                   (0, 1), ['Within Morpheme', 'Morpheme Boundary', ' Word Boundary']), 
                  ('error_position', 'rt', 'Error Position Within Word', 'Reaction Time',
                  (0, 1500), ['Within Morpheme', 'Morpheme Boundary', ' Word Boundary'])]:
    create_pointplot(df_error, *plot_info,  order = ['within_morpheme', 'morpheme_boundary','word_boundary'])
    


# ERROR RATE AS FUNCTION OF ERROR POSITION 
    # SPLIT BETWEEN DIFFERENT WORDLENGTHS
    # NORMALIZE LETTER POSITION TO BE BETWEEN 0 ANT 1 and PLOT ALL WORDLENGTHS TOGETHER

df_error_pos = error_position_letter (df_filtered.query('is_error == 1'))
df_error_pos['norm_error_index'] = df_error_pos['error_index'] / df_error_pos['wordlength']


# DATAFRAME WITH MEAN ERRORRATE PER PARTICIPANT
df_mean_er = df_error_pos.groupby(['target_type', 'norm_error_index'])['error_rate'].mean().reset_index()

# plot rt vs. norm_letter_pos with hue
g = sns.lmplot(data=df_error_pos.query('correct == True'), x='norm_error_index', y='rt', hue='target_type',hue_order=['target', 'control'], 
                     palette=['g', 'r'], order=2, scatter = True)
# Set axis labels
g.set(xlabel='Normalized Letter Position', ylabel='Reaction Time')

# Set legend labels
new_labels = {'target': 'Target', 'control': 'Control'}
for t, l in zip(g._legend.texts, new_labels.values()):
    t.set_text(l)
    
g._legend.set_title('Type')

# Set font size and weight for axis labels and legend
plt.setp(g.ax.xaxis.get_label(), fontsize=14, weight='bold')
plt.setp(g.ax.yaxis.get_label(), fontsize=14, weight='bold')
plt.setp(g._legend.get_texts(), fontsize=12)
plt.setp(g._legend.get_title(), fontsize=12)
g.set(xlim=(0, 1))
g.set (ylim = (0,5000))

plt.show()



g = sns.lmplot(data=df_mean_er, x='norm_error_index', y='error_rate', hue='target_type', hue_order=['target', 'control'], 
                     palette=['g', 'r'], order=2, scatter = False)

# Set axis labels
g.set(xlabel='Normalized Letter Position', ylabel='Mean Error Rate')

# Set legend labels
new_labels = {'target': 'Target', 'control': 'Control'}
for t, l in zip(g._legend.texts, new_labels.values()):
    t.set_text(l)
    
g._legend.set_title('Type')

# Set font size and weight for axis labels and legend
plt.setp(g.ax.xaxis.get_label(), fontsize=14, weight='bold')
plt.setp(g.ax.yaxis.get_label(), fontsize=14, weight='bold')
plt.setp(g._legend.get_texts(), fontsize=12)
plt.setp(g._legend.get_title(), fontsize=12)
g.set(xlim=(0, 1))
g.set(ylim=(0, 1.1))

plt.show()


# REACTION TIME/ERROR RATE AS A FUNCTION OF ERROR POSITION (PREFIX, ROOT, SUFFIX)
df_mean_er = df_error_pos.groupby(['error_to_which_morpheme', 'target_type'])['error_rate'].mean().reset_index()
for plot_info in [(df_mean_er, 'error_to_which_morpheme', 'error_rate', 'Error Position Within Word', 'Error Rate', 
                   (0,0.22), ['Prefix', 'Root', 'Suffix']), 
                  (df_filtered.query('correct == True'), 'error_to_which_morpheme', 'rt', 'Error Position Within Word', 'Reaction Time',
                  (0, 1500), ['Prefix', 'Root', 'Suffix'])]:
    create_pointplot(*plot_info,  order = ['p', 'r', 's'])


df_mean_er = df_error_pos.groupby(['letter_type', 'ID', 'target_type'])['error_rate'].mean().reset_index()
for plot_info in [(df_mean_er, 'letter_type', 'error_rate', 'Error Position Within Word', 'Error Rate', (0,0.5)), 
                  (df_filtered.query('correct == True'), 'letter_type', 'rt', 'Error Position Within Word', 'Reaction Time', (0, 1500))]:
    create_pointplot(*plot_info, order = ['Vowels', 'Consonants', 'Sonorants'])
