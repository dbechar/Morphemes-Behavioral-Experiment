import glob 
import pandas as pd

# DEFINE LANGUAGE OF EXPERIMENT ("english" OR "french")
language = "english"
condition = "pseudo"

# READ IN TRIALLISTS
path = f'../triallists/{language}_{condition}'
csv_files = glob.glob(path + "/*.csv")
df_list = (pd.read_csv(file) for file in csv_files)


df_triallists = pd.concat (df_list, ignore_index = True)

# SAVE EVERYTHING TO TEXT FILE
f = open('verification_code', 'w')

# COUNT NUMBER OF TRIALS PER CONDITION
num_con = df_triallists["condition"].value_counts ()
print ("Number of trials per condition", file = f)
f.write('\n')
print (num_con, file = f)
f.write('\n')
f.write('\n')

# ERROR IN WHICH MORHEME (OVERALL)
error_mor = df_triallists["error_to_which_morpheme"].value_counts()
print ("Error in which morpheme (overall)", file = f) 
f.write('\n')
print (error_mor, file = f)
f.write('\n')
f.write('\n')

# ERROR IN WHICH MORPHEME (PER CONDITION)
error_morcon = df_triallists.groupby("condition")["error_to_which_morpheme"].value_counts()
print ("\n Error in which morpheme (for each condition)", file = f) 
f.write('\n')
print (error_morcon, file = f)
f.write('\n')
f.write('\n')

# INDEX OF ERROR WITHIN MORPHEME (OVERALL)
error_index = df_triallists["i_within_morpheme"].value_counts()
print ("Index of error within morpheme (overall)", file = f) 
f.write('\n')
print (error_index, file = f)
f.write('\n')
f.write('\n')

# INDEX OF ERROR WITHIN MORPHEME (PER CONDITION)
error_indexcon = df_triallists.groupby("condition")["i_within_morpheme"].value_counts()
print ("Index of error within morpheme (for each condition)", file = f) 
f.write('\n')
print (error_indexcon, file = f)
f.write('\n')
f.write('\n')

# IF MULTIPLE PREFIXES/SUFFIXES ERROR IN WHICH PREFIX/SUFFIX (PER CONDITION)
# ONLY PREFIXES (ONLY IMPORTANT IF MUTLIPLE PREFIXES IN CONDITON) 
prefix = df_triallists.loc[df_triallists["error_to_which_morpheme"] == "p"]
error_mor_prefix = prefix.groupby("condition")["i_morpheme"].value_counts()
print ("If error in prefix, then in which prefix exactly", file = f) 
f.write('\n')
print (error_mor_prefix, file = f)
f.write('\n')
f.write('\n')

# ONLY SUFFIXES (ONLY IMPORTANT IF MUTLIPLE SUFFIXES IN CONDITION)
suffix = df_triallists.loc[df_triallists["error_to_which_morpheme"] == "s"]
error_mor_suffix = suffix.groupby("condition")["i_morpheme"].value_counts()
print ("If error in suffix, then in which suffix exactly", file = f) 
f.write('\n')
print (error_mor_suffix, file = f)
f.write('\n')
f.write('\n')


# COUNT WORDLENGTH (OVERALL)
df_triallists["Wordlength"] = df_triallists["first"].str.len()
word_len = df_triallists["Wordlength"].value_counts()
print ("Wordlength overall:", file = f) 
f.write('\n')
print (word_len, file = f)
f.write('\n')
f.write('\n')

# WORDLENGTH PER CONDITION
word_lencon = df_triallists.groupby("condition")["Wordlength"].value_counts()
print ("Wordlength per condition", file = f) 
f.write('\n')
print (word_lencon, file = f)
print (word_lencon)

f.close()
    
    
    
    
