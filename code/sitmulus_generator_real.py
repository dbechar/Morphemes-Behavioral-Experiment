# STIMULUS GENERATOR: REAL WORDS

import random
import glob 
import pandas as pd
from utils_real import choose_targets_and_control
from utils_real import add_errors

import os
os.chdir("C:/Users/delia/OneDrive/Desktop/Morphemes/Morphemes/Code")

random.seed(1)
num_par = 0

# DEFINE LANGUAGE OF EXPERIMENT ("english" OR "french")
language = "french" 

# READ IN STIMULI FILES
df_design = pd.read_csv("../experimental_design/real_words_french_design.csv") 
path = "../experimental_design/real_words_" + language 
csv_files = glob.glob(path + "/*.csv")
realword_files = (pd.read_csv (file) for file in csv_files) 
df_realwords = pd.concat(realword_files, ignore_index = True) 

# SET ERRORRATE
errorrate = 0.5

condition = "prs"

d_target, d_control = {}, {}

# TARGET
words, freq = df_realwords["Word"].loc[df_realwords["Condition"] == condition].tolist(), df_realwords["Frequency"].loc[df_realwords["Condition"] == condition].tolist()
d_target["word"] = random.choices(words, weights= freq)

index =  (df_realwords[df_realwords["Word"]== d_target["word"][0]].index)

d_target["root"] = df_realwords["Root"][index[0]]
d_target["prefix"] = df_realwords["Prefix"][index[0]]
d_target["suffix"] = df_realwords["Suffix"][index[0]]

# CONTROL
# Randomly choose corersponding control word that same word length
words, freq = df_realwords["Word"].loc[df_realwords["Condition"] == "r"].tolist(), df_realwords["Frequency"].loc[df_realwords["Condition"] == "r"].tolist()
d_control["word"] = random.choices(words, weights= freq)
#while len(d_target["word"][0]) != len(d_control["word"][0]): 
#    d_control["word"] = random.choices(words, weights= freq)

# Chose one random control word that has the same wordlength
# ADD TYPE
d_target["type"] = "target"
d_control["type"] = "control"



"""

# GENERATE ALL TARGET WORDS
target_words = []
ds_target_word, ds_control_word = [], []
for i_row, row in df_design.iterrows(): # LOOP OVER CONDITIONS
    condition, n_trials = row['Condition'], row['n_trials']
    for i_word in range(n_trials): # LOOP OVER TRIALS PER CONDITION
        # GENERATE A TARGET WORD AND VERIFIES THAT IT DOES NOT ALREADY EXIST
         while True:
             d_target_word, d_control_word = choose_targets_and_control(condition, df_realwords)
             if d_target_word['word'] not in target_words:
                target_words.append(d_target_word['word'])
                
                # ADD LETTER-SUBSTITUTION ERRORS
                #d_target_word = add_errors(d_target_word, language)
                #d_control_word = add_errors(d_control_word, language)
                
                #ds_target_word.append(d_target_word)
                #ds_control_word.append(d_control_word)

                
                break


df_target = pd.DataFrame(random.sample(ds_target_word, len(ds_target_word)))
df_control = pd.DataFrame(random.sample(ds_control_word, len(ds_control_word)))


# ADD "IS_ERROR" 
df_target["is_error"] = [1] * int(errorrate * len(df_target)) +  [0] * int(errorrate * len(df_target)) 
df_control["is_error"] = [1] * int(errorrate * len(df_control)) +  [0] * int(errorrate * len(df_control)) 

# CONCATE DATAFRAMES
df_complete = pd.concat([df_target, df_control])

# REMOVE LISTS
df_complete["prefixes"] = df_complete["prefixes"].apply (lambda prefixes: "_".join(prefixes))
df_complete["suffixes"] = df_complete["suffixes"].apply (lambda suffixes: "_".join(suffixes))

# CREATE TRIALLIST
first, second =  [], []
word = df_complete["word"].tolist()
error_word = df_complete["error_word"].tolist()
is_error = df_complete["is_error"].tolist ()
  
for i in range (0, len (df_complete)):
    first.append (word[i])
    if is_error [i] == 1: 
        second.append (error_word[i]) 
    else: 
        second.append (word[i])

df_complete.insert (0, "first", first)
df_complete.insert (1, "second", second)
df_complete = df_complete.sample (frac = 1)

# SAVE TRIALLIST IN CORRECT FOLDER
path = "../triallists/" + language + "/" + str(num_par) + "triallist.csv" 
df_complete.to_csv (path, index = False)
"""