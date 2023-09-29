 # bigdata_project

"In this project, I am going to analyze crime data in India. Here, we used big data tools such as Hadoop, Hive, Spark, and Matplotlib. The data downloaded from Kaggle is loaded into Hadoop and then into a Hive table. Analysis is performed on this Hive table. In Hive, we used the SerDe method, as well as group by and order by functions for filtering the data. The output obtained is plotted in a bar graph using Matplotlib in pyspark."
![collage](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/ace96c18-10d4-4a41-8432-06a2837695dc)

steps:

1. The dataset is downloaded from Kaggle and loaded into HDFS.
   
![1 createfolderinhadoop](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/ae86e4a0-a24a-4c32-80e2-5b6f447ad7ed)
![2 dataloaded in hadoop](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/41c8a5cb-a885-45b1-8558-38739a743846)

2. From HDFS, data is loaded into Hive by creating databases.

![Screenshot from 2023-09-24 00-03-34](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/9932391a-f27c-4409-8fa3-f011b2a2ba8a)
![2 data baseescapes_from_police_custody ](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/1fee5d80-a90d-4e32-a00d-e0f1141709f8)

   a) Using SerDe properties, data is loaded into a table by removing quotes.
   
       * 2016 Cases against Police Personnels
    
 ![1 create normal table](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/36c6820e-9158-4609-8cb3-03eb08a606d3)
 ![1 loaddatahdfs2016](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/a62218c7-4a2a-4e4a-8e3c-faa37ca15d1b)

        * 2017 Cases against Police Personnels
    
 ![2 createnormal table 2017](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/9c7898f9-cf86-4033-b189-50833971b2da)
 ![2 loaddatahdfs2017](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/b11c4f07-e888-479b-a940-71a50c797de7)

        * 2018 Cases against Police Personnels

 ![3 create normal table 2018](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/5f865551-c72d-4e61-b093-4d1edebd3ea0)
 ![3 loaddatahdfs2018](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/ac802f71-b88b-4698-bb63-31fd2a93b74a)

        * 2016 Escapes from Police Custody
        
 ![1 create normal table2016](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/2b4357e7-5a70-477d-842b-97afab052d3a)
 ![1 loaddatahdfs2016(1)](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/34642863-29a3-484a-9e87-081ef1ae17d0)
 
         * 2017 Escapes from Police Custody
         
 ![2 create normal table 2017](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/b4ba28b0-7202-498f-bb4c-8bf6b2273534)
 ![2 loaddatahdfs2017(1)](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/d7c00fe3-94ee-46ff-9151-ee1434222ac2)

         * 2018 Escapes from Police Custody
         
  ![3 create noraml table 2018](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/9070209c-b45d-48f9-aa34-76e69c69889b)
  ![3 loaddata hdfs 2018](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/e088fcf6-b941-423b-93b4-29c4ac664027)

   b) From this table, data is loaded into another table.
    
           * 2016 Cases against Police Personnels
           
![1 newtable created 2016](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/a2717f1f-3299-45d3-aaf9-bd70d3b7ada3)
![1 insert2016](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/40e12319-06c9-48a4-82cd-35b72491476d)

          * 2017 Cases against Police Personnels
          
![2 create newtable2017](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/f36ee291-b32b-466d-b8e9-68fc3c885f33)
![2 insert2017](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/c7cb4e27-7375-4488-a458-43a83facec87)

          * 2018 Cases against Police Personnels
          
![3 create new table 2018](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/53cdbf80-4866-47d6-b4e2-847b2b6a80fa)
![3 insert 2018 ](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/93031c92-c821-430c-b350-8acd36e223e2)

        * 2016 Escapes from Police Custody
        
![1 newtable2016](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/0001b5fa-80ac-4e44-9ee1-5913533004e0)
![1 insert 2016 ](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/3384900a-eea4-42f2-8402-3960aa6483ce)


        * 2017 Escapes from Police Custody
        
![2 2017 new table create](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/2942c6f4-4446-4508-a2a6-64317ee34cf1)
![2 insert 2017](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/80c684c6-564e-43ec-a69e-4d7200168b4a)


        * 2018 Escapes from Police Custody

![3 create newtable 2018](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/4d97ed7a-37b2-4c4e-8e10-6697f7ca94c9)
![3 insert 2018](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/c391129a-3895-4108-a1a8-c2de76af1663)

   c) Using the group by and order by functions in Hive, the top 10 states with the highest number of cases for three years(2016,2017,2018) recorded are filtered, and this result is loaded into a table.
   
   Total number of cases in three years(2016,2017,2018)
   
![1 create 3 table 2016(2)](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/67037ce6-0e19-464a-abc0-b759cae65706)
![1 3 table insert](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/5665ecdc-fcdb-464f-a53d-09eb2f3cd686)
![2  3 table insert](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/911196b0-01c0-4bc2-a9a4-09b57ad0fe42)
![3 3 insert table](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/1d04b018-20de-4234-a971-b9ecf878898c)

![1 total_cases police](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/4856a7d8-867c-40c9-9365-38ad928a52d4)
![Screenshot from 2023-09-24 00-16-01](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/ca4af555-b8cc-48ee-95a1-1dab77bd62e6)
![Screenshot from 2023-09-23 22-55-17](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/f9ff81a2-7f2e-486a-a82e-20783aa44625)

   Total number of persons escaped in three years(2016,2017,2018)
   
![1 create 3 table 2016(1)](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/2fdad2b8-26ea-4a9c-bb40-3cfa76348e27)
![1 insert 3 tables2016](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/2932a40d-8e84-4a90-9f4c-8703c66e81cf)
![2 insert 3 tables2017](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/b4b1d6c9-b5fe-4da2-aec6-0e5c15950792)
![3 insert 3 table 2018](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/343e3231-db06-479f-ae5b-b7750acaaced)



   
d)From each table with cases in the years 2016, 2017, and 2018, the top 10 states with the highest number of cases reported in each year are filtered.

       * 2016 Cases against Police Personnels
       
![1 add table to new table2016(1)](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/c0fcbc9b-c3a5-4350-b744-483d27fc5cfa)
![Screenshot from 2023-09-23 23-23-44](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/53564737-303d-44b8-ab7b-eb5708200ae5)
![Screenshot from 2023-09-24 15-22-07](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/1a0ab155-50a6-43cb-a62d-79c8912a18a0)

          * 2017 Cases against Police Personnels

![2 add table newtable 2017](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/d288ee12-48bb-488a-9424-8c7f3c77838d)
![Screenshot from 2023-09-23 23-28-20](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/10c889c9-7c9e-4fa0-a10f-1661f7819f80)
![Screenshot from 2023-09-24 15-24-46](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/b4fdd6af-2fa9-4379-927a-e7f609be07b5)

          * 2018 Cases against Police Personnels

![3 add table 2018](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/7892dd13-ab33-46eb-9eb6-aac1afa75e01)
![Screenshot from 2023-09-23 23-28-59](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/35f6a93c-ad25-4fb0-931b-a85ef6bfd813)
![Screenshot from 2023-09-24 15-25-28](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/9a02edae-d79f-4daa-86f0-f54312442581)


e)The results are plotted using matplotlib in pyspark.
 
The files regarding the cases against police personnel, escapes from police custody, and victims of rape are mentioned above as cases.py, escapes.py, and victims.py respectively.




       




   




          




   
  
   


