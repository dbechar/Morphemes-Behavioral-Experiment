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
# load libraries
import pandas as pd
import os

os.chdir("C:/Users/delia/OneDrive/Desktop/Morphemes/Morphemes/Code")
from Functions import (generateRoots, generatePolymorphemes, generateMonomorphemes, generateError)

# Read in file 
data = pd.read_excel("C:/Users/delia/OneDrive/Desktop/Morphemes/Morphemes/Experimental Design/Design.xlsx", 
                     sheet_name =["Design", "Prefixes", "Roots", "Suffixes"])

#---- Generate roots ----
data["Roots"]["Root"] = generateRoots(value = 10)

#---- Generate morphologically complex pseudowords ----
df_Polymorphemes = generatePolymorphemes(data, value = 8)

#---- Generate mono-morphemic pseudowords that are based on morphologically complex pseudowords ---- 
df_Monomorphemes = generateMonomorphemes (df = df_Polymorphemes)

# ---- Generate Errorwords for Polymorphemes ----
df_Error = generateError(df = df_Polymorphemes)

#---- Concate all dataframes ----
df_complete = pd.concat([df_Polymorphemes, df_Monomorphemes, df_Error], axis = 1)

#---- Save experimental design as .xslx ----
with pd.ExcelWriter("C:/Users/delia/OneDrive/Desktop/Morphemes/Morphemes/Experimental Design/Design.xlsx") as writer:
    df_complete.to_excel(writer, sheet_name="Design", index= False)
    data["Prefixes"].to_excel(writer, sheet_name="Prefixes", index= False)
    data["Roots"].to_excel(writer, sheet_name="Roots", index= False)
    data["Suffixes"].to_excel(writer, sheet_name="Suffixes", index= False)