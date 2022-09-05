# -*- coding: UTF-8 -*-
"""
Software: LingFeat - Comprehensive Linguistic Features for Readability Assessment
Page: extractor.py
License: CC-BY-SA 4.0

Original Author: Bruce W. Lee (이웅성) @brucewlee
Affiliation 1: LXPER AI, Seoul, South Korea
Affiliation 2: University of Pennsylvania, PA, USA
Contributing Author: -
Affiliation : -
"""

# utilities
import math
import os
import warnings
import logging
import tqdm
def nop(it, *a, **k):
    return it
tqdm.tqdm = nop
from utils import nan_check

# performance-central dependencies
import spacy 
# import supar
from supar import Parser

# discourse features
import _Discourse.EnDF as Disco_EnDF
import _Discourse.EnGF as Disco_EnGF

# syntactic features
import _Syntactic.POSF as Synta_POSF
import _Syntactic.PhrF as Synta_PhrF
import _Syntactic.TrSF as Synta_TrSF

# lexico-Semantic features
import _LexicoSemantic.TTRF as LxSem_TTRF
import _LexicoSemantic.VarF as LxSem_VarF

# shallow features
import _ShallowTraditional.ShaF as ShaTr_ShaF

# ignore warning
warnings.filterwarnings("ignore")

# current path
dir_path = os.path.dirname(os.path.realpath(__file__))

# load models
#NLP = spacy.load('en_core_web_sm')
NLP=spacy.load('zh_core_web_trf')
#SuPar = Parser.load('crf-con-en')
SuPar=Parser.load('crf-con-zh')

from stanfordcorenlp import StanfordCoreNLP
# stanfordnlp = StanfordCoreNLP('/Users/fred6/codes/PhD/Research/2022/ARR/stanford-corenlp-full-2018-02-27', lang='zh')
stanfordnlp = StanfordCoreNLP('http://localhost', port=9000, lang='zh')

class pass_text:
    
    """
    Initialize pipeline

    input :
    - text: original input text to analyze

    saves :
    - self.origin_doc
    - self.NLP_doc: spacy pipeline object
    - self.depends: syntactical dependency tree by stanfordcoreNLP
    """
    def __init__(self, text:str):
        self.NLP_doc = NLP(text)
        self.origin_doc = text
        self.depends = stanfordnlp.dependency_parse(text)


    """
    Preprocess given text, count tokens & sentences
    ** throughout this program, only n_token and n_sent are defaulted at 1 to prevent division error

    input :
    - short (default False): include shorts words of under 3 letters
    - see_token (default False): return token_list
    - see_sent_token (default False): return sent_token_list

    saves :
    - self.n_token
    - self.n_sent
    - self.token_list: lemmatized token list, only alphabets
    - self.sent_token_list: token list, no lemmatization, list of list in sentence

    output:
    - n_token
    - n_sent
    - token_list (optional)
    - sent_token_list (optional)
    """
    def preprocess(self, short=False, see_token=False, see_sent_token=False):
        n_token = 1
        n_sent = 1
        token_list = []
        raw_token_list = []
        sent_token_list = []

        # sent_list is for raw string sentences
        sent_list = []

        # Chinese punctunations list
        ChiPuns = "！？｡。＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏."
        # ChiPuns = ChiPuns.decode('utf-8')

        # count tokens, sentence + make lists
        for sent in self.NLP_doc.sents:
            n_sent += 1
            sent_list.append(sent.text)
            temp_list = []
            for token in sent:
                print(token)
                if token.text in ChiPuns:
                    temp_list.append(token.text)
                else:
                    if short == True:
                        n_token += 1
                        #token_list.append(token.lemma_.lower())
                        token_list.append(token.text)
                    if short == False:
                        if len(token.text) >= 3:
                            n_token += 1
                            token_list.append(token.text.lower())
                        else:
                            continue

                '''
                if token.text.isalpha():
                    temp_list.append(token.text)
                if short == True:
                    n_token += 1
                    #token_list.append(token.lemma_.lower())
                    token_list.append(token.text)
                if short == False:
                    if len(token.text) >= 3:
                        n_token += 1
                        token_list.append(token.text.lower())
                '''
            if len(temp_list) > 1:
                temp_list.extend(token_list)
                sent_token_list.append(temp_list)
        '''
        if n_token != 1:
            n_token -= 1 # discard the default n_token = 1
        if n_sent != 1:
            n_sent -= 1 # discard the default n_sent = 1
        '''
        self.n_token = n_token 
        self.n_sent = n_sent
        self.token_list = token_list
        self.sent_token_list = sent_token_list
            
        result = {"n_token": self.n_token, 
                  "n_sent": self.n_sent,
                    }

        if see_token == True:
            result["token"] = token_list
        if see_sent_token == True:
            result["sent_token"] = sent_token_list

        return result


    """
    Shallow Features -> 35

    output (type -> dictionary): 
    - as_fewStroke_C: Percentage of characters containing 1 to 10 strokes per sentence
    - as_moderateStroke_C: Percentage of characters 11 to 20 strokes per sentence
    - as_highStroke_C: Percentage of characters containing over 20 strokes per sentence
    - at_Stroke_C: Average number of strokes per word
    - as_lowhsk_C: Percentage of HSK1 to HSK3-characters per sentence
    - as_moderatehsk_C: Percentage of HSK4 to HSK5-characters per sentence
    - as_highhsk_C: Percentage of HSK6-characters per sentence
    - as_nonhsk_C: Percentage of not-HSK-characters per sentence
    - to_fewStroke_C: Total number of characters containing 1 to 10 strokes
    - to_moderateStroke_C: Total number of characters containing 11 to 20 strokes
    - as_Chara_C: average count of characters per sentence
    - at_Chara_C: average count of characters per token

    - ats_Chara_C: Average number of characters per word per sentence
    - ats_Utoken_C: Average number of characters per unique word per sentence
    - as_TwoWord_C: Number of two-character words per sentence
    - Per_TwoWord_C: Percentage of two-character words per sentence
    - as_ThreeWord_C: Number of three-character words per sentence
    - Per_ThreeWord_C: Percentage of three-character words per sentence
    - as_FourWord_C: Number of four-character words per sentence
    - Per_FourWord_C: Percentage of four-character words per sentence
    - as_upFiveWord_C: Number of five-up-character words per sentence
    - Per_upFiveWord_C: Percentage of five-up-character words per sentence
    - as_lowhsk_W: Percentage of HSK1 to HSK3-words per sentence
    - as_moderatehsk_W: Percentage of HSK4 to HSK5-words per sentence
    - as_highhsk_W: Percentage of HSK6-words per sentence
    - as_nonhsk_W: Percentage of Not-HSK-words per sentence
    - as_firstcommon_W: Percentage of words in 1-1000 mardain frequency list (most-common) per sentence
    - as_secondcommon_W: Percentage of words in 2-2000 mardain frequency list (second-most-common) per sentence
    - as_allcommon_W: Percentage of words in 1-3000 mardain frequency list (all most-common) per sentence
    - TokSenM_S: total count of tokens x total count of sentence
    - TokSenS_S: sqrt(total count of tokens x total count of sentence)
    - TokSenL_S: log(total count of tokens)/log(total count of sentence)
    - as_Token_C: average count of tokens per sentence

    - as_MultiWord: Number of multi-character words per sentence
    - at_DiffWord: Proportion of difficult words, as according to mandarin frequency lists, divided by the total number of words    
    """

    def ShaF_(self):
        result = ShaTr_ShaF.retrieve(self.origin_doc, self.token_list, self.sent_token_list, self.n_token, self.n_sent, threshold_diff=3000)
        result = nan_check(result)
        return result

    """
    Part-of-Speech Features -> 55 -> 132 - 4 -> 128

    output (type -> dictionary): 
    - to_NoTag_C: total count of Noun POS tags
    - as_NoTag_C: average count of Noun POS tags per sentence
    - at_NoTag_C: average count of Noun POS tags per token
    - ra_NoAjT_C: ratio of Noun POS count to Adjective POS count
    - ra_NoVeT_C: ratio of Noun POS count to Verb POS count
    - ra_NoAvT_C: ratio of Noun POS count to Adverb POS count
    - ra_NoSuT_C: ratio of Noun POS count to Subordinating Conjunction count
    - ra_NoCoT_C: ratio of Noun POS count to Coordinating Conjunction count

    - to_VeTag_C: total count of Verb POS tags
    - as_VeTag_C: average count of Verb POS tags per sentence
    - at_VeTag_C: average count of Verb POS tags per token
    - ra_VeAjT_C: ratio of Verb POS count to Adjective POS count
    - ra_VeNoT_C: ratio of Verb POS count to Noun POS count
    - ra_VeAvT_C: ratio of Verb POS count to Adverb POS count
    - ra_VeSuT_C: ratio of Verb POS count to Subordinating Conjunction count
    - ra_VeCoT_C: ratio of Verb POS count to Coordinating Conjunction count

    - to_AjTag_C: total count of Adjective POS tags
    - as_AjTag_C: average count of Adjective POS tags per sentence
    - at_AjTag_C: average count of Adjective POS tags per token
    - ra_AjNoT_C: ratio of Adjective POS count to Noun POS count
    - ra_AjVeT_C: ratio of Adjective POS count to Verb POS count
    - ra_AjAvT_C: ratio of Adjective POS count to Adverb POS count
    - ra_AjSuT_C: ratio of Adjective POS count to Subordinating Conjunction count
    - ra_AjCoT_C: ratio of Adjective POS count to Coordinating Conjunction count

    - to_AvTag_C: total count of Adverb POS tags
    - as_AvTag_C: average count of Adverb POS tags per sentence
    - at_AvTag_C: average count of Adverb POS tags per token
    - ra_AvAjT_C: ratio of Adverb POS count to Adjective POS count
    - ra_AvNoT_C: ratio of Adverb POS count to Noun POS count
    - ra_AvVeT_C: ratio of Adverb POS count to Verb POS count
    - ra_AvSuT_C: ratio of Adverb POS count to Subordinating Conjunction count
    - ra_AvCoT_C: ratio of Adverb POS count to Coordinating Conjunction count

    - to_SuTag_C: total count of Subordinating Conjunction POS tags
    - as_SuTag_C: average count of Subordinating Conjunction POS tags per sentence
    - at_SuTag_C: average count of Subordinating Conjunction POS tags per token
    - ra_SuAjT_C: ratio of Subordinating Conjunction POS count to Adjective POS count
    - ra_SuNoT_C: ratio of Subordinating Conjunction POS count to Noun POS count
    - ra_SuVeT_C: ratio of Subordinating Conjunction POS count to Verb POS count
    - ra_SuAvT_C: ratio of Subordinating Conjunction POS count to Adverb POS count
    - ra_SuCoT_C: ratio of Subordinating Conjunction POS count to Coordinating Conjunction count

    - to_CoTag_C: total count of Coordinating Conjunction POS tags
    - as_CoTag_C: average count of Coordinating Conjunction POS tags per sentence
    - at_CoTag_C: average count of Coordinating Conjunction POS tags per token
    - ra_CoAjT_C: ratio of Coordinating Conjunction POS count to Adjective POS count
    - ra_CoNoT_C: ratio of Coordinating Conjunction POS count to Noun POS count
    - ra_CoVeT_C: ratio of Coordinating Conjunction POS count to Verb POS count
    - ra_CoAvT_C: ratio of Coordinating Conjunction POS count to Adverb POS count
    - ra_CoSuT_C: ratio of Coordinating Conjunction POS count to Subordinating Conjunction count

    - to_ContW_C: total count of Content words
    - as_ContW_C: average count of Content words per sentence
    - at_ContW_C: average count of Content words per token
    - to_FuncW_C: total count of Function words
    - as_FuncW_C: average count of Function words per sentence
    - at_FuncW_C: average count of Function words per token
    - ra_CoFuW_C: ratio of Content words to Function words

    - at_UAdj_C: Percentage of unique adjectives per sentence
    - as_UAdj_C: Number of unique adjectives per sentence
    - at_UFunction_C: Percentage of unique functional words per sentence
    - as_UFunction_C: Number of unique functional words per sentence
    - at_UVerb_C: Percentage of unique verbs per sentence
    - as_UVerb_C: Number of unique verbs per sentence
    - at_UNoun_C: Percentage of unique nouns per sentence
    - as_UNoun_C: Number of unique nouns per sentence
    - at_UContent_C: Percentage of unique content words per sentence
    - as_UContent_C: Number of unique content words per sentence
    - at_UAdverb_C: Percentage of unique adverbs per sentence
    - as_UAdverb_C: Number of unique adverbs per sentence

    - to_NoPhr_C: total count of Noun phrases
    - as_NoPhr_C: average count of Noun phrases per sentence
    - at_NoPhr_C: average count of Noun phrases per token
    - ra_NoVeP_C: ratio of Noun phrases count to Verb phrases count
    - ra_NoSuP_C: ratio of Noun phrases count to Subordinate Clauses count
    - ra_NoPrP_C: ratio of Noun phrases count to Prep phrases count
    - ra_NoAjP_C: ratio of Noun phrases count to Adj phrases count
    - ra_NoAvP_C: ratio of Noun phrases count to Adv phrases count
    
    - to_VePhr_C: total count of Verb phrases
    - as_VePhr_C: average count of Verb phrases per sentence
    - at_VePhr_C: average count of Verb phrases per token
    - ra_VeNoP_C: ratio of Verb phrases count to Noun phrases count
    - ra_VeSuP_C: ratio of Verb phrases count to Subordinate Clauses count
    - ra_VePrP_C: ratio of Verb phrases count to Prep phrases count
    - ra_VeAjP_C: ratio of Verb phrases count to Adj phrases count
    - ra_VeAvP_C: ratio of Verb phrases count to Adv phrases count

    - to_SuPhr_C: total count of Subordinate Clauses
    - as_SuPhr_C: average count of Subordinate Clauses per sentence
    - at_SuPhr_C: average count of Subordinate Clauses per token
    - ra_SuNoP_C: ratio of Subordinate Clauses count to Noun phrases count
    - ra_SuVeP_C: ratio of Subordinate Clauses count to Verb phrases count
    - ra_SuPrP_C: ratio of Subordinate Clauses count to Prep phrases count
    - ra_SuAjP_C: ratio of Subordinate Clauses count to Adj phrases count
    - ra_SuAvP_C: ratio of Subordinate Clauses count to Adv phrases count

    - to_PrPhr_C: total count of prepositional phrases
    - as_PrPhr_C: average count of prepositional phrases per sentence
    - at_PrPhr_C: average count of prepositional phrases per token
    - ra_PrNoP_C: ratio of Prep phrases count to Noun phrases count
    - ra_PrVeP_C: ratio of Prep phrases count to Verb phrases count
    - ra_PrSuP_C: ratio of Prep phrases count to Subordinate Clauses count
    - ra_PrAjP_C: ratio of Prep phrases count to Adj phrases count
    - ra_PrAvP_C: ratio of Prep phrases count to Adv phrases count

    - to_AjPhr_C: total count of Adjective phrases
    - as_AjPhr_C: average count of Adjective phrases per sentence
    - at_AjPhr_C: average count of Adjective phrases per token
    - ra_AjNoP_C: ratio of Adj phrases count to Noun phrases count
    - ra_AjVeP_C: ratio of Adj phrases count to Verb phrases count
    - ra_AjSuP_C: ratio of Adj phrases count to Subordinate Clauses count
    - ra_AjPrP_C: ratio of Adj phrases count to Prep phrases count
    - ra_AjAvP_C: ratio of Adj phrases count to Adv phrases count

    - to_AvPhr_C: total count of Adverb phrases
    - as_AvPhr_C: average count of Adverb phrases per sentence
    - at_AvPhr_C: average count of Adverb phrases per token
    - ra_AvNoP_C: ratio of Adv phrases count to Noun phrases count
    - ra_AvVeP_C: ratio of Adv phrases count to Verb phrases count
    - ra_AvSuP_C: ratio of Adv phrases count to Subordinate Clauses count
    - ra_AvPrP_C: ratio of Adv phrases count to Prep phrases count
    - ra_AvAjP_C: ratio of Adv phrases count to Adj phrases count

    - as_LenNPhrase_C: Average length of noun phrases per sentence
    - as_LenVPhrase_C: 	Average length of verbal phrases per sentence
    - as_LenPrePhrase_C: Average length of prepositional phrases per sentence

    - to_TreeH_C: total Tree height of all sentences
    - as_TreeH_C: average Tree height per sentence
    - at_TreeH_C: average Tree height per token (word)
    - to_FTree_C: total length of flattened Trees
    - as_FTree_C: average length of flattened Trees per sentence
    - at_FTree_C: average length of flattened Trees per token (word)
    - as_DisDepend: Average dependency distance per sentence
    - max_DisDepend: Maximum dependency distance per sentence
    - to_DisDepend_C: Total number of dependency distances per sentence
    - as_DisDepend_C: Average number of dependency distances per sentence
    """
    
    def POSF_(self):
        result = Synta_POSF.retrieve(self.NLP_doc, self.depends, self.n_token, self.n_sent)
        result = nan_check(result)
        return result
    
    def PhrF_(self):
        result = Synta_PhrF.retrieve(SuPar, self.sent_token_list, self.n_token, self.n_sent)
        result = nan_check(result)
        return result
    
    def TrSF_(self):
        result = Synta_TrSF.retrieve(SuPar, self.sent_token_list, self.n_token, self.n_sent)
        result = nan_check(result)
        return result
    

    """
    Extract Entity Density Features -> 27 -> 56

    output (type -> dictionary): 
    - to_EntiM_C: total number of named Entities Mentions counts
    - as_EntiM_C: average number of named Entities Mentions counts per sentence
    - at_EntiM_C: average number of named Entities Mentions counts per token (word)
    - to_UEnti_C: total number of unique named Entities
    - as_UEnti_C: average number of unique named Entities per sentence
    - at_UEnti_C: average number of unique namend Entities per token (word)
    - Per_nonEnti_C: Percentage of Not-NE nouns per sentence
    - as_nonEnti_C: Number of Not-NE nouns per sentence

    - ra_SSToT_C: ratio of ss transitions to total
    - ra_SOToT_C: ratio of so transitions to total
    - ra_SXToT_C: ratio of sx transitions to total
    - ra_SNToT_C: ratio of sn transitions to total
    - ra_OSToT_C: ratio of os transitions to total
    - ra_OOToT_C: ratio of oo transitions to total
    - ra_OXToT_C: ratio of ox transitions to total
    - ra_ONToT_C: ratio of on transitions to total
    - ra_XSToT_C: ratio of xs transitions to total
    - ra_XOToT_C: ratio of xo transitions to total
    - ra_XXToT_C: ratio of xx transitions to total
    - ra_XNToT_C: ratio of xn transitions to total
    - ra_NSToT_C: ratio of ns transitions to total
    - ra_NOToT_C: ratio of no transitions to total
    - ra_NXToT_C: ratio of nx transitions to total
    - ra_NNToT_C: ratio of nn transitions to total
    - LoCohPA_S: Local Coherence for PA score
    - LoCohPW_S: Local Coherence for PW score
    - LoCohPU_S: Local Coherence for PU score
    - LoCoDPA_S: Local Coherence distance for PA score    
    - LoCoDPW_S: Local Coherence distance for PW score    
    - LoCoDPU_S: Local Coherence distance for PU score   

    - Per_UConj_C: Percentage of conjunctions per sentence
    - as_UConj_C: Number of unique conjunctions per sentence
    - Per_UConj_C: Percentage of unique conjunctions per sentence
    - Per_Pronoun_C: Percentage of pronouns per sentence
    - as_UPronoun_C: Number of unique pronouns per sentence
    - Per_UPronoun_C: Percentage of unique pronouns per sentence
    - to_Personal_C: Total number of personal pronouns
    - to_FirstPersonal_C: Total number of first person pronouns
    - to_ThirdPersonal_C: Total number of third person pronouns
    
    - SimpNoV_S: unique Nouns/total Nouns (Noun Variation-1)
    - SquaNoV_S: (unique Nouns**2)/total Nouns (Squared Noun Variation-1)
    - CorrNoV_S: unique Nouns/sqrt(2*total Nouns) (Corrected Noun Variation-1)
    - SimpVeV_S: unique Verbs/total Verbs (Verb Variation-1)
    - SquaVeV_S: (unique Verbs**2)/total Verbs (Squared Verb Variation-1)
    - CorrVeV_S: unique Verbs/sqrt(2*total Verbs) (Corrected Verb Variation-1)
    - SimpAjV_S: unique Adjectives/total Adjectives (Adjective Variation-1)
    - SquaAjV_S: (unique Adjectives**2)/total Adjectives (Squared Adjective Variation-1)
    - CorrAjV_S: unique Adjectives/sqrt(2*total Adjectives) (Corrected Adjective Variation-1)
    - SimpAvV_S: unique Adverbs/total Adverbs (AdVerb Variation-1)
    - SquaAvV_S: (unique Adverbs**2)/total Adverbs (Squared AdVerb Variation-1)
    - CorrAvV_S: unique Adverbs/sqrt(2*total Adverbs) (Corrected AdVerb Variation-1)

    - SimpTTR_S: unique tokens/total tokens (TTR)
    - CorrTTR_S: unique tokens/sqrt(2*total tokens) (Corrected TTR)
    - BiLoTTR_S: log(unique tokens)/log(total tokens) (Bi-Logarithmic TTR)
    - UberTTR_S: (log(unique tokens))^2/log(total tokens/unique tokens) (Uber Index)
    - MTLDTTR_S: Measure of Textual Lexical Diversity (default TTR = 0.72)

    """
    def EnDF_(self):
        result = Disco_EnDF.retrieve(self.NLP_doc, self.n_sent, self.n_token)
        result = nan_check(result)
        return result

    def EnGF_(self):
        """
        if self.n_sent <= 2:
            raise RuntimeError(
                "\n|-.-'-.- LingFeat -.-'-.-|\n"
                +"Error Raised:\n"
                +"This problem might be caused due to the following reasons.\n"
                +"1.Entity Grid needs at least two sentences, found: {}.\n".format(self.n_sent))
        else:
        """
        result = Disco_EnGF.EntityGrid(self.NLP_doc, n_sent=self.n_sent).retrieve()
        result = nan_check(result)
        return result
    
    def VarF_(self):
        result = LxSem_VarF.retrieve(self.NLP_doc)
        result = nan_check(result)
        return result

    def TTRF_(self):
        result = LxSem_TTRF.retrieve(self.n_token, self.token_list)
        result = nan_check(result)
        return result
    