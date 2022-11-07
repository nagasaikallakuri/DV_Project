# -*- coding: utf-8 -*-


#############################################################################

import pandas as pd
from mlxtend.frequent_patterns import association_rules 
from mlxtend.frequent_patterns import fpgrowth

syndrome =['Heart Problems', 'Vocal Problems', 'abdominal pain', 'abscess', 'bleeding', 'body pain', 
 'breathing', 'chest', 'cough', 'cramp', 'deficit', 'diabetic', 'diarrhea', 'dizziness',
 'fatigue', 'fever', 'headache', 'infections', 'injury', 'laceration', 'migraine', 'others', 'pregnant', 'rash',
 'urinate', 'vaginal', 'vision', 'vomiting']


#####################################################################
##aleppo data
def fp_growth(dataframe) :
    frq_items = fpgrowth(dataframe[syndrome], min_support = 0.0050, use_colnames = True) 
    # Collecting the inferred rules in a dataframe 
    rules = association_rules(frq_items, metric ="lift", min_threshold = 1) 
    rules = rules.sort_values(['confidence', 'lift'], ascending =[False, False]) 
    #print(rules.iloc[0:10,:]) 
    return rules.iloc[0:10000,:]


def perform_FP_Growth(filename) : 
    country=filename[:-4]
    aleppo=pd.read_csv("./merged_data/Saudi-Arabia_final.csv")

    aleppo = aleppo.sample(frac=1).reset_index(drop=True)
    aleppo=aleppo.iloc[0:6000000]
    aleppo.drop(['AGE','GENDER','AGE_GROUP', 'LIFE_SPAN','DATE', 'DATE_OF_DEATH','PATIENT_ID'], axis=1, inplace=True)
    aleppo=aleppo
    aleppo_death = aleppo.loc[(aleppo['DEATH'] == 1)]
    #aleppo_alive=aleppo.loc[(aleppo['DEATH']==0)]  
    aleppo_result= fp_growth(aleppo)
    aleppo_result.to_csv("FP_growth_Hosp"+file,index=False)
    aleppo_death_result = fp_growth(aleppo_death)
    aleppo_death_result.to_csv("FP_growth_dead"+file,index=False)
    #aleppo_alive_result=fp_growth(aleppo_alive)
    #aleppo_alive_result.to_csv("FP_growth_alive"+file,index=False)
    
    
all_files = [
'aleppo.csv',
'colombia.csv'
 'iran.csv',
'karachi.csv'
'lebanon.csv'
'nairobi.csv',
'saudiarabia.csv',
'thailand.csv'
 'turkey.csv'
 'venezuela.csv',
 'aleppo.csv'
'Yemen.csv'
]


for file in all_files:
    print(file)
    ans=perform_FP_Growth(file)
    #print(ans)