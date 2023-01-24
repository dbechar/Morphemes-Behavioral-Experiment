"""
#----Triallist creator script for all subject----#

# This script does:
    # - read in stimulus lists
    # - randomly creates roots
    # - randomly creates pseudowords
    # - creates all errorwords for created words
    # - save all created words and additional information in Excel-File


# Author: Deliane Bechar

# Date: 24.01.2023

"""

#---- Preperation ----
# load libraries
import pandas as pd
import os

# Set working directory 
os.getcwd() # check working directory
os.chdir("C:/Users/delia/OneDrive/Desktop/Morphemes/Code")

# Read in file 
data = pd.read_excel("C:/Users/delia/OneDrive/Desktop/Morphemes/Experimental Design/ExperimentList.xlsx", 
                     sheet_name =["Design", "Prefixes", "Roots", "Suffixes"])

# Read in Functions
from functions import (generateRoots, generatePolymorphemes, generatePseudowords, generateError)

#---- Generate roots ----
root = generateRoots(value = 200)
# Save generated roots to Excel File
data["Roots"]["Root"] = root
data["Roots"].to_excel("C:/Users/delia/OneDrive/Desktop/Morphemes/Experimental Design/Roots.xlsx", sheet_name="Roots", index=False)

#---- Generate morphologically complex pseudowords ----
df = generatePolymorphemes(prefixes = data["Prefixes"]["Prefix"].tolist(), 
                           prefixes_weights = data["Prefixes"]["PrefixFrequency"].tolist(), 
                           prefix_pos = data["Prefixes"]["PrefixPOS"].tolist(), 
                           roots = root, 
                           suffixes = data["Suffixes"]["Suffix"].tolist(), 
                           suffixes_weights = data["Suffixes"]["SuffixFrequency"].tolist(), 
                           suffix_pos = data["Suffixes"]["SuffixPOS"].tolist(), 
                           value = 7)

#---- Generate mono-morphemic pseudowords that are based on morphologically complex pseudowords ---- 
df = generatePseudowords (prefix2 = df["prefix2"].tolist(),
                          prefix1 = df["prefix1"].tolist(),
                          root = df["root"].tolist(),
                          suffix1 = df["suffix1"].tolist(),
                          suffix2 = df["suffix2"].tolist(),
                          newword = df["newword"].tolist(),
                          condition = df["condition"].tolist())

# ---- Generate Errorwords ----
df = generateError(prefix2 = df["Prefix2"].tolist(), 
                   prefix1 = df["Prefix1"].tolist(),
                   root = df["Root"].tolist(),
                   suffix1 = df["Suffix1"].tolist(),
                   suffix2 = df["Suffix2"].tolist(), 
                   df = df)

#---- Save experimental design as .xslx ----
df.to_excel("C:/Users/delia/OneDrive/Desktop/Morphemes/Experimental Design/Design.xlsx", sheet_name="Design", index=False)
