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
from Functions import (generateRoots, generatePolymorphemes, generateMonomorphemes, generateError, generateErrorMono)

# Read in file 
data = pd.read_excel("C:/Users/delia/OneDrive/Desktop/Morphemes/Morphemes/Experimental Design/ExperimentList.xlsx", 
                     sheet_name =["Design", "Prefixes", "Roots", "Suffixes"])

#---- Generate roots ----
data["Roots"]["Root"] = generateRoots(value = 200)
# Save generated roots to Excel File
data["Roots"].to_excel("C:/Users/delia/OneDrive/Desktop/Morphemes/Morphemes/Experimental Design/Roots.xlsx", sheet_name="Roots", index=False)

#---- Generate morphologically complex pseudowords ----
df_Polymorphemes = generatePolymorphemes(data, value = 1000)

#---- Generate mono-morphemic pseudowords that are based on morphologically complex pseudowords ---- 
df_Monomorphemes = generateMonomorphemes (df = df_Polymorphemes)

# ---- Generate Errorwords for Monomorphemes ----
# For polymorphemes
df_Error = generateError(df = df_Polymorphemes)

# For polymorphemes: 
df_ErrorPoly = generateErrorMono (df = df_Monomorphemes)

#---- Concate all dataframes ----
df_complete = pd.concat([df_Polymorphemes, df_Monomorphemes, df_Error, df_ErrorPoly], axis = 1)


#---- Save experimental design as .xslx ----
df_complete.to_csv("C:/Users/delia/OneDrive/Desktop/Morphemes/Morphemes/Experimental Design/Pseudoword_English_Pool.csv", index = False)
