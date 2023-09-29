from pyspark.sql import SparkSession
spark=SparkSession.builder.appName('project').getOrCreate()
# 2016 criminal cases

most_10_criminal_cases_in_2016=spark.read.csv('hdfs://localhost:9000//project/CasesagainstPolicePersonnels/2016_cases/000000_0',inferSchema=True)
most_10_criminal_cases_in_2016=most_10_criminal_cases_in_2016.selectExpr('_c0 as s_no','_c1 as category','_c2 as state_ut','_c3 as total_criminal_cases')
most_10_criminal_cases_in_2016.show()

import matplotlib.pyplot as plt
most_10_criminal_cases_in_2016.toPandas().plot(kind='bar', x='state_ut', y='total_criminal_cases', figsize=(20, 10))
plt.xlabel("state")
plt.ylabel("count")
plt.title("2016 cases")
plt.xticks(rotation=90)
plt.show()

# 2017 criminal cases

most_10_criminal_cases_in_2017=spark.read.csv('hdfs://localhost:9000//project/CasesagainstPolicePersonnels/2017_cases/000000_0',inferSchema=True)
most_10_criminal_cases_in_2017 = most_10_criminal_cases_in_2017.selectExpr('_c0 AS s_no','_c1 AS category','_c2 AS state_ut','_c3 AS total_criminal_cases')
most_10_criminal_cases_in_2017.show()

import matplotlib.pyplot as plt
most_10_criminal_cases_in_2017.toPandas().plot(kind='bar', x='state_ut', y='total_criminal_cases', figsize=(20, 10))
plt.xlabel("state")
plt.ylabel("count")
plt.title("2017 cases")
plt.xticks(rotation=90)
plt.legend()
plt.show()

# 2018 criminal cases

most_10_criminal_cases_in_2018=spark.read.csv('hdfs://localhost:9000//project/CasesagainstPolicePersonnels/2018_cases/000000_0',inferSchema=True)
most_10_criminal_cases_in_2018=most_10_criminal_cases_in_2018.selectExpr('_c0 as s_no','_c1 as category','_c2 as state_ut','_c3 as total_criminal_cases')
most_10_criminal_cases_in_2018.show()

import matplotlib.pyplot as plt

most_10_criminal_cases_in_2018.toPandas().plot(kind='bar', x='state_ut', y='total_criminal_cases', figsize=(20, 10))
plt.xlabel("state")
plt.ylabel("count")
plt.title("2018 cases")
plt.xticks(rotation=90)
plt.show()

# total no of cases

total_no_of_cases=spark.read.csv('hdfs://localhost:9000//project/CasesagainstPolicePersonnels/total_no_of_cases',inferSchema=True)
total_no_of_cases=total_no_of_cases.selectExpr('_c0 as s_no','_c1 as state_ut','_c2 as total_cases')
total_no_of_cases.show()

import matplotlib.pyplot as plt

total_no_of_cases.toPandas().plot(kind='bar', x='state_ut', y='total_cases', figsize=(20, 10))
plt.xlabel("state")
plt.ylabel("count")
plt.title("total no of cases")
plt.xticks(rotation=90)
plt.show()








