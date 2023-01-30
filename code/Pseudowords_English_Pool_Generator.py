"""
#---- Pseudowords: English Pool----#

# This script does:
    # - read in stimulus lists
    # - randomly creates roots
    # - randomly creates polymorphemic words
    # - randomly creates mono-morphemic words
    # - create all errorwords for created words
    # - generate a pool of English Pseudowords 
    # - save pool as .csv (under Experimentdesign?)

-> Just change values in stimulus creater:
    1. Create Roots and make sure that there are no accidental real words
    2. Use updated roots to create all words and all additional information

Author: Deliane Bechar

Date: 24.01.2023

"""
#---- Preperation ----
# Load libraries
import os
os.chdir("C:/Users/delia/OneDrive/Desktop/Morphemes/Morphemes/Code")
import pandas as pd
from Functions import (generateRoots, generatePolymorphemes, generateMonomorphemes, generateError, generateErrorMono, verifyWords)

# Read in file 
prefixes = pd.read_csv("../experimental_design/prefixes.csv")
roots = pd.read_csv("../experimental_design/roots.csv")
suffixes = pd.read_csv("../experimental_design/suffixes.csv")

#---- Generate roots ----
#root = generateRoots(value = 10)

#---- Generate morphologically complex pseudowords ----
df_Polymorphemes = generatePolymorphemes(prefixes, roots, suffixes, value = 1500)


#---- Generate mono-morphemic pseudowords that are based on morphologically complex pseudowords ---- 
df_Monomorphemes = generateMonomorphemes (df = df_Polymorphemes)

# ---- Generate Errorwords for Monomorphemes ----
# For polymorphemes
df_Error = generateError(df = df_Polymorphemes)

# For polymorphemes: 
df_ErrorPoly = generateErrorMono (df = df_Monomorphemes)

#---- Concate all dataframes ----
df_complete = pd.concat([df_Polymorphemes, df_Monomorphemes, df_Error, df_ErrorPoly], axis = 1)

#---- Test readability of words ----
df_verified = verifyWords (df_complete)
    
#---- Save stimuli pool as .csv ----
df_verified.to_csv("../experimental_design/pseudoword_english_pool.csv", index = False)


