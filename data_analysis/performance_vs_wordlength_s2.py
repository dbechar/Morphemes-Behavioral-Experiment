import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from utils_analysis import load_df, remove_outliers
from utils_analysis import create_pointplot, create_boxplot
from utils_analysis import ttest


# DEFINE LANGUAGE AND CONDITION OF EXPERIMENT ('english' OR 'french'; 'pseudo' OR 'real')
language, condition = 'french', 'pseudo'

# READ IN TRIALLISTS
df = load_df (language, condition)

# REMOVE OUTLIERS
df_filtered = remove_outliers(df)


# PLOT 
for plot_info in [(df_filtered.query('correct == True'),'wordlength', 'rt', 'Number of Characters', 'Reaction Time', (0, 6000)), 
                  (df_filtered.query('correct == True'),'num_morphemes', 'rt', 'Number of Morphemes', 'Reaction Time', (0, 6000)), 
                  (df_filtered.query('correct == True'), 'wordlength', 'encoding_time', 'Number of Characters', 'Encoding Time', (0,7000)), 
                  (df_filtered.query('correct == True'), 'num_morphemes', 'encoding_time', 'Number of Morphemes', 'Encoding Time', (0, 7000)), 
                  (df_filtered, 'wordlength', 'error_rate', 'Number of Characters', 'Error Rate', (0, 0.9)), 
                  (df_filtered, 'num_morphemes', 'error_rate', 'Number of Morphemes', 'Error Rate', (0, 0.9))]:
    create_pointplot(*plot_info)
    

# ENCODING TIME, RT, AND ERROR-RATE AS A FUNCTION OF WORDLENGTH AND NUMBER OF MORPHEMES (MEANS & MEDIANS)
for variable in ['encoding_time', 'rt']:
    for grouping_variable in ['wordlength', 'num_morphemes']:
        df_grouped = df_filtered.query('correct == True').groupby(grouping_variable)[variable].agg(['median', 'mean', 'std'])
        print(f' {variable} as a function of {grouping_variable}: {df_grouped}')


# ERROR RATE AS A FUNCTION OF NUMBER OF CHARACTERS AND NUMBER OF MORPHEMES (MEANS & MEDIANS)
for grouping_variable in ['wordlength', 'num_morphemes']:
    df_grouped = df_filtered.groupby(grouping_variable)['error_rate'].agg(['median', 'mean', 'std'])
    print(f'Error rate as a function of {grouping_variable}: {df_grouped}')


# T-TEST (RT ~ EQUAL WORDLENGTH, DIFFERENT NUMBER OF MORPHEMES)
word_lencon = df_filtered.query('correct == True').groupby("num_morphemes")["wordlength"].value_counts()
print (word_lencon)

# DATAFRAME WITH MEAN ERRORRATE PER PARTICIPANT
df_mean_er = df_filtered.groupby(['wordlength', 'num_morphemes', 'target_type'])['error_rate'].mean().reset_index()

ttest_args = [(11, 2, 4), (10, 3, 4)] # wl, n_morph1, n_morph2
for args in ttest_args:
    for var in ['rt', 'encoding_time']:
        ttest(df_filtered.query('correct == True'), wl=args[0], n_morph1=args[1], n_morph2=args[2], variable = var)
        df_plot = df_filtered.query('correct == True')[(df_filtered.query('correct == True')['wordlength'] == args[0]) & ((df_filtered.query('correct == True')['num_morphemes'] == args[1]) | (df_filtered.query('correct == True')['num_morphemes'] == args[2]))]
        create_boxplot (x = 'num_morphemes', y = var, data = df_plot, xlabel = f'Number of Morphemes (Wordlength:{args[0]})', ylabel = f'{var.capitalize()}', ylim = (0,4000))

for args in ttest_args: 
        ttest(df_filtered, wl=args[0], n_morph1=args[1], n_morph2=args[2], variable = 'error_rate')
        df_plot = df_mean_er[(df_mean_er['wordlength'] == args[0]) & ((df_mean_er['num_morphemes'] == args[1]) | (df_mean_er['num_morphemes'] == args[2]))]
        create_boxplot (x = 'num_morphemes', y = 'error_rate', data = df_plot, xlabel = f'Number of Morphemes (Wordlength:{args[0]})', ylabel = 'Mean Error Rate', ylim = (0, 0.3))
      

# CREATE REGRESSION MODELS 
mod_rt_wl = ols('rt ~ wordlength * target_type', data=df_filtered.query('correct == True')).fit()
mod_encoding_time_wl = ols('encoding_time ~ wordlength * target_type', data=df_filtered.query('correct == True')).fit()
mod_error_rate_wl = ols('error_rate ~ wordlength * target_type', data=df_mean_er).fit()

mod_rt_nom = ols('rt ~ num_morphemes * target_type', data=df_filtered.query('correct == True')).fit()
mod_encoding_time_nom = ols('encoding_time ~ num_morphemes * target_type', data=df_filtered.query('correct == True')).fit()
mod_error_rate_nom = ols('error_rate ~ num_morphemes * target_type', data=df_mean_er).fit()

# PRINT SUMMARY OF THE MODELS
# WORDLENGTH
print(mod_rt_wl.summary())
print(mod_encoding_time_wl.summary())
print(mod_error_rate_wl.summary())

# NUMBER OF MORPHEMES
print(mod_rt_nom.summary())
print(mod_encoding_time_nom.summary())
print(mod_error_rate_nom.summary())


# PLOT NOT FILTERED FOR ACCURACY
for plot_info in [(df_filtered,'wordlength', 'rt', 'Number of Characters', 'Reaction Time', (0, 6000)), 
                  (df_filtered,'num_morphemes', 'rt', 'Number of Morphemes', 'Reaction Time', (0, 6000)), 
                  (df_filtered, 'wordlength', 'encoding_time', 'Number of Characters', 'Encoding Time', (0,7000)), 
                  (df_filtered, 'num_morphemes', 'encoding_time', 'Number of Morphemes', 'Encoding Time', (0, 7000))]:
    create_pointplot(*plot_info)
    

df_filtered['target_type'] = df_filtered['target_type'].replace({'target': 'Target', 'control': 'Control'})

# Rename the labels for the legend and style
hue_labels = {'num_morphemes': 'Number of Morphemes'}
style_labels = {'target_type': 'Type'}

# Map the new labels to the dataframe
df_filtered = df_filtered.rename(columns = hue_labels)
df_filtered = df_filtered.rename(columns =style_labels)

# Calculate the mean reaction times per group
df_mean_er = df_filtered.groupby(['wordlength', 'Number of Morphemes', 'Type'])['error_rate'].mean().reset_index()
df_mean_rt_et = df_filtered.query('correct == True').groupby(['wordlength', 'Number of Morphemes', 'Type']).mean().reset_index()

# ENCODING TIME
# Plot the mean encoding times per wordlength with hue set to num_morphemes and target type
plot = sns.scatterplot(data=df_mean_rt_et, x='wordlength', y='encoding_time', hue='Number of Morphemes', style='Type', palette='coolwarm')
plot.set_xlabel('Number of Characters', fontdict={'size': 14, 'weight': 'bold'})
plot.set_ylabel('Encoding Time', fontdict={'size': 14, 'weight': 'bold'})
plot.set(ylim=(0, 5000))

# Move the legend outside of the plot
legend_bbox = (1.02, 0.5)
legend_pos = 'center left'
plot.legend(bbox_to_anchor=legend_bbox, loc=legend_pos)
plt.show()

# REACTION TIME
# Plot the mean reaction times per wordlength with hue set to num_morphemes and target type
plot = sns.scatterplot(data=df_mean_rt_et, x='wordlength', y='rt', hue='Number of Morphemes', style='Type', palette='coolwarm')
plot.set_xlabel('Number of Characters', fontdict={'size': 14, 'weight': 'bold'})
plot.set_ylabel('Reaction Time', fontdict={'size': 14, 'weight': 'bold'})
plot.set(ylim=(0, 2000))

# Move the legend outside of the plot
legend_bbox = (1.02, 0.5)
legend_pos = 'center left'
plot.legend(bbox_to_anchor=legend_bbox, loc=legend_pos)
plt.show()

# Error Rate
# Plot the mean error rates per wordlength with hue set to num_morphemes and target type
plot = sns.scatterplot(data=df_mean_er, x='wordlength', y='error_rate', hue='Number of Morphemes', style='Type', palette='coolwarm')
plot.set_xlabel('Number of Characters', fontdict={'size': 14, 'weight': 'bold'})
plot.set_ylabel('Error Rate', fontdict={'size': 14, 'weight': 'bold'})
plot.set(ylim=(0, 1))

# Move the legend outside of the plot
legend_bbox = (1.02, 0.5)
legend_pos = 'center left'
plot.legend(bbox_to_anchor=legend_bbox, loc=legend_pos)
plt.show()


# NEW REGRESSION MODELS
mod_rt_wl_morphemes = ols('rt ~ wordlength + num_morphemes', data=df_filtered.query('correct == True')).fit()
mod_encoding_time_wl_morphemes = ols('encoding_time ~ wordlength + num_morphemes', data=df_filtered.query('correct == True')).fit()
mod_error_rate_wl_morphemes = ols('error_rate ~ wordlength + num_morphemes', data=df_mean_er).fit()

print("Word Length and Number of Morphemes Model:")
print(mod_rt_wl_morphemes.summary())
print(mod_encoding_time_wl_morphemes.summary())
print(mod_error_rate_wl_morphemes.summary())
























