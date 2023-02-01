### Experimental Design
This script does:
- read in stimulus lists
- randomly creates roots
- randomly creates polymorphemic words
- randomly creates mono-morphemic words
- create all types of errorwords for the polymorphemes
- save all created words and additional information in Excel-File

Author: Deliane Bechar <br>
Date: 24.01.2023


#### Preperation
First, all necessary libraries have to be downloaded: pandas, os (to set the working directory), and the functions we created.
```python
# Load libraries
import pandas as pd
import os
os.chdir("C:/Users/delia/OneDrive/Desktop/Morphemes/Morphemes/Code")
from Functions import (generatePolymorphemes, generateMonomorphemes, generateError, generateReverseRoot)
```
#### Read in Stimuli
In order to create the design sheet we first need to read in all of our prefixes, roots, and suffixes.
```python
# Read in file 
prefixes = pd.read_csv("../experimental_design/prefixes.csv")
roots = pd.read_csv("../experimental_design/roots.csv")
suffixes = pd.read_csv("../experimental_design/suffixes.csv")
```

#### Generate Roots
If roots are not pre defined we can randomly create new once. <br> 
However, this function is not in the newest version of "Functions" and thus would need to be readded if desired.

```python
#---- Generate roots ----
# roots["Root"] = generateRoots(value = 10)
```
####  Generate Reversed Root
We can now generate the reversed roots to check, if they make sense as they will be used for the control monomorphemes. <br>
Roots that after reversing them are no longer easily readable, joinable with the prefixes and roots or actually become real words will be discluded.
```python
#---- Generate reversed root ----
testdf = generateReverseRoot (roots)
```
#### Generate Morphologically Complex Words
Based on the final list of prefixes, root, and suffixes the morphologically complex words are created.
```python
#---- Generate morphologically complex pseudowords ----
df_Polymorphemes = generatePolymorphemes(prefixes, roots, suffixes)
```
#### Generate Monomorphemic Control
Based on these morphologically complex words our monomorphemic control words. <br>
Each affix from the original morphologically complex word is taken and reversed and then added together again to create a new word. 
```python
#---- Generate mono-morphemic pseudowords that are based on morphologically complex pseudowords ---- 
df_Monomorphemes = generateMonomorphemes (df = df_Polymorphemes)
```
#### Generate Errors
The errorwords will be created for all words in all potential affixes (so we will have an "Prefix1Error", "RootError"... column). <br>
One letter will be randomly chosen that will be replaced by another letter. <br> The errorwords for the monomorphemic control words again are based <br>
on the morphologically complex words: rekagable -> rakagable; ergakelba -> argakelba
```python
# ---- Generate Errorwords for Polymorphemes ----
df_Error = generateError(df = df_Polymorphemes)
```
#### Merge Dataframes Together
All dataframes will be concated to create one final dataframe that includes all information.
```python
#---- Concate all dataframes ----
df_complete = pd.concat([df_Polymorphemes, df_Monomorphemes, df_Error], axis = 1)
```

#### Save Final Dataframe
At the end the Design sheet will be saved.
```python
#---- Save experimental design as .csv ----
df_complete.to_csv("../experimental_design/design.csv", index = False)
```
