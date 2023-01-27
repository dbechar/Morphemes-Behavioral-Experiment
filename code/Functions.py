"""
#---- Functions----#

# This script does: 
    # - define vocals/consonants/sonorants and their frequencies
    # - create a function that generates random roots based on letter frequency
    # - create polymorphemic words using previously defined morphemes 
    # - create a function that generates mono-morphemic words based 
        on the polymorphemic words
    # - create a function that generates random errors for monomorphemes
    # - create a function that generates random errors for polymorphemes
    # - create a function that checks all words 
    
    
# Date: 24.01.2023

# Author: Deliane Bechar

"""
#---- Preperation ----
#---- Load libraries ----
import random 
import pandas as pd

# Set seed
random.seed(19)

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
        while word in root: 
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
        while word in root: 
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
        while word in root: 
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
        while word in root: 
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
        while word in root: 
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
        while word in root: 
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
         while word in root: 
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
        while word in root:
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
        while word in root:
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
        while word in root:
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


def generatePolymorphemes (dfprefixes, dfroots, dfsuffixes, value):
    prefixes = dfprefixes ["Prefix"].tolist()
    prefixes_weights = dfprefixes["PrefixFrequency"].tolist()
    prefix_pos = dfprefixes["PrefixPOS"].tolist()
    prefix_pos2 = dfprefixes["PrefixPOS2"].tolist()
    roots = dfroots["Root"].tolist()
    suffixes = dfsuffixes["Suffix"].tolist()
    suffixes_weights = dfsuffixes["SuffixFrequency"].tolist ()
    suffix_pos = dfsuffixes["SuffixPOS"].tolist()
    suffix_pos2 = dfsuffixes["SuffixPOS2"].tolist()
    newword = []
    num_of_conditions = 8
    prefix2 = []
    prefix1 = []
    root = []
    suffix1 = []
    suffix2 = []
    num_of_mor = []
    condition = []
    end = round (value/num_of_conditions)
    
    # condition 1: root
    for x in range (0, end):
        prefix2.append ("")
        prefix1.append ("")
        root.append ("".join(random.choices(roots)))
        suffix1.append ("")
        suffix2.append ("")
        newword.append (prefix2[x] + 
                        prefix1[x] + 
                        root[x] + 
                        suffix1[x] + 
                        suffix2[x])
        num_of_mor.append (1)
        condition.append("r")
        
    # condition 2: prefix + root (pr)
    for x in range (0, end):
        prefix2.append ("")
        prefix1.append ("".join (random.choices (prefixes, weights = prefixes_weights, cum_weights=(None), k = 1)))
        root.append ("".join(random.choices(roots)))
        suffix1.append ("")
        suffix2.append ("")
        newword.append (prefix2[x + end] +
                        prefix1[x + end] + 
                        root[x + end] + 
                        suffix1[x + end] + 
                        suffix2[x + end])
        num_of_mor.append (2)
        condition.append("pr")
    
    # condition 3: root + suffix
    for x in range (0, end):
        prefix2.append ("")
        prefix1.append ("")
        root.append ("".join(random.choices(roots)))
        suffix1.append ("".join(random.choices (suffixes, weights = suffixes_weights, cum_weights=(None), k = 1)))
        suffix2.append ("")
        newword.append (prefix2[x + 2 * end] + 
                        prefix1[x + 2 *  end] + 
                        root[x + 2 * end] + 
                        suffix1[x + 2 * end] + 
                        suffix2[x + 2 * end])
        num_of_mor.append (2)
        condition.append("rs")
        
    # condition 4: prefix + root + suffix
    for x in range (0, end):
        prefix2.append ("")
        prefix1.append ("".join(random.choices (prefixes, weights = prefixes_weights, cum_weights=(None), k = 1)))
        root.append ("".join(random.choices(roots)))
        suffix1.append ("".join(random.choices (suffixes, weights = suffixes_weights, cum_weights=(None), k = 1)))
        suffix2.append ("")
        newword.append (prefix2[x +3 *end] + 
                        prefix1[x + 3 * end] + 
                        root[x + 3 * end] + 
                        suffix1[x + 3 * end] + 
                        suffix2[x + 3 * end])
        num_of_mor.append (3)
        condition.append("prs")
    
    # condition 5: prefix + prefix + root
    for x in range (0, end):
        n_prefix2 = ("".join(random.choices (prefixes, weights = prefixes_weights, cum_weights=(None), k = 1)))
        n_prefix1 = ("".join(random.choices (prefixes, weights = prefixes_weights, cum_weights=(None), k = 1)))
        index_p2 = prefixes.index (n_prefix2)
        index_p1 = prefixes.index (n_prefix1)
        
        # Make sure that prefix1 and prefix2 are different
        while n_prefix1 == n_prefix2 or prefix_pos[index_p1] != prefix_pos2[index_p2]: 
            n_prefix2 = ("".join(random.choices (prefixes, weights = prefixes_weights, cum_weights=(None), k = 1)))
            index_p2 = prefixes.index (n_prefix2)
        
        prefix2.append (n_prefix2)
        prefix1.append (n_prefix1)
        root.append ("".join(random.choices(roots)))
        suffix1.append ("")
        suffix2.append ("")
        newword.append (prefix2[x + 4 * end] + 
                        prefix1[x + 4 * end] + 
                        root[x + 4 * end] + 
                        suffix1[x + 4 * end] + 
                        suffix2[x + 4 * end])
        num_of_mor.append (3)
        condition.append("ppr")
    
    # condition 6: root + suffix + suffix
    for x in range (0, end):
        n_suffix1 = ("".join(random.choices (suffixes, weights = suffixes_weights, cum_weights=(None), k = 1)))
        n_suffix2 = ("".join(random.choices (suffixes, weights = suffixes_weights, cum_weights=(None), k = 1)))
        index_s1 = suffixes.index (n_suffix1)
        index_s2 = suffixes.index (n_suffix2)
        
        # Make sure that suffix1 and suffix2 are different
        while n_suffix1 == n_suffix2 or suffix_pos[index_s1] != suffix_pos2[index_s2]: 
            n_suffix2 = ("".join(random.choices (suffixes, weights = suffixes_weights, cum_weights=(None), k = 1)))
            index_s2 = suffixes.index (n_suffix2)
        
        prefix2.append ("")
        prefix1.append ("")
        root.append ("".join((random.choices(roots))))
        suffix1.append (n_suffix1)
        suffix2.append (n_suffix2)
        newword.append (prefix2[x + 5 * end] + 
                        prefix1[x + 5 * end] + 
                        root[x + 5 * end] + 
                        suffix1[x + 5 * end] + 
                        suffix2[x + 5 * end])
        num_of_mor.append (3)
        condition.append("rss")
        
    # condition 7: prefix + root + suffix + suffix
    for x in range (0, end):
        n_suffix1 = ("".join(random.choices (suffixes, weights = suffixes_weights, cum_weights=(None), k = 1)))
        n_suffix2 = ("".join(random.choices (suffixes, weights = suffixes_weights, cum_weights=(None), k = 1)))
        index_s1 = suffixes.index (n_suffix1)
        index_s2 = suffixes.index (n_suffix2)
        
        # Make sure that suffix1 and suffix2 are different
        while n_suffix1 == n_suffix2 or suffix_pos[index_s1] != suffix_pos2[index_s2]: 
            n_suffix2 = ("".join(random.choices (suffixes, weights = suffixes_weights, cum_weights=(None), k = 1)))
            index_s2 = suffixes.index (n_suffix2)
            
        prefix2.append ("")
        prefix1.append ("".join(random.choices (prefixes, weights = prefixes_weights, cum_weights=(None), k = 1)))
        root.append ("".join(random.choices(roots)))
        suffix1.append (n_suffix1)
        suffix2.append (n_suffix2)
        newword.append (prefix2[x + 6*end] + 
                        prefix1[x + 6*end] + 
                        root[x + 6 * end] + 
                        suffix1[x + 6 * end] + 
                        suffix2[x + 6 * end])
        num_of_mor.append (4)
        condition.append("prss")
        
    # condition 8: prefix + prefix + root + suffix
    for x in range (0, end):
        n_prefix1 = ("".join(random.choices (prefixes, weights = prefixes_weights, cum_weights=(None), k = 1)))
        n_prefix2 = ("".join(random.choices (prefixes, weights = prefixes_weights, cum_weights=(None), k = 1)))
        index_p1 = prefixes.index (n_prefix1)
        index_p2 = prefixes.index (n_prefix2)
        
        # Make sure that prefix1 and prefix2 are different
        while n_prefix1 == n_prefix2 or prefix_pos[index_p1] != prefix_pos2[index_p2]: 
            n_prefix2 = ("".join(random.choices (prefixes, weights = prefixes_weights, cum_weights=(None), k = 1)))
            index_p2 = prefixes.index (n_prefix2)
    
        prefix2.append (n_prefix2)
        prefix1.append (n_prefix1) 
        root.append ("".join(random.choices(roots)))
        suffix1.append ("".join(random.choices (suffixes, weights = suffixes_weights, cum_weights=(None), k = 1)))
        suffix2.append ("")
        newword.append (prefix2[x + 7 * end] + 
                        prefix1[x + 7 * end] + 
                        root[x + 7 * end] + 
                        suffix1[x + 7 * end] + 
                        suffix2[x + 7 * end])
        num_of_mor.append (4)
        condition.append("pprs")
    
            
    df = pd.DataFrame()  
    df["Token"] = newword
    # df["Num_of_mor"] = num_of_mor
    df["Condition"] = condition
    df["Prefix2"] = prefix2
    df["Prefix1"] = prefix1
    df["Root"] = root 
    df["Suffix1"] = suffix1
    df["Suffix2"] = suffix2
    df["Wordlength"] = df["Token"].str.len()
    return df   

#---- Generate pseudowords (by reversing affixes) ----
# Input for function: 
    # - dataframe that has all of the necessary information (Prefi2, Prefix1, Root, Suffix1, Suffix2)

def generateMonomorphemes (df):
    prefix2 = df["Prefix2"].tolist()
    prefix1 = df["Prefix1"].tolist()
    root = df["Root"].tolist()                        
    suffix1 = df["Suffix1"].tolist()
    suffix2 = df["Suffix2"].tolist()
    monomorphemes = []
    mono_prefix2 = []
    mono_prefix1 = []
    mono_root = []
    mono_suffix1 = []
    mono_suffix2 = []
    
    for i in range(0, len (root)):
        monoprefix2 = prefix2[i]
        mono_prefix2.append (monoprefix2 [::-1])

        monoprefix1 = prefix1[i]
        mono_prefix1.append (monoprefix1[::-1])
        
        monoroot = root[i]
        monoroot = monoroot [::-1]
        while monoroot == root[i]: 
            monoroot = list (root[i])
            monoroot = random.sample (monoroot, k = len (monoroot))
            monoroot = "".join(monoroot)
    
        mono_root.append (monoroot)

        monosuffix1 = suffix1[i]
        mono_suffix1.append(monosuffix1[::-1])
        
        monosuffix2 = suffix2[i]
        mono_suffix2.append (monosuffix2[::-1])
        
        
        monomorphemes.append (monoprefix2 + 
                              monoprefix1 + 
                              monoroot + 
                              monosuffix1 + 
                              monosuffix2)
        
    df_Monomorpheme = pd.DataFrame ()
    df_Monomorpheme["Monomorpheme"] = monomorphemes
    df_Monomorpheme["MonoPrefix2"] = mono_prefix2
    df_Monomorpheme["MonoPrefix1"] = mono_prefix1
    df_Monomorpheme["MonoRoot"] = mono_root
    df_Monomorpheme["MonoSuffix1"] = mono_suffix1
    df_Monomorpheme["MonoSuffix2"] = mono_suffix2
        
    return df_Monomorpheme


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
                char = "".join(char)
            word[index] = "".join(char)
            # Finally save the string in the modified format in a second list (error_word).
            word = "".join(word)
            error_word.append (word)
        elif char in sonorants: 
            while char == word[index]:
                char = random.choices(sonorants, weights = sonorants_weights, cum_weights=(None), k = value)
                char = "".join(char)
            word[index] = "".join(char)
            # Finally save the string in the modified format in a second list (error_word).
            word = "".join(word)
            error_word.append (word)
        else: 
            while char == word[index]:
                char = random.choices(consonants, weights = consonant_weights, cum_weights=(None), k = value)
                char = "".join(char)
            word[index] = "".join(char)
            # Finally save the string in the modified format in a second list (error_word).
            word = "".join(word)
            error_word.append (word)  
            

#---- Function that creates new errorwords, where errors are in a specific morpheme----

# Input: either dataframe that includes all of that information OR list
    # - Dataframe in which information is supposed to be saved in 
def generateError (df): 
    prefix2 = df["Prefix2"].tolist() 
    prefix1 = df["Prefix1"].tolist()
    root = df["Root"].tolist() 
    suffix1 = df["Suffix1"].tolist()
    suffix2 = df["Suffix2"].tolist()
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
            error_suffix2.append (prefix2[i] + prefix1[i] + root[i] + suffix1[i] + esuffix2[i])
        
    df_Error = pd.DataFrame()
    df_Error["ErrorPrefix2"] = error_prefix2
    df_Error["ErrorPrefix1"] = error_prefix1
    df_Error["ErrorRoot"] = error_root
    df_Error["ErrorSuffix1"] = error_suffix1
    df_Error["ErrorSuffix2"] = error_suffix2
    df_Error["ChangedIndexP2"] = changed_index_p2
    df_Error["ChangedIndexP1"] = changed_index_p1
    df_Error["ChangedIndexR"] = changed_index_r
    df_Error["ChangedIndexS1"] = changed_index_s1
    df_Error["ChangedIndexS2"] = changed_index_s2
    
    return df_Error

    
def generateErrorMono (df): 
    prefix2 = df["MonoPrefix2"].tolist()
    prefix1 = df["MonoPrefix1"].tolist()
    root = df["MonoRoot"].tolist()
    suffix1 = df["MonoSuffix1"].tolist()
    suffix2 = df["MonoSuffix2"].tolist() 
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
            error_suffix2.append (prefix2[i] + prefix1[i] + root[i] + suffix1[i] + esuffix2[i])
        
    df_MonoError = pd.DataFrame()
    df_MonoError["MonoErrorPrefix2"] = error_prefix2
    df_MonoError["MonoErrorPrefix1"] = error_prefix1
    df_MonoError["MonoErrorRoot"] = error_root
    df_MonoError["MonoErrorSuffix1"] = error_suffix1
    df_MonoError["MonoErrorSuffix2"] = error_suffix2
    df_MonoError["MonoChangedIndexP2"] = changed_index_p2
    df_MonoError["MonoChangedIndexP1"] = changed_index_p1
    df_MonoError["MonoChangedIndexR"] = changed_index_r
    df_MonoError["MonoChangedIndexS1"] = changed_index_s1
    df_MonoError["MonoChangedIndexS2"] = changed_index_s2
    
    return df_MonoError



def generateParticipantFile (data, condition, p_error, p_polymor):
    # Define error distribution per condition (create function and put that all into function)
    errortype_r = ["NoErrorPoly"] * int (condition["r"] * 0.5) + ["Root"] * int (condition["r"] * 0.5)
    errortype_pr = ["NoErrorPoly"] * int (condition["pr"] * (1-p_error) * p_polymor) + ["Prefix1"] * int (condition["pr"] * p_error * p_polymor * 0.5) + ["Root"] * int (condition["pr"] * p_error * p_polymor * 0.5) + ["NoErrorMono"] * int (condition["pr"] * (1-p_error) * (1-p_polymor)) +["MonoPrefix1"] * int (condition["pr"] * p_error * (1-p_polymor) * 0.5) + ["MonoRoot"] * int (condition["pr"] * p_error * (1-p_polymor) * 0.5) 
    errortype_rs = ["NoErrorPoly"] * int (condition["rs"] * (1-p_error) * p_polymor) + ["Root"] * int (condition["rs"] * p_error * p_polymor * 0.5) +["Suffix1"] * int (condition["rs"] * p_error * p_polymor * 0.5) +  ["NoErrorMono"] * int (condition["rs"] * (1-p_error) * (1-p_polymor)) + ["MonoRoot"] * int (condition["rs"] * p_error * (1-p_polymor) * 0.5) + ["MonoSuffix1"] * int (condition["rs"] * p_error * (1-p_polymor) * 0.5) 
    errortype_prs = ["NoErrorPoly"] * int (condition["prs"] * (1-p_error) * p_polymor) + ["Prefix1"] * int (condition["prs"] * p_error * p_polymor * (1/3)) + ["Root"] * int (condition["prs"] * p_error * p_polymor * (1/3)) + ["Suffix1"] * int (condition["prs"] * p_error * p_polymor * (1/3)) + ["NoErrorMono"] * int (condition["prs"] * (1-p_error) * (1-p_polymor)) + ["MonoPrefix1"] * int (condition["prs"] * p_error * (1-p_polymor) * (1/3)) + ["MonoRoot"] * int (condition["prs"] * p_error * (1-p_polymor) * (1/3)) + ["MonoSuffix1"] * int (condition["prs"] * p_error * (1-p_polymor) * (1/3))  
    errortype_ppr = ["NoErrorPoly"] * int (condition["ppr"] * (1-p_error) * p_polymor) + ["Prefix2"] * int (condition["ppr"] * p_error * p_polymor * (1/3)) + ["Prefix1"] * int (condition["ppr"] * p_error * p_polymor * (1/3)) + ["Root"] * int (condition["ppr"] * p_error * p_polymor * (1/3)) + ["NoErrorMono"] * int (condition["ppr"] * (1-p_error) * (1-p_polymor)) + ["MonoPrefix2"] * int (condition["ppr"] * p_error * (1-p_polymor) * (1/3)) + ["MonoPrefix1"] * int (condition["ppr"] * p_error * (1-p_polymor) * (1/3)) + ["MonoRoot"] * int (condition["ppr"] * p_error * (1-p_polymor) * (1/3)) 
    errortype_rss = ["NoErrorPoly"] * int (condition["rss"] * (1-p_error) * p_polymor)+ ["Root"] * int (condition["rss"] * p_error * p_polymor * (1/3)) + ["Suffix1"] * int (condition["rss"] * p_error * p_polymor * (1/3))  + ["Suffix2"] * int (condition["rss"] * p_error * p_polymor * (1/3)) + ["NoErrorMono"] * int (condition["rss"] * (1-p_error) * (1-p_polymor)) + ["MonoRoot"] * int (condition["rss"] * p_error * (1-p_polymor) * (1/3)) + ["MonoSuffix1"] * int (condition["rss"] * p_error * (1-p_polymor) * (1/3)) + ["MonoSuffix2"] * int (condition["rss"] * p_error * (1-p_polymor) * (1/3))
    errortype_prss =["NoErrorPoly"] * int (condition["prss"] * (1-p_error) * p_polymor)+ ["Prefix1"] * int (condition["prss"] * p_error * p_polymor * (1/4)) + ["Root"] * int (condition["prss"] * p_error * p_polymor * (1/4)) + ["Suffix1"] * int (condition["prss"] * p_error * p_polymor * (1/4))  + ["Suffix2"] * int (condition["prss"] * p_error * p_polymor * (1/4)) + ["NoErrorMono"] * int (condition["prss"] * (1-p_error) * (1-p_polymor)) + ["MonoPrefix1"] * int (condition["prss"] * p_error * (1-p_polymor) * (1/4)) + ["MonoRoot"] * int (condition["prss"] * p_error * (1-p_polymor) * (1/4)) + ["MonoSuffix1"] * int (condition["prss"] * p_error * (1-p_polymor) * (1/4)) + ["MonoSuffix2"] * int (condition["prss"] * p_error * (1-p_polymor) * (1/4))
    errortype_pprs = ["NoErrorPoly"] * int (condition["pprs"] * (1-p_error) * p_polymor)+ ["Prefix2"] * int (condition["pprs"] * p_error * p_polymor * (1/4)) + ["Prefix1"] * int (condition["pprs"] * p_error * p_polymor * (1/4)) +["Root"] * int (condition["pprs"] * p_error * p_polymor * (1/4)) + ["Suffix1"] * int (condition["pprs"] * p_error * p_polymor * (1/4))  + ["NoErrorMono"] * int (condition["pprs"] * (1-p_error) * (1-p_polymor)) + ["MonoPrefix2"] * int (condition["pprs"] * p_error * (1-p_polymor) * (1/4)) + ["MonoPrefix1"] * int (condition["pprs"] * p_error * (1-p_polymor) * (1/4)) + ["MonoRoot"] * int (condition["pprs"] * p_error * (1-p_polymor) * (1/4)) + ["MonoSuffix1"] * int (condition["pprs"] * p_error * (1-p_polymor) * (1/4)) 

    # randomly pick ncondition-times trials per condition and save in in a df
    r = data.query("Condition == 'r'").sample (n = condition["r"])
    r.insert(0, "errortype", errortype_r)
    pr = data.query("Condition == 'pr'").sample (n = condition["pr"])
    pr.insert(0, "errortype", errortype_pr)
    rs = data.query("Condition == 'rs'").sample (n = condition["rs"])
    rs.insert(0, "errortype", errortype_rs)
    prs = data.query("Condition == 'prs'").sample (n = condition["prs"])
    prs.insert(0, "errortype", errortype_prs)
    ppr = data.query("Condition == 'ppr'").sample (n = condition["ppr"])
    ppr.insert(0, "errortype", errortype_ppr)
    rss = data.query("Condition == 'rss'").sample (n = condition["rss"])
    rss.insert(0, "errortype", errortype_rss)
    prss = data.query("Condition == 'prss'").sample (n = condition["prss"])
    prss.insert(0, "errortype", errortype_prss)
    pprs = data.query("Condition == 'pprs'").sample (n = condition["pprs"])   
    pprs.insert(0, "errortype", errortype_pprs)
                                        
    pardf= pd.concat ([r,pr,rs, prs, ppr, rss, prss, pprs])
    
    # Add Information if it is an error trial: 1 = True; 0 = False
    is_error = []
    for i in range (0, len(pardf)):
        errortype = pardf["errortype"].tolist()
        if errortype [i] == "NoErrorMono" or  errortype [i] == "NoErrorPoly": 
            is_error.append (0)
        else: 
            is_error.append (1)
            
    pardf.insert (1, "Is_Error", is_error)

    return pardf



def generateTriallist (df):
    # Define necessary variables
    word1 = []
    word2 = []
    token = df["Token"].tolist()
    errortype = df["errortype"].tolist()
    monomorpheme = df["Monomorpheme"].tolist()
    errorprefix2 = df["ErrorPrefix2"].tolist()
    errorprefix1 = df["ErrorPrefix1"].tolist()
    errorroot = df["ErrorRoot"].tolist()
    errorsuffix1 = df["ErrorSuffix1"].tolist()
    errorsuffix2 = df["ErrorSuffix2"].tolist()
    monoerrorprefix2 = df["MonoErrorPrefix2"].tolist()
    monoerrorprefix1 = df["MonoErrorPrefix1"].tolist()
    monoerrorroot = df["MonoErrorRoot"].tolist()
    monoerrorsuffix1 = df["MonoErrorSuffix1"].tolist()
    monoerrorsuffix2 = df["MonoErrorSuffix2"].tolist()
    
    
    for i in range (0, len (df)): 
        # In case of errortrial (Polymorpheme)
        if errortype[i] == "Prefix2": 
            word1.append (token[i])
            word2.append (errorprefix2[i])
        elif errortype[i] == "Prefix1": 
            word1.append (token[i])
            word2.append (errorprefix1[i])
        elif errortype[i] == "Root": 
            word1.append (token[i])
            word2.append (errorroot[i])
        elif errortype[i] == "Suffix1": 
            word1.append (token[i])
            word2.append (errorsuffix1[i])
        elif errortype[i] == "Suffix2": 
            word1.append (token[i])
            word2.append (errorsuffix2[i])
            
        # In case of errortrial (Monomorpheme):
        elif errortype[i] == "MonoPrefix2": 
            word1.append (monomorpheme[i])
            word2.append (monoerrorprefix2[i])
        elif errortype[i] == "MonoPrefix1": 
            word1.append (monomorpheme[i])
            word2.append (monoerrorprefix1[i])
        elif errortype[i] == "MonoRoot": 
            word1.append (monomorpheme[i])
            word2.append (monoerrorroot[i])
        elif errortype[i] == "MonoSuffix1": 
            word1.append (monomorpheme[i])
            word2.append (monoerrorsuffix1[i])
        elif errortype[i] == "MonoPrefix2": 
            word1.append (monomorpheme[i])
            word2.append (monoerrorsuffix2[i])
        
        # In case of no errortrial (Monomorpheme):
        elif errortype[i] == "NoErrorPoly":
            word1.append(token[i])
            word2.append(token[i])
        
        # In case of no errortrial (Polymorpheme):
        else: 
            word1.append(monomorpheme[i])
            word2.append(monomorpheme[i])
    df.insert(0, "Word1", word1)
    df.insert(1, "Word2", word2)
    
    # randomize order
    df = df.sample (frac=1)
    return df

def verifyWords (df):
    # See if end of prefix1 and beginning of root make sense together (Poylmorpheme)
    prefixroot = []
    prefix1 = df["Prefix1"].tolist()
    root = df["Root"].tolist()
    
    for i in range (0, len(df)): 
        # if there is a prefix 1 check how well it goes with the root 
        if prefix1[i] != "": 
            if prefix1[i][-1] != root[i][0]:
                prefixroot.append ("0")
            else: 
                prefixroot.append ("1")
        # if there is no prefix1 then: 
        else: 
            prefixroot.append ("0")
    
    
    # See if end of root and beginning of sufffix 1 make sense together (Polymorpheme)
    suffixroot = []
    suffix1 = df["Suffix1"].tolist()
    root = df["Root"].tolist()

    for i in range (0, len(df)): 
        # if there is a prefix 1 check how well it goes with the root 
        if suffix1[i] != "": 
            if root[i][-1] != suffix1[i][0]:
                suffixroot.append ("0")
            else: 
                suffixroot.append ("1")
        # if there is no prefix1 then: 
        else: 
            suffixroot.append ("0")
            
            
    # See if end of prefix2 and beginning of prefix1 make sense together (Monomorpheme)
    monoprefixprefix = []
    monoprefix1 = df["MonoPrefix1"].tolist()
    monoprefix2 = df["MonoPrefix2"].tolist()
    
    for i in range (0, len(df)): 
        # if there is a prefix 1 check how well it goes with the root 
        if monoprefix1[i] != "" and monoprefix2[i] != "": 
            if monoprefix1[i][-1] != monoprefix2[i][0]:
                monoprefixprefix.append ("0")
            else: 
                monoprefixprefix.append ("1")
        # if there is no prefix1 then: 
        else: 
            monoprefixprefix.append ("0")        
    
    
    # See if end of prefix1 and beginning of root make sense together (Monomorpheme)
    monoprefixroot = []
    monoprefix1 = df["MonoPrefix1"].tolist()
    monoroot = df["MonoRoot"].tolist()
    
    for i in range (0, len(df)): 
        # if there is a prefix 1 check how well it goes with the root 
        if monoprefix1[i] != "": 
            if monoprefix1[i][-1] != monoroot[i][0]:
                monoprefixroot.append ("0")
            else: 
                monoprefixroot.append ("1")
        # if there is no prefix1 then: 
        else: 
            monoprefixroot.append ("0")
    
    
    # See if end of root and beginning of sufffix 1 make sense together (Monomorpheme)
    monosuffixroot = []
    monosuffix1 = df["MonoSuffix1"].tolist()
    monoroot = df["MonoRoot"].tolist()
    
    for i in range (0, len(df)): 
        # if there is a prefix 1 check how well it goes with the root 
        if monosuffix1[i] != "": 
            if monoroot[i][-1] != monosuffix1[i][0]:
                monosuffixroot.append ("0")
            else: 
                monosuffixroot.append ("1")
        # if there is no prefix1 then: 
        else: 
            monosuffixroot.append ("0")

    
    # See if end of suffix1 and beginning of suffix2 make sense together (Monomorpheme)
    monosuffixsuffix = []
    monosuffix1 = df["MonoSuffix1"].tolist()
    monosuffix2 = df["MonoSuffix2"].tolist()
    
    for i in range (0, len(df)): 
        # if there is a prefix 1 check how well it goes with the root 
        if monosuffix1[i] != "" and monosuffix2[i] != "": 
            if monosuffix1[i][-1] != monosuffix2[i][0]:
                monosuffixsuffix.append ("0")
            else: 
                monosuffixsuffix.append ("1")
        # if there is no prefix1 then: 
        else: 
            monosuffixsuffix.append ("0")


    # Save all rows in which the same letters appear right after another in a list (these rows will be removed)
    indexlist = []
    for i in range (0, len(df)): 
        if prefixroot[i] == "1" or monoprefixroot[i] == "1" or suffixroot[i] == "1" or monosuffixroot[i] == "1" or monosuffixsuffix[i] == "1" or monoprefixprefix == "1": 
            indexlist.append (i)
        
    df.drop (df.index[indexlist], inplace = True)
    
    return df



