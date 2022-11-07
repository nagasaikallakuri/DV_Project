import pandas as pd
from datetime import date

dataset=pd.read_csv('./data/Yemen.csv')
Death_dataset = pd.read_csv('./data/Yemen-deaths.csv')

sym_dict = {
    "ache":"ache",       
    "abcess":"abscess",
    "abd":"abdomen",
    "abdomen":"abdomen",
    "abdominal":"abdomen",
    "abdmnal":"abdomen",
    "abdback":"abdomen",
    "ankle":"ankle",
    "assaulted":"assault",
    "assult":"assault",
    "bleeds":"bleeding",
    "blood":"bleeding",
    "bleed":"bleeding",
    "blurry":"blurred",
    "blurried":"blurred",
    "cough":"cough",
    "cardiac":"heart",
    "card":"heart",
    "cardio":"card",
    "defecit":"deficit",
    "difficulties":"difficulty",
    "diff":"difficulty",
    "disturbance":"disturb",
    "disturbancies":"disturb",
    "heart":"heart",
    "dizzy":"dizzy",
    "dizziness":"dizzy",
    "elev":"elevated",
    "eval":"evaluation",
    "facial":"face",
    "fever":"fever",
    "gen":"general",
    "generalized":"general",
    "giddiness":"dizzy",
    "handwrist":"handwrist",
    "headache":"headache",
    "headaches":"headache",
    "inj":"injury",
    "lac":"laceration",
    "l":"left",
    "lt":"left",
    "med":"medical",
    "migrane":"migraine",
    "migrain":"migraine",
    "neckback":"neck",
    "neck":"neck",
    "nec":"neck",
    "nos":"nose",
    "pain":"pain",
    "poss":"possible",
    "pregnant":"preg",
    "pregnancy":"preg",
    "r":"right",
    "rt":"right",
    "respiratory":"resp",
    "speach":"speech",
    "urinary":"urinate",
    "urinates":"urinate",
    "urination":"urinate",
    "urinating":"urinate",
    "vag":"vaginal",
    "visual":"vision",
    "vomit":"vomiting",
    "vomting":"vomiting",
    "vomitting":"vomiting",
    "vomiting":"vomiting",
    "winjury":"winjury",
    "sinusitis":"sinus",
    "head":"ache",
    "injury":"inj",
    "ears":"ear",
    "ear":"ear"
}

groups = {
    "ab":"abdominal pain",
    "abdmnal":"abdominal pain",
    "abdomen":"abdominal pain",
    "adb":"abdominal pain",
    "adbback":"abdominal pain",
    "addominal":"abdominal pain",
    "abdominal":"abdominal pain",
    "genital":"abdominal pain",
    "abscess":"abscess",
    "abcess":"abscess",
    "accident":"injury",
    "assault":"injury",
    "bite":"injury",
    "assaulted":"injury",
    "inj":"injury",
    "bleeding":"bleeding",
    "bled":"bleeding",
    "bleed":"bleeding",
    "bleeds":"bleeding",
    "blood":"bleeding",
    "epistaxis":"bleeding",
    "nosebleed":"bleeding",
    "ear" : "body pain",
    "ache":"body pain",
    "ankle":"body pain",
    "hurts":"body pain",
    "leg":"body pain",
    "neck":"body pain",
    "pain":"body pain",
    "pn":"body pain",
    "stomach":"body pain",
    "asthama":"breathing",
    "breathing":"breathing",
    "breath":"breathing",
    "resp":"breathing",
    "respira":"breathing",
    "wheezing":"breathing",
    "chest":"chest",
    "cold":"cough",
    "cough":"cough",
    "sinu":"cough",
    "sinus":"cough",
    "sore":"cough",
    "cramp":"cramp",
    "cramping":"cramp",
    "defecit":"deficit",
    "diab":"diabetic",
    "diarr":"diarrhea",
    "diarrhea":"diarrhea",
    "gastro":"diarrhea",
    "stool":"diarrhea",
    "dizz":"dizziness",
    "giddiness":"dizziness",
    "vertigo":"dizziness",
    "dizziness":"dizziness",
    "dizzy":"dizziness",
    "fatigue":"fatigue",
    "letharg":"fatigue",
    "lighthead":"fatigue",
    "seizure":"fatigue",
    "weak":"fatigue",
    "fever":"fever",
    "febril":"fever",
    "ill":"fever",
    "temp":"fever",
    "headache":"headache",
    "head":"headache",
    "headaches":"headache",
    "allerg":"infections",
    "allergy":"infections",
    "infections":"infections",
    "lac":"laceration",
    "migraine":"migraine",
    "migrain":"migraine",
    "migrane":"migraine",
    "contraction":"pregnant",
    "csection":"pregnant",
    "preg":"pregnant",
    "labor":"pregnant",
    "miscarria":"pregnant",
    "pregnancy":"pregnant",
    "pregnant":"pregnant",
    "spotting":"pregnant",
    "itch":"rash",
    "rash":"rash",
    "skin":"rash",
    "eczema":"rash",
    "hives":"rash",
    "urinate":"urinate",
    "urin":"urinate",
    "urinates":"urinate",
    "urinating":"urinate",
    "urine":"urinate",
    "vag":"vaginal",
    "vaginal":"vaginal",
    "blur":"vision",
    "obscur":"vision",
    "blurred":"vision",
    "blurried":"vision",
    "blurry":"vision",
    "eye":"vision",
    "visio":"vision",
    "vision":"vision",
    "visual":"vision",
    "vom":"vomiting",
    "vomiting":"vomiting",
    "nausea":"vomiting",
    "vomit":"vomiting",
    "diabetic":"diabetic",
    "injury":"injury",
    "heart":"Heart Problems",
    "laceration":"laceration",
    "nose":"cough",
    "speech":"Vocal Problems",
    "others":"others"
}

################################ Helper functions ################################

def death_Dict(row) :
    death_data[row['ID']]=row['DATE_OF_DEATH']

def spell_check(curr_syndrome) :
    if curr_syndrome in sym_dict:
        return sym_dict[curr_syndrome]
    else : 
        for substring in correct_val :
            if substring in curr_syndrome :
                return substring
    return curr_syndrome

def check_Group(word) :
    if word in groups :
        return groups[word]
    else :
        return "others"

def Syndrome_change(syndrome,check) :
    sym=syndrome
    sym=sym.replace(',',' ')
    sym=sym.replace('"',' ')
    sym=sym.replace('.',' ')
    sym=sym.lower()
    symp=sym.split()
    
    SYM_CORRECT=[]
    SYM_GROUP=set()
    for word in symp :
        z=spell_check(word)
        SYM_CORRECT.append(z) 
        
        g=check_Group(z)
        SYM_GROUP.add(g)
    
    if(len(SYM_GROUP)>1 and "others" in SYM_GROUP) :
        SYM_GROUP.remove("others")
    
    if check =="group" :
        return list(SYM_GROUP)
    elif check=="sym" :     
        return SYM_CORRECT 
    elif check in SYM_GROUP :
        return 1
    else :
        return 0

def Death_change(row,check)  :
    pid=row['PATIENT_ID']
    if check=="death" :
        if pid in death_data :
            return 1
        else :
            return 0
    if check=="death_date" :
        if pid in death_data :
            return death_data[pid]
        else :
            return "0-0-0"  

def Days_Alive(row ) :
    pid=row['PATIENT_ID']
    
    if pid in death_data :
        start =row['DATE']
        end = death_data[pid]
        s=start.split('-')
        e=end.split('-')
        first = date(int(s[2]), int(s[0]), int(s[1]))
        last = date(int(e[2]), int(e[0]), int(e[1]))
        delta = last - first
        return delta.days
    return 0

def age_grouper(row):
    age=row['AGE']
    if(age<20):
        group='R1'
    elif age<40:
        group='R2'
    elif age<60:
        group='R3'
    elif age<80:
        group='R4'
    else:
        group='R5'
    return group

################################ Helper functions end ################################

################################ Control flow begins ################################
death_data={}
Death_dataset.apply(death_Dict,axis=1)
df_data = dataset.iloc[:,:]
comp_data=df_data.copy(deep='True')

comp_data['COUNTRY']=["Yemen"]*len(comp_data)
comp_data['SYM_GROUP']=[[]]*len(comp_data)
comp_data['DEATH']=[0]*len(comp_data)
comp_data['DATE_OF_DEATH']=["0-0-0"]*len(comp_data)
comp_data['LIFE_SPAN']=["0-0-0"]*len(comp_data)
comp_data['AGE_GROUP']=['R']*len(comp_data)

correct_val =list(sym_dict.values())

for sym in set(groups.values()) :
    comp_data[sym]=[0]*len(comp_data)

comp_data['SYM_GROUP']= comp_data['SYNDROME'].apply(Syndrome_change,check="group")
comp_data['DEATH']= comp_data.apply(Death_change,check="death",axis=1)
comp_data['DATE_OF_DEATH']= comp_data.apply(Death_change,check="death_date",axis=1)
comp_data['LIFE_SPAN']= comp_data.apply(Days_Alive,axis=1)
comp_data['AGE_GROUP']= comp_data.apply(age_grouper,axis=1)

for sym in set(groups.values()) :
    comp_data[sym]= comp_data['SYNDROME'].apply(Syndrome_change,check=sym)

comp_data = comp_data.drop('USER_WARNING', 1)
comp_data.to_csv("./merged_data/yemen_final.csv",index=False)

#################################################################