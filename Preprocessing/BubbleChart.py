import numpy as np
import pandas as pd

#Iran

df = pd.read_csv("iran_final.csv")

df

df5 = pd.DataFrame()

col = ['Syndrome','Iran_Hosp', 'Iran_Dead' ,'Colombia_Hosp', 'Colombia_Dead', 'Lebanon_Hosp','Lebanon_Dead', 'Thailand_Hosp','Thailand_Dead','Turkey_Hosp','Turkey_Dead','Venezuela_Hosp', 'Venezuela_Dead','Yemen_Hosp','Yemen_Dead','Aleppo_Hosp',
       'Aleppo_Dead','Nairobi_Hosp', 'Nairobi_Dead','Karachi_Hosp', 'Karachi_Dead','Saudiarabia_Hosp', 'Saudiarabia_Dead','All_Hosp','All_Dead']
df5 =pd.DataFrame(columns= col)

df5

l=[]
for (columnName, columnData) in df.iteritems():
    l.append(columnName)
print(l)

l = l[11:]
l

df5['Syndrome']=l
df5

dead=0
hosp=0
d=[]
h=[]
for i,r in df.iterrows():
    if r['bleeding']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)

d

h

dead=0
hosp=0
for i,r in df.iterrows():
    if r['abscess']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['dizziness']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['breathing']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['chest']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['urinate']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['Vocal Problems']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['vomiting']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['headache']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['laceration']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['cramp']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['pregnant']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['migraine']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['rash']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['fatigue']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['injury']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['deficit']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['vaginal']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['diarrhea']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['abdominal pain']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['infections']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['cough']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['diabetic']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['body pain']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['Heart Problems']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['fever']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['vision']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['others']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

len(l)

df5['Iran_Hosp'] = h
df5['Iran_Dead'] = d

df5

#Colombia

df = pd.read_csv('colombia_final.csv')

df

dead=0
hosp=0
d=[]
h=[]
for i,r in df.iterrows():
    if r['bleeding']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print(d)
print(h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['abscess']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['dizziness']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['breathing']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['chest']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['urinate']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['Vocal Problems']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['vomiting']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['headache']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['laceration']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['cramp']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['pregnant']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['migraine']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['rash']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['fatigue']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['injury']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['deficit']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['vaginal']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['diarrhea']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['abdominal pain']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['infections']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['cough']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['diabetic']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['body pain']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['Heart Problems']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['fever']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['vision']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

dead=0
hosp=0
for i,r in df.iterrows():
    if r['others']==1:
        if r['DEATH']==1:
            dead += 1
        else: 
            hosp += 1
d.append(dead) 
h.append(hosp)
print('d',d)
print('h',h)

len(d)

len(h)

df5['Colombia_Hosp']=h
df5['Colombia_Dead']=d

df5

#Lebanon:

df = pd.read_csv('lebanon_final.csv')

df

print(l)

d=[]
h=[]
for j in l:
    dead=0
    hosp=0
    for i,r in df.iterrows():
        if r[j]==1:
            if r['DEATH']==1:
                dead += 1
            else: 
                hosp += 1
    d.append(dead) 
    h.append(hosp)

print(d)
print(h)
print(len(d))
print(len(h))

df5['Lebanon_Dead'] = d
df5['Lebanon_Hosp'] = h

df5

#Thailand:

df = pd.read_csv('thailand_final.csv')

df

d=[]
h=[]
for j in l:
    dead=0
    hosp=0
    for i,r in df.iterrows():
        if r[j]==1:
            if r['DEATH']==1:
                dead += 1
            else: 
                hosp += 1
    d.append(dead) 
    h.append(hosp)

print(d)
print(h)
print(len(d))
print(len(h))

df5['Thailand_Dead'] = d
df5['Thailand_Hosp'] = h

df5

#Turkey:

df = pd.read_csv('turkey_final.csv')

df

d=[]
h=[]
for j in l:
    dead=0
    hosp=0
    for i,r in df.iterrows():
        if r[j]==1:
            if r['DEATH']==1:
                dead += 1
            else: 
                hosp += 1
    d.append(dead) 
    h.append(hosp)

print(d)
print(h)
print(len(d))
print(len(h))

df5['Turkey_Dead'] = d
df5['Turkey_Hosp'] = h

df5

#Venezuela

df = pd.read_csv('venezuela_final.csv')

df 

d=[]
h=[]
for j in l:
    dead=0
    hosp=0
    for i,r in df.iterrows():
        if r[j]==1:
            if r['DEATH']==1:
                dead += 1
            else: 
                hosp += 1
    d.append(dead) 
    h.append(hosp)

print(d)
print(h)
print(len(d))
print(len(h))

df5['Venezuela_Dead'] = d
df5['Venezuela_Hosp'] = h

df5

#Yemen

df = pd.read_csv('yemen_final.csv')

df

d=[]
h=[]
for j in l:
    dead=0
    hosp=0
    for i,r in df.iterrows():
        if r[j]==1:
            if r['DEATH']==1:
                dead += 1
            else: 
                hosp += 1
    d.append(dead) 
    h.append(hosp)

print(d)
print(h)
print(len(d))
print(len(h))

df5['Yemen_Dead'] = d
df5['Yemen_Hosp'] = h

#Aleppo

df = pd.read_csv('aleppo_final.csv')

df

d=[]
h=[]
for j in l:
    dead=0
    hosp=0
    for i,r in df.iterrows():
        if r[j]==1:
            if r['DEATH']==1:
                dead += 1
            else: 
                hosp += 1
    d.append(dead) 
    h.append(hosp)

df5['Aleppo_Dead'] = d
df5['Aleppo_Hosp'] = h

df5

#Nairobi

df = pd.read_csv('nairobi_final.csv')

df

d=[]
h=[]
for j in l:
    dead=0
    hosp=0
    for i,r in df.iterrows():
        if r[j]==1:
            if r['DEATH']==1:
                dead += 1
            else: 
                hosp += 1
    d.append(dead) 
    h.append(hosp)

print(d)
print(h)
print(len(d))
print(len(h))

df5['Nairobi_Dead'] = d
df5['Nairobi_Hosp'] = h

df5

#Karachi

df = pd.read_csv('karachi_final.csv')

df

d=[]
h=[]
for j in l:
    dead=0
    hosp=0
    for i,r in df.iterrows():
        if r[j]==1:
            if r['DEATH']==1:
                dead += 1
            else: 
                hosp += 1
    d.append(dead) 
    h.append(hosp)

df5['Karachi_Dead'] = d
df5['Karachi_Hosp'] = h

df5

#Saudi Arabia:

df = pd.read_csv('saudi_arabia_final.csv')

df

d=[]
h=[]
for j in l:
    dead=0
    hosp=0
    for i,r in df.iterrows():
        if r[j]==1:
            if r['DEATH']==1:
                dead += 1
            else: 
                hosp += 1
    d.append(dead) 
    h.append(hosp)

df5['Saudiarabia_Dead'] = d
df5['Saudiarabia_Hosp'] = h

df5

df5.columns

df5['All_Hosp'] = df5['Iran_Hosp'] + df5['Colombia_Hosp'] + df5['Lebanon_Hosp'] + df5['Thailand_Hosp'] + df5['Turkey_Hosp'] + df5['Venezuela_Hosp'] +df5['Yemen_Hosp'] + df5['Aleppo_Hosp'] + \
df5['Nairobi_Hosp'] + df5['Karachi_Hosp'] + df5['Saudiarabia_Hosp']

df5


df5['All_Dead'] = df5['Iran_Dead'] + df5['Colombia_Dead'] + df5['Lebanon_Dead'] + df5['Thailand_Dead'] + df5['Turkey_Dead'] + df5['Venezuela_Dead'] +df5['Yemen_Dead'] + df5['Aleppo_Dead'] + \
df5['Nairobi_Dead'] + df5['Karachi_Dead'] + df5['Saudiarabia_Dead']

df5

df5.to_csv('BubbleChartData.csv')

