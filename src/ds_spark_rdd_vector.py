import os
import findspark
home = os.path.expanduser("~")
findspark.init(os.path.join(home,"code/s_201511079","spark-2.0.0-bin-hadoop2.6"))

import pyspark
myConf=pyspark.SparkConf()
spark = pyspark.sql.SparkSession.builder.master("local").appName("myApp").config(conf=myConf).config('spark.sql.warehouse.dir','file:///C:/Users/Eunda/code/s_201511079/data').getOrCreate()

documents = spark.sparkContext.textFile("data/ds_spark_wiki.txt")\
    .map(lambda line: line.split(" "))
from pyspark.mllib.feature import HashingTF

hashingTF = HashingTF()
htf = hashingTF.transform(documents)
htf.collect()