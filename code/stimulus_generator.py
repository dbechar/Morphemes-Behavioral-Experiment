import random
import pandas as pd
from utils import generate_random_word_and_control
from utils import add_errors

random.seed(1)

df_design = pd.read_csv("../experimental_design/design.csv")
df_prefix_pool = pd.read_csv("../experimental_design/prefixes.csv")
df_root_pool = pd.read_csv("../experimental_design/roots.csv")
df_suffix_pool = pd.read_csv("../experimental_design/suffixes.csv")


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
                d_target_word = add_errors(d_target_word)
                d_control_word = add_errors(d_control_word)
                
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