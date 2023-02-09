## Behavoral Experiment on Language Processing

### Task
Participants will be shown a string of letters that they will have to memorize. Afterward, a second string of letters will be shown and they will need to decided whether the two words are the same or not by pressing the "F" and "J" key. Which key stands for "same words" and which for "different words" changes randomly across participants. 
  
### Experimental Design (pseudowords/English)
The [experimental design](https://github.com/dbechar/Morphemes-Behavioral-Experiment/blob/main/experimental_design/design.csv) consists of conditions with words of varying morphological complexity.
To generate morphologically complex pseudowords, we predefined [roots](https://github.com/dbechar/Morphemes-Behavioral-Experiment/blob/main/experimental_design/roots_english.csv) that sound like English words, however cannot be found in a dictionary. For the [prefixes](https://github.com/dbechar/Morphemes-Behavioral-Experiment/blob/main/experimental_design/prefixes_english.csv) and [suffixes](https://github.com/dbechar/Morphemes-Behavioral-Experiment/blob/main/experimental_design/suffixes_english.csv) we limited ourselves to derivational affixes and also predefined combinations that do appear frequently in the English language (e.g., full + ness). Based on this affix pool we randomly created monomorphemic words (just the root) and polymorphemic words ( 0-3 prefixes + the root + 0-3 suffixes). The different word conditions therefore were: r, pr, rs, prs, ppr, rss, prss pprs, pppr, rsss, prsss, ppprs, pprss, pprsss, ppprss, ppprsss. 
<br><br>
For the same-different task, to create the errors, we opted to change only one letter within the word. Vowels are replaced with other vowels, consonants with consonants, and sonorants with sonorants.
There is equal probability to create an error on the prefix part of the word, its root its suffix part (i.e., in conditions prs, pprss, etc, the error to occur in any of these three parts of the word was 1/3; in pr, ppr, pppr 1/2 and rs, rss, etc. 1/2). If there are mutliple prefixes in the prefix part of the word, the chance of the error being in one of them is equal across all prefixes (e.g., in the condition ppr the chance of getting an error in any prefix is 0.5 and the chance to get an error in the root is 0.5). This is the same for multiple suffixes in the suffix part of the word.
<br><br>
The ratio between error-trials and no-error-trials is set at the beginning of the [stimulus_generator](https://github.com/dbechar/Morphemes-Behavioral-Experiment/blob/main/code/stimulus_generator.py) script (currently set to 0.5).
<br> <br>
Since morphological complexity covaries with word length, as a control, we created mono-morphemic pseudowords, which contain the same exact letter, only in different order.
In most cases, we opted to simply reverse every affix of the initial target word and then add them back together (e.g., target word = unkamable turns into control = numakelba). Similarily to the target words, to create the error we randomly changed one letter. Here too, vowels replaced vowels, consonants replaced consonants, and sonorants replaced sonorants. Errors were divided equally across affixes. The morpheme and specific index within the morpheme in which the error occurs in is random but evens out across participants (see [verification code](https://github.com/dbechar/Morphemes-Behavioral-Experiment/blob/main/code/verification_code)).

### Experimental Design (real words/English)
3-4 sentences, with links to the final pools.

### Other Languages
We created a similar design for French. 
## French
[roots](https://github.com/dbechar/Morphemes-Behavioral-Experiment/blob/main/experimental_design/roots_french.csv)

[prefixes](https://github.com/dbechar/Morphemes-Behavioral-Experiment/blob/main/experimental_design/prefixes_french.csv)

[suffixes](https://github.com/dbechar/Morphemes-Behavioral-Experiment/blob/main/experimental_design/suffixes_french.csv)

[real words (target)]

[real words (control)]

