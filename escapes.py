from pyspark.sql import SparkSession
spark=SparkSession.builder.appName('project').getOrCreate()
import matplotlib.pyplot as plt
# 2016 escapes from police custody

most_persons_escaped_in_2016=spark.read.csv('hdfs://localhost:9000//project/EscapesfromPoliceCustody/2016_escapes',inferSchema=True)
most_persons_escaped_in_2016=most_persons_escaped_in_2016.selectExpr('_c0 as s_no','_c1 as state_ut','_c2 as case_registered','_c3 as total_persons_escaped')
most_persons_escaped_in_2016.show()
most_persons_escaped_in_2016.toPandas().plot(kind='bar', x='state_ut', y='total_persons_escaped', figsize=(20, 10),color='r')
plt.xlabel("state")
plt.ylabel("count")
plt.title("2016 escapes")
plt.xticks(rotation=90)
plt.legend()
plt.show()

# 2017 escapes from police custody

most_persons_escaped_in_2017=spark.read.csv('hdfs://localhost:9000//project/EscapesfromPoliceCustody/2017_escapes/000000_0',inferSchema=True)
most_persons_escaped_in_2017=most_persons_escaped_in_2017.selectExpr('_c0 as s_no','_c1 as state_ut','_c2 as case_registered','_c3 as total_persons_escaped')
most_persons_escaped_in_2017.show()
most_persons_escaped_in_2017.toPandas().plot(kind='bar', x='state_ut', y='total_persons_escaped', figsize=(20, 10),color='r')
plt.xlabel("state")
plt.ylabel("count")
plt.title("2017 escapes")
plt.xticks(rotation=90)
plt.show()

#2018 escapes from police custody

most_persons_escaped_in_2018=spark.read.csv('hdfs://localhost:9000//project/EscapesfromPoliceCustody/2018_escapes/000000_0',inferSchema=True)
most_persons_escaped_in_2018=most_persons_escaped_in_2018.selectExpr('_c0 as s_no','_c1 as state_ut','_c2 as case_registered','_c3 as total_persons_escaped')
most_persons_escaped_in_2018.show()
most_persons_escaped_in_2018.toPandas().plot(kind='bar', x='state_ut', y='total_persons_escaped', figsize=(20, 10),color='r')
plt.xlabel("state")
plt.ylabel("count")
plt.title("2018 escapes")
plt.xticks(rotation=90)
plt.show()

# total no of escapes

total_no_of_escapes=spark.read.csv('hdfs://localhost:9000//project/EscapesfromPoliceCustody/total_no_of_escape/000000_0',inferSchema=True)
total_no_of_escapes=total_no_of_escapes.selectExpr('_c0 as s_no','_c1 as state_ut','_c2 as total_escapes')
total_no_of_escapes.show()
total_no_of_escapes.toPandas().plot(kind='bar', x='state_ut', y='total_escapes', figsize=(20, 10),color='r')
plt.xlabel("state")
plt.ylabel("count")
plt.title("total no of escapes")
plt.xticks(rotation=90)
plt.show()
