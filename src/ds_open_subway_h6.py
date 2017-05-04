import os
import requests
import mylib

def doIt():
    _url='http://openAPI.seoul.go.kr:8088'
    keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
    key=mylib.getKey(keyPath)
    _key=str(key['dataseoul'])
    _type='xml'
    _service='CardSubwayStatisticsService'
    _start_index=1
    _end_index=5
    _use_mon='201306'
    _maxIter=2
    _iter=0
    while _iter<_maxIter:
        _api=_url+'/'+_key+'/'+_type+'/'+_service+'/'+str(_start_index)+'/'+str(_end_index)+'/'+_use_mon
        response = requests.get(_api).text
        print response
        _start_index+=5
        _end_index+=5
        _iter+=1

if __name__=="__main__":
    doIt()