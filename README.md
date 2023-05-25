## Behavoral Experiment on Language Processing

### Task
Participants will be shown a string of letters that they will have to memorize. Afterward, a second string of letters will be shown and they will need to decided whether the two words are the same or not by pressing the "F" and "J" key. Which key stands for "same words" and which for "different words" changes randomly across participants. 
  
### Experimental Design (pseudowords/English)
To generate morphologically complex pseudowords, we predefined [roots](https://github.com/dbechar/Morphemes-Behavioral-Experiment/blob/main/experimental_design/roots_english.csv) which are well-formed English-sounding phonological strings. For the prefixes and suffixes we limited ourselves to derivational affixes and also predefined combinations that appear frequently in the English language (e.g., full + ness; all combinations can be viewed [here](https://github.com/dbechar/Morphemes-Behavioral-Experiment/tree/main/experimental_design/english_pseudo)). Based on this root and affix pool we randomly selected monomorphemic words (words that only consisted of a root) and created polymorphemic words that differed in their comprised number of morphemes. For the English pseudo version, words could include between zero and two prefixes and zero and four suffixes. This left us with words that had between one and five morphemes and an overall number of 17 conditions (see [experimentla design](https://github.com/dbechar/Morphemes-Behavioral-Experiment/blob/main/experimental_design/design.csv) for more details).
<br><br>
To create the error words for all stimuli we opted to change one letter within the word while remaining consistent in the type of letter change: vowels were replaced with vowel, sonorants with sonorants and consonants with consonants. There is equal probability for the error to appear in the prefix, root, or suffix part of the word (i.e., in conditions prs, pprss, etc, the error to occur in any of these three parts of the word was 1/3; in pr, ppr, pppr 1/2 and rs, rss, etc. 1/2). If there are mutliple prefixes in the prefix part of the word, the chance of the error being in one of them is equal across all prefixes (e.g., in the condition ppr the chance of getting an error in any prefix is 0.5 and the chance to get an error in the root is 0.5). This is the same for multiple suffixes in the suffix part of the word.
<br><br>
The ratio between error-trials and no-error-trials is set at the beginning of the [stimulus_generator](https://github.com/dbechar/Morphemes-Behavioral-Experiment/blob/main/code/stimulus_generator.py) script (currently set to 0.5).
<br> <br>

Since morphological complexity covaries with word length, as a control, we created mono-morphemic pseudowords, which contain the same exact letter, only in different order.
In most cases, we opted to simply reverse every affix of the initial target word and then add them back together (e.g., target word = unkamable turns into control = numakelba). 

The morpheme and specific index within the morpheme in which the error occurs in is random but evens out across participants (see [verification code](https://github.com/dbechar/Morphemes-Behavioral-Experiment/blob/main/code/verification_code)).

### Experimental Design (real words/English)
Participants are shown real words with a varying number of morphemes (all conditions included in this experiment can be found in [design](https://github.com/dbechar/Morphemes-Behavioral-Experiment/blob/main/experimental_design/english_real/design_english_real.csv)). Our morphologically complex real words (target) were matched with real monomorphemic words (control) that are of the same length. The selected words ranged in length from five to twelve letters and contained between zero and two prefixes, as well as zero to four suffixes. Consequently, we arrived at a total of 13 conditions, with two to three trials per condition. The stimuli pool for the real words English experiment can be found in [english pool](https://github.com/dbechar/Morphemes-Behavioral-Experiment/tree/main/experimental_design/real_words_englisch). We used the same procedure as in the English pseudo version to create the errors. 

### Other Languages
We created a similar design for French (design for the french pseudo versio). 


