"""
#----This script does: ----

    # - define vocals/consonants and their frequencies
    # - create a function that generates random roots based on letter frequency
    # - create polymorphemic words using previously defined morphemes 
    # - create a function that generates pseudowords (mono-morphemic words) based 
        on the polymorphemic words
    # - create function that generates random errors
    
Date: 24.01.2023

Author: Deliane Bechar

"""

#---- Load necessary libraries ----
import random 
import pandas as pd

#---- Generate random roots based on letter frequency ----
# source for weights: https://www.sttmedia.com/characterfrequency-english

# Input: List in which words are supposed to be saved and number of new words that are supposed to be created (only creates a multiples of 10)
# Output: List full of words
    
def generateRoots (value):
    root = []
    vowels=["a", "e", "i", "o", "u"]
    vowel_weights=[8.34, 12.60, 6.71, 7.7, 2.85]
    consonants=["b", "c", "d", "f", "g", "h", "k",
                "p", "q", "s", "t", "v", "x", "z"]
    consonant_weights=[1.54, 2.73, 4.14, 2.03, 1.92, 6.11, 0.87, 
                       4.24,  0.09, 6.11, 9.37, 1.06, 0.20, 0.06]
    sonorants = ["j", "l", "m", "n", "r", "w", "y"]
    sonorants_weights = [0.23, 2.53, 6.8, 1.66, 5.68, 2.34, 2.04]
    num_of_patterns = 10
    
    # pattern 1 = cvc
    for index in range (0, round (value/num_of_patterns)): 
        word = []
        word = (random.choices(consonants, weights = consonant_weights, cum_weights=(None), k = 1) + 
                random.choices(vowels, weights = vowel_weights, cum_weights=(None), k = 1) + 
                random.choices(consonants, weights = consonant_weights, cum_weights=(None), k = 1))
        root.append ("".join(word))
    # pattern 2 = vcv
    for index in range (0, round (value/num_of_patterns)): 
        word = []
        word = (random.choices(vowels, weights = vowel_weights, cum_weights=(None), k = 1) + 
                random.choices(consonants, weights = consonant_weights, cum_weights=(None), k = 1) + 
                random.choices(vowels, weights = vowel_weights, cum_weights=(None), k = 1))
        root.append ("".join(word))
    # pattern 3 = cvcv
    for index in range (0, round (value/num_of_patterns)): 
        word = []
        word = (random.choices(consonants, weights = consonant_weights, cum_weights=(None), k = 1) +
                random.choices(vowels, weights = vowel_weights, cum_weights=(None), k = 1) + 
                random.choices(consonants, weights = consonant_weights, cum_weights=(None), k = 1) +
                random.choices(vowels, weights = vowel_weights, cum_weights=(None), k = 1))
        root.append ("".join(word))
    # pattern 4: vcvc
    for index in range (0, round (value/num_of_patterns)): 
        word = []
        word = (random.choices(vowels, weights = vowel_weights, cum_weights=(None), k = 1) + 
                random.choices(consonants, weights = consonant_weights, cum_weights=(None), k = 1) +
                random.choices(vowels, weights = vowel_weights, cum_weights=(None), k = 1) + 
                random.choices(consonants, weights = consonant_weights, cum_weights=(None), k = 1))
        root.append ("".join(word))
    # pattern 5: cvcvc
    for index in range (0, round (value/num_of_patterns)): 
        word = []
        word = (random.choices(consonants, weights = consonant_weights, cum_weights=(None), k = 1) +
                random.choices(vowels, weights = vowel_weights, cum_weights=(None), k = 1) + 
                random.choices(consonants, weights = consonant_weights, cum_weights=(None), k = 1) +
                random.choices(vowels, weights = vowel_weights, cum_weights=(None), k = 1) + 
                random.choices(consonants, weights = consonant_weights, cum_weights=(None), k = 1))
        root.append ("".join(word))
    # pattern 6: vscv
    for index in range (0, round (value/num_of_patterns)): 
        word = []
        word = (random.choices(vowels, weights = vowel_weights, cum_weights=(None), k = 1) +
                random.choices(sonorants, weights = sonorants_weights, cum_weights=(None), k = 1) + 
                random.choices(consonants, weights = consonant_weights, cum_weights=(None), k = 1) +
                random.choices(vowels, weights = vowel_weights, cum_weights=(None), k = 1))
        root.append ("".join(word))
    # pattern 7: vsc
    for index in range (0, round (value/num_of_patterns)): 
         word = []
         word = (random.choices(vowels, weights = vowel_weights, cum_weights=(None), k = 1) +
                 random.choices(sonorants, weights = sonorants_weights, cum_weights=(None), k = 1) + 
                 random.choices(consonants, weights = consonant_weights, cum_weights=(None), k = 1))
         root.append ("".join(word))    
    # pattern 8: svsc
    for index in range (0, round (value/num_of_patterns)): 
        word = []
        word = (random.choices(sonorants, weights = sonorants_weights, cum_weights=(None), k = 1) + 
                random.choices(vowels, weights = vowel_weights, cum_weights=(None), k = 1) +
                random.choices(sonorants, weights = sonorants_weights, cum_weights=(None), k = 1) + 
                random.choices(consonants, weights = consonant_weights, cum_weights=(None), k = 1))
        root.append ("".join(word))
    # pattern 9: svc
    for index in range (0, round (value/num_of_patterns)): 
        word = []
        word = (random.choices(sonorants, weights = sonorants_weights, cum_weights=(None), k = 1) + 
                random.choices(vowels, weights = vowel_weights, cum_weights=(None), k = 1) + 
                random.choices(consonants, weights = consonant_weights, cum_weights=(None), k = 1))
        root.append ("".join(word))
    # pattern 10: cvs
    for index in range (0, round (value/num_of_patterns)): 
        word = []
        word = (random.choices(consonants, weights = consonant_weights, cum_weights=(None), k = 1) + 
                random.choices(vowels, weights = vowel_weights, cum_weights=(None), k = 1) + 
                random.choices(sonorants, weights = sonorants_weights, cum_weights=(None), k = 1))
        root.append ("".join(word))
    return root



#---- Generate polymorphemic words ----
# 1. If there are two prefixes or suffixes make sure that they are of the same or the same type
# Input for function: 
    # - List of all prefixes, suffixes, and roots
    # - List of frequency of prefix and suffix (to be used as weights)
    # - Value: How many words should be created
    # - Output: Dataframe that includes infromation about the Polymorphemes


def generatePolymorphemes (prefixes, prefixes_weights, prefix_pos, roots, suffixes, suffixes_weights, suffix_pos, value):
    df = pd.DataFrame()
    newword = []
    num_of_conditions = 7
    prefix2 = []
    prefix1 = []
    root = []
    suffix1 = []
    suffix2 = []
    num_of_mor = []
    condition = []
    end = round (value/num_of_conditions)
    
    # condition 1: prefix + root (pr)
    for x in range (0, end):
        prefix2.append ("")
        prefix1.append ("".join (random.choices (prefixes, weights = prefixes_weights, cum_weights=(None), k = 1)))
        root.append ("".join(random.choices(roots)))
        suffix1.append ("")
        suffix2.append ("")
        newword.append (prefix2[x] + 
                        prefix1[x] + 
                        root[x] + 
                        suffix1[x] + 
                        suffix2[x])
        num_of_mor.append (2)
        condition.append("pr")
    
    # condition 2: root + suffix
    for x in range (0, end):
        prefix2.append ("")
        prefix1.append ("")
        root.append ("".join(random.choices(roots)))
        suffix1.append ("".join(random.choices (suffixes, weights = suffixes_weights, cum_weights=(None), k = 1)))
        suffix2.append ("")
        newword.append (prefix2[x + end] + 
                        prefix1[x + end] + 
                        root[x + end] + 
                        suffix1[x + end] + 
                        suffix2[x + end])
        num_of_mor.append (2)
        condition.append("rs")
        
    # condition 3: prefix + root + suffix
    for x in range (0, end):
        prefix2.append ("")
        prefix1.append ("".join(random.choices (prefixes, weights = prefixes_weights, cum_weights=(None), k = 1)))
        root.append ("".join(random.choices(roots)))
        suffix1.append ("".join(random.choices (suffixes, weights = suffixes_weights, cum_weights=(None), k = 1)))
        suffix2.append ("")
        newword.append (prefix2[x +2 *end] + 
                        prefix1[x + 2 * end] + 
                        root[x + 2 * end] + 
                        suffix1[x + 2 * end] + 
                        suffix2[x + 2 * end])
        num_of_mor.append (3)
        condition.append("prs")
    
    # condition 4: prefix + prefix + root
    for x in range (0, end):
        n_prefix1 = ("".join(random.choices (prefixes, weights = prefixes_weights, cum_weights=(None), k = 1)))
        n_prefix2 = ("".join(random.choices (prefixes, weights = prefixes_weights, cum_weights=(None), k = 1)))
        index_p1 = prefixes.index (n_prefix1)
        index_p2 = prefixes.index (n_prefix2)
        
        # Make sure that prefix1 and prefix2 are different
        while n_prefix1 == n_prefix2 and prefix_pos[index_p1] != prefix_pos[index_p2]: 
            n_prefix2 = ("".join(random.choices (prefixes, weights = prefixes_weights, cum_weights=(None), k = 1)))
            index_p2 = prefixes.index (n_prefix2)
        
        prefix2.append (n_prefix2)
        prefix1.append (n_prefix1)
        root.append ("".join(random.choices(roots)))
        suffix1.append ("")
        suffix2.append ("")
        newword.append (prefix2[x + 3 * end] + 
                        prefix1[x + 3 * end] + 
                        root[x + 3 * end] + 
                        suffix1[x + 3 * end] + 
                        suffix2[x + 3 * end])
        num_of_mor.append (3)
        condition.append("ppr")
    
    # condition 5: root + suffix + suffix
    for x in range (0, end):
        n_suffix1 = ("".join(random.choices (suffixes, weights = suffixes_weights, cum_weights=(None), k = 1)))
        n_suffix2 = ("".join(random.choices (suffixes, weights = suffixes_weights, cum_weights=(None), k = 1)))
        index_s1 = suffixes.index (n_suffix1)
        index_s2 = suffixes.index (n_suffix2)
        
        # Make sure that suffix1 and suffix2 are different
        while n_suffix1 == n_suffix2 and index_s1 != index_s2: 
            n_suffix2 = ("".join(random.choices (suffixes, weights = suffixes_weights, cum_weights=(None), k = 1)))
            index_s2 = suffixes.index (n_suffix2)
        
        prefix2.append ("")
        prefix1.append ("")
        root.append ("".join((random.choices(roots))))
        suffix1.append (n_suffix1)
        suffix2.append (n_suffix2)
        newword.append (prefix2[x + 4 * end] + 
                        prefix1[x + 4 * end] + 
                        root[x + 4 * end] + 
                        suffix1[x + 4 * end] + 
                        suffix2[x + 4 * end])
        num_of_mor.append (3)
        condition.append("rss")
        
    # condition 6: prefix + root + suffix + suffix
    for x in range (0, end):
        n_suffix1 = ("".join(random.choices (suffixes, weights = suffixes_weights, cum_weights=(None), k = 1)))
        n_suffix2 = ("".join(random.choices (suffixes, weights = suffixes_weights, cum_weights=(None), k = 1)))
        index_s1 = suffixes.index (n_suffix1)
        index_s2 = suffixes.index (n_suffix2)
        
        # Make sure that suffix1 and suffix2 are different
        while n_suffix1 == n_suffix2 and index_s1 != index_s2: 
            n_suffix2 = ("".join(random.choices (suffixes, weights = suffixes_weights, cum_weights=(None), k = 1)))
            index_s2 = suffixes.index (n_suffix2)
            
        prefix2.append ("")
        prefix1.append ("".join(random.choices (prefixes, weights = prefixes_weights, cum_weights=(None), k = 1)))
        root.append ("".join(random.choices(roots)))
        suffix1.append (n_suffix1)
        suffix2.append (n_suffix2)
        newword.append (prefix2[x + 5*end] + 
                        prefix1[x + 5*end] + 
                        root[x + 5 * end] + 
                        suffix1[x + 5 * end] + 
                        suffix2[x + 5 * end])
        num_of_mor.append (4)
        condition.append("prss")
        
    # condition 7: prefix + prefix + root + suffix
    for x in range (0, end):
        n_prefix1 = ("".join(random.choices (prefixes, weights = prefixes_weights, cum_weights=(None), k = 1)))
        n_prefix2 = ("".join(random.choices (prefixes, weights = prefixes_weights, cum_weights=(None), k = 1)))
        index_p1 = prefixes.index (n_prefix1)
        index_p2 = prefixes.index (n_prefix2)
        
        # Make sure that prefix1 and prefix2 are different
        while n_prefix1 == n_prefix2 and prefix_pos[index_p1] != prefix_pos[index_p2]: 
            n_prefix2 = ("".join(random.choices (prefixes, weights = prefixes_weights, cum_weights=(None), k = 1)))
            index_p2 = prefixes.index (n_prefix2)
    
        prefix2.append (n_prefix2)
        prefix1.append (n_prefix1) 
        root.append ("".join(random.choices(roots)))
        suffix1.append ("".join(random.choices (suffixes, weights = suffixes_weights, cum_weights=(None), k = 1)))
        suffix2.append ("")
        newword.append (prefix2[x + 6 * end] + 
                        prefix1[x + 6 * end] + 
                        root[x + 6 * end] + 
                        suffix1[x + 6 * end] + 
                        suffix2[x + 6 * end])
        num_of_mor.append (4)
        condition.append("pprs")
        
    df["newword"] = newword
    df["num_of_mor"] = num_of_mor
    df["condition"] = condition
    df["prefix2"] = prefix2
    df["prefix1"] = prefix1
    df["root"] = root 
    df["suffix1"] = suffix1
    df["suffix2"] = suffix2
    return df   

#---- Generate random pseudowords ----

# Input for function: 
    # - list for each morpheme 
    # - list in which new pseudowords are supposed to be saved in 


def generateMonomorphemes (prefix2, prefix1, root, suffix1, suffix2, newword, condition):
    for i in range(0, len (root)):
        pseudoprefix2 = prefix2[i]
        if prefix2[i] == "":
            pseudoprefix2 = ""
            
        else: 
            while pseudoprefix2 == prefix2[i]: 
                pseudoprefix2 = list (prefix2[i])
                pseudoprefix2 = random.sample (pseudoprefix2, k = len (pseudoprefix2))
                pseudoprefix2 = "".join(pseudoprefix2)
        prefix2.append (pseudoprefix2)

        pseudoprefix1 = prefix1[i]
        if prefix1 [i] == "":
            pseudoprefix1 = ""
        else:
            while pseudoprefix1 == prefix1[i]:
                pseudoprefix1 = list (prefix1[i])
                pseudoprefix1 = random.sample (pseudoprefix1, k = len (pseudoprefix1))
                pseudoprefix1 = "".join(pseudoprefix1)
        prefix1.append (pseudoprefix1)
        
        pseudoroot = root[i]
        if root[i] == "": 
            pseudoroot = ""
        else: 
            while pseudoroot == root[i]: 
                pseudoroot = list (root[i])
                pseudoroot = random.sample (pseudoroot, k = len (pseudoroot))
                pseudoroot = "".join(pseudoroot)
        root.append (pseudoroot)
        
        pseudosuffix1 = suffix1[i]
        if suffix1 [i] == "": 
            pseudosuffix1 = ""
        else:  
            while pseudosuffix1 == suffix1[i]: 
                pseudosuffix1 = list (suffix1[i])
                pseudosuffix1 = random.sample (pseudosuffix1, k = len (pseudosuffix1))
                pseudosuffix1 = "".join(pseudosuffix1)
        suffix1.append(pseudosuffix1)
        
        pseudosuffix2 = suffix2[i]
        if suffix2 [i] == "": 
            pseudosuffix2 = ""
        else:
            while pseudosuffix2 == suffix2[i]:
                pseudosuffix2 = list (suffix2[i])
                pseudosuffix2 = random.sample (pseudosuffix2, k = len (pseudosuffix2))
                pseudosuffix2 = "".join(pseudosuffix2)
        suffix2.append (pseudosuffix2)
        
        condition.append ("r")
        newword.append (pseudoprefix2 + 
                        pseudoprefix1 + 
                        pseudoroot + 
                        pseudosuffix1 + 
                        pseudosuffix2)
        
    df = pd.DataFrame({
        "Token": newword,
        "Condition": condition, 
        "Prefix2": prefix2, 
        "Prefix1": prefix1, 
        "Root": root, 
        "Suffix1": suffix1, 
        "Suffix2": suffix2
        })
    # df["Wordlength"] = df["Token"].str.len()
        
    return df

#---- Generate random errors ----
# Input: 
    # - word: The word in which letters should change
    # - value: the number of letters that change within word
    # - list in which words with errors are supposed to be saved
# Output:
    # - list in which words with errors are saved
    
# Randomly chooses one letter of word to change with another letter 
def randomlyChangeNChar(word, value, changed_index, error_word):
    # Define necessary variables for function
    vowels=["a", "e", "i", "o", "u"]
    vowel_weights=[8.34, 12.60, 6.71, 7.7, 2.85]
    consonants=["b", "c", "d", "f", "g", "h", "k",
                "p", "q", "s", "t", "v", "x", "z"]
    consonant_weights=[1.54, 2.73, 4.14, 2.03, 1.92, 6.11, 0.87, 
                       4.24,  0.09, 6.11, 9.37, 1.06, 0.20, 0.06]
    sonorants = ["j", "l", "m", "n", "r", "w", "y"]
    sonorants_weights = [0.23, 2.53, 6.8, 1.66, 5.68, 2.34, 2.04]
    
    length = len(word)
    word = list(word)
    
    # This will select the distinct index for us to replace
    k = random.sample(range(0, length), value) 
    
    for index in k:
        # This will replace the characters at the specified index with the generated characters
        char = word[index]
        
        # Save which index will change
        changed_index.append (index)
        
        if char in vowels: 
            while char == word[index]:
                char = random.choices(vowels, weights = vowel_weights, cum_weights=(None), k = value)
                word[index] = "".join(char)
            # Finally save the string in the modified format in a second list (second_word).
            word = "".join(word)
            error_word.append (word)
        elif char in sonorants: 
            while char == word[index]:
                char = random.choices(sonorants, weights = sonorants_weights, cum_weights=(None), k = value)
                word[index] = "".join(char)
            # Finally save the string in the modified format in a second list (second_word).
            word = "".join(word)
            error_word.append (word)
        else: 
            while char == word[index]:
                char = random.choices(consonants, weights = consonant_weights, cum_weights=(None), k = value)
                word[index] = "".join(char)
            # Finally save the string in the modified format in a second list (second_word).
            word = "".join(word)
            error_word.append (word)  
            

#---- Function that creates new errorwords, where errors are in a specific morpheme----

# Input: either dataframe that includes all of that information OR list
    # - Dataframe in which information is supposed to be saved in 
def generateError (prefix1, prefix2, root, suffix1, suffix2, df): 
       
    eprefix1 = []
    eprefix2 = []
    eroot = []
    esuffix1 = []
    esuffix2 = []
    error_prefix2 = []
    error_prefix1 = []
    error_root = []
    error_suffix1 = []
    error_suffix2 = []
    changed_index_p2 = []
    changed_index_p1 = []
    changed_index_r = []
    changed_index_s1 = []
    changed_index_s2 = []

    for i in range (0, len (root)):
        if prefix2[i] == "": 
            error_prefix2.append("")
            changed_index_p2.append ("")
            eprefix2.append ("")
        else: 
            randomlyChangeNChar(word = prefix2[i], value = 1, changed_index = changed_index_p2, error_word = eprefix2)
            error_prefix2.append (eprefix2[i] + prefix1[i] + root [i] + suffix1[i] + suffix2[i])
        
        if prefix1[i] == "": 
            error_prefix1.append("")
            changed_index_p1.append("")
            eprefix1.append("")
        else: 
            randomlyChangeNChar(word = prefix1[i], value = 1, changed_index = changed_index_p1, error_word = eprefix1)
            error_prefix1.append (prefix2[i] + eprefix1[i] + root [i] + suffix1[i] + suffix2[i])
            
        if root[i] == "": 
            error_root.append("")
            changed_index_r.append ("")
            eroot.append ("")
        else: 
            randomlyChangeNChar(word = root[i], value = 1, changed_index=changed_index_r, error_word = eroot)
            error_root.append (prefix2[i] + prefix1[i] + eroot [i] + suffix1[i] + suffix2[i])
        
        if suffix1[i] == "": 
            error_suffix1.append("")
            changed_index_s1.append("")
            esuffix1.append("")
        else: 
            randomlyChangeNChar(word = suffix1[i], value = 1, changed_index = changed_index_s1, error_word = esuffix1)
            error_suffix1.append (prefix2[i] + prefix1[i] + root [i] + esuffix1[i] + suffix2[i])
        
        if suffix2[i] == "": 
            error_suffix2.append("")
            changed_index_s2.append("")
            esuffix2.append("")
        else: 
            randomlyChangeNChar(word = suffix2[i], value = 1, changed_index = changed_index_s2, error_word = esuffix2)
            error_suffix2.append (prefix2[i] + prefix1[i] + root [i] + suffix1[i] + esuffix2[i])
        

    df["ErrorPrefix2"] = error_prefix2
    df["ErrorPrefix1"] = error_prefix1
    df["ErrorRoot"] = error_root
    df["ErrorSuffix1"] = error_suffix1
    df["ErrorSuffix2"] = error_suffix2
    df["ChangedIndexP2"] = changed_index_p2
    df["ChangedIndexP1"] = changed_index_p1
    df["ChangedIndexR"] = changed_index_r
    df["ChangedIndexS1"] = changed_index_s1
    df["ChangedIndexS2"] = changed_index_s2
    
    return df

    


