# -*- coding: UTF-8 -*-
"""
Software: LingFeat - Comprehensive Linguistic Features for Readability Assessment
Page: POSF.py (Part-of-Speech Features)
License: CC-BY-SA 4.0

Original Author: Bruce W. Lee (이웅성) @brucewlee
Affiliation 1: LXPER AI, Seoul, South Korea
Affiliation 2: University of Pennsylvania, PA, USA
Contributing Author: -
Affiliation : -

References:
>>> Part-of-Speech features inspired by 
Publication 1: Feng, Lijun, Noémie Elhadad, and Matt Huenerfauth. "Cognitively motivated features for readability assessment." Proceedings of the 12th Conference of the European Chapter of the ACL (EACL 2009). 2009.
"""

from lingfeat.utils import division
    
def retrieve(NLP_doc, n_token, n_sent):
    to_NoTag_C = 0
    to_VeTag_C = 0
    to_AjTag_C = 0
    to_AvTag_C = 0
    to_SuTag_C = 0
    to_CoTag_C = 0
    to_ContW_C = 0
    to_FuncW_C = 0
    to_Subj_C= 0
    to_Obj_C = 0
    to_SubjO_C=0
    to_Conj_C=0
    to_Pronoun_C=0
    to_Pronoun_Person_C=0
    to_Pronoun_Person1_C=0
    to_Pronoun_Person3_C=0
    to_UPronoun_C=0
    to_Personal_C=0
    to_FirstPersonal_C=0
    to_ThirdPersonal_C=0
    to_UConj_C=0
    to_UAdj_C=0
    to_UVerb_C=0
    to_UNoun_C=0
    to_UAdverb_C=0
    to_UContent_C=0
    to_UFunction_C=0
    pronoun_list=[]
    conj_list=[]
    adj_list=[]
    adverb_list=[]
    verb_list=[]
    noun_list=[]
    contentWord_list=[]
    functionWord_list=[]

    for token in NLP_doc:
        #print(token,token.pos_)
        if token.pos_ == "NOUN" or token.pos_ == "VERB" or token.pos_ == "NUM" or token.pos_ == "ADJ" or token.pos_ == "ADV":
            to_ContW_C += 1
            contentWord_list.append(token.text)
        else:
            to_FuncW_C += 1
            functionWord_list.append(token.text)

        if token.pos_ == "NOUN":
            to_NoTag_C += 1
            noun_list.append(token.text)
        if token.pos_ == "VERB":
            to_VeTag_C += 1
            verb_list.append(token.text)
        if token.pos_ == "ADJ":
            to_AjTag_C += 1
            adj_list.append(token.text)
        if token.pos_ == "ADV":
            to_AvTag_C += 1
            adverb_list.append(token.text)
        if token.pos_ == "CONJ":
            to_Conj_C += 1
            conj_list.append(token.text)
        if token.pos_ == "SCONJ":
            to_SuTag_C += 1
        if token.pos_ == "CCONJ":
            to_CoTag_C += 1
        if token.dep_ == "nsubj":
            to_Subj_C += 1
        if token.dep_ == "dobj":
            to_Obj_C += 1
        if token.pos_ == "PRON":
            to_Pronoun_C += 1
            pronoun_list.append(token.text)
        if token.text=='我' or token.text=='我們' or token.text=='你' or token.text=='你們' or token.text=='您' or token.text=='咱們' or token.text=='他' or token.text=='她' or token.text=='它' or token.text=='他們' or token.text=='她們' or token.text=='它們':
            #print(token.text,to_Personal_C)
            to_Personal_C +=1
        if token.text=='我' or token.text=='我們':
            to_FirstPersonal_C +=1
            #print(token.text,to_FirstPersonal_C)
        if token.text=='他' or token.text=='她' or token.text=='它' or token.text=='他們' or token.text=='她們' or token.text=='它們':
            to_ThirdPersonal_C +=1
            #print(token.text,to_ThirdPersonal_C)
    to_UPronoun_C = len(set(pronoun_list))
    #print(set(pronoun_list))
    to_UConj_C = len(set(conj_list))
    #print(set(conj_list))
    to_UAdj_C = len(set(adj_list))
    #print(set(adj_list))
    to_UVerb_C = len(set(verb_list))
    #print(set(verb_list))
    to_UAdverb_C= len(set(adverb_list))
    #print(set(adverb_list))
    to_UNoun_C= len(set(noun_list))
    #print(set(noun_list))
    to_UContent_C=len(set(contentWord_list))
    #print(set(contentWord_list))
    to_UFunction_C=len(set(functionWord_list))
    #print(set(functionWord_list))
    #print(to_UPronoun_C,to_UConj_C,to_UAdj_C,to_UVerb_C,to_UAdverb_C,to_UNoun_C,to_UContent_C,to_UFunction_C)
    #print(to_FirstPersonal_C,to_ThirdPersonal_C,to_Personal_C)
    if to_Subj_C==0:
        to_SubjO_C=1
        #print(to_SubjO_C)
    
    result = {
        "to_NoTag_C":float(to_NoTag_C),
        "as_NoTag_C":float(division(to_NoTag_C,n_sent)),
        "at_NoTag_C":float(division(to_NoTag_C,n_token)),
        "ra_NoAjT_C":float(division(to_NoTag_C,to_AjTag_C)),
        "ra_NoVeT_C":float(division(to_NoTag_C,to_VeTag_C)),
        "ra_NoAvT_C":float(division(to_NoTag_C,to_AvTag_C)),
        "ra_NoSuT_C":float(division(to_NoTag_C,to_SuTag_C)),
        "ra_NoCoT_C":float(division(to_NoTag_C,to_CoTag_C)),
        "to_VeTag_C":float(to_VeTag_C),
        "as_VeTag_C":float(division(to_VeTag_C,n_sent)),
        "at_VeTag_C":float(division(to_VeTag_C,n_token)),
        "ra_VeAjT_C":float(division(to_VeTag_C,to_AjTag_C)),
        "ra_VeNoT_C":float(division(to_VeTag_C,to_NoTag_C)),
        "ra_VeAvT_C":float(division(to_VeTag_C,to_AvTag_C)),
        "ra_VeSuT_C":float(division(to_VeTag_C,to_SuTag_C)),
        "ra_VeCoT_C":float(division(to_VeTag_C,to_CoTag_C)),
        "to_AjTag_C":float(to_AjTag_C),
        "as_AjTag_C":float(division(to_AjTag_C,n_sent)),
        "at_AjTag_C":float(division(to_AjTag_C,n_token)),
        "ra_AjNoT_C":float(division(to_AjTag_C,to_NoTag_C)),
        "ra_AjVeT_C":float(division(to_AjTag_C,to_VeTag_C)),
        "ra_AjAvT_C":float(division(to_AjTag_C,to_AvTag_C)),
        "ra_AjSuT_C":float(division(to_AjTag_C,to_SuTag_C)),
        "ra_AjCoT_C":float(division(to_AjTag_C,to_CoTag_C)),
        "to_AvTag_C":float(to_AvTag_C),
        "as_AvTag_C":float(division(to_AvTag_C,n_sent)),
        "at_AvTag_C":float(division(to_AvTag_C,n_token)),
        "ra_AvAjT_C":float(division(to_AvTag_C,to_AjTag_C)),
        "ra_AvNoT_C":float(division(to_AvTag_C,to_NoTag_C)),
        "ra_AvVeT_C":float(division(to_AvTag_C,to_VeTag_C)),
        "ra_AvSuT_C":float(division(to_AvTag_C,to_SuTag_C)),
        "ra_AvCoT_C":float(division(to_AvTag_C,to_CoTag_C)),
        "to_SuTag_C":float(to_SuTag_C),
        "as_SuTag_C":float(division(to_SuTag_C,n_sent)),
        "at_SuTag_C":float(division(to_SuTag_C,n_token)),
        "ra_SuAjT_C":float(division(to_SuTag_C,to_AjTag_C)),
        "ra_SuNoT_C":float(division(to_SuTag_C,to_NoTag_C)),
        "ra_SuVeT_C":float(division(to_SuTag_C,to_VeTag_C)),
        "ra_SuAvT_C":float(division(to_SuTag_C,to_AvTag_C)),
        "ra_SuCoT_C":float(division(to_SuTag_C,to_CoTag_C)),
        "to_CoTag_C":float(to_CoTag_C),
        "as_CoTag_C":float(division(to_CoTag_C,n_sent)),
        "at_CoTag_C":float(division(to_CoTag_C,n_token)),
        "ra_CoAjT_C":float(division(to_CoTag_C,to_AjTag_C)),
        "ra_CoNoT_C":float(division(to_CoTag_C,to_NoTag_C)),
        "ra_CoVeT_C":float(division(to_CoTag_C,to_VeTag_C)),
        "ra_CoAvT_C":float(division(to_CoTag_C,to_AvTag_C)),
        "ra_CoSuT_C":float(division(to_CoTag_C,to_SuTag_C)),
        "to_ContW_C":float(to_ContW_C),
        "as_ContW_C":float(division(to_ContW_C,n_sent)),
        "at_ContW_C":float(division(to_ContW_C,n_token)),
        "to_FuncW_C":float(to_FuncW_C),
        "as_FuncW_C":float(division(to_FuncW_C,n_sent)),
        "at_FuncW_C":float(division(to_FuncW_C,n_token)),
        "ra_CoFuW_C":float(division(to_ContW_C,to_FuncW_C)), 
        "as_FuncW_C":float(division(to_Subj_C,n_sent)),
        "at_FuncW_C":float(division(to_Subj_C,n_token)),
        "as_Subj_C":float(division(to_Subj_C,n_sent)),
        "at_Subj_C":float(division(to_Subj_C,n_token)),
        "as_Obj_C":float(division(to_Obj_C,n_sent)),
        "at_Obj_C":float(division(to_Obj_C,n_token)),
        "as_SubjO_C":float(division(to_SubjO_C,n_sent)),
        "at_SubjO_C":float(division(to_SubjO_C,n_token)),
        "to_Pronoun_C":float(to_Pronoun_C),
        "as_Pronoun_C":float(division(to_Pronoun_C,n_sent)),
        "at_Pronoun_C":float(division(to_Pronoun_C,n_token)),
        "to_UPronoun_C":float(to_UPronoun_C),
        "as_UPronoun_C":float(division(to_UPronoun_C,n_sent)),
        "at_UPronoun_C":float(division(to_UPronoun_C,n_token)),
        #above is the AACL submission feature list
        "to_Personal_C":float(to_Personal_C),
        "to_FirstPersonal_C":float(to_FirstPersonal_C),
        "to_ThirdPersonal_C":float(to_ThirdPersonal_C),
        "to_Conj_C":float(to_Conj_C),
        "as_Conj_C":float(division(to_Conj_C,n_sent)),
        "at_Conj_C":float(division(to_Conj_C,n_token)),
        "to_UConj_C":float(to_UConj_C),
        "as_UConj_C":float(division(to_UConj_C,n_sent)),
        "at_UConj_C":float(division(to_UConj_C,n_token)),
        "to_UAdj_C":float(to_UAdj_C),
        "as_UAdj_C":float(division(to_UAdj_C,n_sent)),
        "at_UAdj_C":float(division(to_UAdj_C,n_token)),
        "to_UVerb_C":float(to_UVerb_C),
        "as_UVerb_C":float(division(to_UVerb_C,n_sent)),
        "at_UVerb_C":float(division(to_UVerb_C,n_token)),
        "to_UAdverb_C":float(to_UAdverb_C),
        "as_UAdverb_C":float(division(to_UAdverb_C,n_sent)),
        "at_UAdverb_C":float(division(to_UAdverb_C,n_token)),
        "to_UNoun_C":float(to_UNoun_C),
        "as_UNoun_C":float(division(to_UNoun_C,n_sent)),
        "at_UNoun_C":float(division(to_UNoun_C,n_token)),
        "to_UFunction_C":float(to_UFunction_C),
        "as_UFunction_C":float(division(to_UFunction_C,n_sent)),
        "at_UFunction_C":float(division(to_UFunction_C,n_token)),
        "to_UContent_C":float(to_UContent_C),
        "as_UContent_C":float(division(to_UContent_C,n_sent)),
        "at_UContent_C":float(division(to_UContent_C,n_token)),
    }
    return result