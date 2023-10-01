from pyspark.sql import SparkSession
spark=SparkSession.builder.appName('project').getOrCreate()
import matplotlib.pyplot as plt
# 2016 rape victims

most_rape_victims_in_2016=spark.read.csv('hdfs://localhost:9000//project/VictimsofRape/2016_victims/000000_0',inferSchema=True)
most_rape_victims_in_2016=most_rape_victims_in_2016.selectExpr('_c0 as s_no','_c1 as state_ut','_c2 as case_reported','_c3 as total_rape_victims')
most_rape_victims_in_2016.show()
most_rape_victims_in_2016.toPandas().plot(kind='bar', x='state_ut', y='total_rape_victims', figsize=(20, 10),color='r')
plt.xlabel("state")
plt.ylabel("count")
plt.title("2016 victims")
plt.xticks(rotation=90)
plt.show()

# 2017 rape victims

most_rape_victims_in_2017=spark.read.csv('hdfs://localhost:9000//project/VictimsofRape/2017_victims/000000_0',inferSchema=True)
most_rape_victims_in_2017=most_rape_victims_in_2017.selectExpr('_c0 as s_no','_c1 as state_ut','_c2 as case_reported','_c3 as total_rape_victims')
most_rape_victims_in_2017.show()
most_rape_victims_in_2017.toPandas().plot(kind='bar', x='state_ut', y='total_rape_victims', figsize=(20, 10),color='r')
plt.xlabel("state")
plt.ylabel("count")
plt.title("2017 victims")
plt.xticks(rotation=90)
plt.show()

# 2018 rape victims

most_rape_victims_in_2018=spark.read.csv('hdfs://localhost:9000//project/VictimsofRape/2018_victims/000000_0',inferSchema=True)
most_rape_victims_in_2018=most_rape_victims_in_2018.selectExpr('_c0 as s_no','_c1 as state_ut','_c2 as case_reported','_c3 as total_rape_victims')
most_rape_victims_in_2018.show()
most_rape_victims_in_2018.toPandas().plot(kind='bar', x='state_ut', y='total_rape_victims', figsize=(20, 10),color='r')
plt.xlabel("state")
plt.ylabel("count")
plt.title("2018 victims")
plt.xticks(rotation=90)
plt.show()

# total rape victims

total_rape_victims=spark.read.csv('hdfs://localhost:9000//project/VictimsofRape/total_rape_victims/000000_0',inferSchema=True)
total_rape_victims=total_rape_victims.selectExpr('_c0 as s_no','_c1 as state_ut','_c2 as total_rape_victims')
total_rape_victims.show()
total_rape_victims.toPandas().plot(kind='bar', x='state_ut', y='total_rape_victims', figsize=(20, 10),color='r')
plt.xlabel("state")
plt.ylabel("count")
plt.title("total rape victims")
plt.xticks(rotation=90)
plt.show()
