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

# Set working directory 
os.getcwd() # check working directory
os.chdir("C:/Users/delia/OneDrive/Desktop/Morphemes/Morphemes")

# Read in Stimuli Pool
data = pd.read_csv("Experimental Design\Pseudoword_English_Pool.csv")

# Define necessary variables
random.seed(19)
trialnumber = 280
p_error = 0.5
p_polymor = 0.5 # probability of using polymorphemes 

# If error:
#p_prefix1 = 0.2
#p_prefix2 = 0.2
#p_root = 0.2
#p_suffix1 = 0.2
#p_suffix2 = 0.2

# Number of trials per condition that should be picked: 
ncondition = round (trialnumber / 7)

# Define errortype distribution per condition
# Define errortype distribution per condition
errortype_pr = ["NoErrorPoly"] * int (ncondition * p_polymor * (1-p_error)) + ["Prefix1"] * round (ncondition * ((p_polymor)*(p_error) * 0.5)) +  ["Root"] * round (ncondition * ((p_polymor)*(p_error) * 0.5)) + ["NoErrorMono"] * round (ncondition * (1-p_polymor) * (1-p_error)) + ["MonoPrefix1"] * round (ncondition * (1-p_polymor) * (p_error) * 0.5) + ["MonoRoot"] * round (ncondition * (1-p_polymor) * (p_error) * 0.5)  
random.shuffle (errortype_pr)
errortype_rs = ["NoErrorPoly"] * int (ncondition * p_polymor * (1-p_error)) + ["Suffix1"] * round (ncondition * ((p_polymor)*(p_error) * 0.5)) +  ["Root"] * round (ncondition * ((p_polymor)*(p_error) * 0.5)) + ["NoErrorMono"] * round (ncondition * (1-p_polymor) * (1-p_error)) + ["MonoSuffix1"] * round (ncondition * (1-p_polymor) * (p_error) * 0.5) + ["MonoRoot"] * round (ncondition * (1-p_polymor) * (p_error) * 0.5)  
random.shuffle(errortype_rs)
errortype_prs = ["NoErrorPoly"] * int (ncondition * p_polymor * (1-p_error)) + ["Prefix1"] * round (ncondition * ((p_polymor)*(p_error) * (1/3))) +  ["Root"] * round (ncondition * ((p_polymor)*(p_error) * (1/3))) + ["Suffix1"] * round (ncondition * ((p_polymor)*(p_error) * (1/3))) + ["NoErrorMono"] * round (ncondition * (1-p_polymor) * (1-p_error)) + ["MonoPrefix1"] * round (ncondition * (1-p_polymor) * (p_error) * (1/3)) + ["MonoRoot"] * round (ncondition * (1-p_polymor) * (p_error) * (1/3)) + ["MonoSuffix1"] * round (ncondition * ((p_polymor)*(p_error) * (1/3))) 
random.shuffle (errortype_prs)
errortype_ppr = ["NoErrorPoly"] * int (ncondition * p_polymor * (1-p_error)) + ["Prefix1"] * round (ncondition * ((p_polymor)*(p_error) * (1/3))) +  ["Root"] * round (ncondition * ((p_polymor)*(p_error) * (1/3))) + ["Prefix2"] * round (ncondition * ((p_polymor)*(p_error) * (1/3))) + ["NoErrorMono"] * round (ncondition * (1-p_polymor) * (1-p_error)) + ["MonoPrefix1"] * round (ncondition * (1-p_polymor) * (p_error) * (1/3)) + ["MonoRoot"] * round (ncondition * (1-p_polymor) * (p_error) * (1/3)) + ["MonoPrefix2"] * round (ncondition * ((p_polymor)*(p_error) * (1/3))) 
random.shuffle (errortype_ppr)
errortype_rss = ["NoErrorPoly"] * int (ncondition * p_polymor * (1-p_error)) + ["Suffix2"] * round (ncondition * ((p_polymor)*(p_error) * (1/3))) +  ["Root"] * round (ncondition * ((p_polymor)*(p_error) * (1/3))) + ["Suffix1"] * round (ncondition * ((p_polymor)*(p_error) * (1/3))) + ["NoErrorMono"] * round (ncondition * (1-p_polymor) * (1-p_error)) + ["MonoSuffix2"] * round (ncondition * (1-p_polymor) * (p_error) * (1/3)) + ["MonoRoot"] * round (ncondition * (1-p_polymor) * (p_error) * (1/3)) + ["MonoSuffix1"] * round (ncondition * ((p_polymor)*(p_error) * (1/3))) 
random.shuffle (errortype_rss)
errortype_prss = ["NoErrorPoly"] * round (ncondition * p_polymor * (1-p_error)) + ["Prefix1"] * round (ncondition * ((p_polymor)*(p_error) * (1/4))) +  ["Root"] * round (ncondition * ((p_polymor)*(p_error) * (1/4))) + ["Suffix1"] * round (ncondition * ((p_polymor)*(p_error) * (1/4))) +["Suffix2"] * round (ncondition * ((p_polymor)*(p_error) * (1/4))) + ["NoErrorMono"] * round (ncondition * (1-p_polymor) * (1-p_error)) + ["MonoPrefix1"] * round (ncondition * (1-p_polymor) * (p_error) * (1/4)) + ["MonoRoot"] * round (ncondition * (1-p_polymor) * (p_error) * (1/4)) + ["MonoSuffix1"] * round (ncondition * ((p_polymor)*(p_error) * (1/4))) +["MonoSuffix2"] * round (ncondition * ((p_polymor)*(p_error) * (1/4))) 
random.shuffle (errortype_prss)
errortype_pprs = ["NoErrorPoly"] * round (ncondition * p_polymor * (1-p_error)) + ["Prefix1"] * round (ncondition * ((p_polymor)*(p_error) * (1/4))) +  ["Root"] * round (ncondition * ((p_polymor)*(p_error) * (1/4))) + ["Suffix1"] * round (ncondition * ((p_polymor)*(p_error) * (1/4))) +["Prefix2"] * round (ncondition * ((p_polymor)*(p_error) * (1/4))) + ["NoErrorMono"] * round (ncondition * (1-p_polymor) * (1-p_error)) + ["MonoPrefix1"] * round (ncondition * (1-p_polymor) * (p_error) * (1/4)) + ["MonoRoot"] * round (ncondition * (1-p_polymor) * (p_error) * (1/4)) + ["MonoSuffix1"] * round (ncondition * ((p_polymor)*(p_error) * (1/4))) +["MonoPrefix2"] * round (ncondition * ((p_polymor)*(p_error) * (1/4))) 
random.shuffle (errortype_pprs)
ncondition = len (errortype_pprs)



    # randomly pick ncondition-times trials per condition and save in in a df
pr = data.query("Condition == 'pr'").sample (n = ncondition)
pr ["errortype"] = errortype_pr[0:ncondition]
rs = data.query("Condition == 'rs'").sample (n = ncondition)
rs ["errortype"] = errortype_rs[0:ncondition]
prs = data.query("Condition == 'pr'").sample (n = ncondition)
prs ["errortype"] = errortype_prs[0:ncondition]
ppr = data.query("Condition == 'ppr'").sample (n = ncondition)
ppr ["errortype"] = errortype_ppr[0:ncondition]
rss = data.query("Condition == 'rss'").sample (n = ncondition)
rss ["errortype"] = errortype_rss[0:ncondition]
prss = data.query("Condition == 'prss'").sample (n = ncondition)
prss ["errortype"] = errortype_prss[0:ncondition]
pprs = data.query("Condition == 'pprs'").sample (n = ncondition)   
pprs ["errortype"] = errortype_pprs[0:ncondition]
                                    

pardf= pd.concat ([pr,rs, prs, ppr, rss, prss, pprs])
    
    
# Define necessary variables
word1 = []
word2 = []
worddf = pd.DataFrame()
token = pardf["Token"].tolist()
errortypefull = pardf["errortype"].tolist()
monomorpheme = pardf["Monomorpheme"].tolist()
errorprefix2 = pardf["ErrorPrefix2"].tolist()
errorprefix1 = pardf["ErrorPrefix1"].tolist()
errorroot = pardf["ErrorRoot"].tolist()
errorsuffix1 = pardf["ErrorSuffix1"].tolist()
errorsuffix2 = pardf["ErrorSuffix2"].tolist()
monoerrorprefix2 = pardf["MonoErrorPrefix2"].tolist()
monoerrorprefix1 = pardf["MonoErrorPrefix1"].tolist()
monoerrorroot = pardf["MonoErrorRoot"].tolist()
monoerrorsuffix1 = pardf["MonoErrorSuffix1"].tolist()
monoerrorsuffix2 = pardf["MonoErrorSuffix2"].tolist()


for i in range (0, len (pardf)): 
    # In case of errortrial (Polymorpheme)
    if errortypefull[i] == "Prefix2": 
        word1.append (token[i])
        word2.append (errorprefix2[i])
    elif errortypefull[i] == "Prefix1": 
        word1.append (token[i])
        word2.append (errorprefix1[i])
    elif errortypefull[i] == "Root": 
        word1.append (token[i])
        word2.append (errorroot[i])
    elif errortypefull[i] == "Suffix1": 
        word1.append (token[i])
        word2.append (errorsuffix1[i])
    elif errortypefull[i] == "Suffix2": 
        word1.append (token[i])
        word2.append (errorsuffix2[i])
        
    # In case of errortrial (Monomorpheme):
    elif errortypefull[i] == "MonoPrefix2": 
        word1.append (monomorpheme[i])
        word2.append (monoerrorprefix2[i])
    elif errortypefull[i] == "MonoPrefix1": 
        word1.append (monomorpheme[i])
        word2.append (monoerrorprefix1[i])
    elif errortypefull[i] == "MonoRoot": 
        word1.append (monomorpheme[i])
        word2.append (monoerrorroot[i])
    elif errortypefull[i] == "MonoSuffix1": 
        word1.append (monomorpheme[i])
        word2.append (monoerrorsuffix1[i])
    elif errortypefull[i] == "MonoPrefix2": 
        word1.append (monomorpheme[i])
        word2.append (monoerrorsuffix2[i])
    
    # In case of no errortrial (Monomorpheme):
    elif errortypefull[i] == "NoErrorPoly":
        word1.append(token[i])
        word2.append(token[i])
    
    # In case of no errortrial (Polymorpheme):
    else: 
        word1.append(monomorpheme[i])
        word2.append(monomorpheme[i])
pardf["Word1"] = word1
pardf["Word2"] = word2
worddf["Word1"] = word1
worddf["Word2"] = word2

# randomize order
worddf = worddf.sample (frac=1)

# Save one csv file per participant to Triallist folder
path = "Triallists/" + str (1) + "-triallist.csv"
worddf.to_csv (path, index = False)
