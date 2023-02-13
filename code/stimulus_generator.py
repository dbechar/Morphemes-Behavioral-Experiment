import random
import pandas as pd
from utils import generate_random_word_and_control
from utils import add_errors


random.seed(1)
num_par = 1

# DEFINE LANGUAGE OF EXPERIMENT ("english" OR "french")
language = "french" 

df_design = pd.read_csv("../experimental_design/design.csv")
df_prefix_pool = pd.read_csv ("../experimental_design/prefixes_" + language + ".csv")
df_root_pool = pd.read_csv("../experimental_design/roots_" + language + ".csv")
df_suffix_pool = pd.read_csv("../experimental_design/suffixes_" + language + ".csv")


# SET ERRORRATE
errorrate = 0.5

for par in range (num_par): 
    # GENERATE ALL TARGET WORDS
    target_words = []
    ds_target_word, ds_control_word = [], []
    for i_row, row in df_design.iterrows(): # LOOP OVER CONDITIONS
        condition, n_trials = row['Condition'], row['n_trials']
        for i_word in range(n_trials): # LOOP OVER TRIALS PER CONDITION
            # GENERATE A TARGET WORD AND VERIFIES THAT IT DOES NOT ALREADY EXIST
            while True:
                d_target_word, d_control_word = generate_random_word_and_control(condition,
                                                          df_prefix_pool,
                                                          df_root_pool,
                                                          df_suffix_pool)
                if d_target_word['word'] not in target_words:
                    target_words.append(d_target_word['word'])
                    
                    # ADD LETTER-SUBSTITUTION ERRORS
                    d_target_word = add_errors(d_target_word, language)
                    d_control_word = add_errors(d_control_word, language)
                    
                    ds_target_word.append(d_target_word)
                    ds_control_word.append(d_control_word)
                    
                    print(condition, i_word,
                          d_target_word['word'], d_target_word['error_word'],
                          d_control_word['word'], d_control_word['error_word'])
                    
                    break
    
    df_target = pd.DataFrame(random.sample(ds_target_word, len(ds_target_word)))
    df_control = pd.DataFrame(random.sample(ds_control_word, len(ds_control_word)))
    
    print(df_target)
    print(df_control)
    
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
    path = "../triallists/" + language + "/" + str(par) + "triallist.csv"
    df_complete.to_csv (path, index = False)



