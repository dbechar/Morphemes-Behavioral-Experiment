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
First, all necessary libraries have to be downloaded: pandas and the functions we created.
```python
# Load libraries
import pandas as pd
from Functions import (generatePolymorphemes, generateMonomorphemes, generateError, generateReverseRoot)
```
#### Read in Stimuli
In order to create the design sheet we first need to read in all of our prefixes, roots, and suffixes. The stimuli pools are saved in the experimental_design folder as .csv.
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
Roots that after reversing them are no longer easily readable, joinable with the prefixes and roots or become real words will be discluded.
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
Based on these morphologically complex words our monomorphemic control words will be created. <br>
Each affix from the original morphologically complex word is taken and reversed and then added together again to create a new word. 
```python
#---- Generate mono-morphemic pseudowords that are based on morphologically complex pseudowords ---- 
df_Monomorphemes = generateMonomorphemes (df = df_Polymorphemes)
```
#### Generate Errors
The errorwords will be created for all words in all potential affixes (so we will have an "Prefix1Error", "RootError"... column).
One letter will be randomly chosen that will be replaced by another letter. The errorwords for the monomorphemic control words again are basedon the morphologically complex words: rekagable -> rakagable; ergakelba -> argakelba
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
At the end the Design sheet will be saved in the experimental_design folder.
```python
#---- Save experimental design as .csv ----
df_complete.to_csv("../experimental_design/design.csv", index = False)
```
