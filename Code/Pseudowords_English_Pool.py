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
# load libraries
import pandas as pd
import os

# Set working directory 
os.getcwd() # check working directory
os.chdir("C:/Users/delia/OneDrive/Desktop/Morphemes/Morphemes/Code")

# Read in file 
data = pd.read_excel("C:/Users/delia/OneDrive/Desktop/Morphemes/Morphemes/Experimental Design/ExperimentList.xlsx", 
                     sheet_name =["Design", "Prefixes", "Roots", "Suffixes"])

# Read in Functions
from functions import (generateRoots, generatePolymorphemes, generateMonomorphemes, generateError, generateErrorPoly)

#---- Generate roots ----
data["Roots"]["Root"] = generateRoots(value = 500)
# Save generated roots to Excel File
data["Roots"].to_excel("C:/Users/delia/OneDrive/Desktop/Morphemes/Morphemes/Experimental Design/TestRoots.xlsx", sheet_name="Roots", index=False)

# Read in checked roots
roots = pd.read_excel("C:/Users/delia/OneDrive/Desktop/Morphemes/Morphemes/Experimental Design/Roots.xlsx")

#---- Generate morphologically complex pseudowords ----
df = generatePolymorphemes(prefixes = data["Prefixes"]["Prefix"].tolist(), 
                           prefixes_weights = data["Prefixes"]["PrefixFrequency"].tolist(), 
                           prefix_pos = data["Prefixes"]["PrefixPOS"].tolist(), 
                           roots = roots["Root"], 
                           suffixes = data["Suffixes"]["Suffix"].tolist(), 
                           suffixes_weights = data["Suffixes"]["SuffixFrequency"].tolist(), 
                           suffix_pos = data["Suffixes"]["SuffixPOS"].tolist(), 
                           value = 5000)

#---- Generate mono-morphemic pseudowords that are based on morphologically complex pseudowords ---- 
df = generateMonomorphemes (prefix2 = df["Prefix2"].tolist(),
                            prefix1 = df["Prefix1"].tolist(),
                            root = df["Root"].tolist(),
                            suffix1 = df["Suffix1"].tolist(),
                            suffix2 = df["Suffix2"].tolist(),
                            df = df)

# ---- Generate Errorwords ----
# For polymorphemes: 
df = generateError(prefix2 = df["Prefix2"].tolist(), 
                   prefix1 = df["Prefix1"].tolist(),
                   root = df["Root"].tolist(),
                   suffix1 = df["Suffix1"].tolist(),
                   suffix2 = df["Suffix2"].tolist(), 
                   df = df)
# For monomorpehmes: 
df = generateErrorPoly (prefix2 = df["MonoPrefix2"].tolist(), 
                        prefix1 = df["MonoPrefix1"].tolist(),
                        root = df["MonoRoot"].tolist(),
                        suffix1 = df["MonoSuffix1"].tolist(),
                        suffix2 = df["MonoSuffix2"].tolist(), 
                        df = df)



#---- Save experimental design as .xslx ----
df.to_csv("C:/Users/delia/OneDrive/Desktop/Morphemes/Morphemes/Experimental Design/Pseudoword_English_Pool.csv", index = False)
