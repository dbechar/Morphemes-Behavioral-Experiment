"""
#---- Triallist Creator ----#

# This script does: 
        # - Creat individual triallists for all participants
        # - save all triallists as .csv in the triallists folder


# Author: Deliane Bechar

# Date: 24.01.2023

"""
#---- Preperation ----
# load libraries
import pandas as pd
import random
import os

# os.chdir("C:/Users/delia/OneDrive/Desktop/Morphemes/Morphemes/Code")
from Functions import (generateParticipantFile, generateTriallist)

# Set working directory 
os.getcwd() # check working directory
#os.chdir("C:/Users/delia/OneDrive/Desktop/Morphemes/Morphemes")

# Read in Stimuli Pool
data = pd.read_csv("C:/Users/delia/OneDrive/Desktop/Morphemes/Morphemes/Experimental Design/Pseudoword_English_Pool.csv")

# Set seed
random.seed(19)

# Define number of trials per condition 
condition = {}
condition ["r"] = 24 
condition ["pr"] = 48
condition ["rs"] = 48 
condition["prs"] = 48 
condition ["ppr"] = 48 
condition ["rss"] = 48 
condition ["prss"] = 48 
condition ["pprs"] = 48
 
# Define errorrate and probabilty of using polymorphemes
p_error = 0.5
p_polymor = 0.5

# Randomly pick out trials based on specifications
pardf = generateParticipantFile (data, condition, p_error, p_polymor)

# Define Word 1 and Word 2 for final participant triallist: 
triallist = generateTriallist (df = pardf)
 
# Save triallist as csv file in the Triallist folder
triallist.to_csv ("C:/Users/delia/OneDrive/Desktop/Morphemes/Morphemes/Triallists/triallist.csv", index = False)

