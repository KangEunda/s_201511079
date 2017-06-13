# coding: utf-8
import os
import mylib_cmd
import urlparse
import requests
import re
import json
import io
import pymongo
from pymongo import MongoClient

mydict = dict()
client = MongoClient('localhost:27017')
db=client.taxiDB
p={"MOST_TAXI_OFF_TIME":mydict}


print u'<요일별 택시 최대 하차 시간 및 횟수 at 상명대>'
print '--------------------------------------------------------------------------------------'
keyPath=os.path.join(os.getcwd(),'key.properties')
key=mylib_cmd.getKey(keyPath)
KEY=str(key['dataseoul'])
TYPE='xml'
SERVICE='ListTaxiDrivingDataset'
START_INDEX=str(1)
END_INDEX=str(100)
X_PART=str(126.954904)
Y_PART=str(37.601767)


uday=[u'월',u'화',u'수',u'목',u'금']
day = 2
while day<=6 :
    DAY = str(day)
    lst=[]
    max=0
    mydict['day'] = day
    for time in range(17,41):
        TIME=str(time)
        final=0
        for w in (-1, 1, 2, 3):
            WEATHER=str(w)
            params=KEY+'/'+TYPE+'/'+SERVICE+'/'+START_INDEX+'/'+END_INDEX+'/'+X_PART+'/'+Y_PART+'/'+DAY+'/'+TIME+'/'+WEATHER

            _url = 'http://openAPI.seoul.go.kr:8088/'
            url=urlparse.urljoin(_url, params)

            data=requests.get(url).text
            p = re.compile('<CNT_OFF>(.+?)</CNT_OFF>')
            res=p.findall(data)
            sum=0
            for item in res:
                sum +=int(item)
            final += sum 
        lst.append(final)
        if(max < lst[time-17]):
            max = lst[time-17]
            maxtime=time
    if (maxtime%2 == 1):
        realtime=maxtime/2
        print uday[day-2],u'요일, 최대하차시간은',realtime,u'시 30분부터', realtime+1, u'시까지이며 1년간 총',max,u'대가 하차했습니다.'
    else :
        realtime=maxtime/2
        print uday[day-2],u'요일, 최대하차시간은',realtime,u'시부터', realtime, u'시 30분까지까지이며 1년간 총',max,u'대가 하차했습니다.'

    mydict['day']=day
    mydict['maxTime']=maxtime
    mydict['maxNum']=max
    
    json_file=open(os.path.join('project_mongo.json'),'w')
    json.dump(p,json_file)
    json_file.close()
    
    fp=open(os.path.join('project_mongo.json'),'r')
    data.fp.read()
    
    pjson=json.loads(data)
    
    db.taxiColletion.insert_one(pjson)
    results=db.taxiCollection.find()
    print results
    day += 1
    
