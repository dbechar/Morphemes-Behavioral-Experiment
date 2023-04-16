from utils_analysis import load_df
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# DEFINE LANGUAGE AND CONDITION OF EXPERIMENT ('english' OR 'french'; 'pseudo' OR 'real')
language, condition = 'french', 'pseudo'

# READ IN TRIALLISTS
df = load_df (language, condition)


#### SEABORN HEATMAP ERROR LETTOR TYPE
# Subset the data by letter type
df ['count'] = 1
vowels = df[df['letter_type'] == 'Vowels']
sonorants = df[df['letter_type'] == 'Sonorants']
consonants = df[df['letter_type'] == 'Consonants']



# Create crosstabs for each subset
df_ct = pd.crosstab(df['target_letter_before_error'], df['letter_after_error'])
vowels_ct = pd.crosstab(vowels['target_letter_before_error'], vowels['letter_after_error'])
sonorants_ct = pd.crosstab(sonorants['target_letter_before_error'], sonorants['letter_after_error'])
consonants_ct = pd.crosstab(consonants['target_letter_before_error'], consonants['letter_after_error'])


### VOWELS
vowels_before = vowels['target_letter_before_error'].nunique()
vowels_after = vowels['letter_after_error'].nunique()
g = sns.jointplot(data=vowels, x='letter_after_error', y='target_letter_before_error', kind='hist', bins=(vowels_after, vowels_before), height = 0.7)
g.ax_marg_y.cla()
g.ax_marg_x.cla()
sns.heatmap(vowels_ct, annot=True, ax=g.ax_joint, cmap='coolwarm', cbar=False)
g.ax_joint.set_xlabel('Letter After Error', fontsize=18)
g.ax_joint.set_ylabel('Letter Before Error', fontsize=18)
g.fig.suptitle('Letter Exchange Frequencies for Vowels', fontsize=22)

g.ax_marg_y.barh(np.arange(0.5, vowels_before), vowels.groupby(['target_letter_before_error'])['count'].sum().to_numpy(), color='navy')
g.ax_marg_x.bar(np.arange(0.5, vowels_after), vowels.groupby(['letter_after_error'])['count'].sum().to_numpy(), color='navy')

x_tick_positions = np.arange(0, vowels_after+1) 
x_tick_labels = vowels['letter_after_error'].unique().tolist() + ['']
g.ax_joint.set_xticks(x_tick_positions)
g.ax_joint.set_xticklabels(x_tick_labels, fontsize=14)

y_tick_positions = np.arange(0, vowels_before+1) 
y_tick_labels = [''] + vowels['target_letter_before_error'].unique().tolist()
g.ax_joint.set_yticks(y_tick_positions)
g.ax_joint.set_yticklabels(y_tick_labels, fontsize=14, rotation = 0)

# remove ticks between heatmap and histograms
g.ax_marg_x.tick_params(axis='x', bottom=False, labelbottom=False)
g.ax_marg_y.tick_params(axis='y', left=False, labelleft=False)
# remove ticks showing the heights of the histograms
g.ax_marg_x.tick_params(axis='y', left=False, labelleft=False)
g.ax_marg_y.tick_params(axis='x', bottom=False, labelbottom=False)

g.fig.set_size_inches(20, 8)  # jointplot creates its own figure, the size can only be changed afterwards
g.fig.subplots_adjust(hspace=0, wspace=0)  # less spaced needed when there are no tick labels
plt.show()



### SONORANTS
sonorants_before = sonorants ['target_letter_before_error'].nunique()
sonorants_after = sonorants ['letter_after_error'].nunique()
g = sns.jointplot(data=sonorants, x='letter_after_error', y='target_letter_before_error', kind='hist', bins=(sonorants_after, sonorants_before), height = 0.7)
g.ax_marg_y.cla()
g.ax_marg_x.cla()
sns.heatmap(sonorants_ct, annot=True, ax=g.ax_joint, cmap='coolwarm', cbar=False)
g.ax_joint.set_xlabel('Letter After Error', fontsize=18)
g.ax_joint.set_ylabel('Letter Before Error', fontsize=18)
g.fig.suptitle('Letter Exchange Frequencies for Sonorants', fontsize=22)


g.ax_marg_y.barh(np.arange(0.5, sonorants_before), sonorants.groupby(['target_letter_before_error'])['count'].sum().to_numpy(), color='navy')
g.ax_marg_x.bar(np.arange(0.5, sonorants_after), sonorants.groupby(['letter_after_error'])['count'].sum().to_numpy(), color='navy')

x_tick_positions = np.arange(0, sonorants_after+1) 
x_tick_labels = sonorants['letter_after_error'].unique().tolist() + ['']
g.ax_joint.set_xticks(x_tick_positions)
g.ax_joint.set_xticklabels(x_tick_labels, fontsize=14)

y_tick_positions = np.arange(0, sonorants_before+1) 
y_tick_labels = [''] + sonorants['target_letter_before_error'].unique().tolist()
g.ax_joint.set_yticks(y_tick_positions)
g.ax_joint.set_yticklabels(y_tick_labels, fontsize=14, rotation = 0)

# remove ticks between heatmap and histograms
g.ax_marg_x.tick_params(axis='x', bottom=False, labelbottom=False)
g.ax_marg_y.tick_params(axis='y', left=False, labelleft=False)
# remove ticks showing the heights of the histograms
g.ax_marg_x.tick_params(axis='y', left=False, labelleft=False)
g.ax_marg_y.tick_params(axis='x', bottom=False, labelbottom=False)

g.fig.set_size_inches(20, 8)  # jointplot creates its own figure, the size can only be changed afterwards
g.fig.subplots_adjust(hspace=0, wspace=0)  # less spaced needed when there are no tick labels
plt.show()


### CONSONANTS
consonants_before = consonants['target_letter_before_error'].nunique()
consonants_after = consonants['letter_after_error'].nunique()
g = sns.jointplot(data=consonants, x='letter_after_error', y='target_letter_before_error', kind='hist', bins=(consonants_after, consonants_before), height = 0.7)
g.ax_marg_y.cla()
g.ax_marg_x.cla()
sns.heatmap(consonants_ct, annot=True, ax=g.ax_joint, cmap='coolwarm', cbar=False)
g.ax_joint.set_xlabel('Letter After Error', fontsize=18)
g.ax_joint.set_ylabel('Letter Before Error', fontsize=18)
g.fig.suptitle('Letter Exchange Frequencies for Consonants', fontsize=22)


g.ax_marg_y.barh(np.arange(0.5, consonants_before), consonants.groupby(['target_letter_before_error'])['count'].sum().to_numpy(), color='navy')
g.ax_marg_x.bar(np.arange(0.5, consonants_after), consonants.groupby(['letter_after_error'])['count'].sum().to_numpy(), color='navy')

x_tick_positions = np.arange(0, consonants_after+1) 
x_tick_labels = consonants['letter_after_error'].unique().tolist() + ['']
g.ax_joint.set_xticks(x_tick_positions)
g.ax_joint.set_xticklabels(x_tick_labels, fontsize=14)

y_tick_positions = np.arange(0, consonants_before+1) 
y_tick_labels = [''] + consonants['target_letter_before_error'].unique().tolist()
g.ax_joint.set_yticks(y_tick_positions)
g.ax_joint.set_yticklabels(y_tick_labels, fontsize=14, rotation = 0)

# remove ticks between heatmap and histograms
g.ax_marg_x.tick_params(axis='x', bottom=False, labelbottom=False)
g.ax_marg_y.tick_params(axis='y', left=False, labelleft=False)
# remove ticks showing the heights of the histograms
g.ax_marg_x.tick_params(axis='y', left=False, labelleft=False)
g.ax_marg_y.tick_params(axis='x', bottom=False, labelbottom=False)

g.fig.set_size_inches(20, 8)  # jointplot creates its own figure, the size can only be changed afterwards
g.fig.subplots_adjust(hspace=0, wspace=0)  # less spaced needed when there are no tick labels
plt.show()



### ALL TOGETHER
letter_before = df['target_letter_before_error'].nunique()
letter_after = df['letter_after_error'].nunique()
g = sns.jointplot(data=df, x='letter_after_error', y='target_letter_before_error', kind='hist', bins=(letter_after, letter_before), height = 0.7)
g.ax_marg_y.cla()
g.ax_marg_x.cla()
sns.heatmap(df_ct, annot=True, ax=g.ax_joint, cmap='coolwarm', cbar=False)
g.ax_joint.set_xlabel('Letter After Error', fontsize=22)
g.ax_joint.set_ylabel('Letter Before Error', fontsize=22)
g.fig.suptitle('Letter Exchange Frequencies', fontsize=28)


g.ax_marg_y.barh(np.arange(0.5, letter_before), df.groupby(['target_letter_before_error'])['count'].sum().to_numpy(), color='navy')
g.ax_marg_x.bar(np.arange(0.5, letter_after), df.groupby(['letter_after_error'])['count'].sum().to_numpy(), color='navy')

x_tick_positions = np.arange(0, letter_after+1) 
x_tick_labels = sorted(df['letter_after_error'].unique().tolist()) + ['']
g.ax_joint.set_xticks(x_tick_positions)
g.ax_joint.set_xticklabels(x_tick_labels, fontsize=16)

y_tick_positions = np.arange(0, letter_before+1) 
y_tick_labels = [''] + sorted(df['target_letter_before_error'].unique().tolist(), reverse=True)
g.ax_joint.set_yticks(y_tick_positions)
g.ax_joint.set_yticklabels(y_tick_labels, fontsize=16, rotation = 0)

# remove ticks between heatmap and histograms
g.ax_marg_x.tick_params(axis='x', bottom=False, labelbottom=False)
g.ax_marg_y.tick_params(axis='y', left=False, labelleft=False)
# remove ticks showing the heights of the histograms
g.ax_marg_x.tick_params(axis='y', left=False, labelleft=False)
g.ax_marg_y.tick_params(axis='x', bottom=False, labelbottom=False)

g.fig.set_size_inches(20, 8)  # jointplot creates its own figure, the size can only be changed afterwards
g.fig.subplots_adjust(hspace=0, wspace=0)  # less spaced needed when there are no tick labels
plt.show()

