import numpy as np
import pandas as pd

df = pd.read_csv("iran_final.csv")

df

unique_dates= df['DATE'].unique()

unique_dates

dict1 = {}

for i in unique_dates:
    dict1[i]=0
print(dict1)

for i in unique_dates:
    dict1[i]=[0,0]
for i, r in df.iterrows():
    if r['DEATH']==1:
        dict1[r['DATE']][1] += 1
    dict1[r['DATE']][0]+=1
print(dict1)

df

for i in unique_dates:
    count = df[df['DATE']==i].count()[0]
    print(i, count)




def datapreproc(df):
    dict2={}
    unique_dates= df['DATE'].unique()
    for i in unique_dates:
        count = df[df['DATE']==i].count()[0]
    for i in unique_dates:
        dict2[i]=[0,0]
    for i, r in df.iterrows():
        if r['DEATH']==1:
            dict2[r['DATE']][1] += 1
        dict2[r['DATE']][0]+=1
    return dict2

data = [['tom', 10], ['nick', 15], ['juli', 14]]
  
# Create the pandas DataFrame
df3 = pd.DataFrame(data, columns = ['Name', 'Age'])
  
df3

dict1[i][0]

l=[]
dataframe = []

for i in unique_dates: 
    dataframe.append([i,dict1[i][0],dict1[i][1]])
    
df5=pd.DataFrame(dataframe,columns=['DATE','HOSP','DEAD'])

print(df5)

print(type(df5))

df5

df = pd.read_csv("colombia_final.csv")

df

dict1= datapreproc(df)


str1 = "Mira_Kumar"
str1.split('_')

df5 = df5.rename(columns={'HOSP': 'Iran_HOSP', 'DEAD':'Iran_DEAD'}, index={'ONE': 'Row_1'})

df5

print(dict1)

Columbia_hosp=[]
Columbia_dead=[]

for i in unique_dates: 
    Columbia_hosp.append(dict1[i][0])
    Columbia_dead.append(dict1[i][1])   
df5['Columbia_HOSP']=Columbia_hosp
df5['Columbia_DEAD']=Columbia_dead
df5

df = pd.read_csv("lebanon_final.csv")

df

dict1= datapreproc(df)

print(dict1)



Leb_hosp=[]
Leb_dead=[]

for i in unique_dates: 
    Leb_hosp.append(dict1[i][0])
    Leb_dead.append(dict1[i][1])   
df5['Lebanon_HOSP']=Leb_hosp
df5['Lebanon_DEAD']=Leb_dead
df5


df = pd.read_csv("thailand_final.csv")

df

dict1= datapreproc(df)
print(dict1)

#Added missing value for 04-20-2009 in Dict:
dict1['4-20-2009']= [0,0]

dict1

hosp=[]
dead=[]

for i in unique_dates: 
    hosp.append(dict1[i][0])
    dead.append(dict1[i][1])   
df5['Thailand_HOSP']=hosp
df5['Thailand_DEAD']=dead
df5


df = pd.read_csv("turkey_final.csv")

df

dict1= datapreproc(df)
print(dict1)

dict1['5-25-2009']= [0,0]

hosp=[]
dead=[]

for i in unique_dates: 
    hosp.append(dict1[i][0])
    dead.append(dict1[i][1])   
df5['Turkey_HOSP']=hosp
df5['Turkey_DEAD']=dead
df5


df = pd.read_csv("venezuela_final.csv")

df

dict1= datapreproc(df)
print(dict1)

dict1['4-20-2009']= [0,0]

hosp=[]
dead=[]

for i in unique_dates: 
    hosp.append(dict1[i][0])
    dead.append(dict1[i][1])   
df5['Venezuela_HOSP']=hosp
df5['Venezuela_DEAD']=dead
df5


df = pd.read_csv("yemen_final.csv")
df

dict1 = datapreproc(df)

print(dict1)

hosp=[]
dead=[]

for i in unique_dates: 
    hosp.append(dict1[i][0])
    dead.append(dict1[i][1])   
df5['Yemen_HOSP']=hosp
df5['Yemen_DEAD']=dead
df5



#Dataframe to csv:

df5.to_csv('HospAndDeath.csv')

df5


df = pd.read_csv("aleppo_final.csv")
df

dict1 = datapreproc(df)

dict1

hosp=[]
dead=[]

for i in unique_dates: 
    hosp.append(dict1[i][0])
    dead.append(dict1[i][1])   
df5['Aleppo_HOSP']=hosp
df5['Aleppo_DEAD']=dead
df5



df = pd.read_csv("nairobi_final.csv")
df

dict1 = datapreproc(df)
dict1

hosp=[]
dead=[]

for i in unique_dates: 
    hosp.append(dict1[i][0])
    dead.append(dict1[i][1])   
df5['Nairobi_HOSP']=hosp
df5['Nairobi_DEAD']=dead
df5



df = pd.read_csv("karachi_final.csv")
df

dict1 = datapreproc(df)
dict1

hosp=[]
dead=[]

for i in unique_dates: 
    hosp.append(dict1[i][0])
    dead.append(dict1[i][1])   
df5['Karachi_Hosp']=hosp
df5['Karachi_Dead']=dead
df5



df = pd.read_csv("saudi_arabia_final.csv")
df

dict1 = datapreproc(df)
dict1

hosp=[]
dead=[]

for i in unique_dates: 
    hosp.append(dict1[i][0])
    dead.append(dict1[i][1])   
df5['Saudiarabia_Hosp']=hosp
df5['Saudiarabia_Dead']=dead
df5

df5.columns

df5 = df5.rename(columns={'Iran_HOSP': 'Iran_Hosp', 'Iran_DEAD':'Iran_Dead', 'Columbia_HOSP': 'Columbia_Hosp', \
                          'Columbia_DEAD':'Columbia_Dead', 'Lebanon_HOSP':'Lebanon_Hosp', 'Lebanon_DEAD':\
                          'Lebanon_Dead', 'Thailand_HOSP': 'Thailand_Hosp', 'Thailand_DEAD': 'Thailand_Dead', \
                          'Turkey_HOSP':'Turkey_Hosp', 'Turkey_DEAD':'Turkey_Dead', 'Venezuela_HOSP':'Venezuela_Hosp',\
                          'Venezuela_DEAD':'Venezuela_Dead', 'Yemen_HOSP':'Yemen_Hosp', \
                          'Yemen_DEAD':'Yemen_Dead','Aleppo_HOSP':'Aleppo_Hosp','Aleppo_DEAD':'Aleppo_Dead', \
                          'Nairobi_HOSP':'Nairobi_Hosp', 'Nairobi_DEAD':'Nairobi_Dead'
                         }, index={'ONE': 'Row_1'})




df5


df5.columns

df5['All_Hosp'] = df5['Iran_Hosp'] + df5['Columbia_Hosp'] + df5['Lebanon_Hosp'] + df5['Thailand_Hosp'] + \
                    df5['Turkey_Hosp'] + df5['Venezuela_Hosp'] + df5['Yemen_Hosp'] + df5['Aleppo_Hosp'] + \
                    df5['Nairobi_Hosp'] + df5['Saudiarabia_Hosp'] + df5['Karachi_Hosp'] 



df5

df5['All_Dead'] = df5['Iran_Dead'] + df5['Columbia_Dead'] + df5['Lebanon_Dead'] + df5['Thailand_Dead'] + \
                    df5['Turkey_Dead'] + df5['Venezuela_Dead'] + df5['Yemen_Dead'] + df5['Aleppo_Dead'] + \
                    df5['Nairobi_Dead'] + df5['Saudiarabia_Dead'] + df5['Karachi_Dead'] 

df5

df5.columns

df5 = df5.rename(columns={'Columbia_Hosp': 'Colombia_Hosp', 'Columbia_Dead':'Colombia_Dead'}, index={'ONE': 'Row_1'})

df5.columns

df5.to_csv('StreamgraphData.csv')


df6= pd.read_csv('StreamgraphData.csv')

df6.columns

df5.columns

df5 = df5.rename(columns={'Columbia_Hosp': 'Colombia_Hosp', 'Columbia_Dead':'Colombia_Dead'}, index={'ONE': 'Row_1'})

df5.to_csv('StreamgraphData.csv')


df = pd.read_csv('StreamgraphData.csv')

df

df.drop(columns={'All_Hosp', 'All_Dead'})

df.drop(columns={'Unnamed: 0'})

df.to_csv('StreamgraphData.csv')

df

df.columns

df = df.drop(columns={'All_Hosp', 'All_Dead'})

df.columns


df = df.drop(columns={'Unnamed: 0'})

df.columns

df.to_csv('StreamgraphData.csv')

