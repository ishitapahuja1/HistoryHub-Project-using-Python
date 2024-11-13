import pickle
import requests
import json
from random import randint
import datetime
import calendar
import pandas as pd

def fetchFactForDay(month, day):
    req='https://history.muffinlabs.com/date/'+ str(month) + "/" + str(day)

    r1 = requests.get(req)
    r1=r1.json()
    facts = r1['data']['Events']
    count = len(facts) - 1
    i = randint(0, count)
    factObject = facts[i]
    factText = factObject['text']
    factYear = factObject['year']
    formattedFact = 'On ' + calendar.month_name[month] + ' ' + str(day) + ' in ' + factYear + ', ' + factText
    return formattedFact,factYear

result_dict={}
for day in range (1,32):
    if day%10==0:
        print("Completed writing historical events till",day)
    for month in range(1,13):
        for year in range (1,2): 
                try:
                    fact,factYear=fetchFactForDay(month,day)
                    if fact is None:
                        pass
                    elif 'BC' in str(factYear) or 'AD' in str(factYear):
                        pass
                    else:
                        factYear=int(factYear)
                        date=datetime.datetime(factYear,month,day)
                        if date not in result_dict.keys():
                            result_dict[date]=fact
                except Exception as e:
                    pass
print('Done')

df=pd.DataFrame(result_dict.items())
df.columns=['date','event']
df['date']=pd.to_datetime(df['date'],errors = 'coerce')
df['month']=df['date'].dt.month
df['day']=df['date'].dt.day
df['year']=df['date'].dt.year
df.dropna(subset=['date'],inplace=True)

records=df[['day','month','year','event']].values.tolist()

f=open("Historical_Events.dat","wb")
pickle.dump(records,f)
print("Record writen in the File ...")
f.close()