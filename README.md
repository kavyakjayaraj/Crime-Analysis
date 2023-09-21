# bigdata_project

"In this project, I am going to analyze crime data in India. Here, we used big data tools such as Hadoop, Hive, Spark, and Matplotlib. The data downloaded from Kaggle is loaded into Hadoop and then into a Hive table. Analysis is performed on this Hive table. In Hive, we used the SerDe method, as well as group by and order by functions for filtering the data. The output obtained is plotted in a bar graph using Matplotlib in pyspark."
![collage](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/ace96c18-10d4-4a41-8432-06a2837695dc)

steps:

1. The dataset is downloaded from Kaggle and loaded into HDFS.
   
![1 createfolderinhadoop](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/ae86e4a0-a24a-4c32-80e2-5b6f447ad7ed)
![2 dataloaded in hadoop](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/41c8a5cb-a885-45b1-8558-38739a743846)

2. From HDFS, data is loaded into Hive.
   
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

   c) Using the group by and order by functions in Hive, the top 10 states with the highest number of cases recorded are filtered, and this result is loaded into a table.
   
          * 2016 Cases against Police Personnels
![1 total_cases police](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/4856a7d8-867c-40c9-9365-38ad928a52d4)


   




          




   
  
   


