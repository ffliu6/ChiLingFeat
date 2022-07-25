# ChiLingFeat

ChiLingFeat is a Python research project for various Chinese handcrafted linguistic features. 

For extracting features, the spacy is firstly utilized to tokenize the input passage/sentence (for sentence, the tokenized list contain one sentence). Then currently, the sentence-level features are parsed by StanfordCoreNLP, the passge-level features are obtained the same way as the LingFeat.

In total, we provided 240 Chinese features, X for sentence-level, and X for passage-level. As shown in the table below, the Fun column represents if the feature is for sentence or passage, in which *S* represents only for *sentence-level*, *P* represents only for *passage-level*, *S/P* represents for both *sentence-level* and *passage-level*. 

| Index | Category | Sub-category | Description | Sung et al. 2015 | Lu et al. 2020 | Lee et al. 2021 | State | Fun | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Shallow features | Character | Percentage of most-common characters per sentence |  | 1 |  | B | S | 
| 2 |  |  | Percentage of second-most-common characters per sentence |  | 1 |  | B | S | 
| 3 |  |  | Percentage of all common-characters per sentence |  | 1 |  | B | S | 
| 4 |  |  | Percentage of low-stroke-count characters per sentence |  | 1 |  | B | S | 
| 5 |  |  | Percentage of medium-stroke-count characters per sentence |  | 1 |  | B | S | 
| 6 |  |  | Percentage of high-stroke-count characters per sentence |  | 1 |  | B | S | 
| 7 |  |  | Average number of strokes per word per sentence |  | 1 |  | B | S | 
| 8 |  |  | Percentage of HSK1 to HSK3-characters per sentence |  | 1 |  | B | S | 
| 9 |  |  | Percentage of HSK4 to HSK5-characters per sentence |  | 1 |  | B | S | 
| 10 |  |  | Percentage of HSK6-characters per sentence |  | 1 |  | B | S | 
| 11 |  |  | Percentage of not-HSK-characters per sentence |  | 1 |  | B | S | 
| 12 |  |  | Total number of characters containing 1 to 10 strokes | 1 |  |  | A/B | S | 
| 13 |  |  | Total number of characters containing 11 to 20 strokes | 1 |  |  | A/B | S/P | 
| 14 |  |  | Total number of two-character words | 1 |  |  | A/B | S/P | 
| 15 |  |  | Total number of three-character words | 1 |  |  | A/B | S/P | 
| 16 |  |  | average count of characters per sentence |  |  | 1 | A/B | S/P | 
| 17 |  |  | average count of characters per token |  |  | 1 | A/B | S/P | 
| 18 |  | Word | Average number of characters per word per sentence |  | 1 | 1 | A/B | S | 
| 19 |  |  | Average number of characters per unique word per sentence |  | 1 |  | B | S | 
| 20 |  |  | Number of two-character words per sentence |  | 1 |  | B | S | 
| 21 |  |  | Percentage of two-character words per sentence |  | 1 |  | B | S | 
| 22 |  |  | Number of three-character words per sentence |  | 1 |  | B | S | 
| 23 |  |  | Percentage of three-character words per sentence |  | 1 |  | B | S | 
| 24 |  |  | Number of four-character words per sentence |  | 1 |  | B | S | 
| 25 |  |  | Percentage of four-character words per sentence |  | 1 |  | B | S | 
| 26 |  |  | Number of five-up-character words per sentence |  | 1 |  | B | S | 
| 27 |  |  | Percentage of five-up-character words per sentence |  | 1 |  | B | S | 
| 28 |  |  | Percentage of HSK1 to HSK3-words per sentence |  | 1 |  | B | S | 
| 29 |  |  | Percentage of HSK4 to HSK5-words per sentence |  | 1 |  | B | S | 
| 30 |  |  | Percentage of HSK6-words per sentence |  | 1 |  | B | S | 
| 31 |  |  | Percentage of Not-HSK-words per sentence |  | 1 |  | B | S | 
| 32 |  |  | total count of tokens x total count of sentence |  | 1 | A/B | S/P | 
| 33 |  |  | sqrt(total count of tokens x total count of sentence) |  |  | 1 | A/B | S/P | 
| 34 |  |  | log(total count of tokens)/log(total count of sentence) |  |  | 1 | A/B | S/P | 
| 35 |  |  | average count of tokens per sentence | 1 |  | 1 | A/B | S/P | 
| 36 |  |  | average count of syllables per sentence |  |  | 1 | N | *N | 
| 37 |  |  | average count of syllables per token |  |  | 1 | N | *N | 
| 38 |  | Sentence | Number of multi-character words per sentence |  | 1 |  | B | S | 
| 39 |  |  | Number of words per sentence |  | 1 |  | B | S | 
| 40 |  |  | Number of characters per sentence |  | 1 |  | B | S | 
| 41 |  |  | Number of characters (including punctuations, numerical, and symbols) per sentence |  | 1 |  | B | S | 
| 42 |  |  | Total word difficulty, as according to 8,000 Chinese Words, divided by the total number of words | 1 |  |  |  | *N | 
| 43 |  |  | Sum of the squares of word difficulty, as defined by 8,000 Chinese Words, divided by the total number of words | 1 |  |  |  | *N | 
| 44 |  |  | Sum of words belonging to the vantage and effective operational proficiency levels of 8,000 Chinese Words | 1 |  |  |  | *N | 
| 45 |  |  | Total number of words listed in Academia Sinica database of 3000 difficult words | 1 |  |  |  | *N | 
| 46 | Syntactic features | POS | total count of Noun POS tags |  | 1 | 1 | A/B | S/P | 
| 47 |  |  | average count of Noun POS tags per sentence |  | 1 | 1 | A/B | S/P | 
| 48 |  |  | average count of Noun POS tags per token |  |  | 1 | A/B | S/P | 
| 49 |  |  | ratio of Noun POS count to Adjective POS count |  |  | 1 | A/B | S/P | 
| 50 |  |  | ratio of Noun POS count to Verb POS count |  |  | 1 | A/B | S/P | 
| 51 |  |  | ratio of Noun POS count to Adverb POS count |  |  | 1 | A/B | S/P | 
| 52 |  |  | ratio of Noun POS count to Subordinating Conjunction count |  |  | 1 | A/B | S/P | 
| 53 |  |  | ratio of Noun POS count to Coordinating Conjunction count |  |  | 1 | A/B | S/P | 
| 54 |  |  | total count of Verb POS tags |  | 1 | 1 | A/B | S/P | 
| 55 |  |  | average count of Verb POS tags per sentence |  | 1 | 1 | A/B | S/P | 
| 56 |  |  | average count of Verb POS tags per token |  |  | 1 | A/B | S/P | 
| 57 |  |  | ratio of Verb POS count to Adjective POS count |  |  | 1 | A/B | S/P | 
| 58 |  |  | ratio of Verb POS count to Noun POS count |  |  | 1 | A/B | S/P | 
| 59 |  |  | ratio of Verb POS count to Adverb POS count |  |  | 1 | A/B | S/P | 
| 60 |  |  | ratio of Verb POS count to Subordinating Conjunction count |  |  | 1 | A/B | S/P | 
| 61 |  |  | ratio of Verb POS count to Coordinating Conjunction count |  |  | 1 | A/B | S/P | 
| 62 |  |  | total count of Adjective POS tags |  | 1 | 1 | A/B | S/P | 
| 63 |  |  | average count of Adjective POS tags per sentence |  | 1 | 1 | A/B | S/P | 
| 64 |  |  | average count of Adjective POS tags per token |  |  | 1 | A/B | S/P | 
| 65 |  |  | ratio of Adjective POS count to Noun POS count |  |  | 1 | A/B | S/P | 
| 66 |  |  | ratio of Adjective POS count to Verb POS count |  |  | 1 | A/B | S/P | 
| 67 |  |  | ratio of Adjective POS count to Adverb POS count |  |  | 1 | A/B | S/P | 
| 68 |  |  | ratio of Adjective POS count to Subordinating Conjunction count |  |  | 1 | A/B | S/P | 
| 69 |  |  | ratio of Adjective POS count to Coordinating Conjunction count |  |  | 1 | A/B | S/P | 
| 70 |  |  | total count of Adverb POS tags |  | 1 | 1 | A/B | S/P | 
| 71 |  |  | average count of Adverb POS tags per sentence |  | 1 | 1 | A/B | S/P | 
| 72 |  |  | average count of Adverb POS tags per token |  |  | 1 | A/B | S/P | 
| 73 |  |  | ratio of Adverb POS count to Adjective POS count |  |  | 1 | A/B | S/P | 
| 74 |  |  | ratio of Adverb POS count to Noun POS count |  |  | 1 | A/B | S/P | 
| 75 |  |  | ratio of Adverb POS count to Verb POS count |  |  | 1 | A/B | S/P | 
| 76 |  |  | ratio of Adverb POS count to Subordinating Conjunction count |  |  | 1 | A/B | S/P | 
| 77 |  |  | ratio of Adverb POS count to Coordinating Conjunction count |  |  | 1 | A/B | S/P | 
| 78 |  |  | total count of Subordinating Conjunction POS tags | 1 | 1 | 1 | A/B | S/P | 
| 79 |  |  | average count of Subordinating Conjunction POS tags per sentence |  | 1 | 1 | A/B | S/P | 
| 80 |  |  | average count of Subordinating Conjunction POS tags per token |  |  | 1 | A/B | S/P | 
| 81 |  |  | ratio of Subordinating Conjunction POS count to Adjective POS count |  |  | 1 | A/B | S/P | 
| 82 |  |  | ratio of Subordinating Conjunction POS count to Noun POS count |  |  | 1 | A/B | S/P | 
| 83 |  |  | ratio of Subordinating Conjunction POS count to Verb POS count |  |  | 1 | A/B | S/P | 
| 84 |  |  | ratio of Subordinating Conjunction POS count to Adverb POS count |  |  | 1 | A/B | S/P | 
| 85 |  |  | ratio of Subordinating Conjunction POS count to Coordinating Conjunction count |  |  | 1 | A/B | S/P | 
| 86 |  |  | total count of Coordinating Conjunction POS tags | 1 | 1 | 1 | A/B | S/P | 
| 87 |  |  | average count of Coordinating Conjunction POS tags per sentence |  | 1 | 1 | A/B | S/P | 
| 88 |  |  | average count of Coordinating Conjunction POS tags per token |  |  | 1 | A/B | S/P | 
| 89 |  |  | ratio of Coordinating Conjunction POS count to Adjective POS count |  |  | 1 | A/B | S/P | 
| 90 |  |  | ratio of Coordinating Conjunction POS count to Noun POS count |  |  | 1 | A/B | S/P | 
| 91 |  |  | ratio of Coordinating Conjunction POS count to Verb POS count |  |  | 1 | A/B | S/P | 
| 92 |  |  | ratio of Coordinating Conjunction POS count to Adverb POS count |  |  | 1 | A/B | S/P | 
| 93 |  |  | ratio of Coordinating Conjunction POS count to Subordinating Conjunction count |  |  | 1 | A/B | S/P | 
| 94 |  |  | total count of Content words | 1 | 1 | 1 | A/B | S/P | 
| 95 |  |  | average count of Content words per sentence |  | 1 | 1 |  | S/P | 
| 96 |  |  | average count of Content words per token |  |  | 1 |  | S/P | 
| 97 |  |  | total count of Function words |  | 1 | 1 |  | S/P | 
| 98 |  |  | average count of Function words per sentence |  | 1 | 1 |  | S/P | 
| 99 |  |  | average count of Function words per token |  |  | 1 |  | S/P | 
| 100 |  |  | ratio of Content words to Function words |  |  | 1 |  | S/P | 
| 101 |  |  | Logarithm of the average frequency of content words, according to Education Ministry word frequency list | 1 |  |  |  | *N | 
| 102 |  |  | Percentage of unique adjectives per sentence |  | 1 |  | B | S | 
| 103 |  |  | Number of unique adjectives per sentence |  | 1 |  | B | S | 
| 104 |  |  | Percentage of unique functional words per sentence |  | 1 |  | B | S | 
| 105 |  |  | Number of unique functional words per sentence |  | 1 |  | B | S | 
| 106 |  |  | Number of unique verbs per sentence |  | 1 |  | B | S | 
| 107 |  |  | Percentage of unique verbs per sentence |  | 1 |  | B | S | 
| 108 |  |  | Number of unique nouns per sentence |  | 1 |  | B | S | 
| 109 |  |  | Percentage of unique nouns per sentence |  | 1 |  | B | S | 
| 110 |  |  | Number of unique All-Nouns per sentence |  | 1 |  | B | S | 
| 111 |  |  | Percentage of unique All-Nouns per sentence |  | 1 |  | B | S | 
| 112 |  |  | Number of unique content words per sentence |  | 1 |  | A | S/P | 
| 113 |  |  | Percentage of unique content words per sentence |  | 1 |  | A | S/P | 
| 114 |  |  | Number of unique idioms per sentence |  | 1 |  | A | S/P | 
| 115 |  |  | Percentage of unique idioms per sentence |  | 1 |  | A | S/P | 
| 116 |  |  | Percentage of unique adverbs per sentence |  | 1 |  | A | S/P | 
| 117 |  |  | Number of unique adverbs per sentence |  | 1 |  | A | S/P | 
| 118 |  | Phrases | total count of Noun phrases |  | 1 | 1 | A | S/P | 
| 119 |  |  | average count of Noun phrases per sentence |  |  | 1 | A | S/P | 
| 120 |  |  | average count of Noun phrases per token |  |  | 1 | A | S/P | 
| 121 |  |  | ratio of Noun phrases count to Verb phrases count |  |  | 1 | A | S/P | 
| 122 |  |  | ratio of Noun phrases count to Subordinate Clauses count |  |  | 1 | A | S/P | 
| 123 |  |  | ratio of Noun phrases count to Prep phrases count |  |  | 1 | A | S/P | 
| 124 |  |  | ratio of Noun phrases count to Adj phrases count |  |  | 1 | A | S/P | 
| 125 |  |  | ratio of Noun phrases count to Adv phrases count |  |  | 1 | A | S/P | 
| 126 |  |  | total count of Verb phrases |  | 1 | 1 | A | S/P | 
| 127 |  |  | average count of Verb phrases per sentence |  |  | 1 | A | S/P | 
| 128 |  |  | average count of Verb phrases per token |  |  | 1 | A | S/P | 
| 129 |  |  | ratio of Verb phrases count to Noun phrases count |  |  | 1 | A | S/P | 
| 130 |  |  | ratio of Verb phrases count to Subordinate Clauses count |  |  | 1 | A | S/P | 
| 131 |  |  | ratio of Verb phrases count to Prep phrases count |  |  | 1 | A | S/P | 
| 132 |  |  | ratio of Verb phrases count to Adj phrases count |  |  | 1 | A | S/P | 
| 133 |  |  | ratio of Verb phrases count to Adv phrases count |  |  | 1 | A | S/P | 
| 134 |  |  | total count of Subordinate Clauses |  |  | 1 | A | S/P | 
| 135 |  |  | average count of Subordinate Clauses per sentence |  |  | 1 | A | S/P | 
| 136 |  |  | average count of Subordinate Clauses per token |  |  | 1 | A | S/P | 
| 137 |  |  | ratio of Subordinate Clauses count to Noun phrases count |  |  | 1 | A | S/P | 
| 138 |  |  | ratio of Subordinate Clauses count to Verb phrases count |  |  | 1 | A | S/P | 
| 139 |  |  | ratio of Subordinate Clauses count to Prep phrases count |  |  | 1 | A | S/P | 
| 140 |  |  | ratio of Subordinate Clauses count to Adj phrases count |  |  | 1 | A | S/P | 
| 141 |  |  | ratio of Subordinate Clauses count to Adv phrases count |  |  | 1 | A | S/P | 
| 142 |  |  | total count of prepositional phrases |  | 1 | 1 | A | S/P | 
| 143 |  |  | average count of prepositional phrases per sentence | 1 |  | 1 | A | S/P | 
| 144 |  |  | average count of prepositional phrases per token |  |  | 1 | A | S/P | 
| 145 |  |  | ratio of Prep phrases count to Noun phrases count |  |  | 1 | A | S/P | 
| 146 |  |  | ratio of Prep phrases count to Verb phrases count |  |  | 1 | A | S/P | 
| 147 |  |  | ratio of Prep phrases count to Subordinate Clauses count |  |  | 1 | A | S/P | 
| 148 |  |  | ratio of Prep phrases count to Adj phrases count |  |  | 1 | A | S/P | 
| 149 |  |  | ratio of Prep phrases count to Adv phrases count |  |  | 1 | A | S/P | 
| 150 |  |  | total count of Adjective phrases |  |  | 1 | A | S/P | 
| 151 |  |  | average count of Adjective phrases per sentence |  |  | 1 | A | S/P | 
| 152 |  |  | average count of Adjective phrases per token |  |  | 1 | A | S/P | 
| 153 |  |  | ratio of Adj phrases count to Noun phrases count |  |  | 1 | A | S/P | 
| 154 |  |  | ratio of Adj phrases count to Verb phrases count |  |  | 1 | A | S/P | 
| 155 |  |  | ratio of Adj phrases count to Subordinate Clauses count |  |  | 1 | A | S/P | 
| 156 |  |  | ratio of Adj phrases count to Prep phrases count |  |  | 1 | A | S/P | 
| 157 |  |  | ratio of Adj phrases count to Adv phrases count |  |  | 1 | A | S/P | 
| 158 |  |  | total count of Adverb phrases |  |  | 1 | A | S/P | 
| 159 |  |  | average count of Adverb phrases per sentence |  |  | 1 | A | S/P | 
| 160 |  |  | average count of Adverb phrases per token |  |  | 1 |  | S/P | 
| 161 |  |  | ratio of Adv phrases count to Noun phrases count |  |  | 1 |  | S/P | 
| 162 |  |  | ratio of Adv phrases count to Verb phrases count |  |  | 1 |  | S/P | 
| 163 |  |  | ratio of Adv phrases count to Subordinate Clauses count |  |  | 1 | A | S/P | 
| 164 |  |  | ratio of Adv phrases count to Prep phrases count |  |  | 1 | A | S/P | 
| 165 |  |  | ratio of Adv phrases count to Adj phrases count |  |  | 1 | A | S/P | 
| 166 |  |  | Average length of noun phrases per sentence |  | 1 |  | A | S/P | 
| 167 |  |  | Average length of verbal phrases per sentence |  | 1 |  | A | S/P | 
| 168 |  |  | Average length of prepositional phrases per sentence |  | 1 |  | A | S/P | 
| 169 |  | Clauses | total Tree height of all sentences |  |  | 1 | B | S/P | 
| 170 |  |  | average Tree height per sentence |  | 1 | 1 | B | S/P | 
| 171 |  |  | average Tree height per token (word) |  |  | 1 | B | S/P | 
| 172 |  |  | total length of flattened Trees |  |  | 1 | B | S/P | 
| 173 |  |  | average length of flattened Trees per sentence |  |  | 1 |  | S/P | 
| 174 |  |  | average length of flattened Trees per token (word) |  |  | 1 |  | S/P | 
| 175 |  |  | Number of punctuation-clauses per sentence |  | 1 |  |  | S/P | 
| 176 |  |  | Average dependency distance per sentence |  | 1 |  | A/B | S/P | 
| 177 |  |  | Maximum dependency distance per sentence |  | 1 |  | A/B | S/P | 
| 178 |  |  | Total number of dependency distances per sentence |  | 1 |  | A/B | S/P | 
| 179 |  |  | Average number of dependency distances per sentence |  | 1 |  | A/B | S/P | 
| 180 |  |  | Total number of complex sentences with complex syntactic structure | 1 |  |  | A | P | 
| 181 |  |  | Proportion of simple sentences | 1 |  |  | A | P | 
| 182 | Cohension | Entity Density | total number of Entities Mentions counts |  | 1 | 1 | B | S/P | 
| 183 |  |  | average number of Entities Mentions counts per sentence |  | 1 | 1 | B | S/P | 
| 184 |  |  | average number of Entities Mentions counts per token (word) |  |  | 1 | B | S/P | 
| 185 |  |  | total number of unique Entities |  | 1 | 1 | B | S/P | 
| 186 |  |  | average number of unique Entities per sentence |  | 1 | 1 | B | S/P | 
| 187 |  |  | average number of unique Entities per token (word) |  |  | 1 | A/B | S/P | 
| 188 |  |  | Percentage of named entities per sentence |  | 1 |  | A/B | S/P | 
| 189 |  |  | Percentage of named entities against total number of entities per sentence |  | 1 |  | A/B | S/P | 
| 190 |  |  | Percentage of Not-NE nouns per sentence |  | 1 |  | A/B | S/P | 
| 191 |  |  | Number of Not-NE nouns per sentence |  | 1 |  | A/B | S/P | 
| 192 |  |  | Number of Not-Entity nouns per sentence |  | 1 |  | A/B | S/P | 
| 193 |  |  | ratio of ss transitions to total |  |  | 1 | A | P | 
| 194 |  |  | ratio of so transitions to total |  |  | 1 | A | P | 
| 195 |  |  | ratio of sx transitions to total |  |  | 1 | A | P | 
| 196 |  |  | ratio of sn transitions to total |  |  | 1 | A | P | 
| 197 |  |  | ratio of os transitions to total |  |  | 1 | A | P | 
| 198 |  |  | ratio of oo transitions to total |  |  | 1 | A | P | 
| 199 |  |  | ratio of ox transitions to total |  |  | 1 | A | P | 
| 200 |  |  | ratio of on transitions to total |  |  | 1 | A | P | 
| 201 |  |  | ratio of xs transitions to total |  |  | 1 | A | P | 
| 202 |  |  | ratio of xo transitions to total |  |  | 1 | A | P | 
| 203 |  |  | ratio of xx transitions to total |  |  | 1 | A | P | 
| 204 |  |  | ratio of xn transitions to total |  |  | 1 | A | P | 
| 205 |  |  | ratio of ns transitions to total |  |  | 1 | A | P | 
| 206 |  |  | ratio of no transitions to total |  |  | 1 | A | P | 
| 207 |  |  | ratio of nx transitions to total |  |  | 1 | A | P | 
| 208 |  |  | ratio of nn transitions to total |  |  | 1 | A | P | 
| 209 |  |  | Local Coherence for PA score |  |  | 1 | A | P | 
| 210 |  |  | Local Coherence for PW score |  |  | 1 | A | P | 
| 211 |  |  | Local Coherence distance for PU score |  |  | 1 | A | P | 
| 212 |  | Discourse | Percentage of conjunctions per sentence |  | 1 |  | B | S/P | 
| 213 |  |  | Number of unique conjunctions per sentence | 1 | 1 |  | B | S/P | 
| 214 |  |  | Percentage of unique conjunctions per sentence |  | 1 |  | B | S/P | 
| 215 |  |  | Percentage of pronouns per sentence |  | 1 |  | A/B | S/P | 
| 216 |  |  | Number of unique pronouns per sentence | 1 | 1 |  | A/B | S/P | 
| 217 |  |  | Percentage of unique pronouns per sentence | 1 |  |  | A/B | S/P | 
| 218 |  |  | Total number of positive conjunctions | 1 |  |  | A/B | S/P | 
| 219 |  |  | Total number of negative conjunctions | 1 |  |  | A/B | S/P | 
| 220 |  |  | Total number of causal conjunctions | 1 |  |  | A/B | S/P | 
| 221 |  |  | Total number of personal pronouns | 1 |  |  | A/B | S/P | 
| 222 |  |  | Total number of first person pronouns | 1 |  |  | A/B | S/P | 
| 223 |  |  | Total number of third person pronouns | 1 |  |  | A/B | S/P | 
| 224 |  | Variation | unique Nouns/total Nouns (Noun Variation-1) |  |  | 1 |  | S/P | 
| 225 |  |  | (unique Nouns**2)/total Nouns (Squared Noun Variation-1) |  |  | 1 |  | S/P | 
| 226 |  |  | unique Nouns/sqrt(2*total Nouns) (Corrected Noun Variation-1) |  |  | 1 |  | S/P | 
| 227 |  |  | unique Verbs/total Verbs (Verb Variation-1) |  |  | 1 |  | S/P | 
| 228 |  |  | (unique Verbs**2)/total Verbs (Squared Verb Variation-1) |  |  | 1 |  | S/P | 
| 229 |  |  | unique Verbs/sqrt(2*total Verbs) (Corrected Verb Variation-1) |  |  | 1 |  | S/P | 
| 230 |  |  | unique Adjectives/total Adjectives (Adjective Variation-1) |  |  | 1 |  | S/P | 
| 231 |  |  | (unique Adjectives**2)/total Adjectives (Squared Adjective Variation-1) |  |  | 1 |  | S/P | 
| 232 |  |  | unique Adjectives/sqrt(2*total Adjectives) (Corrected Adjective Variation-1) |  |  | 1 | A | S/P | 
| 233 |  |  | unique Adverbs/total Adverbs (AdVerb Variation-1) |  |  | 1 | A | S/P | 
| 234 |  |  | (unique Adverbs**2)/total Adverbs (Squared AdVerb Variation-1) |  |  | 1 | A | S/P | 
| 235 |  |  | unique Adverbs/sqrt(2*total Adverbs) (Corrected AdVerb Variation-1) |  |  | 1 | A | S/P | 
| 236 |  | TTR | unique tokens/total tokens (TTR) |  |  | 1 | A/B | S/P | 
| 237 |  |  | unique tokens/sqrt(2*total tokens) (Corrected TTR) |  |  | 1 | A/B | S/P | 
| 238 |  |  | log(unique tokens)/log(total tokens) (Bi-Logarithmic TTR) |  |  | 1 | A/B | S/P | 
| 239 |  |  | (log(unique tokens))^2/log(total tokens/unique tokens) (Uber Index) |  |  | 1 | A/B | S/P | 
| 240 |  |  | Measure of Textual Lexical Diversity (default TTR = 0.72) |  |  | 1 | A/B | S/P | 
