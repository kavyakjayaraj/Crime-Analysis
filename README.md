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
![Screenshot from 2023-09-30 19-51-16](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/5c38f10e-84c8-43b8-aa68-73c4ac617a05)

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

        * 2016 Victims of Rape
   The datas are already in integer datatype so serDe property is not used instead table is directly loaded in HDFS .(2016&2017 victims of rape)
   
   ![1 loaddatahsdfs2016](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/f8439b0b-9028-46de-8cfd-5460966b686c)
   
        * 2017 Victims of Rape
        
   ![2 loaddatahdfs2017(2)](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/e7661454-7580-4df5-9619-cbcfd417e2c3)
   
        * 2018 Victims of Rape
        
   ![3 create normal table2018 ](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/e54a807d-27cd-4afe-84da-5a03efb138f2)
   ![3 loaddatafromhdfs2018](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/3e71b990-e02b-44a5-a30b-3c0f6fed62b5)

  
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

        * 2016 Victims of Rape
        
![1 create table vit2016(2)](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/7c790857-f29e-442b-9d76-d53a0c440cfa)

        * 2017 Victims of Rape
        
![2 create table vit 2017](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/9618c952-676e-4630-8cd4-34d377dde02b)

        * 2018 Victims of Rape
        
![3 create newtable2018](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/5ea163e0-9468-4413-b342-389c8fffb6ea)
![3 insert tble2018](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/9439d5dd-db17-4e6a-9d0c-72a55fdb8b0e)

   c) Using the group by and order by functions in Hive, the top 10 states with the highest number of cases recorded ,the most persons escaped and the highest number of rape victims for three years(2016,2017,2018)are filtered, and this result is loaded into a table.
   
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

![Screenshot from 2023-09-29 21-01-17](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/fb40d31a-3c1b-4ebf-90d2-4651a35bf9d7)
![Screenshot from 2023-09-29 21-06-31](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/b3a1cca1-ffe0-4157-831b-a843044fac7b)
![Screenshot from 2023-09-29 21-10-53](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/46a9eeeb-fa5e-4d4c-86e7-a4be8a9f252a)

Total number of rape victims in three years(2016,2017,2018)

![1 create 3 table 2016(2)](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/b934ca77-fc0c-4bbd-8349-243d4d8eb7ba)
![1 insert 3 table 2016](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/e73541f0-6770-4142-a743-3bcb7895d35c)
![2 insert 3 table 2017](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/ce5cb727-5d54-43fa-869a-72a94cf58b64)
![3 insert 3 table 2018(1)](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/d58a5d64-f406-434b-be30-7c2076caee9e)

![1 victims_cases create table](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/1b2e83a7-d308-476b-8bcc-7a200ba8c0bc)
![1 victims total rape victims](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/101238e1-5f49-4ad5-8c58-755a523bf0cc)
![1  total_rape _ victims insert hdfs](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/d5cf932f-7571-4388-9a94-b80565fa97a6)

d)From each table containing cases,escapes and victims for the years 2016, 2017, and 2018, the top 10 states with the highest number of cases reported,the most persons escaped and highest number of rape victims in each year are filtered.

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

        * 2016 Escapes from Police Custody
        
![Screenshot from 2023-09-29 21-31-16](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/5b456733-d78f-4dbf-a1a0-102c4256fb45)
![Screenshot from 2023-09-29 21-51-36](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/a0603066-1205-4470-a04f-60839d21afef)
![Screenshot from 2023-09-29 22-03-04](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/f64426af-31f5-45fc-9830-5ce6f5fdc9f3)

        * 2017 Escapes from Police Custody
        
![Screenshot from 2023-09-29 22-06-34](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/7f8f075f-1723-49f8-a68a-fe7473deed1c)
![Screenshot from 2023-09-29 22-08-01](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/8982a8fe-0013-47c6-bd9a-52c27a8f5878)
![Screenshot from 2023-09-29 22-09-21](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/44a061b4-a551-45d6-aea1-92981b1eb771)

        * 2018 Escapes from Police Custody

![Screenshot from 2023-09-29 22-11-25](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/60ee789b-2019-49be-a939-e3e6e2f89338)
![Screenshot from 2023-09-29 22-12-37](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/866008c5-6496-4820-88dd-e1e7fe191811)
![Screenshot from 2023-09-29 22-14-19](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/c28004be-4aeb-4a90-83f0-d30f1f33a550)

        * 2016 Victims of Rape
        
![Screenshot from 2023-09-30 17-20-27](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/da3b3d40-aa2c-456e-89ea-0ab6d43ca16b)
![Screenshot from 2023-09-30 17-23-16](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/5eccd45a-8eae-4656-84cf-f3bef1a05c95)
![Screenshot from 2023-09-30 17-26-14](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/b37bcf8e-788d-4aa4-b5dd-165f2e1a6fd2)

        * 2017 Victims of Rape
        
![Screenshot from 2023-09-30 17-27-59](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/e5e8620e-0c78-42bc-b7ec-c297690984f6)
![Screenshot from 2023-09-30 17-29-01](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/d102007f-5601-4fd9-8377-915850f5d670)
![Screenshot from 2023-09-30 17-29-53](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/d56a838d-8c62-42e9-8fb4-33a6913e7fb9)

        * 2018 Victims of Rape
        
![Screenshot from 2023-09-30 17-31-11](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/f88e549a-cec8-4fd6-b3ab-67c33108fccc)
![Screenshot from 2023-09-30 17-31-54](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/822c8ce9-0054-435b-8290-967e2fb24581)
![Screenshot from 2023-09-30 17-32-54](https://github.com/kavyakjayaraj/bigdata_project/assets/127305603/801a68df-a0e6-472c-b0a9-5d75eb68410e)

e)The results are plotted using matplotlib in pyspark.
 
The files regarding the cases against police personnel, escapes from police custody, and victims of rape are mentioned above as cases.py, escapes.py, and victims.py respectively.




       




   




          




   
  
   


