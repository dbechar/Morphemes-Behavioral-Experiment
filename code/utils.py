 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 04:59:35 2023

@author: yair
"""
import random

def generate_random_word_and_control(condition, prefix_pool, root_pool, suffix_pool):
    
    d_target, d_control = {}, {}
    d_target['condition'], d_control['condition'] = condition, condition
    
    n_prefixes, n_suffixes = condition.count('p'), condition.count('s')
    d_target['prefix_template'], d_target['suffix_template'] = 'p' * n_prefixes, 's' * n_suffixes
    d_control['prefix_template'], d_control['suffix_template'] = 'p' * n_prefixes, 's' * n_suffixes
    
    # GENERATE ROOT
    d_target['root'], d_control['root'] = sample_root(root_pool)
    
    # GENERATE PREFIXES
    d_target['prefixes'], d_control['prefixes'] = sample_affixes(prefix_pool,
                                                           d_target['prefix_template'])
    # GENERATE SUFFIXES
    d_target['suffixes'], d_control['suffixes'] = sample_affixes(suffix_pool,
                                                           d_target['suffix_template'])
    
    # COMBINE AFFIXES
    d_target['word'] = ''.join(d_target['prefixes'] + [d_target['root']] + d_target['suffixes'])
    d_control['word'] = ''.join(d_control['prefixes'] + [d_control['root']] + d_control['suffixes'])
    
    # ADD TYPE
    d_target["type"] = "target"
    d_control["type"] = "control"
    return d_target, d_control


def sample_root(root_pool):
    root = random.choice(root_pool['Root'])
    root_permuted = random.choice(root_pool['ReverseRoot'])
    return root, root_permuted


def sample_affixes(affix_pool, affix_template):
    n_affixes = len(affix_template)
    if n_affixes > 0:
        df_pool = affix_pool[affix_pool['n_affixes']==n_affixes]
        IX = random.choices(range(len(df_pool)),
                            weights=df_pool['Frequency'],
                            k=1)
        
        a1, a2, a3, _, _, _ = df_pool.iloc[IX].values[0]
        if 'p' in affix_template:
            affixes = [a3, a2, a1]
        elif 's' in affix_template:
            affixes = [a1, a2, a3]
        affixes = affixes[:n_affixes]
        
        affixes_reversed = [a[::-1] for a in affixes]
        return affixes[::-1], affixes_reversed[::-1]
    else:
        return [''], ['']
    
    
def add_errors(d):
    prefixes, root, suffixes = d['prefixes'].copy(), d['root'], d['suffixes'].copy()
    
    morphemes_template = list(set(list(d['condition']))) # Remove redundancy in control template (e.g., pprs -> prs or rss -> rs)
    error_to_which_morpheme = random.choice(morphemes_template)
    
    if error_to_which_morpheme == 'r':
        i_morpheme, target_morpheme = None, d['root']  
    elif error_to_which_morpheme == 'p':
        i_morpheme, target_morpheme = random.choice(list(enumerate(d['prefixes'])))
    elif error_to_which_morpheme == 's':
        i_morpheme, target_morpheme = random.choice(list(enumerate(d['suffixes'])))
        
    i_within_morpheme, target_letter_before_error = random.choice(list(enumerate(list(target_morpheme))))
    
    letter_after_error = substitute_letter(target_letter_before_error)
    
   
    d['error_to_which_morpheme'] = error_to_which_morpheme
    d['i_morpheme'] = i_morpheme
    d['i_within_morpheme'] = i_within_morpheme
    d['target_letter_before_error'] = target_letter_before_error
    d['letter_after_error'] = letter_after_error
    
    # BUILD ERROR WORD
    if error_to_which_morpheme == 'r':
        root = list(root)
        root[i_within_morpheme] = letter_after_error
        root = ''.join(root)
    elif error_to_which_morpheme in ['p', 's']:
        morpheme_with_error = list(target_morpheme)
        morpheme_with_error[i_within_morpheme] = letter_after_error
        morpheme_with_error = ''.join(morpheme_with_error)
        if error_to_which_morpheme == 'p':
            prefixes[i_morpheme] = morpheme_with_error
        elif error_to_which_morpheme == 's':
            suffixes[i_morpheme] = morpheme_with_error
    d['error_word'] = ''.join(prefixes + [root] + suffixes)
    
    return d


def substitute_letter(letter):
    
    d_letter_groups = {}
    for group in ['vowels', 'consonants', 'sonorants']:
        d_letter_groups[group] = {}
    d_letter_groups['vowels']['letters'] = ["a", "e", "i", "o", "u"]
    d_letter_groups['vowels']['weights'] = [8.34, 12.60, 6.71, 7.7, 2.85]
    d_letter_groups['consonants']['letters'] = ["b", "c", "d", "f", "g", "h", "k", "p", "q", "s", "t", "v", "x", "z"]
    d_letter_groups['consonants']['weights'] = [1.54, 2.73, 4.14, 2.03, 1.92, 6.11, 0.87, 4.24,  0.09, 6.11, 9.37, 1.06, 0.20, 0.06]
    d_letter_groups['sonorants']['letters'] = ["j", "l", "m", "n", "r", "w", "y"]
    d_letter_groups['sonorants']['weights'] = [0.23, 2.53, 6.8, 1.66, 5.68, 2.34, 2.04]
    
    for group in d_letter_groups.keys():
        if letter in d_letter_groups[group]['letters']:
            letters, weights = d_letter_groups[group]['letters'], d_letter_groups[group]['weights']
            i_vowel = letters.index(letter)
            del letters[i_vowel], weights[i_vowel]
            error_letter = random.choices(letters, weights)
    
    return error_letter[0]