### Triallist Creator
This script does:
- Read in and create all test words
- Creat one triallists that is based on certain prerequisits that are set at the beginning 
- save triallists as .csv in the triallists folder

Author: Deliane Bechar <br>
Date: 30.01.2023

#### LOAD LIBRARIES AND FUNCTIONS
First, all necessary libraries have to read in as well as all necessary functions.
```python
import pandas as pd
import random
from Functions import (generatePolymorphemes, generateMonomorphemes, generateError, verifyWords, generateParticipantFile, generateTriallist)
```

#### READ IN STIMULUS FILES
To create the morphologically complex and control words, the predefined prefixes, roots, and suffixes will have to be read in.
```python
prefixes = pd.read_csv("../experimental_design/prefixes.csv")
roots = pd.read_csv("../experimental_design/roots.csv")
suffixes = pd.read_csv("../experimental_design/suffixes.csv")
```

#### SET SEED
Set seed as control.
```python
random.seed(19)
```

#### DEFINE FILE NUMBER
```python
file_number = 1
```

#### DEFINE NUMBER OF TRIALS PER CONDITION
The number of trials per condition that should be included in the final triallist is defined here.
```python
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
```

#### DEFINE ERRORRATE
Before running the script the errorrate has to be defined. That means it has to be defined how many percent of trials should show the errorwords. <br>
Also the ratio between morphologically complex and the control words has to be set. 
```python
p_error = 0.5
p_polymor = 0.5
```

#### GENERATE POLYMORPHEMES 
Based on the final list of prefixes, root, and suffixes the morphologically complex words are created.
```pyhon
df_Polymorphemes = generatePolymorphemes(prefixes, roots, suffixes)
```

#### GENERATE CONTROL (MONOMORPHEMES) 
Based on these morphologically complex words our monomorphemic control words. <br>
Each affix from the original morphologically complex word is taken and reversed and then added together again to create a new word.
```python
df_Monomorphemes = generateMonomorphemes (df = df_Polymorphemes)
```

#### ADD ERROR 
The errorwords will be created for all words in all potential affixes (so we will have an "Prefix1Error", "RootError"... column). <br>
One letter will be randomly chosen that will be replaced by another letter. The errorwords for the monomorphemic control words <br>
again are basedon the morphologically complex words: rekagable -> rakagable; ergakelba -> argakelba
```python
df_Error = generateError(df = df_Polymorphemes)
```

#### CONCATE DATAFRAMES
All dataframes will be concated to create one final dataframe that includes all information.
```python
df_complete = pd.concat([df_Polymorphemes, df_Monomorphemes, df_Error], axis = 1)
```

#### VERIFICATION CODE
Words will be ckecked to make sure they are readable.
```python
df_verified = verifyWords (df_complete)
```

#### RANDOMIZE LIST WITH ERRORS
Depending on the previously defined number of trials per condition that should be included in the final triallist and <br>
the defined errorate and mono-/polymorpheme a new dataframe is created. Which trial should be which kind of error is also defined here. 
```python
pardf = generateParticipantFile (df_verified, condition, p_error, p_polymor)
```

#### GENERATE TRIALLIST
Based on the qssigned error the first and second word that the participant will see are picked out and the final triallist is created. 
```python
triallist = generateTriallist (df = pardf)
```
 
#### SAVE TRIALLIST
The final triallist is saved in the triallist folder. 
```python
path = "../triallists/" + str(file_number) + "triallist.csv"
triallist.to_csv (path, index = False)
```
