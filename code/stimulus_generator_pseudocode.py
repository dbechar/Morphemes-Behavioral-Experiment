
n_words_per_condition = 12
df_design = get_design()

# GENERATE ALL TARGET WORDS
target_words, affixes, conditions = [], []
for i_row, row in df_design.iterrows(): # LOOP OVER CONDITIONS
    condition = row['condition']
    for i_word in range(n_words_per_condition): # LOOP OVER TRIALS PER CONDITION

        # GENERATE A TARGET WORD AND VERIFIES THAT IT DOES NOT ALREADY EXIST
        while True
            target_word, affixes = generate_random_word(condition)
            if target_word not in target_words:
                target_words.append(target_word)
                affixess.append(affixes)
                conditions.append(condition)
                break

# LOOP OVER TARGET WORDS AND ADD CONTROL WORDS AND CORRESPONING ERRORS
for target_word, affixes, condition in zip(target_words, affixess, conditions):        

    # ADD ERROR TO TARGET WORD
    if condition == 'r':
        target_word_with_error, error_info_target_word = add_error_to_word(target_word, None, 'r', 'mono') # function with two cases: mono/poly
    else:
        target_word_with_error, error_info_target_word = add_error_to_word(target_word, affixes, condition, 'poly')

    # GENERATE CONTROL WORD
    control_word, pseudoaffixes = permute_target_word(target_word)    

    # ADD ERROR TO CONTROL WORD
    control_word_with_error, error_info_control_word = add_error_to_word(control_word, None, 'control', 'mono')
    
    # -----------------------------------------

    # PUT IT ALL TOGETHER (TARGET WORD)
    summarizing_row_to_file = create_row_to_file(target_word, affixes, condition,
                                                 target_word_with_error, error_info_target_word)

    rows.append(summarizing_row_to_file)

    # PUT IT ALL TOGETHER (CONTROL WORD)
    summarizing_row_to_file = create_row_to_file(control_word, None, 'control',
                                                 control_word_with_error, error_info_control_word)
    rows.append(summarizing_row_to_file)

rows = shuffle_rows(rows)
to_csv(rows)

#### TO Functions.py
def generate_random_word(condition):
    # condition = ['pp', 'r', 's']
    morphemes = []
    for morpheme_type in condition: #
        morpheme = generate_morpheme(morpheme_type)
        morphemes.append(morpheme)
    word = ''.join(morphemes)
    return word, morphemes


def generate_morpheme(morpheme_type):
    if morpheme.startswith('p'):
        morpheme = sample_prefixes(morpheme_type)
    elif morpheme == 'r':
        morpheme = sample_root()
    elif morphemne.startswith('s')
        morpheme = sample_suffixes(morpheme_type)
    return morpheme


def sample_root():
    .....
    return root


def sample_suffixes():

    return suffixes
