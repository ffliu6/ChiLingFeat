# -*- coding: UTF-8 -*-
"""
Software: LingFeat - Comprehensive Linguistic Features for Readability Assessment
Page: ShaF.py (Shallow Features)
License: CC-BY-SA 4.0

Original Author: Bruce W. Lee (이웅성) @brucewlee
Affiliation 1: LXPER AI, Seoul, South Korea
Affiliation 2: University of Pennsylvania, PA, USA
Contributing Author: -
Affiliation : -


References:
>>> Shallow features inspired by 
Publication 1: Feng, Lijun, Noémie Elhadad, and Matt Huenerfauth. "Cognitively motivated features for readability assessment." Proceedings of the 12th Conference of the European Chapter of the ACL (EACL 2009). 2009.
"""
import math
from lingfeat.utils import count_syllables
import pandas as pd

strokeDf=pd.read_csv("hanziDB.csv")
strokeDict={}
for index,character in enumerate(strokeDf['charcter']):
    strokeDict[strokeDf.loc[index,'charcter']]=strokeDf.loc[index,'stroke_count']
def retrieve(origin_doc, token_list, n_token, n_sent):
    to_fewStroke_C=0
    to_moderateStroke_C=0
    to_TwoWord=0
    to_ThreeWord=0
    total_count_char = len(origin_doc.replace(" ",""))
    characterList=origin_doc.replace(" ","")
    #print(characterList)
    for character in characterList:
        if character in strokeDict:
            #print(character)
            if int(strokeDict[character])>0 and int(strokeDict[character])<=10:
                #print("few"+character)
                to_fewStroke_C+=1
            if int(strokeDict[character])>10 and int(strokeDict[character])<=20:
                #print("moder"+character)
                to_moderateStroke_C+=1
    for token in token_list:
        if len(token)==2:
            to_TwoWord+=1
        if len(token)==3:
            to_ThreeWord+=1
        #print(token)
    #print(to_TwoWord,to_ThreeWord)
    #print(characterList,to_fewStroke_C,to_moderateStroke_C)
    total_count_tokn = n_token
    total_count_syll = 0
    for token in token_list:
        total_count_syll += count_syllables(token)
    result = {
        "TokSenM_S":float(n_token*n_sent),
        "TokSenS_S":float(math.sqrt(n_token*n_sent)),
        "TokSenL_S":float(math.log(n_token)/math.log(n_sent)),
        "as_Token_C":float(total_count_tokn/n_sent),
        #"as_Sylla_C":float(total_count_syll/n_sent),  
        #"at_Sylla_C":float(total_count_syll/n_token),       
        "as_Chara_C":float(total_count_char/n_sent),   
        "at_Chara_C":float(total_count_char/n_token),
        "to_fewStroke_C":float(to_fewStroke_C),
        "to_moderateStroke_C":float(to_moderateStroke_C),
        "to_TwoWord":float(to_TwoWord),
        "as_TwoWord_C":float(to_TwoWord/n_sent),
        "at_TwoWord_C":float(to_TwoWord/n_token),
        "to_ThreeWord":float(to_ThreeWord),
        "as_ThreeWord_C":float(to_ThreeWord/n_sent),
        "at_ThreeWord_C":float(to_ThreeWord/n_token),
    }
    return result