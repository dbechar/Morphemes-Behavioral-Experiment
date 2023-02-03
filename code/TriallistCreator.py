"""

#---- Triallist Creator ----#

# This script does:
        # - Read in and create all test words
        # - Creat one triallists that is based on certain prerequisits that 
            are set at the beginning 
        # - save triallists as .csv in the triallists folder

# Author: Deliane Bechar

# Date: 30.01.2023

"""
# LOAD LIBRARIES AND FUNCTIONS
import os
os.chdir("C:/Users/delia/OneDrive/Desktop/Morphemes/Morphemes/Code")
import pandas as pd
import random
from Functions import (generatePolymorphemes, generateMonomorphemes, generateError, verifyWords, generateParticipantFile, generateTriallist)


# READ IN STIMULUS FILES
prefixes = pd.read_csv("../experimental_design/prefixes.csv")
roots = pd.read_csv("../experimental_design/roots.csv")
suffixes = pd.read_csv("../experimental_design/suffixes.csv")

# SET SEED
random.seed(19)

# DEFINE FILE NUMBER
file_number = 1

# DEFINE NUMBER OF TRIALS PER CONDITION
condition = {}
condition ["r"] = 24 
condition ["pr"] = 48
condition ["rs"] = 48 
condition["prs"] = 48 
condition ["ppr"] = 48 
condition ["rss"] = 48 
condition ["prss"] = 48 
condition ["pprs"] = 48
condition ["pppr"] = 48 
condition ["rsss"] = 48
 
# DEFINE ERRORRATE
p_error = 0.5
p_polymor = 0.5

#---- GENERATE POLYMORPHEMES ----
df_Polymorphemes = generatePolymorphemes(prefixes, roots, suffixes)


#---- GENERATE CONTROL (MONOMORPHEMES) ---- 
df_Monomorphemes = generateMonomorphemes (df = df_Polymorphemes)

# ---- ADD ERROR ----
df_Error = generateError(df = df_Polymorphemes)

#---- CONCATE DATAFRAMES----
df_complete = pd.concat([df_Polymorphemes, df_Monomorphemes, df_Error], axis = 1)

#---- VERIFICATION CODE ----
df_verified = verifyWords (df_complete)

# RANDOMIZE LIST WITH ERRORS
pardf = generateParticipantFile (df_verified, condition, p_error, p_polymor)

#---- GENERATE TRIALLIST ---- 
triallist = generateTriallist (df = pardf)
 
#---- SAVE TRIALLIST ----
path = "../triallists/" + str(file_number) + "triallist.csv"
triallist.to_csv (path, index = False)
