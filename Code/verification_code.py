# VERIFICATION CODE
import glob 
import pandas as pd

# READ IN TRIALLISTS
path = "../triallists"
csv_files = glob.glob(path + "/*.csv")
df_list = (pd.read_csv(file) for file in csv_files)

df_triallists = pd.concat (df_list, ignore_index = True)


# ERROR IN WHICH MORHEME (error_to_which_morpheme)
df1 = df_triallists["error_to_which_morpheme"].value_counts()
print ("Error in which morpheme:", df1)

# INDEX OF ERROR WITHIN MORPHEME
df2 = df_triallists["i_within_morpheme"].value_counts()
print ("Error in which index of morpheme:", df2)

