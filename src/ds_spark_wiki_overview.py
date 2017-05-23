import os
import sys 
import matplotlib.pyplot as plt

os.environ["SPARK_HOME"]="C:\\Users\\Eunda\\code\\s_201511079\\spark-2.0.0-bin-hadoop2.6"
os.environ["PYLIB"]=os.path.join(os.environ["SPARK_HOME"],'python','lib')
sys.path.insert(0,os.path.join(os.environ["PYLIB"],'py4j-0.10.1-src.zip'))
sys.path.insert(0,os.path.join(os.environ["PYLIB"],'pyspark.zip'))

import pyspark
myConf      = pyspark.SparkConf() 
spark = pyspark.sql.SparkSession.builder.master("local").appName("myApp").config(conf=myConf).config('spark.sql.warehouse.dir','file:///C:/Users/Eunda/code/s_201511079/data').getOrCreate()
filepath    = os.path.join('data','wiki.txt') 
myRdd         = spark.sparkContext.textFile(filepath) 
wc2         = myRdd.flatMap(lambda x:x.split()).map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y).map(lambda x:(x[1],x[0])).sortByKey(False).take(30) 
count       = map(lambda x: x[0],wc2) 
word        = map(lambda x: x[1],wc2) 
plt.barh(range(len(count)),count,color='blue') 
plt.yticks(range(len(count)), word) 
plt.show() 