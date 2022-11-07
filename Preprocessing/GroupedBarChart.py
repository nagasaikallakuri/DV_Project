import numpy as np
import pandas as pd

df = pd.read_csv("iran_final.csv")

df

unique_ages= df['AGE'].unique()

unique_ages

unique_age_grp= df['AGE_GROUP'].unique()
unique_age_grp

def datapreproc(df):
    dict2={}
    unique_age_grp= df['AGE_GROUP'].unique()
    for i in unique_age_grp:
        dict2[i]=[0,0,0]
    for i in unique_age_grp:
        count = df[df['AGE_GROUP']==i].count()[0]
    for i,r in df.iterrows():
        if r['DEATH']==1:
            dict2[r['AGE_GROUP']][1] += 1
        dict2[r['AGE_GROUP']][0]+=1
        dict2[r['AGE_GROUP']][2] = dict2[r['AGE_GROUP']][0] - dict2[r['AGE_GROUP']][1]
    return dict2    

dict1 = datapreproc(df)

dict1

dataframe = []

for i in unique_age_grp: 
    dataframe.append([i,dict1[i][0],dict1[i][1], dict1[i][2]])
    
df5=pd.DataFrame(dataframe,columns=['AGE_GROUP','Iran_Hosp','Iran_Dead','Iran_Recovered'])

df5


#Colombia

df = pd.read_csv("colombia_final.csv")

df

dict1= datapreproc(df)

hosp=[]
dead=[]
recov=[]

for i in unique_age_grp: 
    hosp.append(dict1[i][0])
    dead.append(dict1[i][1])  
    recov.append(dict1[i][2])
df5['Colombia_Hosp']=hosp
df5['Colombia_Dead']=dead
df5['Colombia_Recovered']=recov

df5



#Lebanon

df = pd.read_csv("lebanon_final.csv")
df

dict1= datapreproc(df)

hosp=[]
dead=[]
recov=[]

for i in unique_age_grp: 
    hosp.append(dict1[i][0])
    dead.append(dict1[i][1])  
    recov.append(dict1[i][2])
df5['Lebanon_Hosp']=hosp
df5['Lebanon_Dead']=dead
df5['Lebanon_Recovered']=recov

df5



#Thailand

df = pd.read_csv("thailand_final.csv")
df

dict1= datapreproc(df)
dict1

hosp=[]
dead=[]
recov=[]

for i in unique_age_grp: 
    hosp.append(dict1[i][0])
    dead.append(dict1[i][1])  
    recov.append(dict1[i][2])
df5['Thailand_Hosp']=hosp
df5['Thailand_Dead']=dead
df5['Thailand_Recovered']=recov

df5


#Turkey

df = pd.read_csv("turkey_final.csv")
df

dict1= datapreproc(df)
dict1

hosp=[]
dead=[]
recov=[]

for i in unique_age_grp: 
    hosp.append(dict1[i][0])
    dead.append(dict1[i][1])  
    recov.append(dict1[i][2])
df5['Turkey_Hosp']=hosp
df5['Turkey_Dead']=dead
df5['Turkey_Recovered']=recov

df5



#Venezuela

df = pd.read_csv("venezuela_final.csv")
df

dict1= datapreproc(df)
dict1

hosp=[]
dead=[]
recov=[]

for i in unique_age_grp: 
    hosp.append(dict1[i][0])
    dead.append(dict1[i][1])  
    recov.append(dict1[i][2])
df5['Venezuela_Hosp']=hosp
df5['Venezuela_Dead']=dead
df5['Venezuela_Recovered']=recov

df5



#Yemen

df = pd.read_csv("yemen_final.csv")
df

dict1= datapreproc(df)
dict1

hosp=[]
dead=[]
recov=[]

for i in unique_age_grp: 
    hosp.append(dict1[i][0])
    dead.append(dict1[i][1])  
    recov.append(dict1[i][2])
df5['Yemen_Hosp']=hosp
df5['Yemen_Dead']=dead
df5['Yemen_Recovered']=recov

df5

df5.columns



#Aleppo:

df = pd.read_csv('aleppo_final.csv')
df

dict1= datapreproc(df)
dict1

hosp=[]
dead=[]
recov=[]

for i in unique_age_grp: 
    hosp.append(dict1[i][0])
    dead.append(dict1[i][1])  
    recov.append(dict1[i][2])
df5['Aleppo_Hosp']=hosp
df5['Aleppo_Dead']=dead
df5['Aleppo_Recovered']=recov

df5



#Nairobi

df = pd.read_csv('nairobi_final.csv')
df

dict1= datapreproc(df)
dict1

hosp=[]
dead=[]
recov=[]

for i in unique_age_grp: 
    hosp.append(dict1[i][0])
    dead.append(dict1[i][1])  
    recov.append(dict1[i][2])
df5['Nairobi_Hosp']=hosp
df5['Nairobi_Dead']=dead
df5['Nairobi_Recovered']=recov

df5



##Karachi

df = pd.read_csv('karachi_final.csv')
df

dict1= datapreproc(df)
dict1

hosp=[]
dead=[]
recov=[]

for i in unique_age_grp: 
    hosp.append(dict1[i][0])
    dead.append(dict1[i][1])  
    recov.append(dict1[i][2])
df5['Karachi_Hosp']=hosp
df5['Karachi_Dead']=dead
df5['Karachi_Recovered']=recov

df5



#Saudi Arabia:

df = pd.read_csv('saudi_arabia_final.csv')

df

dict1= datapreproc(df)
dict1

hosp=[]
dead=[]
recov=[]

for i in unique_age_grp: 
    hosp.append(dict1[i][0])
    dead.append(dict1[i][1])  
    recov.append(dict1[i][2])
df5['Saudiarabia_Hosp']=hosp
df5['Saudiarabia_Dead']=dead
df5['Saudiarabia_Recovered']=recov

df5



df5.columns

#All Hosp, All Dead, All Recovered:

df5["All_Hosp"] = df5["Iran_Hosp"] + df5["Colombia_Hosp"] + df5["Lebanon_Hosp"] + df5["Thailand_Hosp"] + df5["Turkey_Hosp"] +\
df5['Venezuela_Hosp'] + df5['Yemen_Hosp'] + df5['Aleppo_Hosp'] + df5['Nairobi_Hosp'] + df5['Karachi_Hosp'] + df5['Saudiarabia_Hosp']


df5["All_Dead"] = df5["Iran_Dead"] + df5["Colombia_Dead"] + df5["Lebanon_Dead"] + df5["Thailand_Dead"] + df5["Turkey_Dead"] +\
df5['Venezuela_Dead'] + df5['Yemen_Dead'] + df5['Aleppo_Dead'] + df5['Nairobi_Dead'] + df5['Karachi_Dead'] + df5['Saudiarabia_Dead']

df5["All_Recovered"] = df5["Iran_Recovered"] + df5["Colombia_Recovered"] + df5["Lebanon_Recovered"] + df5["Thailand_Recovered"] + df5["Turkey_Recovered"] +\
df5['Venezuela_Recovered'] + df5['Yemen_Recovered'] + df5['Aleppo_Recovered'] + df5['Nairobi_Recovered'] + df5['Karachi_Recovered'] + df5['Saudiarabia_Recovered']

df5



df5.to_csv('GroupedBarChart.csv')





















