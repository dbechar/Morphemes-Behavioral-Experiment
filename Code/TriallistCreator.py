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
import os

# Set working directory 
os.getcwd() # check working directory
os.chdir("C:/Users/delia/OneDrive/Desktop/Morphemes/Morphemes")

# Read in Stimuli Pool
data = pd.read_csv("Experimental Design\Pseudoword_English_Pool.csv")

# Define necessary variables
num_of_participants = 3
trialnumber = 280
p_error = 0.5
p_polymor = 0.5 # probability of using 

# If error:
p_prefix1 = 0.2
p_prefix2 = 0.2
p_root = 0.2
p_suffix1 = 0.2
p_suffix2 = 0.2

# Number of trials per condition that should be picked: 
ncondition = round (trialnumber / 7)
print (ncondition)
# Define errortype distribution per condition
errortype = ["NoErrorPoly"] * round (ncondition * p_polymor * (1-p_error)) + ["Prefix2"] * round (ncondition * ((p_polymor)*(p_error)*p_prefix2)) +  ["Prefix1"] * round (ncondition * ((p_polymor)*(p_error)*p_prefix1)) +  ["Root"] * round (ncondition * ((p_polymor)*(p_error)*p_root)) + ["Suffix1"] * round (ncondition * ((p_polymor)*(p_error)*p_suffix1)) + ["Suffix2"] * round (ncondition * ((p_polymor)*(p_error)*p_suffix2))+ ["NoErrorMono"] * round (ncondition * (1-p_polymor) * (1-p_error)) + ["MonoPrefix2"] * round (ncondition * (1-p_polymor) * (p_error) * p_prefix2) + ["MonoPrefix1"] * round (ncondition * (1-p_polymor) * (p_error) * p_prefix1) + ["MonoRoot"] * round (ncondition * (1-p_polymor) * (p_error) * p_root) + ["MonoSuffix1"] * round (ncondition * (1-p_polymor) * (p_error) * p_suffix1) + ["MonoSuffix2"]* round (ncondition * (1-p_polymor) * (p_error) * p_suffix2)


for par in range (0, num_of_participants):
    # randomly pick ncondition-times trials per condition and save in in a df
    pr = data.query("Condition == 'pr'").sample (n = ncondition)
    pr ["errortype"] = errortype
    rs = data.query("Condition == 'rs'").sample (n = ncondition)
    rs ["errortype"] = errortype
    prs = data.query("Condition == 'pr'").sample (n = ncondition)
    prs ["errortype"] = errortype
    ppr = data.query("Condition == 'ppr'").sample (n = ncondition)
    ppr ["errortype"] = errortype
    rss = data.query("Condition == 'rss'").sample (n = ncondition)
    rss ["errortype"] = errortype
    prss = data.query("Condition == 'prss'").sample (n = ncondition)
    prss ["errortype"] = errortype
    pprs = data.query("Condition == 'pprs'").sample (n = ncondition)   
    pprs ["errortype"] = errortype
    
    pardf= pd.concat ([pr,rs, prs, ppr, rss, prss, pprs])
    
  
    for i in range (0, len (pardf)): 
        word1 = []
        word2 = []
        token = pardf["Token"].tolist()
        errortype = pardf["errortype"].tolist()
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
        
        # In case of errortrial (Polymorpheme)
        if errortype[i] == "Prefix2": 
            word1.append (token[i])
            word2.append (errorprefix2[i])
        elif errortype[i] == "Prefix1": 
            word1.append (token[i])
            word2.append (errorprefix1[i])
        elif errortype[i] == "Root": 
            word1.append (token[i])
            word2.append (errorroot[i])
        elif errortype[i] == "Suffix1": 
            word1.append (token[i])
            word2.append (errorsuffix1[i])
        elif errortype[i] == "Suffix2": 
            word1.append (token[i])
            word2.append (errorsuffix2[i])
            
        # In case of errortrial (Monomorpheme):
        elif errortype[i] == "MonoPrefix2": 
            word1.append (monomorpheme[i])
            word2.append (pardf["MonoErrorPrefix2"][i])
        elif errortype[i] == "MonoPrefix1": 
            word1.append (monomorpheme[i])
            word2.append (pardf["MonoErrorPrefix2"][i])
        elif errortype[i] == "MonoRoot": 
            word1.append (monomorpheme[i])
            word2.append (pardf["MonoErrorRoot"][i])
        elif errortype[i] == "MonoSuffix1": 
            word1.append (monomorpheme[i])
            word2.append (pardf["MonoErrorSuffix1"][i])
        elif errortype[i] == "MonoPrefix2": 
            word1.append (monomorpheme[i])
            word2.append (pardf["MonoErrorSuffix2"][i])
        
        # In case of no errortrial (Monomorpheme):
        elif errortype[i] == "NoErrorPoly":
            word1.append(token[i])
            word2.append(token[i])
        
        # In case of no errortrial (Polymorpheme):
        else: 
            word1.append(monomorpheme[i])
            word2.append(monomorpheme[i])

    worddf = pd.DataFrame ({"Word1": word1,
                            "Word2": word2})
# randomize order
    worddf = worddf.sample (frac = 1)

# Save one csv file per participant to Triallist folder
    path = "Triallists/" + str (par) + "-triallist.csv"
    worddf.to_csv (path)
