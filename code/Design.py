"""
#----Experimental Design----#

# This script does:
    # - read in stimulus lists
    # - randomly creates roots
    # - randomly creates polymorphemic words
    # - randomly creates mono-morphemic words
    # - create all types of errorwords for the polymorphemes
    # - save all created words and additional information in Excel-File


# Author: Deliane Bechar

# Date: 24.01.2023

"""

#---- Preperation ----
# Load libraries
import pandas as pd
import os
os.chdir("C:/Users/delia/OneDrive/Desktop/Morphemes/Morphemes/Code")
from Functions import (generatePolymorphemes, generateMonomorphemes, generateError, generateReverseRoot)

# Read in file 
prefixes = pd.read_csv("../experimental_design/prefixes.csv")
roots = pd.read_csv("../experimental_design/roots.csv")
suffixes = pd.read_csv("../experimental_design/suffixes.csv")

#---- Generate roots ----
# roots["Root"] = generateRoots(value = 10)

#---- Generate reversed root ----
testdf = generateReverseRoot (roots)

#---- Generate morphologically complex pseudowords ----
df_Polymorphemes = generatePolymorphemes(prefixes, roots, suffixes)

#---- Generate mono-morphemic pseudowords that are based on morphologically complex pseudowords ---- 
df_Monomorphemes = generateMonomorphemes (df = df_Polymorphemes)

# ---- Generate Errorwords for Polymorphemes ----
df_Error = generateError(df = df_Polymorphemes)

#---- Concate all dataframes ----
df_complete = pd.concat([df_Polymorphemes, df_Monomorphemes, df_Error], axis = 1)

#---- Save experimental design as .csv ----
df_complete.to_csv("../experimental_design/design.csv", index = False)

