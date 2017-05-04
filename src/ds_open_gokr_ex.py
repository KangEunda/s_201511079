
# coding: utf-8
import os
import requests
import urlparse
import urllib
import mylib

def doIt():
    SERVICE='ArpltnInforInqireSvc'
    OPERATION_NAME='getMinuDustFrcstDspth'
    params1=SERVICE+'/'+OPERATION_NAME
    
    _d=dict()
    _d['dataTerm']='month'
    params2 = urllib.urlencode(_d)

    keyPath=os.path.join(os.getcwd(),'src', 'key.properties')
    key=mylib.getKey(keyPath)
    keygokr=key['gokr'] 
    params=params1+'?'+'serviceKey='+keygokr+'&'+params2
    
    _url='http://openapi.airkorea.or.kr/openapi/services/rest'
    url=_url+'/'+params

    data=requests.get(url).text
    print data
    


doIt()