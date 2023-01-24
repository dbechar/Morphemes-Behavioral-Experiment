"""
#----Triallist creator script for all subject----#

# This script does:
    # - read in stimulus lists
    # - randomly creates roots
    # - randomly creates pseudowords
    # - creates all errorwords for created words
    # - save all created words and additional information in Excel-File


# Author: Deliane Bechar

# Date: 20.01.2023

"""

#---- Preperation ----
# load libraries
import pandas as pd
import os

# Set working directory 
os.getcwd() # check working directory
os.chdir("C:/Users/delia/OneDrive/Desktop/Morphemes")

# Read in file 
data = pd.read_excel("Experimental Design/ExperimentList.xlsx", sheet_name =["Design", "Prefixes", "Roots", "Suffixes"])

# Read in Functions
from functions import (generateRoots, generatePolymorphemes, generatePseudowords, generateError)


#---- Generate roots ----
root = []
generateRoots(root, value = 200)

# Save generated roots to Excel File
data["Roots"]["Root"] = root
data["Roots"].to_excel("Experimental Design/Roots.xlsx", sheet_name="Roots", index=False)
    

#---- Generate morphologically complex pseudowords ----
# Define necessary variables for function
prefixes = data["Prefixes"]["Prefix"].tolist()
prefixes_weights = data["Prefixes"]["PrefixFrequency"].tolist()
suffixes = data["Suffixes"]["Suffix"].tolist()
suffixes_weights = data["Suffixes"]["SuffixFrequency"].tolist()
prefix_pos = data["Prefixes"]["PrefixPOS"].tolist()
suffix_pos = data["Suffixes"]["SuffixPOS"].tolist()
roots = root
value = 7
df = pd.DataFrame()



generatePolymorphemes(prefixes, prefixes_weights, prefix_pos, roots, suffixes, suffixes_weights, suffix_pos, value, df)


#---- Generate mono-morphemic pseudowords that are based on morphologically complex pseudowords ---- 
# Define necessary variables for function
prefix2 = df["prefix2"].tolist()
prefix1 = df["prefix1"].tolist()
root = df["root"].tolist()
suffix1 = df["suffix1"].tolist()
suffix2 = df["suffix2"].tolist()
newword = df["newword"].tolist()
condition = df["condition"].tolist()


generatePseudowords (prefix2, prefix1, root, suffix1, suffix2, newword, condition)

# Save information in dataframe
da = pd.DataFrame({
    "Token": newword,
    "Condition": condition, 
    "Prefix2": prefix2, 
    "Prefix1": prefix1, 
    "Root": root, 
    "Suffix1": suffix1, 
    "Suffix2": suffix2
    })
da["Wordlength"] = da["Token"].str.len()


# ---- Generate Error ----
# Define necessary variables for function
prefix2 = da["Prefix2"].tolist()
prefix1 = da["Prefix1"].tolist()
root = da["Root"].tolist()
suffix1 = da["Suffix1"].tolist()
suffix2 = da["Suffix2"].tolist()

generateError(prefix1, prefix2, root, suffix1, suffix2, da)


#---- Save as .xslx ----
da.to_excel("Experimental Design/Design.xlsx", sheet_name="Design", index=False)

