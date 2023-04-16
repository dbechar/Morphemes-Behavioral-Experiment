from utils_analysis import load_df, remove_outliers
from utils_analysis import create_pointplot, create_boxplot
from utils_analysis import error_position, error_position_letter
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# DEFINE LANGUAGE AND CONDITION OF EXPERIMENT ('english' OR 'french'; 'pseudo' OR 'real')
language, condition = 'french', 'pseudo'

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
    


# ERROR RATE AS FUNCTION OF ERROR POSITION 
    # SPLIT BETWEEN DIFFERENT WORDLENGTHS
    # NORMALIZE LETTER POSITION TO BE BETWEEN 0 ANT 1 and PLOT ALL WORDLENGTHS TOGETHER

df_error_pos = error_position_letter (df_filtered.query('is_error == 1'))
df_error_pos['norm_error_index'] = df_error_pos['error_index'] / df_error_pos['wordlength']


# DATAFRAME WITH MEAN ERRORRATE PER PARTICIPANT
mean_error_rate = df_error_pos.groupby(['ID', 'norm_error_index','target_type', 'error_to_which_morpheme', 'letter_type'])['error_rate'].mean()
df_mean_error_rate = pd.DataFrame({'ID': mean_error_rate.index.get_level_values('ID'), 
                                   'target_type': mean_error_rate.index.get_level_values('target_type'),
                                   'letter_type': mean_error_rate.index.get_level_values ('letter_type'),
                                   'mean_error_rate': mean_error_rate.values,
                                   #'error_to_which_morpheme': mean_error_rate.get_level_values ('error_to_which_morpheme'),
                                   'norm_error_index': mean_error_rate.index.get_level_values ('norm_error_index')
                                   })

# plot rt vs. norm_letter_pos with hue
g = sns.lmplot(data=df_error_pos.query('correct == True'), x='norm_error_index', y='rt', hue='target_type',hue_order=['target', 'control'], 
                     palette=['g', 'r'], order=2, scatter = False)
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

plt.show()



g = sns.lmplot(data=df_mean_error_rate, x='norm_error_index', y='mean_error_rate', hue='target_type', hue_order=['target', 'control'], 
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

plt.show()

# ERROR RATE AND RT AS A FUNCTION OF LETTER TYPE
for plot_info in [('letter_type', 'mean_error_rate', df_mean_error_rate, 'Type', 'Mean Error Rate', (0, 0.2)), 
                  ('letter_type', 'rt', df_filtered.query('correct == True'),'Letter Type', 'Reaction Time', (0, 5000), ['Vowels', 'Consonants', 'Sonorants'])]:
    create_boxplot(*plot_info)


def create_boxplot(x, y, data, xlabel, ylabel, ylim, order = None, xticks = None, hue=None, ):
    ax = sns.boxplot(x=x, y=y, data=data, hue=hue, palette= ['r', 'g', 'b'],  order = order)
    sns.despine()
    ax.set_ylim(ylim)
    ax.set_xlabel(xlabel, fontdict={'size': 14, 'weight': 'bold'})
    ax.set_ylabel(ylabel, fontdict={'size': 14, 'weight': 'bold'})
    if xticks != None: 
        ax.set_xticklabels(xticks, fontsize = 10)
    plt.show()
    
# ERROR RATE ROOTS VS AFFIXES
for plot_info in [#('error_to_which_morpheme', 'mean_error_rate', df_mean_error_rate, 'Type', 'Mean Error Rate', (0, 0.2)), 
                  ('error_to_which_morpheme', 'rt', df_filtered.query('correct == True'),'Error Position', 'Reaction Time', (0, 5000),['p', 'r', 's'],  ['Prefix', 'Root', 'Suffix']), 
                  ('error_to_which_morpheme', 'encoding_time', df_filtered.query('correct == True'), 'Error Position', 'Encoding Time', (0,5000), ['p', 'r', 's'],  ['Prefix', 'Root', 'Suffix'])]:
    create_boxplot(*plot_info)

# ERROR RATE AND RT AS A FUNCTION OF LETTER TYPE
for plot_info in [('letter_type', 'mean_error_rate', df_mean_error_rate, 'Letter Type', 'Mean Error Rate', (0, 0.2), ['Vowels', 'Consonants', 'Sonorants']), 
                  ('letter_type', 'rt', df_filtered.query('correct == True'),'Letter Type', 'Reaction Time', (0, 5000), ['Vowels', 'Consonants', 'Sonorants']), ]:
    create_boxplot(*plot_info)
