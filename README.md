## Behavoral Experiment on Language Processing

### Task
Participants will be shown a string of letters that they will have to memorize. Afterward, a second string of letters will be shown and they will need to decided whether the two words are the same or not by pressing the "F" and "J" key. Which key stands for "same words" and which for "different words" changes across participants. 

### Experimental Design
We predefined roots that sound like English words, however cannot be found in a dictionary. For the prefixes and suffixes we limited ourselves to derivational affixes and also predefined combinations that do appear frequently in the English language (e.g., full + ness). Based on this affix pool we randomly created monomorphemic words (just the root) and polymorphemic words ( 0-3 prefixes + the root + 0-3 suffixes). The different word conditions therefore were: r, pr, rss, rs, prs, prss, pprs. These conditions are defined in the [design workbook](https://github.com/dbechar/Morphemes-Behavioral-Experiment/blob/main/experimental_design/design.csv). 
<br><br>
To create the errors we opted to change only one letter within the word. Vowels are replaced with other vowels, consonants with consonants, and sonorants with sonorants.
The position of errors are randomly assigned to the created words. They can be either in any of the prefixes, the root, or any of the suffixes depending on the original word. The ratio between error-trials and no-error-trials is set at the beginning of the [stimulus_generator](https://github.com/dbechar/Morphemes-Behavioral-Experiment/blob/main/code/stimulus_generator.py) script (currently set to 0.5).
<br> <br>
For the control words we opted to reverse every affix of the intital target word and then add them back together (e.g., target word = unkamable turns into control = numakelba). Similarily to the target words, to create the error we randomly changed one letter. Here too vowels replaced vowels, consonants replaced consonants, and sonorants replaced sonorants. The morpheme and specific index within the morpheme in which the error occurs in is random but evens out across participants (see [verification code](https://github.com/dbechar/Morphemes-Behavioral-Experiment/blob/main/code/verification_code.py)). 


