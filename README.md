# ChiLingFeat

ChiLingFeat is a Python research project for various Chinese handcrafted linguistic features. 

| Index | Category | Sub-category | Description | Sung. | Lu. | Lee. | State | Fun | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Shallow features | Character | Percentage of most-common characters per sentence |  | 1 |  |  | S | 
| 2 |  |  | Percentage of second-most-common characters per sentence |  | 1 |  |  | S | 
| 3 |  |  | Percentage of all common-characters per sentence |  | 1 |  |  | S | 
| 4 |  |  | Percentage of low-stroke-count characters per sentence |  | 1 |  |  | S | 
| 5 |  |  | Percentage of medium-stroke-count characters per sentence |  | 1 |  |  | S | 
| 6 |  |  | Percentage of high-stroke-count characters per sentence |  | 1 |  |  | S | 
| 7 |  |  | Average number of strokes per word per sentence |  | 1 |  |  | S | 
| 8 |  |  | Percentage of HSK1 to HSK3-characters per sentence |  | 1 |  |  | S | 
| 9 |  |  | Percentage of HSK4 to HSK5-characters per sentence |  | 1 |  |  | S | 
| 10 |  |  | Percentage of HSK6-characters per sentence |  | 1 |  |  | S | 
| 11 |  |  | Percentage of not-HSK-characters per sentence |  | 1 |  |  | S | 
| 12 |  |  | Total number of characters containing 1 to 10 strokes | 1 |  |  | A | S | 
| 13 |  |  | Total number of characters containing 11 to 20 strokes | 1 |  |  | A | S/P | 
| 14 |  |  | Total number of two-character words | 1 |  |  | A | S/P | 
| 15 |  |  | Total number of three-character words | 1 |  |  | A | S/P | 
| 16 |  |  | average count of characters per sentence |  |  | 1 | A | S | 
| 17 |  |  | average count of characters per token |  |  | 1 | A | S | 
| 18 |  | Word | Average number of characters per word per sentence |  | 1 | 1 | A | S | 
| 19 |  |  | Average number of characters per unique word per sentence |  | 1 |  |  | S | 
| 20 |  |  | Number of two-character words per sentence |  | 1 |  |  | S | 
| 21 |  |  | Percentage of two-character words per sentence |  | 1 |  |  | S | 
| 22 |  |  | Number of three-character words per sentence |  | 1 |  |  | S | 
| 23 |  |  | Percentage of three-character words per sentence |  | 1 |  |  | S | 
| 24 |  |  | Number of four-character words per sentence |  | 1 |  |  | S | 
| 25 |  |  | Percentage of four-character words per sentence |  | 1 |  |  | S | 
| 26 |  |  | Number of five-up-character words per sentence |  | 1 |  |  | S | 
| 27 |  |  | Percentage of five-up-character words per sentence |  | 1 |  |  | S | 
| 28 |  |  | Percentage of HSK1 to HSK3-words per sentence |  | 1 |  |  | S | 
| 29 |  |  | Percentage of HSK4 to HSK5-words per sentence |  | 1 |  |  | S | 
| 30 |  |  | Percentage of HSK6-words per sentence |  | 1 |  |  | S | 
| 31 |  |  | Percentage of Not-HSK-words per sentence |  | 1 |  |  | S | 
| 32 |  |  | total count of tokens x total count of sentence | 
| 1 | A | S/P | 
| 33 |  |  | sqrt(total count of tokens x total count of sentence) |  |  | 1 | A | S/P | 
| 34 |  |  | log(total count of tokens)/log(total count of sentence) |  |  | 1 | A | S/P | 
| 35 |  |  | average count of tokens per sentence | 1 |  | 1 | A | S | 
| 36 |  |  | average count of syllables per sentence |  |  | 1 | N | *N | 
| 37 |  |  | average count of syllables per token |  |  | 1 | N | *N | 
| 38 |  | Sentence | Number of multi-character words per sentence |  | 1 |  |  | S | 
| 39 |  |  | Number of words per sentence |  | 1 |  |  | S | 
| 40 |  |  | Number of characters per sentence |  | 1 |  |  | S | 
| 41 |  |  | Number of characters (including punctuations, numerical, and symbols) per sentence |  | 1 |  |  | S | 
| 42 |  |  | Total word difficulty, as according to 8,000 Chinese Words, divided by the total number of words | 1 |  |  |  | S/P | 
| 43 |  |  | Sum of the squares of word difficulty, as defined by 8,000 Chinese Words, divided by the total number of words | 1 |  |  |  | S/P | 
| 44 |  |  | Sum of words belonging to the vantage and effective operational proficiency levels of 8,000 Chinese Words | 1 |  |  |  | S/P | 
| 45 |  |  | Total number of words listed in Academia Sinica database of 3000 difficult words | 1 |  |  |  | *N | 
| 46 |  | Formula | SmogInd_S |  |  | 1 | A | P | 
| 47 |  |  | ColeLia_S |  |  | 1 | A | P | 
| 48 |  |  | Gunning_S |  |  | 1 | A | P | 
| 49 |  |  | AutoRea_S |  |  | 1 | A | P | 
| 50 |  |  | FleschG_S |  |  | 1 | A | P | 
| 51 |  |  | LinseaW_S |  |  | 1 | A | P | 
| 52 | Syntactic features | POS | total count of Noun POS tags |  | 1 | 1 | A | S/P | 
| 53 |  |  | average count of Noun POS tags per sentence |  | 1 | 1 | A | S | 
| 54 |  |  | average count of Noun POS tags per token |  |  | 1 | A | S/P | 
| 55 |  |  | ratio of Noun POS count to Adjective POS count |  |  | 1 | A | S/P | 
| 56 |  |  | ratio of Noun POS count to Verb POS count |  |  | 1 | A | S/P | 
| 57 |  |  | ratio of Noun POS count to Adverb POS count |  |  | 1 | A | S/P | 
| 58 |  |  | ratio of Noun POS count to Subordinating Conjunction count |  |  | 1 | A | S/P | 
| 59 |  |  | ratio of Noun POS count to Coordinating Conjunction count |  |  | 1 | A | S/P | 
| 60 |  |  | total count of Verb POS tags |  | 1 | 1 | A | S/P | 
| 61 |  |  | average count of Verb POS tags per sentence |  | 1 | 1 | A | S | 
| 62 |  |  | average count of Verb POS tags per token |  |  | 1 | A | S/P | 
| 63 |  |  | ratio of Verb POS count to Adjective POS count |  |  | 1 | A | S/P | 
| 64 |  |  | ratio of Verb POS count to Noun POS count |  |  | 1 | A | S/P | 
| 65 |  |  | ratio of Verb POS count to Adverb POS count |  |  | 1 | A | S/P | 
| 66 |  |  | ratio of Verb POS count to Subordinating Conjunction count |  |  | 1 | A | S/P | 
| 67 |  |  | ratio of Verb POS count to Coordinating Conjunction count |  |  | 1 | A | S/P | 
| 68 |  |  | total count of Adjective POS tags |  | 1 | 1 | A | S/P | 
| 69 |  |  | average count of Adjective POS tags per sentence |  | 1 | 1 | A | S | 
| 70 |  |  | average count of Adjective POS tags per token |  |  | 1 | A | S/P | 
| 71 |  |  | ratio of Adjective POS count to Noun POS count |  |  | 1 | A | S/P | 
| 72 |  |  | ratio of Adjective POS count to Verb POS count |  |  | 1 | A | S/P | 
| 73 |  |  | ratio of Adjective POS count to Adverb POS count |  |  | 1 | A | S/P | 
| 74 |  |  | ratio of Adjective POS count to Subordinating Conjunction count |  |  | 1 | A | S/P | 
| 75 |  |  | ratio of Adjective POS count to Coordinating Conjunction count |  |  | 1 | A | S/P | 
| 76 |  |  | total count of Adverb POS tags |  | 1 | 1 | A | S/P | 
| 77 |  |  | average count of Adverb POS tags per sentence |  | 1 | 1 | A | S | 
| 78 |  |  | average count of Adverb POS tags per token |  |  | 1 | A | S/P | 
| 79 |  |  | ratio of Adverb POS count to Adjective POS count |  |  | 1 | A | S/P | 
| 80 |  |  | ratio of Adverb POS count to Noun POS count |  |  | 1 | A | S/P | 
| 81 |  |  | ratio of Adverb POS count to Verb POS count |  |  | 1 | A | S/P | 
| 82 |  |  | ratio of Adverb POS count to Subordinating Conjunction count |  |  | 1 | A | S/P | 
| 83 |  |  | ratio of Adverb POS count to Coordinating Conjunction count |  |  | 1 | A | S/P | 
| 84 |  |  | total count of Subordinating Conjunction POS tags | 1 | 1 | 1 | A | S/P | 
| 85 |  |  | average count of Subordinating Conjunction POS tags per sentence |  | 1 | 1 | A | S | 
| 86 |  |  | average count of Subordinating Conjunction POS tags per token |  |  | 1 | A | S/P | 
| 87 |  |  | ratio of Subordinating Conjunction POS count to Adjective POS count |  |  | 1 | A | S/P | 
| 88 |  |  | ratio of Subordinating Conjunction POS count to Noun POS count |  |  | 1 | A | S/P | 
| 89 |  |  | ratio of Subordinating Conjunction POS count to Verb POS count |  |  | 1 | A | S/P | 
| 90 |  |  | ratio of Subordinating Conjunction POS count to Adverb POS count |  |  | 1 | A | S/P | 
| 91 |  |  | ratio of Subordinating Conjunction POS count to Coordinating Conjunction count |  |  | 1 | A | S/P | 
| 92 |  |  | total count of Coordinating Conjunction POS tags | 1 | 1 | 1 | A | S/P | 
| 93 |  |  | average count of Coordinating Conjunction POS tags per sentence |  | 1 | 1 | A | S | 
| 94 |  |  | average count of Coordinating Conjunction POS tags per token |  |  | 1 | A | S/P | 
| 95 |  |  | ratio of Coordinating Conjunction POS count to Adjective POS count |  |  | 1 | A | S/P | 
| 96 |  |  | ratio of Coordinating Conjunction POS count to Noun POS count |  |  | 1 | A | S/P | 
| 97 |  |  | ratio of Coordinating Conjunction POS count to Verb POS count |  |  | 1 | A | S/P | 
| 98 |  |  | ratio of Coordinating Conjunction POS count to Adverb POS count |  |  | 1 | A | S/P | 
| 99 |  |  | ratio of Coordinating Conjunction POS count to Subordinating Conjunction count |  |  | 1 | A | S/P | 
| 100 |  |  | total count of Content words | 1 | 1 | 1 | A | S/P | 
| 101 |  |  | average count of Content words per sentence |  | 1 | 1 |  | S | 
| 102 |  |  | average count of Content words per token |  |  | 1 |  | S/P | 
| 103 |  |  | total count of Function words |  | 1 | 1 |  | S/P | 
| 104 |  |  | average count of Function words per sentence |  | 1 | 1 |  | S | 
| 105 |  |  | average count of Function words per token |  |  | 1 |  | S/P | 
| 106 |  |  | ratio of Content words to Function words |  |  | 1 |  | S/P | 
| 107 |  |  | Logarithm of the average frequency of content words, according to Education Ministry word frequency list | 1 |  |  |  | *N | 
| 108 |  |  | Percentage of unique adjectives per sentence |  | 1 |  |  | S | 
| 109 |  |  | Number of unique adjectives per sentence |  | 1 |  |  | S | 
| 110 |  |  | Percentage of unique functional words per sentence |  | 1 |  |  | S | 
| 111 |  |  | Number of unique functional words per sentence |  | 1 |  |  | S | 
| 112 |  |  | Number of unique verbs per sentence |  | 1 |  |  | S | 
| 113 |  |  | Percentage of unique verbs per sentence |  | 1 |  |  | S | 
| 114 |  |  | Number of unique nouns per sentence |  | 1 |  |  | S | 
| 115 |  |  | Percentage of unique nouns per sentence |  | 1 |  |  | S | 
| 116 |  |  | Number of unique All-Nouns per sentence |  | 1 |  |  | S | 
| 117 |  |  | Percentage of unique All-Nouns per sentence |  | 1 |  |  | S | 
| 118 |  |  | Number of unique content words per sentence |  | 1 |  | A | S | 
| 119 |  |  | Percentage of unique content words per sentence |  | 1 |  | A | S | 
| 120 |  |  | Number of unique idioms per sentence |  | 1 |  | A | S | 
| 121 |  |  | Percentage of unique idioms per sentence |  | 1 |  | A | S | 
| 122 |  |  | Percentage of unique adverbs per sentence |  | 1 |  | A | S | 
| 123 |  |  | Number of unique adverbs per sentence |  | 1 |  | A | S | 
| 124 |  | Phrases | total count of Noun phrases |  | 1 | 1 | A | S/P | 
| 125 |  |  | average count of Noun phrases per sentence |  |  | 1 | A | S | 
| 126 |  |  | average count of Noun phrases per token |  |  | 1 | A | S/P | 
| 127 |  |  | ratio of Noun phrases count to Verb phrases count |  |  | 1 | A | S/P | 
| 128 |  |  | ratio of Noun phrases count to Subordinate Clauses count |  |  | 1 | A | S/P | 
| 129 |  |  | ratio of Noun phrases count to Prep phrases count |  |  | 1 | A | S/P | 
| 130 |  |  | ratio of Noun phrases count to Adj phrases count |  |  | 1 | A | S/P | 
| 131 |  |  | ratio of Noun phrases count to Adv phrases count |  |  | 1 | A | S/P | 
| 132 |  |  | total count of Verb phrases |  | 1 | 1 | A | S/P | 
| 133 |  |  | average count of Verb phrases per sentence |  |  | 1 | A | S | 
| 134 |  |  | average count of Verb phrases per token |  |  | 1 | A | S/P | 
| 135 |  |  | ratio of Verb phrases count to Noun phrases count |  |  | 1 | A | S/P | 
| 136 |  |  | ratio of Verb phrases count to Subordinate Clauses count |  |  | 1 | A | S/P | 
| 137 |  |  | ratio of Verb phrases count to Prep phrases count |  |  | 1 | A | S/P | 
| 138 |  |  | ratio of Verb phrases count to Adj phrases count |  |  | 1 | A | S/P | 
| 139 |  |  | ratio of Verb phrases count to Adv phrases count |  |  | 1 | A | S/P | 
| 140 |  |  | total count of Subordinate Clauses |  |  | 1 | A | S/P | 
| 141 |  |  | average count of Subordinate Clauses per sentence |  |  | 1 | A | S | 
| 142 |  |  | average count of Subordinate Clauses per token |  |  | 1 | A | S/P | 
| 143 |  |  | ratio of Subordinate Clauses count to Noun phrases count |  |  | 1 | A | S/P | 
| 144 |  |  | ratio of Subordinate Clauses count to Verb phrases count |  |  | 1 | A | S/P | 
| 145 |  |  | ratio of Subordinate Clauses count to Prep phrases count |  |  | 1 | A | S/P | 
| 146 |  |  | ratio of Subordinate Clauses count to Adj phrases count |  |  | 1 | A | S/P | 
| 147 |  |  | ratio of Subordinate Clauses count to Adv phrases count |  |  | 1 | A | S/P | 
| 148 |  |  | total count of prepositional phrases |  | 1 | 1 | A | S/P | 
| 149 |  |  | average count of prepositional phrases per sentence | 1 |  | 1 | A | S | 
| 150 |  |  | average count of prepositional phrases per token |  |  | 1 | A | S/P | 
| 151 |  |  | ratio of Prep phrases count to Noun phrases count |  |  | 1 | A | S/P | 
| 152 |  |  | ratio of Prep phrases count to Verb phrases count |  |  | 1 | A | S/P | 
| 153 |  |  | ratio of Prep phrases count to Subordinate Clauses count |  |  | 1 | A | S/P | 
| 154 |  |  | ratio of Prep phrases count to Adj phrases count |  |  | 1 | A | S/P | 
| 155 |  |  | ratio of Prep phrases count to Adv phrases count |  |  | 1 | A | S/P | 
| 156 |  |  | total count of Adjective phrases |  |  | 1 | A | S/P | 
| 157 |  |  | average count of Adjective phrases per sentence |  |  | 1 | A | S | 
| 158 |  |  | average count of Adjective phrases per token |  |  | 1 | A | S/P | 
| 159 |  |  | ratio of Adj phrases count to Noun phrases count |  |  | 1 | A | S/P | 
| 160 |  |  | ratio of Adj phrases count to Verb phrases count |  |  | 1 | A | S/P | 
| 161 |  |  | ratio of Adj phrases count to Subordinate Clauses count |  |  | 1 | A | S/P | 
| 162 |  |  | ratio of Adj phrases count to Prep phrases count |  |  | 1 | A | S/P | 
| 163 |  |  | ratio of Adj phrases count to Adv phrases count |  |  | 1 | A | S/P | 
| 164 |  |  | total count of Adverb phrases |  |  | 1 | A | S/P | 
| 165 |  |  | average count of Adverb phrases per sentence |  |  | 1 | A | S | 
| 166 |  |  | average count of Adverb phrases per token |  |  | 1 |  | S/P | 
| 167 |  |  | ratio of Adv phrases count to Noun phrases count |  |  | 1 |  | S/P | 
| 168 |  |  | ratio of Adv phrases count to Verb phrases count |  |  | 1 |  | S/P | 
| 169 |  |  | ratio of Adv phrases count to Subordinate Clauses count |  |  | 1 | A | S/P | 
| 170 |  |  | ratio of Adv phrases count to Prep phrases count |  |  | 1 | A | S/P | 
| 171 |  |  | ratio of Adv phrases count to Adj phrases count |  |  | 1 | A | S/P | 
| 172 |  |  | Average length of noun phrases per sentence |  | 1 |  | A | S | 
| 173 |  |  | Average length of verbal phrases per sentence |  | 1 |  | A | S | 
| 174 |  |  | Average length of prepositional phrases per sentence |  | 1 |  | A | S | 
| 175 |  | Clauses | total Tree height of all sentences |  |  | 1 |  | S/P | 
| 176 |  |  | average Tree height per sentence |  | 1 | 1 |  | S/P | 
| 177 |  |  | average Tree height per token (word) |  |  | 1 |  | S/P | 
| 178 |  |  | total length of flattened Trees |  |  | 1 |  | S/P | 
| 179 |  |  | average length of flattened Trees per sentence |  |  | 1 |  | S/P | 
| 180 |  |  | average length of flattened Trees per token (word) |  |  | 1 |  | S/P | 
| 181 |  |  | Number of punctuation-clauses per sentence |  | 1 |  |  | S/P | 
| 182 |  |  | Average dependency distance per sentence |  | 1 |  | A | S/P | 
| 183 |  |  | Maximum dependency distance per sentence |  | 1 |  | A | S/P | 
| 184 |  |  | Total number of dependency distances per sentence |  | 1 |  | A | S/P | 
| 185 |  |  | Average number of dependency distances per sentence |  | 1 |  | A | S/P | 
| 186 |  |  | Total number of complex sentences with complex syntactic structure | 1 |  |  | A | P | 
| 187 |  |  | Proportion of simple sentences | 1 |  |  | A | P | 
| 187 | Cohension | Entity Density | total number of Entities Mentions counts |  | 1 | 1 |  | S/P | 
| 188 |  |  | average number of Entities Mentions counts per sentence |  | 1 | 1 |  | S/P | 
| 189 |  |  | average number of Entities Mentions counts per token (word) |  |  | 1 |  | S/P | 
| 190 |  |  | total number of unique Entities |  | 1 | 1 |  | S/P | 
| 191 |  |  | average number of unique Entities per sentence |  | 1 | 1 |  | S/P | 
| 192 |  |  | average number of unique Entities per token (word) |  |  | 1 | A | S/P | 
| 193 |  |  | Percentage of named entities per sentence |  | 1 |  | A | S/P | 
| 194 |  |  | Percentage of named entities against total number of entities per sentence |  | 1 |  | A | S/P | 
| 195 |  |  | Percentage of Not-NE nouns per sentence |  | 1 |  | A | S/P | 
| 196 |  |  | Number of Not-NE nouns per sentence |  | 1 |  | A | S/P | 
| 197 |  |  | Number of Not-Entity nouns per sentence |  | 1 |  | A | S/P | 
| 198 |  |  | ratio of ss transitions to total |  |  | 1 | A | *N | 
| 199 |  |  | ratio of so transitions to total |  |  | 1 | A | *N | 
| 200 |  |  | ratio of sx transitions to total |  |  | 1 | A | *N | 
| 201 |  |  | ratio of sn transitions to total |  |  | 1 | A | *N | 
| 202 |  |  | ratio of os transitions to total |  |  | 1 | A | *N | 
| 203 |  |  | ratio of oo transitions to total |  |  | 1 | A | *N | 
| 204 |  |  | ratio of ox transitions to total |  |  | 1 | A | *N | 
| 205 |  |  | ratio of on transitions to total |  |  | 1 | A | *N | 
| 206 |  |  | ratio of xs transitions to total |  |  | 1 | A | *N | 
| 207 |  |  | ratio of xo transitions to total |  |  | 1 | A | *N | 
| 208 |  |  | ratio of xx transitions to total |  |  | 1 | A | *N | 
| 209 |  |  | ratio of xn transitions to total |  |  | 1 | A | *N | 
| 210 |  |  | ratio of ns transitions to total |  |  | 1 | A | *N | 
| 211 |  |  | ratio of no transitions to total |  |  | 1 |  | *N | 
| 212 |  |  | ratio of nx transitions to total |  |  | 1 |  | *N | 
| 213 |  |  | ratio of nn transitions to total |  |  | 1 | A | *N | 
| 214 |  |  | Local Coherence for PA score |  |  | 1 | A | *N | 
| 215 |  |  | Local Coherence for PW score |  |  | 1 | A | *N | 
| 216 |  |  | Local Coherence distance for PU score |  |  | 1 | A | *N | 
| 217 |  | Discourse | Percentage of conjunctions per sentence |  | 1 |  | N | S/P | 
| 218 |  |  | Number of unique conjunctions per sentence | 1 | 1 |  | N | S/P | 
| 219 |  |  | Percentage of unique conjunctions per sentence |  | 1 |  | N | S/P | 
| 220 |  |  | Percentage of pronouns per sentence |  | 1 |  | A | S/P | 
| 221 |  |  | Number of unique pronouns per sentence | 1 | 1 |  | A | S/P | 
| 222 |  |  | Percentage of unique pronouns per sentence | 1 |  |  | A | S/P | 
| 223 |  |  | Total number of positive conjunctions | 1 |  |  | A | S/P | 
| 224 |  |  | Total number of negative conjunctions | 1 |  |  | A | S/P | 
| 225 |  |  | Total number of causal conjunctions | 1 |  |  | A | S/P | 
| 226 |  |  | Total number of personal pronouns | 1 |  |  | A | S/P | 
| 227 |  |  | Total number of first person pronouns | 1 |  |  | A | S/P | 
| 228 |  |  | Total number of third person pronouns | 1 |  |  | A | S/P | 
| 229 | Lee’s | Knowledge | 
| （PS: delete temp） | Semantic Richness, 50 topics extracted from Wikipedia |  |  | 1 | A | 
| 230 |  |  | Semantic Clarity, 50 topics extracted from Wikipedia |  |  | 1 | A | 
| 231 |  |  | Semantic Noise, 50 topics extracted from Wikipedia |  |  | 1 | A | 
| 232 |  |  | Number of topics, 50 topics extracted from Wikipedia |  |  | 1 | A | 
| 233 |  |  | Semantic Richness, 100 topics extracted from Wikipedia |  |  | 1 | A | 
| 234 |  |  | Semantic Clarity, 100 topics extracted from Wikipedia |  |  | 1 | A | 
| 235 |  |  | Semantic Noise, 100 topics extracted from Wikipedia |  |  | 1 | A | 
| 236 |  |  | Number of topics, 100 topics extracted from Wikipedia |  |  | 1 | A | 
| 237 |  |  | Semantic Richness, 150 topics extracted from Wikipedia |  |  | 1 | A | 
| 238 |  |  | Semantic Clarity, 150 topics extracted from Wikipedia |  |  | 1 | A | 
| 239 |  |  | Semantic Noise, 150 topics extracted from Wikipedia |  |  | 1 | A | 
| 240 |  |  | Number of topics, 150 topics extracted from Wikipedia |  |  | 1 | 
| 241 |  |  | Semantic Richness, 200 topics extracted from Wikipedia |  |  | 1 | 
| 242 |  |  | Semantic Clarity, 200 topics extracted from Wikipedia |  |  | 1 | 
| 243 |  |  | Semantic Noise, 200 topics extracted from Wikipedia |  |  | 1 | 
| 244 |  |  | Number of topics, 200 topics extracted from Wikipedia |  |  | 1 | 
| 245 |  |  | Semantic Richness, 50 topics extracted from WeeBit Corpus |  |  | 1 | 
| 246 |  |  | Semantic Clarity, 50 topics extracted from WeeBit Corpus |  |  | 1 | 
| 247 |  |  | Semantic Noise, 50 topics extracted from WeeBit Corpus |  |  | 1 | 
| 248 |  |  | Number of topics, 50 topics extracted from WeeBit Corpus |  |  | 1 | 
| 249 |  |  | Semantic Richness, 100 topics extracted from WeeBit Corpus |  |  | 1 | 
| 250 |  |  | Semantic Clarity, 100 topics extracted from WeeBit Corpus |  |  | 1 | 
| 251 |  |  | Semantic Noise, 100 topics extracted from WeeBit Corpus |  |  | 1 | A | 
| 252 |  |  | Number of topics, 100 topics extracted from WeeBit Corpus |  |  | 1 | A | 
| 253 |  |  | Semantic Richness, 150 topics extracted from WeeBit Corpus |  |  | 1 | A | 
| 254 |  |  | Semantic Clarity, 150 topics extracted from WeeBit Corpus |  |  | 1 | A | 
| 255 |  |  | Semantic Noise, 150 topics extracted from WeeBit Corpus |  |  | 1 | A | 
| 256 |  |  | Number of topics, 150 topics extracted from WeeBit Corpus |  |  | 1 | A | 
| 257 |  |  | Semantic Richness, 200 topics extracted from WeeBit Corpus |  |  | 1 | A | 
| 258 |  |  | Semantic Clarity, 200 topics extracted from WeeBit Corpus |  |  | 1 | 
| 259 |  |  | Semantic Noise, 200 topics extracted from WeeBit Corpus |  |  | 1 | 
| 260 |  |  | Number of topics, 200 topics extracted from WeeBit Corpus |  |  | 1 | 
| 261 |  |  | Semantic Richness, 50 topics extracted from OneStopEng Corpus |  |  | 1 | 
| 262 |  |  | Semantic Clarity, 50 topics extracted from OneStopEng Corpus |  |  | 1 | 
| 263 |  |  | Semantic Noise, 50 topics extracted from OneStopEng Corpus |  |  | 1 | 
| 264 |  |  | Number of topics, 50 topics extracted from OneStopEng Corpus |  |  | 1 | 
| 265 |  |  | Semantic Richness, 100 topics extracted from OneStopEng Corpus |  |  | 1 | 
| 266 |  |  | Semantic Clarity, 100 topics extracted from OneStopEng Corpus |  |  | 1 | 
| 267 |  |  | Semantic Noise, 100 topics extracted from OneStopEng Corpus |  |  | 1 | 
| 268 |  |  | Number of topics, 100 topics extracted from OneStopEng Corpus |  |  | 1 | 
| 269 |  |  | Semantic Richness, 150 topics extracted from OneStopEng Corpus |  |  | 1 | 
| 270 |  |  | Semantic Clarity, 150 topics extracted from OneStopEng Corpus |  |  | 1 | 
| 271 |  |  | Semantic Noise, 150 topics extracted from OneStopEng Corpus |  |  | 1 | A | 
| 272 |  |  | Number of topics, 150 topics extracted from OneStopEng Corpus |  |  | 1 | A | 
| 273 |  |  | Semantic Richness, 200 topics extracted from OneStopEng Corpus |  |  | 1 | A | 
| 274 |  |  | Semantic Clarity, 200 topics extracted from OneStopEng Corpus |  |  | 1 | A | 
| 275 |  |  | Semantic Noise, 200 topics extracted from OneStopEng Corpus |  |  | 1 | N | 
| 276 |  |  | Number of topics, 200 topics extracted from OneStopEng Corpus |  |  | 1 | N | 
| 277 |  | Variation | unique Nouns/total Nouns (Noun Variation-1) |  |  | 1 |  | S/P | 
| 278 |  |  | (unique Nouns**2)/total Nouns (Squared Noun Variation-1) |  |  | 1 |  | S/P | 
| 279 |  |  | unique Nouns/sqrt(2*total Nouns) (Corrected Noun Variation-1) |  |  | 1 |  | S/P | 
| 280 |  |  | unique Verbs/total Verbs (Verb Variation-1) |  |  | 1 |  | S/P | 
| 281 |  |  | (unique Verbs**2)/total Verbs (Squared Verb Variation-1) |  |  | 1 |  | S/P | 
| 282 |  |  | unique Verbs/sqrt(2*total Verbs) (Corrected Verb Variation-1) |  |  | 1 |  | S/P | 
| 283 |  |  | unique Adjectives/total Adjectives (Adjective Variation-1) |  |  | 1 |  | S/P | 
| 284 |  |  | (unique Adjectives**2)/total Adjectives (Squared Adjective Variation-1) |  |  | 1 |  | S/P | 
| 285 |  |  | unique Adjectives/sqrt(2*total Adjectives) (Corrected Adjective Variation-1) |  |  | 1 | A | S/P | 
| 286 |  |  | unique Adverbs/total Adverbs (AdVerb Variation-1) |  |  | 1 | A | S/P | 
| 287 |  |  | (unique Adverbs**2)/total Adverbs (Squared AdVerb Variation-1) |  |  | 1 | A | S/P | 
| 288 |  |  | unique Adverbs/sqrt(2*total Adverbs) (Corrected AdVerb Variation-1) |  |  | 1 | A | S/P | 
| 289 |  | TTR | unique tokens/total tokens (TTR) |  |  | 1 | A | S/P | 
| 290 |  |  | unique tokens/sqrt(2*total tokens) (Corrected TTR) |  |  | 1 | A | S/P | 
| 291 |  |  | log(unique tokens)/log(total tokens) (Bi-Logarithmic TTR) |  |  | 1 | A | S/P | 
| 292 |  |  | (log(unique tokens))^2/log(total tokens/unique tokens) (Uber Index) |  |  | 1 | A | S/P | 
| 293 |  |  | Measure of Textual Lexical Diversity (default TTR = 0.72) |  |  | 1 | A | S/P | 
| 294 |  | Psycholinguistic | 
| (PS: delete temp) | total AoA (Age of Acquisition) of words |  |  | 1 | A | 
| 295 |  |  | average AoA of words per sentence |  |  | 1 | A | 
| 296 |  |  | average AoA of words per token |  |  | 1 | A | 
| 297 |  |  | total lemmas AoA of lemmas |  |  | 1 | A | 
| 298 |  |  | average lemmas AoA of lemmas per sentence |  |  | 1 | A | 
| 299 |  |  | average lemmas AoA of lemmas per token |  |  | 1 | A | 
| 300 |  |  | total lemmas AoA of lemmas, Bird norm |  |  | 1 | A | 
| 301 |  |  | average lemmas AoA of lemmas, Bird norm per sentence |  |  | 1 | A | 
| 302 |  |  | average lemmas AoA of lemmas, Bird norm per token |  |  | 1 | A | 
| 303 |  |  | total lemmas AoA of lemmas, Bristol norm |  |  | 1 | A | 
| 304 |  |  | average lemmas AoA of lemmas, Bristol norm per sentence |  |  | 1 | A | 
| 305 |  |  | average lemmas AoA of lemmas, Bristol norm per token |  |  | 1 | A | 
| 306 |  |  | total AoA of lemmas, Cortese and Khanna norm |  |  | 1 | A | 
| 307 |  |  | average AoA of lemmas, Cortese and Khanna norm per sentence |  |  | 1 | A | 
| 308 |  |  | average AoA of lemmas, Cortese and Khanna norm per token |  |  | 1 | A | 
| 309 |  | Word Family | total SubtlexUS FREQcount value |  |  | 1 | A | 
| 310 |  |  | average SubtlexUS FREQcount value per sentenc |  |  | 1 | A | 
| 311 |  |  | average SubtlexUS FREQcount value per token |  |  | 1 | A | 
| 312 |  |  | total SubtlexUS CDcount value |  |  | 1 | A | 
| 313 |  |  | average SubtlexUS CDcount value per sentence |  |  | 1 | A | 
| 314 |  |  | average SubtlexUS CDcount value per token |  |  | 1 | A | 
| 315 |  |  | total SubtlexUS FREQlow value |  |  | 1 | A | 
| 316 |  |  | average SubtlexUS FREQlow value per sentence |  |  | 1 | A | 
| 317 |  |  | average SubtlexUS FREQlow value per token |  |  | 1 | A | 
| 318 |  |  | total SubtlexUS CDlow value |  |  | 1 | A | 
| 319 |  |  | average SubtlexUS CDlow value per sentence |  |  | 1 | A | 
| 320 |  |  | average SubtlexUS CDlow value per token |  |  | 1 | A | 
| 321 |  |  | total SubtlexUS SUBTLWF value |  |  | 1 | A | 
| 322 |  |  | average SubtlexUS SUBTLWF value per sentence |  |  | 1 | A | 
| 323 |  |  | average SubtlexUS SUBTLWF value per token |  |  | 1 | A | 
| 324 |  |  | total SubtlexUS Lg10WF value |  |  | 1 | A | 
| 325 |  |  | average SubtlexUS Lg10WF value per sentence |  |  | 1 | A | 
| 326 |  |  | average SubtlexUS Lg10WF value per token |  |  | 1 | A | 
| 327 |  |  | total SubtlexUS SUBTLCD value |  |  | 1 | A | 
| 328 |  |  | average SubtlexUS SUBTLCD value per sentence |  |  | 1 | A | 
| 329 |  |  | average SubtlexUS SUBTLCD value per token |  |  | 1 | A | 
| 330 |  |  | total SubtlexUS Lg10CD value |  |  | 1 | A | 
| 331 |  |  | average SubtlexUS Lg10CD value per sentence |  |  | 1 | A | 
| 332 |  |  | average SubtlexUS Lg10CD value per token |  |  | 1 | A | 

