"""
#---- Triallist Creator ----#

# This script does:
        # - Creat one triallists that is based on certain prerequisits that 
            are set at the beginning 
        # - save triallists as .csv in the triallists folder

# Author: Deliane Bechar

# Date: 26.01.2023

"""
#---- Preperation ----
# Load libraries
from Functions import (generateParticipantFile, generateTriallist)
import pandas as pd
import random

# Read in Stimuli Pool
data = pd.read_csv("../experimental_design/pseudoword_english_pool.csv")

# Set seed
random.seed(19)

# Define file number
<<<<<<< HEAD
file_number = 11
=======
file_number = 1
>>>>>>> bbeab571ca7278cd80c4a3dcbe2f3603423183ee

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
path = "../triallists/" + str(file_number) + "triallist.csv"
triallist.to_csv (path, index = False)

