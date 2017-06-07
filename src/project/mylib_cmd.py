import os
def sayHello():
    print "hello"
def sayHello2():
    print "hello 2"
def getKey(keyPath):
    d=dict()
    keyPath=os.path.join('key.properties')
    f=open(keyPath,'r')
    for line in f.readlines():
        row=line.split('=')
        row0=row[0]
        d[row[0]]=row[1].strip()
    return d