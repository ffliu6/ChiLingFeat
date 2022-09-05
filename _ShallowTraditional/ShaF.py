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
import sys
sys.path.append('../')
from utils import count_syllables
from numpy import diff
import pandas as pd
import json
import xlrd
# from stanfordcorenlp import StanfordCoreNLP
# nlp = StanfordCoreNLP("http://localhost", port=9000, lang="zh")


strokeDf=pd.read_csv("hanziDB.csv")
strokeDict={}
hskcharDict = {}
for index,character in enumerate(strokeDf['charcter']):
    strokeDict[strokeDf.loc[index,'charcter']]=strokeDf.loc[index,'stroke_count']
    hskcharDict[strokeDf.loc[index,'charcter']]=strokeDf.loc[index,'hsk_level']

hskwordJf = "hsk.json"
hskwordDict = {}
with open(hskwordJf, 'r', encoding='utf-8', errors='ignore') as f:
    content = json.load(fp=f)
    for line in content:
        hskwordDict[line['hanzi']] = line['level']


def _read_xls_alltables(path):
    workbook = xlrd.open_workbook(path)
    worksheets = workbook.sheet_names()
    all_tables = []
    for i in range(len(workbook.sheets())):
        worksheet = workbook.sheets()[i]
        num_cols = worksheet.ncols
        num_rows = worksheet.nrows
        dict_list = []
        for i in range(1, num_rows):
            temp_dict = {}
            for j in range(0, num_cols):
                temp_dict[worksheet.cell_value(0, j)] = worksheet.cell_value(i, j)
            dict_list.append(temp_dict)
        all_tables.append(dict_list)

    return all_tables


commonwordDf = "Mandarin_Freq.xls"
commonword_tables = _read_xls_alltables(commonwordDf)
commonwordDict = {}
for i in range(len(commonword_tables)):
    commonwordDict[i + 1] = commonword_tables[i]


def retrieve(origin_doc, token_list, sent_token_list, n_token, n_sent, threshold_diff):
    to_fewStroke_C=0
    to_moderateStroke_C=0
    to_highStroke_C=0
    total_count_stroke = 0

    to_lowhsk_C = 0
    to_moderatehsk_C = 0
    to_highhsk_C = 0
    to_nonhsk_C = 0

    to_MultiWord = 0
    to_TwoWord = 0
    to_ThreeWord = 0
    to_FourWord = 0
    to_upFiveWord = 0

    to_lowhsk_W = 0
    to_moderatehsk_W = 0
    to_highhsk_W = 0
    to_nonhsk_W = 0

    to_firstcommon_W = 0
    to_secondcommon_W = 0
    to_allcommon_W = 0

    to_diffwords = 0

    total_count_char = len(origin_doc.replace(" ",""))
    characterList=origin_doc.replace(" ","")

    Utoken_list = set(token_list)

    #print(characterList)
    for character in characterList:
        # calculate stroke number
        if character in strokeDict:
            total_count_stroke += strokeDict[character]
            #print(character)
            if int(strokeDict[character])>0 and int(strokeDict[character])<=10:
                #print("few"+character)
                to_fewStroke_C+=1
            if int(strokeDict[character])>10 and int(strokeDict[character])<=20:
                #print("moder"+character)
                to_moderateStroke_C+=1
            if int(strokeDict[character] > 20):
                to_highStroke_C += 1
        
        # calculate hsk level
        if character in hskcharDict:
            if int(hskcharDict[character]) >= 1 and int(hskcharDict[character]) <= 3:
                to_lowhsk_C += 1
            if int(hskcharDict[character]) >= 4 and int(hskcharDict[character]) <= 5:
                to_moderatehsk_C += 1
            if int(hskcharDict[character]) == 6:
                to_highhsk_C += 1
        if character not in hskcharDict:
            to_nonhsk_C += 1

    threshold_diff = int(round(threshold_diff / 1000))
    diff_words = []
    for i in range(threshold_diff, len(commonword_tables)):
        diff_words.extend(commonword_tables[i])

    for token in token_list:
        if len(token) >= 2:
            to_MultiWord += 1
        if len(token)==2:
            to_TwoWord+=1
        if len(token)==3:
            to_ThreeWord+=1
        if len(token) == 4:
            to_FourWord += 1
        if len(token) >= 5:
            to_upFiveWord += 1
        
        if token in hskwordDict:
            if int(hskwordDict[token]) >= 1 and int(hskwordDict[token]) <= 3:
                to_lowhsk_W += 1
            if int(hskwordDict[token]) >= 4 and int(hskwordDict[token]) <= 5:
                to_moderatehsk_W += 1
            if int(hskwordDict[token]) == 6:
                to_highhsk_W += 1
        if token not in hskwordDict:
            to_nonhsk_W += 1
        
        if token in commonwordDict[1]:
            to_firstcommon_W += 1
            to_allcommon_W += 1
        if token in commonwordDict[2]:
            to_secondcommon_W += 1
            to_allcommon_W += 1
        if token in commonwordDict[3]:
            to_allcommon_W += 1
        
        if token in diff_words:
            to_diffwords += 1
    
        #print(token)
    #print(to_TwoWord,to_ThreeWord)
    #print(characterList,to_fewStroke_C,to_moderateStroke_C)
    total_count_tokn = n_token
    total_count_syll = 0
    for token in token_list:
        total_count_syll += count_syllables(token)
    
    Per_TwoWord_C = 0
    Per_ThreeWord_C = 0
    Per_FourWord_C = 0
    Per_upFiveWord_C = 0

    for sent_tokens in sent_token_list:
        for sent_token in sent_tokens:
            if len(sent_token) == 2:
                Per_TwoWord_C += 1
            if len(sent_token) == 3:
                Per_ThreeWord_C += 1
            if len(sent_token) == 4:
                Per_FourWord_C += 1
            if len(sent_token) >= 5:
                Per_upFiveWord_C += 1
        Per_TwoWord_C += (Per_TwoWord_C / len(sent_tokens))
        Per_ThreeWord_C += (Per_ThreeWord_C / len(sent_tokens))
        Per_FourWord_C += (Per_FourWord_C / len(sent_tokens))
        Per_upFiveWord_C += (Per_upFiveWord_C / len(sent_tokens))
    

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
        "as_fewStroke_C":float(to_fewStroke_C/n_sent),
        "to_moderateStroke_C":float(to_moderateStroke_C),
        "as_moderateStroke_C":float(to_moderateStroke_C/n_sent),
        "to_highStroke_C": float(to_highStroke_C),
        # "as_highStroke_C": float(to_highStroke_C/n_sent),
        "at_Stroke_C": float(total_count_stroke/n_token),
        "as_lowhsk_C": float(to_lowhsk_C / n_sent),
        "as_moderatehsk_C": float(to_moderatehsk_C / n_sent),
        "as_highhsk_C": float(to_highhsk_C / n_sent),
        "as_nonhsk_C": float(to_nonhsk_C / n_sent),

        "ats_Chara_C": float((total_count_char / n_token) / n_sent),
        "ats_Utoken_C": float(total_count_char / len(Utoken_list)),

        "as_MultiWord": float(to_MultiWord / n_sent),
        # "to_TwoWord":float(to_TwoWord),
        "as_TwoWord_C":float(to_TwoWord/n_sent),
        "Per_TwoWord_C": float(Per_TwoWord_C / n_sent),
        # "at_TwoWord_C":float(to_TwoWord/n_token),
        # "to_ThreeWord":float(to_ThreeWord),
        "as_ThreeWord_C":float(to_ThreeWord/n_sent),
        "Per_ThreeWord_C": float(Per_ThreeWord_C / n_sent),
        # "at_ThreeWord_C":float(to_ThreeWord/n_token),
        # "to_FourWord": float(to_FourWord),
        "as_FourWord_C": float(to_FourWord/n_sent),
        "Per_FourWord_C": float(Per_FourWord_C / n_sent),
        # "at_FourWord_C": float(to_FourWord/n_token),
        # "to_upFiveWord": float(to_upFiveWord),
        "as_upFiveWord_C": float(to_upFiveWord/n_sent),
        "Per_upFiveWord_C": float(Per_upFiveWord_C / n_sent),
        # "at_upFiveWord_C": float(to_upFiveWord/n_token),
        "as_lowhsk_W": float(to_lowhsk_W / n_sent),
        "as_moderatehsk_W": float(to_moderatehsk_W / n_sent),
        "as_highhsk_W": float(to_highhsk_W / n_sent),
        "as_nonhsk_W": float(to_nonhsk_W / n_sent),
        "as_firstcommon_W": float(to_firstcommon_W / n_sent),
        "as_secondcommon_W": float(to_secondcommon_W / n_sent),
        "as_allcommon_W": float(to_allcommon_W / n_sent),
        "at_DiffWord": float(to_diffwords / n_token),
    }
    return result