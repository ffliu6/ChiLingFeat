# ChiLingFeat

ChiLingFeat is a Python research project for various Chinese handcrafted linguistic features. 

For extracting features, the spacy is first utilized to tokenize the input Chinese string into sentences (If the input is a sentence, itself would be returned). 

# Installation

1. Install the requirement packages
```bash
git clone https://github.com/ffliu6/ChiLingFeat.git
pip install -r ChiLingFeat/requirements.txt
```

2. Spacy
This library assumes that you have spaCy version 3.0+ installed.
```bash
python -m spacy download zh_core_web_trf
```

3. SuPar
```bash
pip install -U supar==1.0.0
```
# How to use

```python
"""
Import

this is the only import you need
"""
from lingfeat import extractor


"""
Pass text

here, text must be in string type
"""
text = "..."
LingFeat = extractor.pass_text(text)


"""
Preprocess text

options (all boolean):
- short (default False): include short words of < 3 letters
- see_token (default False): return token list
- see_sent_token (default False): return tokens in sentences

output:
- n_token
- n_sent
- token_list (optional)
- sent_token_list (optional)
"""
LingFeat.preprocess()
# or
# print(LingFeat.preprocess())


"""
Extract features

each method returns a dictionary of the corresponding features
"""
# Discourse (Disco) Features
EnDF = LingFeat.EnDF_() # Entity Density Features

# Syntactic (Synta) Features
PhrF = LingFeat.PhrF_() # Noun/Verb/Adj/Adv/... Phrasal Features
TrSF = LingFeat.TrSF_() # (Parse) Tree Structural Features
POSF = LingFeat.POSF_() # Noun/Verb/Adj/Adv/... Part-of-Speech Features

# Lexico Semantic (LxSem) Features
TTRF = LingFeat.TTRF_() # Type Token Ratio Features
VarF = LingFeat.VarF_() # Noun/Verb/Adj/Adv Variation Features 

# Shallow Traditional (ShTra) Features
ShaF = LingFeat.ShaF_() # Shallow Features (e.g. avg number of tokens)
```

# Feature List

In total 231 features would be extracted from four main perspectives, *Shallow features*, *LexicaoSemantic features*, *Syntactic features*, and *Discourse features*. . As shown in the table below, the Fun column represents if the feature is for sentence or passage, in which *S* represents only for *sentence-level*, *P* represents only for *passage-level*, *S/P* represents for both *sentence-level* and *passage-level*. 

| Index | Category | Sub-category | Description | Sung et al. 2015 | Lu et al. 2020 | Lee et al. 2021 | State | Fun | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  Shallow features  |  Character  |  Percentage of characters containing 1 to 10 strokes per sentence  |    |  1  |    |  B  |  S  |  | 
| 2 |    |    |  Percentage of characters 11 to 20 strokes per sentence  |    |  1  |    |  B  |  S  |  | 
| 3 |    |    |  Percentage of characters containing over 20 strokes per sentence  |    |  1  |    |  B  |  S  |  | 
| 4 |    |    |  Average number of strokes per word  |    |  1  |    |  B  |  S  |  | 
| 5 |    |    |  Percentage of HSK1 to HSK3-characters per sentence  |    |  1  |    |  B  |  S  |  | 
| 6 |    |    |  Percentage of HSK4 to HSK5-characters per sentence  |    |  1  |    |  B  |  S  |  | 
| 7 |    |    |  Percentage of HSK6-characters per sentence  |    |  1  |    |  B  |  S  |  | 
| 8 |    |    |  Percentage of not-HSK-characters per sentence  |    |  1  |    |  B  |  S  |  | 
| 9 |    |    |  Total number of characters containing 1 to 10 strokes  |  1  |    |    |  A/B  |  S  |  | 
| 10 |    |    |  Total number of characters containing 11 to 20 strokes  |  1  |    |    |  A/B  |  S/P  |  | 
| 11 |    |    |  average count of characters per sentence  |    |    |  1  |  A/B  |  S/P  |  | 
| 12 |    |    |  average count of characters per token  |    |    |  1  |  A/B  |  S/P  |  | 
| 13 |    |  Word  |  Average number of characters per word per sentence  |    |  1  |  1  |  A/B  |  S  |  | 
| 14 |    |    |  Average number of characters per unique word per sentence  |    |  1  |    |  B  |  S  |  | 
| 15 |    |    |  Number of two-character words per sentence  |    |  1  |    |  B  |  S  |  | 
| 16 |    |    |  Percentage of two-character words per sentence  |    |  1  |    |  B  |  S  |  | 
| 17 |    |    |  Number of three-character words per sentence  |    |  1  |    |  B  |  S  |  | 
| 18 |    |    |  Percentage of three-character words per sentence  |    |  1  |    |  B  |  S  |  | 
| 19 |    |    |  Number of four-character words per sentence  |    |  1  |    |  B  |  S  |  | 
| 20 |    |    |  Percentage of four-character words per sentence  |    |  1  |    |  B  |  S  |  | 
| 21 |    |    |  Number of five-up-character words per sentence  |    |  1  |    |  B  |  S  |  | 
| 22 |    |    |  Percentage of five-up-character words per sentence  |    |  1  |    |  B  |  S  |  | 
| 23 |    |    |  Percentage of HSK1 to HSK3-words per sentence  |    |  1  |    |  B  |  S  |  | 
| 24 |    |    |  Percentage of HSK4 to HSK5-words per sentence  |    |  1  |    |  B  |  S  |  | 
| 25 |    |    |  Percentage of HSK6-words per sentence  |    |  1  |    |  B  |  S  |  | 
| 26 |    |    |  Percentage of Not-HSK-words per sentence  |    |  1  |    |  B  |  S  |  | 
| 27 |    |    |  Percentage of words in 1-1000 mardain frequency list (most-common) per sentence  |    |  1  |    |  B  |  S  |  | 
| 28 |    |    |  Percentage of words in 2-2000 mardain frequency list (second-most-common) per sentence  |    |  1  |    |  B  |  S  |  | 
| 29 |    |    |  Percentage of words in 1-3000 mardain frequency list (all most-common) per sentence  |    |  1  |    |  B  |  S  |  | 
| 30 |    |    |  total count of tokens x total count of sentence  |    |     |  1  |  A/B  |  S/P  |  | 
| 31 |    |    |  sqrt(total count of tokens x total count of sentence)  |    |    |  1  |  A/B  |  S/P  |  | 
| 32 |    |    |  log(total count of tokens)/log(total count of sentence)  |    |    |  1  |  A/B  |  S/P  |  | 
| 33 |    |    |  average count of tokens per sentence  |  1  |    |  1  |  A/B  |  S/P  |  | 
| 34 |    |  Sentence  |  Number of multi-character words per sentence  |    |  1  |    |  B  |  S  |  | 
| 35 |    |    |  Proportion of difficult words, as according to mandarin frequency lists, divided by the total number of words  |  1  |    |    |    |  *N  |  | 
| 36 |  Syntactic features  |  POS  |  total count of Noun POS tags  |    |  1  |  1  |  A/B  |  S/P  |  | 
| 37 |    |    |  average count of Noun POS tags per sentence  |    |  1  |  1  |  A/B  |  S/P  |  | 
| 38 |    |    |  average count of Noun POS tags per token  |    |    |  1  |  A/B  |  S/P  |  | 
| 39 |    |    |  ratio of Noun POS count to Adjective POS count  |    |    |  1  |  A/B  |  S/P  |  | 
| 40 |    |    |  ratio of Noun POS count to Verb POS count  |    |    |  1  |  A/B  |  S/P  |  | 
| 41 |    |    |  ratio of Noun POS count to Adverb POS count  |    |    |  1  |  A/B  |  S/P  |  | 
| 42 |    |    |  ratio of Noun POS count to Subordinating Conjunction count  |    |    |  1  |  A/B  |  S/P  |  | 
| 43 |    |    |  ratio of Noun POS count to Coordinating Conjunction count  |    |    |  1  |  A/B  |  S/P  |  | 
| 44 |    |    |  total count of Verb POS tags  |    |  1  |  1  |  A/B  |  S/P  |  | 
| 45 |    |    |  average count of Verb POS tags per sentence  |    |  1  |  1  |  A/B  |  S/P  |  | 
| 46 |    |    |  average count of Verb POS tags per token  |    |    |  1  |  A/B  |  S/P  |  | 
| 47 |    |    |  ratio of Verb POS count to Adjective POS count  |    |    |  1  |  A/B  |  S/P  |  | 
| 48 |    |    |  ratio of Verb POS count to Noun POS count  |    |    |  1  |  A/B  |  S/P  |  | 
| 49 |    |    |  ratio of Verb POS count to Adverb POS count  |    |    |  1  |  A/B  |  S/P  |  | 
| 50 |    |    |  ratio of Verb POS count to Subordinating Conjunction count  |    |    |  1  |  A/B  |  S/P  |  | 
| 51 |    |    |  ratio of Verb POS count to Coordinating Conjunction count  |    |    |  1  |  A/B  |  S/P  |  | 
| 52 |    |    |  total count of Adjective POS tags  |    |  1  |  1  |  A/B  |  S/P  |  | 
| 53 |    |    |  average count of Adjective POS tags per sentence  |    |  1  |  1  |  A/B  |  S/P  |  | 
| 54 |    |    |  average count of Adjective POS tags per token  |    |    |  1  |  A/B  |  S/P  |  | 
| 55 |    |    |  ratio of Adjective POS count to Noun POS count  |    |    |  1  |  A/B  |  S/P  |  | 
| 56 |    |    |  ratio of Adjective POS count to Verb POS count  |    |    |  1  |  A/B  |  S/P  |  | 
| 57 |    |    |  ratio of Adjective POS count to Adverb POS count  |    |    |  1  |  A/B  |  S/P  |  | 
| 58 |    |    |  ratio of Adjective POS count to Subordinating Conjunction count  |    |    |  1  |  A/B  |  S/P  |  | 
| 59 |    |    |  ratio of Adjective POS count to Coordinating Conjunction count  |    |    |  1  |  A/B  |  S/P  |  | 
| 60 |    |    |  total count of Adverb POS tags  |    |  1  |  1  |  A/B  |  S/P  |  | 
| 61 |    |    |  average count of Adverb POS tags per sentence  |    |  1  |  1  |  A/B  |  S/P  |  | 
| 62 |    |    |  average count of Adverb POS tags per token  |    |    |  1  |  A/B  |  S/P  |  | 
| 63 |    |    |  ratio of Adverb POS count to Adjective POS count  |    |    |  1  |  A/B  |  S/P  |  | 
| 64 |    |    |  ratio of Adverb POS count to Noun POS count  |    |    |  1  |  A/B  |  S/P  |  | 
| 65 |    |    |  ratio of Adverb POS count to Verb POS count  |    |    |  1  |  A/B  |  S/P  |  | 
| 66 |    |    |  ratio of Adverb POS count to Subordinating Conjunction count  |    |    |  1  |  A/B  |  S/P  |  | 
| 67 |    |    |  ratio of Adverb POS count to Coordinating Conjunction count  |    |    |  1  |  A/B  |  S/P  |  | 
| 68 |    |    |  total count of Subordinating Conjunction POS tags  |  1  |  1  |  1  |  A/B  |  S/P  |  | 
| 69 |    |    |  average count of Subordinating Conjunction POS tags per sentence  |    |  1  |  1  |  A/B  |  S/P  |  | 
| 70 |    |    |  average count of Subordinating Conjunction POS tags per token  |    |    |  1  |  A/B  |  S/P  |  | 
| 71 |    |    |  ratio of Subordinating Conjunction POS count to Adjective POS count  |    |    |  1  |  A/B  |  S/P  |  | 
| 72 |    |    |  ratio of Subordinating Conjunction POS count to Noun POS count  |    |    |  1  |  A/B  |  S/P  |  | 
| 73 |    |    |  ratio of Subordinating Conjunction POS count to Verb POS count  |    |    |  1  |  A/B  |  S/P  |  | 
| 74 |    |    |  ratio of Subordinating Conjunction POS count to Adverb POS count  |    |    |  1  |  A/B  |  S/P  |  | 
| 75 |    |    |  ratio of Subordinating Conjunction POS count to Coordinating Conjunction count  |    |    |  1  |  A/B  |  S/P  |  | 
| 76 |    |    |  total count of Coordinating Conjunction POS tags  |  1  |  1  |  1  |  A/B  |  S/P  |  | 
| 77 |    |    |  average count of Coordinating Conjunction POS tags per sentence  |    |  1  |  1  |  A/B  |  S/P  |  | 
| 78 |    |    |  average count of Coordinating Conjunction POS tags per token  |    |    |  1  |  A/B  |  S/P  |  | 
| 79 |    |    |  ratio of Coordinating Conjunction POS count to Adjective POS count  |    |    |  1  |  A/B  |  S/P  |  | 
| 80 |    |    |  ratio of Coordinating Conjunction POS count to Noun POS count  |    |    |  1  |  A/B  |  S/P  |  | 
| 81 |    |    |  ratio of Coordinating Conjunction POS count to Verb POS count  |    |    |  1  |  A/B  |  S/P  |  | 
| 82 |    |    |  ratio of Coordinating Conjunction POS count to Adverb POS count  |    |    |  1  |  A/B  |  S/P  |  | 
| 83 |    |    |  ratio of Coordinating Conjunction POS count to Subordinating Conjunction count  |    |    |  1  |  A/B  |  S/P  |  | 
| 84 |    |    |  total count of Content words  |  1  |  1  |  1  |  A/B  |  S/P  |  | 
| 85 |    |    |  average count of Content words per sentence  |    |  1  |  1  |  A  |  S/P  |  | 
| 86 |    |    |  average count of Content words per token  |    |    |  1  |  A  |  S/P  |  | 
| 87 |    |    |  total count of Function words  |    |  1  |  1  |  A  |  S/P  |  | 
| 88 |    |    |  average count of Function words per sentence  |    |  1  |  1  |  A  |  S/P  |  | 
| 89 |    |    |  average count of Function words per token  |    |    |  1  |  A  |  S/P  |  | 
| 90 |    |    |  ratio of Content words to Function words  |    |    |  1  |  A  |  S/P  |  |  
| 92 |    |    |  Percentage of unique adjectives per sentence  |    |  1  |    |  A/B  |  S  |  | 
| 93 |    |    |  Number of unique adjectives per sentence  |    |  1  |    |  A/B  |  S  |  | 
| 94 |    |    |  Percentage of unique functional words per sentence  |    |  1  |    |  A/B  |  S  |  | 
| 95 |    |    |  Number of unique functional words per sentence  |    |  1  |    |  A/B  |  S  |  | 
| 96 |    |    |  Number of unique verbs per sentence  |    |  1  |    |  A/B  |  S  |  | 
| 97 |    |    |  Percentage of unique verbs per sentence  |    |  1  |    |  A/B  |  S  |  | 
| 98 |    |    |  Number of unique nouns per sentence  |    |  1  |    |  A/B  |  S  |  | 
| 99 |    |    |  Percentage of unique nouns per sentence  |    |  1  |    |  A/B  |  S  |  | 
| 102 |    |    |  Number of unique content words per sentence  |    |  1  |    |  A  |  S/P  |  | 
| 103 |    |    |  Percentage of unique content words per sentence  |    |  1  |    |  A  |  S/P  |  |  
| 106 |    |    |  Percentage of unique adverbs per sentence  |    |  1  |    |  A  |  S/P  |  | 
| 107 |    |    |  Number of unique adverbs per sentence  |    |  1  |    |  A  |  S/P  |  | 
| 108 |    |  Phrases  |  total count of Noun phrases  |    |  1  |  1  |  A  |  S/P  |  | 
| 109 |    |    |  average count of Noun phrases per sentence  |    |    |  1  |  A  |  S/P  |  | 
| 110 |    |    |  average count of Noun phrases per token  |    |    |  1  |  A  |  S/P  |  | 
| 111 |    |    |  ratio of Noun phrases count to Verb phrases count  |    |    |  1  |  A  |  S/P  |  | 
| 112 |    |    |  ratio of Noun phrases count to Subordinate Clauses count  |    |    |  1  |  A  |  S/P  |  | 
| 113 |    |    |  ratio of Noun phrases count to Prep phrases count  |    |    |  1  |  A  |  S/P  |  | 
| 114 |    |    |  ratio of Noun phrases count to Adj phrases count  |    |    |  1  |  A  |  S/P  |  | 
| 115 |    |    |  ratio of Noun phrases count to Adv phrases count  |    |    |  1  |  A  |  S/P  |  | 
| 116 |    |    |  total count of Verb phrases  |    |  1  |  1  |  A  |  S/P  |  | 
| 117 |    |    |  average count of Verb phrases per sentence  |    |    |  1  |  A  |  S/P  |  | 
| 118 |    |    |  average count of Verb phrases per token  |    |    |  1  |  A  |  S/P  |  | 
| 119 |    |    |  ratio of Verb phrases count to Noun phrases count  |    |    |  1  |  A  |  S/P  |  | 
| 120 |    |    |  ratio of Verb phrases count to Subordinate Clauses count  |    |    |  1  |  A  |  S/P  |  | 
| 121 |    |    |  ratio of Verb phrases count to Prep phrases count  |    |    |  1  |  A  |  S/P  |  | 
| 122 |    |    |  ratio of Verb phrases count to Adj phrases count  |    |    |  1  |  A  |  S/P  |  | 
| 123 |    |    |  ratio of Verb phrases count to Adv phrases count  |    |    |  1  |  A  |  S/P  |  | 
| 124 |    |    |  total count of Subordinate Clauses  |    |    |  1  |  A  |  S/P  |  | 
| 125 |    |    |  average count of Subordinate Clauses per sentence  |    |    |  1  |  A  |  S/P  |  | 
| 126 |    |    |  average count of Subordinate Clauses per token  |    |    |  1  |  A  |  S/P  |  | 
| 127 |    |    |  ratio of Subordinate Clauses count to Noun phrases count  |    |    |  1  |  A  |  S/P  |  | 
| 128 |    |    |  ratio of Subordinate Clauses count to Verb phrases count  |    |    |  1  |  A  |  S/P  |  | 
| 129 |    |    |  ratio of Subordinate Clauses count to Prep phrases count  |    |    |  1  |  A  |  S/P  |  | 
| 130 |    |    |  ratio of Subordinate Clauses count to Adj phrases count  |    |    |  1  |  A  |  S/P  |  | 
| 131 |    |    |  ratio of Subordinate Clauses count to Adv phrases count  |    |    |  1  |  A  |  S/P  |  | 
| 132 |    |    |  total count of prepositional phrases  |    |  1  |  1  |  A  |  S/P  |  | 
| 133 |    |    |  average count of prepositional phrases per sentence  |  1  |    |  1  |  A  |  S/P  |  | 
| 134 |    |    |  average count of prepositional phrases per token  |    |    |  1  |  A  |  S/P  |  | 
| 135 |    |    |  ratio of Prep phrases count to Noun phrases count  |    |    |  1  |  A  |  S/P  |  | 
| 136 |    |    |  ratio of Prep phrases count to Verb phrases count  |    |    |  1  |  A  |  S/P  |  | 
| 137 |    |    |  ratio of Prep phrases count to Subordinate Clauses count  |    |    |  1  |  A  |  S/P  |  | 
| 138 |    |    |  ratio of Prep phrases count to Adj phrases count  |    |    |  1  |  A  |  S/P  |  | 
| 139 |    |    |  ratio of Prep phrases count to Adv phrases count  |    |    |  1  |  A  |  S/P  |  | 
| 140 |    |    |  total count of Adjective phrases  |    |    |  1  |  A  |  S/P  |  | 
| 141 |    |    |  average count of Adjective phrases per sentence  |    |    |  1  |  A  |  S/P  |  | 
| 142 |    |    |  average count of Adjective phrases per token  |    |    |  1  |  A  |  S/P  |  | 
| 143 |    |    |  ratio of Adj phrases count to Noun phrases count  |    |    |  1  |  A  |  S/P  |  | 
| 144 |    |    |  ratio of Adj phrases count to Verb phrases count  |    |    |  1  |  A  |  S/P  |  | 
| 145 |    |    |  ratio of Adj phrases count to Subordinate Clauses count  |    |    |  1  |  A  |  S/P  |  | 
| 146 |    |    |  ratio of Adj phrases count to Prep phrases count  |    |    |  1  |  A  |  S/P  |  | 
| 147 |    |    |  ratio of Adj phrases count to Adv phrases count  |    |    |  1  |  A  |  S/P  |  | 
| 148 |    |    |  total count of Adverb phrases  |    |    |  1  |  A  |  S/P  |  | 
| 149 |    |    |  average count of Adverb phrases per sentence  |    |    |  1  |  A  |  S/P  |  | 
| 150 |    |    |  average count of Adverb phrases per token  |    |    |  1  |  A  |  S/P  |  | 
| 151 |    |    |  ratio of Adv phrases count to Noun phrases count  |    |    |  1  |  A  |  S/P  |  | 
| 152 |    |    |  ratio of Adv phrases count to Verb phrases count  |    |    |  1  |  A  |  S/P  |  | 
| 153 |    |    |  ratio of Adv phrases count to Subordinate Clauses count  |    |    |  1  |  A  |  S/P  |  | 
| 154 |    |    |  ratio of Adv phrases count to Prep phrases count  |    |    |  1  |  A  |  S/P  |  | 
| 155 |    |    |  ratio of Adv phrases count to Adj phrases count  |    |    |  1  |  A  |  S/P  |  | 
| 156 |    |    |  Average length of noun phrases per sentence  |    |  1  |    |    |  S/P  |  | 
| 157 |    |    |  Average length of verbal phrases per sentence  |    |  1  |    |    |  S/P  |  | 
| 158 |    |    |  Average length of prepositional phrases per sentence  |    |  1  |    |    |  S/P  |  | 
| 159 |    |  Clauses  |  total Tree height of all sentences  |    |    |  1  |  A/B  |  S/P  |  | 
| 160 |    |    |  average Tree height per sentence  |    |  1  |  1  |  A/B  |  S/P  |  | 
| 161 |    |    |  average Tree height per token (word)  |    |    |  1  |  A/B  |  S/P  |  | 
| 162 |    |    |  total length of flattened Trees  |    |    |  1  |  A/B  |  S/P  |  | 
| 163 |    |    |  average length of flattened Trees per sentence  |    |    |  1  |  A  |  S/P  |  | 
| 164 |    |    |  average length of flattened Trees per token (word)  |    |    |  1  |  A  |  S/P  |  | 
| 165 |    |    |  Average dependency distance per sentence  |    |  1  |    |  B  |  P  |  | 
| 166 |    |    |  Maximum dependency distance per sentence  |    |  1  |    |  B  |  P  |  | 
| 167 |    |    |  Total number of dependency distances per sentence  |    |  1  |    |  B  |  S/P  |  | 
| 168 |    |    |  Average number of dependency distances per sentence  |    |  1  |    |  B  |  S/P  |  | 
| 169 |  Cohension  |  Entity Density  |  total number of named Entities Mentions counts  |    |  1  |  1  |  A/B  |  S/P  |  | 
| 170 |    |    |  average number of named Entities Mentions counts per sentence  |    |  1  |  1  |  A/B  |  S/P  |  | 
| 171 |    |    |  average number of named Entities Mentions counts per token (word)  |    |    |  1  |  A/B  |  S/P  |  | 
| 172 |    |    |  total number of unique named Entities  |    |  1  |  1  |  A/B  |  S/P  |  | 
| 173 |    |    |  average number of unique named Entities per sentence  |    |  1  |  1  |  A/B  |  S/P  |  | 
| 174 |    |    |  average number of unique namend Entities per token (word)  |    |    |  1  |  A/B  |  S/P  |  | 
| 175 |    |    |  Percentage of Not-NE nouns per sentence  |    |  1  |    |  A/B  |  S/P  |  | 
| 176 |    |    |  Number of Not-NE nouns per sentence  |    |  1  |    |  A/B  |  S/P  |  | 
| 177 |    |    |  ratio of ss transitions to total  |    |    |  1  |  A  |  P  |  | 
| 178 |    |    |  ratio of so transitions to total  |    |    |  1  |  A  |  P  |  | 
| 179 |    |    |  ratio of sx transitions to total  |    |    |  1  |  A  |  P  |  | 
| 180 |    |    |  ratio of sn transitions to total  |    |    |  1  |  A  |  P  |  | 
| 181 |    |    |  ratio of os transitions to total  |    |    |  1  |  A  |  P  |  | 
| 182 |    |    |  ratio of oo transitions to total  |    |    |  1  |  A  |  P  |  | 
| 183 |    |    |  ratio of ox transitions to total  |    |    |  1  |  A  |  P  |  | 
| 184 |    |    |  ratio of on transitions to total  |    |    |  1  |  A  |  P  |  | 
| 185 |    |    |  ratio of xs transitions to total  |    |    |  1  |  A  |  P  |  | 
| 186 |    |    |  ratio of xo transitions to total  |    |    |  1  |  A  |  P  |  | 
| 187 |    |    |  ratio of xx transitions to total  |    |    |  1  |  A  |  P  |  | 
| 188 |    |    |  ratio of xn transitions to total  |    |    |  1  |  A  |  P  |  | 
| 189 |    |    |  ratio of ns transitions to total  |    |    |  1  |  A  |  P  |  | 
| 190 |    |    |  ratio of no transitions to total  |    |    |  1  |  A  |  P  |  | 
| 191 |    |    |  ratio of nx transitions to total  |    |    |  1  |  A  |  P  |  | 
| 192 |    |    |  ratio of nn transitions to total  |    |    |  1  |  A  |  P  |  | 
| 193 |    |    |  Local Coherence for PA score  |    |    |  1  |  A  |  P  |  | 
| 194 |    |    |  Local Coherence for PW score  |    |    |  1  |  A  |  P  |  | 
| 195 |    |    |  Local Coherence distance for PU score  |    |    |  1  |  A  |  P  |  | 
| 196 |    |  Discourse  |  Percentage of conjunctions per sentence  |    |  1  |    |  A/B  |  S/P  |  | 
| 197 |    |    |  Number of unique conjunctions per sentence  |  1  |  1  |    |  A/B  |  S/P  |  | 
| 198 |    |    |  Percentage of unique conjunctions per sentence  |    |  1  |    |  A/B  |  S/P  |  | 
| 199 |    |    |  Percentage of pronouns per sentence  |    |  1  |    |  A/B  |  S/P  |  | 
| 200 |    |    |  Number of unique pronouns per sentence  |  1  |  1  |    |  A/B  |  S/P  |  | 
| 201 |    |    |  Percentage of unique pronouns per sentence  |  1  |    |    |  A/B  |  S/P  |  | 
| 202 |    |    |  Total number of personal pronouns  |  1  |    |    |  A/B  |  S/P  |  | 
| 203 |    |    |  Total number of first person pronouns  |  1  |    |    |  A/B  |  S/P  |  | 
| 204 |    |    |  Total number of third person pronouns  |  1  |    |    |  A/B  |  S/P  |  | 
| 205 |    |  Variation  |  unique Nouns/total Nouns (Noun Variation-1)  |    |    |  1  |  A  |  S/P  |  | 
| 206 |    |    |  (unique Nouns**2)/total Nouns (Squared Noun Variation-1)  |    |    |  1  |  A  |  S/P  |  | 
| 207 |    |    |  unique Nouns/sqrt(2*total Nouns) (Corrected Noun Variation-1)  |    |    |  1  |  A  |  S/P  |  | 
| 208 |    |    |  unique Verbs/total Verbs (Verb Variation-1)  |    |    |  1  |  A  |  S/P  |  | 
| 209 |    |    |  (unique Verbs**2)/total Verbs (Squared Verb Variation-1)  |    |    |  1  |  A  |  S/P  |  | 
| 210 |    |    |  unique Verbs/sqrt(2*total Verbs) (Corrected Verb Variation-1)  |    |    |  1  |  A  |  S/P  |  | 
| 211 |    |    |  unique Adjectives/total Adjectives (Adjective Variation-1)  |    |    |  1  |  A  |  S/P  |  | 
| 212 |    |    |  (unique Adjectives**2)/total Adjectives (Squared Adjective Variation-1)  |    |    |  1  |  A  |  S/P  |  | 
| 213 |    |    |  unique Adjectives/sqrt(2*total Adjectives) (Corrected Adjective Variation-1)  |    |    |  1  |  A  |  S/P  |  | 
| 214 |    |    |  unique Adverbs/total Adverbs (AdVerb Variation-1)  |    |    |  1  |  A  |  S/P  |  | 
| 215 |    |    |  (unique Adverbs**2)/total Adverbs (Squared AdVerb Variation-1)  |    |    |  1  |  A  |  S/P  |  | 
| 216 |    |    |  unique Adverbs/sqrt(2*total Adverbs) (Corrected AdVerb Variation-1)  |    |    |  1  |  A  |  S/P  |  | 
| 217 |    |  TTR  |  unique tokens/total tokens (TTR)  |    |    |  1  |  A/B  |  S/P  |  | 
| 218 |    |    |  unique tokens/sqrt(2*total tokens) (Corrected TTR)  |    |    |  1  |  A/B  |  S/P  |  | 
| 219 |    |    |  log(unique tokens)/log(total tokens) (Bi-Logarithmic TTR)  |    |    |  1  |  A/B  |  S/P  |  | 
| 220 |    |    |  (log(unique tokens))^2/log(total tokens/unique tokens) (Uber Index)  |    |    |  1  |  A/B  |  S/P  |  | 
| 221 |    |    |  Measure of Textual Lexical Diversity (default TTR = 0.72)  |    |    |  1  |  A/B  |  S/P  |  | 
