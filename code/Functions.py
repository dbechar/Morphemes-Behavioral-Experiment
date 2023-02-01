"""
#---- Functions----#

# This script does: 
    # - create polymorphemic words based on the given stimulus pool
    # - create a function that generates mono-morphemic words based 
        on the polymorphemic words
    # - create a function that generates random errors for monomorphemes
    # - create a function that generates random errors for polymorphemes
    # - create a function that checks all words 
    
    
# Date: 24.01.2023

# Author: Deliane Bechar

"""
# LOAD LIBRARIES
import pandas as pd
import random

# GENERATE REVERSED ROOTS
def generateReverseRoot (dfroot):
    root = dfroot["Root"]
    reverseroot = []
    for i in range(0, len (root)):
        rr = root[i][::-1]
        reverseroot.append (rr)
    dfroot ["ReverseRoot"] = reverseroot
    return dfroot

# GENERATE POLYMORPHEMES
def generatePolymorphemes (prefixes, roots, suffixes):
   prefixes = prefixes.fillna("")
   suffixes = suffixes.fillna("")
   prefix3 = prefixes["Prefix3"].tolist ()
   prefix2 =  prefixes["Prefix2"].tolist ()
   prefix1 =  prefixes["Prefix1"].tolist ()
   root = roots["Root"].tolist ()
   suffix1 = suffixes["Suffix1"].tolist ()
   suffix2 = suffixes["Suffix2"].tolist ()
   suffix3 =  suffixes["Suffix3"].tolist ()
   condition_prefix = prefixes["Condition"].tolist ()
   condition_suffix = suffixes["Condition"].tolist ()
   token = []
   condition = []
   prefix1_list = []
   prefix2_list = []
   prefix3_list = []
   root_list = []
   suffix1_list = []
   suffix2_list = []
   suffix3_list = []

   for i in range (0, len(root)):
       token.append (root[i])
       prefix3_list.append ("")
       prefix2_list.append ("")
       prefix1_list.append ("")
       root_list.append (root[i])
       suffix1_list.append ("")
       suffix2_list.append ("")
       suffix3_list.append ("")
       condition.append ("r")
       for prefix in range (0, len (prefix1)): 
           prefix3_list.append (prefix3[prefix])
           prefix2_list.append (prefix2[prefix])
           prefix1_list.append (prefix1[prefix])
           root_list.append (root[i])
           suffix1_list.append ("")
           suffix2_list.append ("")
           suffix3_list.append ("")
           token.append (prefix3[prefix] + prefix2[prefix] + prefix1[prefix]+ root[i])
           condition.append (str (condition_prefix [prefix]) + "r") 

   for i in range (0, len(token)):
       for suffix in range (0, len(suffix1)): 
           token.append  (token[i] + suffix1[suffix] + suffix2[suffix] + suffix3[suffix])
           prefix3_list.append (prefix3_list[i])
           prefix2_list.append (prefix2_list[i])
           prefix1_list.append (prefix1_list[i])
           root_list.append(root_list[i])
           suffix1_list.append (suffix1[suffix])
           suffix2_list.append (suffix2[suffix])
           suffix3_list.append (suffix3[suffix])
           condition.append (str (condition[i]) + condition_suffix [suffix])

       
   df = pd.DataFrame({"Token": 10*token, 
                      "Condition": 10*condition,
                      "Prefix3": 10*prefix3_list, 
                      "Prefix2": 10*prefix2_list,
                      "Prefix1": 10*prefix1_list,
                      "Root": 10*root_list, 
                      "Suffix1": 10*suffix1_list, 
                      "Suffix2": 10*suffix2_list, 
                      "Suffix3": 10*suffix3_list
       })

   df["Wordlength"] = df["Token"].str.len()
   return df


# GENERATE POLYMORPHEMES
def generateMonomorphemes (df):
    prefix3 = df["Prefix3"].tolist()
    prefix2 = df["Prefix2"].tolist()
    prefix1 = df["Prefix1"].tolist()
    root = df["Root"].tolist()                        
    suffix1 = df["Suffix1"].tolist()
    suffix2 = df["Suffix2"].tolist()
    suffix3 = df["Suffix3"].tolist()
    monomorphemes = []
    mono_prefix3 = []
    mono_prefix2 = []
    mono_prefix1 = []
    mono_root = []
    mono_suffix1 = []
    mono_suffix2 = []
    mono_suffix3 = []
    
    for i in range(0, len (root)):
        monoprefix3 = prefix3[i] [::-1]
        mono_prefix3.append (monoprefix3)
        monoprefix2 = prefix2[i] [::-1]
        mono_prefix2.append (monoprefix2)
        monoprefix1 = prefix1[i][::-1]
        mono_prefix1.append (monoprefix1)
        monoroot = root[i]
        monoroot = monoroot [::-1]
        while monoroot == root[i]: 
            monoroot = list (root[i])
            monoroot = random.sample (monoroot, k = len (monoroot))
            monoroot = "".join(monoroot)
        mono_root.append (monoroot)
        monosuffix1 = suffix1[i] [::-1]
        mono_suffix1.append(monosuffix1)
        monosuffix2 = suffix2[i] [::-1]
        mono_suffix2.append (monosuffix2)
        monosuffix3 = suffix3[i] [::-1]
        mono_suffix3.append (monosuffix3)
        monomorphemes.append (monoprefix3 + monoprefix2 + monoprefix1 + monoroot + monosuffix1 + monosuffix2 + monosuffix3)
        
    df_Monomorpheme = pd.DataFrame ()
    df_Monomorpheme["Monomorpheme"] = monomorphemes
    df_Monomorpheme["MonoPrefix3"] = mono_prefix3
    df_Monomorpheme["MonoPrefix2"] = mono_prefix2
    df_Monomorpheme["MonoPrefix1"] = mono_prefix1
    df_Monomorpheme["MonoRoot"] = mono_root
    df_Monomorpheme["MonoSuffix1"] = mono_suffix1
    df_Monomorpheme["MonoSuffix2"] = mono_suffix2
    df_Monomorpheme["MonoSuffix3"] = mono_suffix3
    
    return df_Monomorpheme


# RANDOMLY CHANGE N CHARACTERS
def randomlyChangeNChar(word, value, changed_index, error_word):
    vowels=["a", "e", "i", "o", "u"]
    vowel_weights=[8.34, 12.60, 6.71, 7.7, 2.85]
    consonants=["b", "c", "d", "f", "g", "h", "k", "p", "q", "s", "t", "v", "x", "z"]
    consonant_weights=[1.54, 2.73, 4.14, 2.03, 1.92, 6.11, 0.87, 4.24,  0.09, 6.11, 9.37, 1.06, 0.20, 0.06]
    sonorants = ["j", "l", "m", "n", "r", "w", "y"]
    sonorants_weights = [0.23, 2.53, 6.8, 1.66, 5.68, 2.34, 2.04]
    length = len(word)
    word = list(word)
    k = random.sample(range(0, length), value) 
    
    for index in k:
        char = word[index]
        changed_index.append (index)
        if char in vowels: 
            while char == word[index]:
                char = random.choices(vowels, weights = vowel_weights, cum_weights=(None), k = value)
                char = "".join(char)
            word[index] = "".join(char)
            word = "".join(word)
            error_word.append (word)
        elif char in sonorants: 
            while char == word[index]:
                char = random.choices(sonorants, weights = sonorants_weights, cum_weights=(None), k = value)
                char = "".join(char)
            word[index] = "".join(char)
            word = "".join(word)
            error_word.append (word)
        else: 
            while char == word[index]:
                char = random.choices(consonants, weights = consonant_weights, cum_weights=(None), k = value)
                char = "".join(char)
            word[index] = "".join(char)
            word = "".join(word)
            error_word.append (word)  


# GENERATE ERROR
def generateError (df): 
    prefix3 = df["Prefix3"].tolist() 
    prefix2 = df["Prefix2"].tolist() 
    prefix1 = df["Prefix1"].tolist()
    root = df["Root"].tolist() 
    suffix1 = df["Suffix1"].tolist()
    suffix2 = df["Suffix2"].tolist()
    suffix3 = df["Suffix3"].tolist()
    eprefix1 = []
    eprefix2 = []
    eprefix3 = []
    eroot = []
    esuffix1 = []
    esuffix2 = []
    esuffix3 = []
    error_prefix3 = []
    error_prefix2 = []
    error_prefix1 = []
    error_root = []
    error_suffix1 = []
    error_suffix2 = []
    error_suffix3 = []
    changed_index_p3 = []
    changed_index_p2 = []
    changed_index_p1 = []
    changed_index_r = []
    changed_index_s1 = []
    changed_index_s2 = []
    changed_index_s3 = []
    monoerror_prefix3 = []
    monoerror_prefix2 = []
    monoerror_prefix1 = []
    monoerror_root = []
    monoerror_suffix1 = []
    monoerror_suffix2 = []
    monoerror_suffix3 = []

    for i in range (0, len (root)):
        if prefix3[i] == "": 
            error_prefix3.append("")
            changed_index_p3.append ("")
            eprefix3.append ("")
            monoerror_prefix3.append ("")
        else: 
            randomlyChangeNChar(word = prefix3[i], value = 1, changed_index = changed_index_p3, error_word = eprefix3)
            error_prefix3.append (eprefix3[i] + prefix2[i] + prefix1[i] + root [i] + suffix1[i] + suffix2[i] + suffix3[i])
            monoerror_prefix3.append (eprefix3[i][::-1] + prefix2[i][::-1] + prefix1[i][::-1] + root [i][::-1] + suffix1[i][::-1] + suffix2[i][::-1] + suffix3[i][::-1])
       
        if prefix2[i] == "": 
            error_prefix2.append("")
            changed_index_p2.append ("")
            eprefix2.append ("")
            monoerror_prefix2.append ("")
        else: 
            randomlyChangeNChar(word = prefix2[i], value = 1, changed_index = changed_index_p2, error_word = eprefix2)
            error_prefix2.append (prefix3[i] + eprefix2[i] + prefix1[i] + root [i] + suffix1[i] + suffix2[i]+ suffix3[i])
            monoerror_prefix2.append (prefix3[i][::-1] + eprefix2[i][::-1] + prefix1[i][::-1] + root [i][::-1] + suffix1[i][::-1] + suffix2[i][::-1]+ suffix3[i][::-1])
        
        if prefix1[i] == "": 
            error_prefix1.append("")
            changed_index_p1.append("")
            eprefix1.append("")
            monoerror_prefix1.append ("")
        else: 
            randomlyChangeNChar(word = prefix1[i], value = 1, changed_index = changed_index_p1, error_word = eprefix1)
            error_prefix1.append (prefix3[i] + prefix2[i] + eprefix1[i] + root [i] + suffix1[i] + suffix2[i] + suffix3[i]) 
            monoerror_prefix1.append (prefix3[i][::-1] + prefix2[i][::-1] + eprefix1[i][::-1] + root [i][::-1] + suffix1[i][::-1] + suffix2[i][::-1] + suffix3[i][::-1]) 
        
        if root[i] == "": 
            error_root.append("")
            changed_index_r.append ("")
            eroot.append ("")
            monoerror_root.append ("")
        else: 
            randomlyChangeNChar(word = root[i], value = 1, changed_index=changed_index_r, error_word = eroot)
            error_root.append (prefix3[i] + prefix2[i] + prefix1[i] + eroot [i] + suffix1[i] + suffix2[i] + suffix3[i])
            monoerror_root.append (prefix3[i][::-1] + prefix2[i][::-1] + prefix1[i][::-1] + eroot [i][::-1] + suffix1[i][::-1] + suffix2[i][::-1] + suffix3[i][::-1])
        
        if suffix1[i] == "": 
            error_suffix1.append("")
            changed_index_s1.append("")
            esuffix1.append("")
            monoerror_suffix1.append ("")
        else: 
            randomlyChangeNChar(word = suffix1[i], value = 1, changed_index = changed_index_s1, error_word = esuffix1)
            error_suffix1.append (prefix3[i] + prefix2[i] + prefix1[i] + root [i] + esuffix1[i] + suffix2[i] + suffix3[i])
            monoerror_suffix1.append (prefix3[i][::-1] + prefix2[i][::-1] + prefix1[i][::-1] + root [i][::-1] + esuffix1[i][::-1] + suffix2[i][::-1] + suffix3[i][::-1])
        
        if suffix2[i] == "": 
            error_suffix2.append("")
            changed_index_s2.append("")
            esuffix2.append("")
            monoerror_suffix2.append ("")
        else: 
            randomlyChangeNChar(word = suffix2[i], value = 1, changed_index = changed_index_s2, error_word = esuffix2)
            error_suffix2.append (prefix3[i] + prefix2[i] + prefix1[i] + root[i] + suffix1[i] + esuffix2[i] + suffix3[i])
            monoerror_suffix2.append (prefix3[i][::-1] + prefix2[i][::-1] + prefix1[i][::-1] + root[i][::-1] + suffix1[i][::-1] + esuffix2[i][::-1] + suffix3[i][::-1])
        
        if suffix3[i] == "": 
            error_suffix3.append("")
            changed_index_s3.append("")
            esuffix3.append("")
            monoerror_suffix3.append ("")
        else: 
            randomlyChangeNChar(word = suffix3[i], value = 1, changed_index = changed_index_s3, error_word = esuffix3)
            error_suffix3.append (prefix3[i] + prefix2[i] + prefix1[i] + root[i] + suffix1[i] + suffix2[i] + esuffix3[i])
            monoerror_suffix3.append (prefix3[i][::-1] + prefix2[i][::-1] + prefix1[i][::-1] + root[i][::-1] + suffix1[i][::-1] + suffix2[i][::-1] + esuffix3[i][::-1])
        
    df_Error = pd.DataFrame()
    df_Error["ErrorPrefix3"] = error_prefix3
    df_Error["ErrorPrefix2"] = error_prefix2
    df_Error["ErrorPrefix1"] = error_prefix1
    df_Error["ErrorRoot"] = error_root
    df_Error["ErrorSuffix1"] = error_suffix1
    df_Error["ErrorSuffix2"] = error_suffix2
    df_Error["ErrorSuffix3"] = error_suffix3
    df_Error["MonoErrorPrefix3"] = monoerror_prefix3
    df_Error["MonoErrorPrefix2"] = monoerror_prefix2
    df_Error["MonoErrorPrefix1"] = monoerror_prefix1
    df_Error["MonoErrorRoot"] = monoerror_root
    df_Error["MonoErrorSuffix1"] = monoerror_suffix1
    df_Error["MonoErrorSuffix2"] = monoerror_suffix2
    df_Error["MonoErrorSuffix3"] = monoerror_suffix3
    df_Error["ChangedIndexP2"] = changed_index_p3
    df_Error["ChangedIndexP2"] = changed_index_p2
    df_Error["ChangedIndexP1"] = changed_index_p1
    df_Error["ChangedIndexR"] = changed_index_r
    df_Error["ChangedIndexS1"] = changed_index_s1
    df_Error["ChangedIndexS2"] = changed_index_s2
    df_Error["ChangedIndexS2"] = changed_index_s3
    
    return df_Error

# GENERATE PARTICIPANT FILES
def generateParticipantFile (data, condition, p_error, p_polymor):
    # Define error distribution per condition (create function and put that all into function)
    errortype_r = ["NoErrorPoly"] * int (condition["r"] * 0.5) + ["Root"] * int (condition["r"] * 0.5)
    errortype_pr = ["NoErrorPoly"] * int (condition["pr"] * (1-p_error) * p_polymor) + ["Prefix1"] * int (condition["pr"] * p_error * p_polymor * 0.5) + ["Root"] * int (condition["pr"] * p_error * p_polymor * 0.5) + ["NoErrorMono"] * int (condition["pr"] * (1-p_error) * (1-p_polymor)) +["MonoPrefix1"] * int (condition["pr"] * p_error * (1-p_polymor) * 0.5) + ["MonoRoot"] * int (condition["pr"] * p_error * (1-p_polymor) * 0.5) 
    errortype_rs = ["NoErrorPoly"] * int (condition["rs"] * (1-p_error) * p_polymor) + ["Root"] * int (condition["rs"] * p_error * p_polymor * 0.5) +["Suffix1"] * int (condition["rs"] * p_error * p_polymor * 0.5) +  ["NoErrorMono"] * int (condition["rs"] * (1-p_error) * (1-p_polymor)) + ["MonoRoot"] * int (condition["rs"] * p_error * (1-p_polymor) * 0.5) + ["MonoSuffix1"] * int (condition["rs"] * p_error * (1-p_polymor) * 0.5) 
    errortype_prs = ["NoErrorPoly"] * int (condition["prs"] * (1-p_error) * p_polymor) + ["Prefix1"] * int (condition["prs"] * p_error * p_polymor * (1/3)) + ["Root"] * int (condition["prs"] * p_error * p_polymor * (1/3)) + ["Suffix1"] * int (condition["prs"] * p_error * p_polymor * (1/3)) + ["NoErrorMono"] * int (condition["prs"] * (1-p_error) * (1-p_polymor)) + ["MonoPrefix1"] * int (condition["prs"] * p_error * (1-p_polymor) * (1/3)) + ["MonoRoot"] * int (condition["prs"] * p_error * (1-p_polymor) * (1/3)) + ["MonoSuffix1"] * int (condition["prs"] * p_error * (1-p_polymor) * (1/3))  
    errortype_ppr = ["NoErrorPoly"] * int (condition["ppr"] * (1-p_error) * p_polymor) + ["Prefix2"] * int (condition["ppr"] * p_error * p_polymor * (1/3)) + ["Prefix1"] * int (condition["ppr"] * p_error * p_polymor * (1/3)) + ["Root"] * int (condition["ppr"] * p_error * p_polymor * (1/3)) + ["NoErrorMono"] * int (condition["ppr"] * (1-p_error) * (1-p_polymor)) + ["MonoPrefix2"] * int (condition["ppr"] * p_error * (1-p_polymor) * (1/3)) + ["MonoPrefix1"] * int (condition["ppr"] * p_error * (1-p_polymor) * (1/3)) + ["MonoRoot"] * int (condition["ppr"] * p_error * (1-p_polymor) * (1/3)) 
    errortype_rss = ["NoErrorPoly"] * int (condition["rss"] * (1-p_error) * p_polymor)+ ["Root"] * int (condition["rss"] * p_error * p_polymor * (1/3)) + ["Suffix1"] * int (condition["rss"] * p_error * p_polymor * (1/3))  + ["Suffix2"] * int (condition["rss"] * p_error * p_polymor * (1/3)) + ["NoErrorMono"] * int (condition["rss"] * (1-p_error) * (1-p_polymor)) + ["MonoRoot"] * int (condition["rss"] * p_error * (1-p_polymor) * (1/3)) + ["MonoSuffix1"] * int (condition["rss"] * p_error * (1-p_polymor) * (1/3)) + ["MonoSuffix2"] * int (condition["rss"] * p_error * (1-p_polymor) * (1/3))
    errortype_prss =["NoErrorPoly"] * int (condition["prss"] * (1-p_error) * p_polymor)+ ["Prefix1"] * int (condition["prss"] * p_error * p_polymor * (1/4)) + ["Root"] * int (condition["prss"] * p_error * p_polymor * (1/4)) + ["Suffix1"] * int (condition["prss"] * p_error * p_polymor * (1/4))  + ["Suffix2"] * int (condition["prss"] * p_error * p_polymor * (1/4)) + ["NoErrorMono"] * int (condition["prss"] * (1-p_error) * (1-p_polymor)) + ["MonoPrefix1"] * int (condition["prss"] * p_error * (1-p_polymor) * (1/4)) + ["MonoRoot"] * int (condition["prss"] * p_error * (1-p_polymor) * (1/4)) + ["MonoSuffix1"] * int (condition["prss"] * p_error * (1-p_polymor) * (1/4)) + ["MonoSuffix2"] * int (condition["prss"] * p_error * (1-p_polymor) * (1/4))
    errortype_pprs = ["NoErrorPoly"] * int (condition["pprs"] * (1-p_error) * p_polymor)+ ["Prefix2"] * int (condition["pprs"] * p_error * p_polymor * (1/4)) + ["Prefix1"] * int (condition["pprs"] * p_error * p_polymor * (1/4)) +["Root"] * int (condition["pprs"] * p_error * p_polymor * (1/4)) + ["Suffix1"] * int (condition["pprs"] * p_error * p_polymor * (1/4))  + ["NoErrorMono"] * int (condition["pprs"] * (1-p_error) * (1-p_polymor)) + ["MonoPrefix2"] * int (condition["pprs"] * p_error * (1-p_polymor) * (1/4)) + ["MonoPrefix1"] * int (condition["pprs"] * p_error * (1-p_polymor) * (1/4)) + ["MonoRoot"] * int (condition["pprs"] * p_error * (1-p_polymor) * (1/4)) + ["MonoSuffix1"] * int (condition["pprs"] * p_error * (1-p_polymor) * (1/4)) 
    errortype_pppr = ["NoErrorPoly"] * int (condition["pppr"] * (1-p_error) * p_polymor)+ ["Prefix3"] * int (condition["pppr"] * p_error * p_polymor * (1/4)) + ["Prefix2"] * int (condition["pppr"] * p_error * p_polymor * (1/4)) + ["Prefix1"] * int (condition["pppr"] * p_error * p_polymor * (1/4)) +["Root"] * int (condition["pppr"] * p_error * p_polymor * (1/4))  + ["NoErrorMono"] * int (condition["pppr"] * (1-p_error) * (1-p_polymor)) + ["MonoPrefix3"] * int (condition["pppr"] * p_error * (1-p_polymor) * (1/4)) + ["MonoPrefix2"] * int (condition["pppr"] * p_error * (1-p_polymor) * (1/4)) + ["MonoPrefix1"] * int (condition["pppr"] * p_error * (1-p_polymor) * (1/4)) + ["MonoRoot"] * int (condition["pppr"] * p_error * (1-p_polymor) * (1/4)) 
    errortype_rsss = ["NoErrorPoly"] * int (condition["rsss"] * (1-p_error) * p_polymor)+  ["Root"] * int (condition["rsss"] * p_error * p_polymor * (1/4)) + ["Suffix1"] * int (condition["rsss"] * p_error * p_polymor * (1/4))  + ["Suffix2"] * int (condition["rsss"] * p_error * p_polymor * (1/4)) + ["Suffix3"] * int (condition["rsss"] * p_error * p_polymor * (1/4)) + ["NoErrorMono"] * int (condition["rsss"] * (1-p_error) * (1-p_polymor)) + ["MonoRoot"] * int (condition["rsss"] * p_error * (1-p_polymor) * (1/4)) + ["MonoSuffix1"] * int (condition["rsss"] * p_error * (1-p_polymor) * (1/4)) + ["MonoSuffix2"] * int (condition["rsss"] * p_error * (1-p_polymor) * (1/4))+ ["MonoSuffix3"] * int (condition["rsss"] * p_error * (1-p_polymor) * (1/4))
 

    # randomly pick ncondition-times trials per condition and save in in a df
    r = data.query("Condition == 'r'").sample (n = condition["r"])
    r.insert(0, "errortype", errortype_r)
    pr = data.query("Condition == 'pr'").sample (n = condition["pr"])
    pr.insert(0, "errortype", errortype_pr)
    rs = data.query("Condition == 'rs'").sample (n = condition["rs"])
    rs.insert(0, "errortype", errortype_rs)
    prs = data.query("Condition == 'prs'").sample (n = condition["prs"])
    prs.insert(0, "errortype", errortype_prs)
    ppr = data.query("Condition == 'ppr'").sample (n = condition["ppr"])
    ppr.insert(0, "errortype", errortype_ppr)
    rss = data.query("Condition == 'rss'").sample (n = condition["rss"])
    rss.insert(0, "errortype", errortype_rss)
    prss = data.query("Condition == 'prss'").sample (n = condition["prss"])
    prss.insert(0, "errortype", errortype_prss)
    pprs = data.query("Condition == 'pprs'").sample (n = condition["pprs"])   
    pprs.insert(0, "errortype", errortype_pprs)
    pppr = data.query("Condition == 'pppr'").sample (n = condition ["pppr"])
    pppr.insert (0, "errortype", errortype_pppr)
    rsss = data.query ("Condition == 'rsss'").sample (n = condition["rsss"])    
    rsss.insert (0, "errortype", errortype_rsss)
                                    
    
    pardf= pd.concat ([r,pr,rs, prs, ppr, rss, prss, pprs, pppr, rsss])
    
    # Add Information if it is an error trial: 1 = True; 0 = False
    is_error = []
    for i in range (0, len(pardf)):
        errortype = pardf["errortype"].tolist()
        if errortype [i] == "NoErrorMono" or  errortype [i] == "NoErrorPoly": 
            is_error.append (0)
        else: 
            is_error.append (1)
            
    pardf.insert (1, "Is_Error", is_error)

    return pardf


# GENERATE FINAL TRIALLIST FOR PARTICIPANT
def generateTriallist (df):
    word1 = []
    word2 = []
    token = df["Token"].tolist()
    errortype = df["errortype"].tolist()
    monomorpheme = df["Monomorpheme"].tolist()
    errorprefix3 = df["ErrorPrefix3"].tolist()
    errorprefix2 = df["ErrorPrefix2"].tolist()
    errorprefix1 = df["ErrorPrefix1"].tolist()
    errorroot = df["ErrorRoot"].tolist()
    errorsuffix1 = df["ErrorSuffix1"].tolist()
    errorsuffix2 = df["ErrorSuffix2"].tolist()
    errorsuffix3 = df["ErrorSuffix3"].tolist()
    monoerrorprefix3 = df["MonoErrorPrefix3"].tolist()
    monoerrorprefix2 = df["MonoErrorPrefix2"].tolist()
    monoerrorprefix1 = df["MonoErrorPrefix1"].tolist()
    monoerrorroot = df["MonoErrorRoot"].tolist()
    monoerrorsuffix1 = df["MonoErrorSuffix1"].tolist()
    monoerrorsuffix2 = df["MonoErrorSuffix2"].tolist()
    monoerrorsuffix3 = df["MonoErrorSuffix3"].tolist()
    
    for i in range (0, len (df)): 
        # In case of errortrial (Polymorpheme)
        if errortype[i] == "Prefix3": 
            word1.append (token[i])
            word2.append (errorprefix3[i])
        elif errortype[i] == "Prefix2": 
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
        elif errortype[i] == "Suffix3": 
            word1.append (token[i])
            word2.append (errorsuffix3[i])
            
        # In case of errortrial (Monomorpheme):
        elif errortype[i] == "MonoPrefix3": 
            word1.append (monomorpheme[i])
            word2.append (monoerrorprefix3[i])
        elif errortype[i] == "MonoPrefix2": 
            word1.append (monomorpheme[i])
            word2.append (monoerrorprefix2[i])
        elif errortype[i] == "MonoPrefix1": 
            word1.append (monomorpheme[i])
            word2.append (monoerrorprefix1[i])
        elif errortype[i] == "MonoRoot": 
            word1.append (monomorpheme[i])
            word2.append (monoerrorroot[i])
        elif errortype[i] == "MonoSuffix1": 
            word1.append (monomorpheme[i])
            word2.append (monoerrorsuffix1[i])
        elif errortype[i] == "MonoSuffix2": 
            word1.append (monomorpheme[i])
            word2.append (monoerrorsuffix2[i])
        elif errortype[i] == "MonoSuffix3": 
            word1.append (monomorpheme[i])
            word2.append (monoerrorsuffix3[i])
        
        # In case of no errortrial (Monomorpheme):
        elif errortype[i] == "NoErrorPoly":
            word1.append(token[i])
            word2.append(token[i])
        
        # In case of no errortrial (Polymorpheme):
        else: 
            word1.append(monomorpheme[i])
            word2.append(monomorpheme[i])
            
    df.insert(0, "First", word1)
    df.insert(1, "Second", word2)
    df = df.sample (frac=1)
    
    return df


# VERIFICATION CODE
def verifyWords (df):
    prefixroot = []
    prefix1 = df["Prefix1"].tolist()
    root = df["Root"].tolist()
    for i in range (0, len(df)): 
        if prefix1[i] != "": 
            if prefix1[i][-1] != root[i][0]:
                prefixroot.append ("0")
            else: 
                prefixroot.append ("1") 
        else: 
            prefixroot.append ("0")
    
    suffixroot = []
    suffix1 = df["Suffix1"].tolist()
    root = df["Root"].tolist()
    for i in range (0, len(df)): 
        if suffix1[i] != "": 
            if root[i][-1] != suffix1[i][0]:
                suffixroot.append ("0")
            else: 
                suffixroot.append ("1")
        else: 
            suffixroot.append ("0")
            
    monoprefixprefix = []
    monoprefix1 = df["MonoPrefix1"].tolist()
    monoprefix2 = df["MonoPrefix2"].tolist()
    for i in range (0, len(df)): 
        if monoprefix1[i] != "" and monoprefix2[i] != "": 
            if monoprefix1[i][-1] != monoprefix2[i][0]:
                monoprefixprefix.append ("0")
            else: 
                monoprefixprefix.append ("1")
        else: 
            monoprefixprefix.append ("0")        
    
    monoprefixroot = []
    monoprefix1 = df["MonoPrefix1"].tolist()
    monoroot = df["MonoRoot"].tolist()
    for i in range (0, len(df)): 
        if monoprefix1[i] != "": 
            if monoprefix1[i][-1] != monoroot[i][0]:
                monoprefixroot.append ("0")
            else: 
                monoprefixroot.append ("1")
        else: 
            monoprefixroot.append ("0")
 
    monosuffixroot = []
    monosuffix1 = df["MonoSuffix1"].tolist()
    monoroot = df["MonoRoot"].tolist()
    for i in range (0, len(df)): 
        if monosuffix1[i] != "": 
            if monoroot[i][-1] != monosuffix1[i][0]:
                monosuffixroot.append ("0")
            else: 
                monosuffixroot.append ("1") 
        else: 
            monosuffixroot.append ("0")

    monosuffixsuffix = []
    monosuffix1 = df["MonoSuffix1"].tolist()
    monosuffix2 = df["MonoSuffix2"].tolist()
    for i in range (0, len(df)): 
        if monosuffix1[i] != "" and monosuffix2[i] != "": 
            if monosuffix1[i][-1] != monosuffix2[i][0]:
                monosuffixsuffix.append ("0")
            else: 
                monosuffixsuffix.append ("1")
        else: 
            monosuffixsuffix.append ("0")

    indexlist = []
    for i in range (0, len(df)): 
        if prefixroot[i] == "1" or monoprefixroot[i] == "1" or suffixroot[i] == "1" or monosuffixroot[i] == "1" or monosuffixsuffix[i] == "1" or monoprefixprefix == "1": 
            indexlist.append (i)
    df.drop (df.index[indexlist], inplace = True)
    
    return df
