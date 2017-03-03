02/2017  
Dataquest : Data Analyst Path  
Step 3: The Command Line  
SubStep : Command Line: Beginner : Challenge: Navigating The File System
samedi, 25. février 2017 05:59 

---
#1: Exploring The File System
In this challenge, you'll practice the basics of the command line by working with files in the filesystem. Often times working in a command line environment is faster than using a GUI or writing a Python program just to accomplish a specific task. In this challenge, you'll be interacting with a directory of datasets that are used in other missions at Dataquest.  

To start things off, get familiar with the file system.  


##Instructions  
 - Display the current directory.
 - Display the list of files in the current directory along with each file's metadata. Use the appropriate flag so the file permissions, file size, etc. are displayed.
 
```bash
pwd
ls -l
```

####Results: 
```bash  
/home/dq$ pwd                                                                   
/home/dq                                                                        
/home/dq$ ls -l                                                                 
total 708                                                                       
-rwxrwxrwx 1 dq dq   1030 Feb 25 17:04 crime_rates.json                         
-rwxrwxrwx 1 dq dq  25478 Feb 25 17:04 forest_fires.cssv                        
-rwxrwxrwx 1 dq dq 520300 Feb 25 17:04 legislators                              
-rwxrwxrwx 1 dq dq  54145 Feb 25 17:04 nfl.csv                                  
-rwxrwxrwx 1 dq dq 108283 Feb 25 17:04 titanic_survival.csv 
```


---
#2: Moving Problematic Files To A Separate Folder
There are 5 datasets in your home directory and while all datasets are actually CSV formatted and should have the .csv file extension, 3 files have issues with their file extensions. Let's move the problematic files into their own directory.  


##Instructions  
 - Move all the files that don't have .csv as the file extension to a new folder called problematic.
 
```bash
mkdir problematic
mv crime_rates.json problematic
mv forest_fires.cssv problematic
mv legislators problematic
```

####Results: 
```bash  
/home/dq$ man mv                                                                
/home/dq$ mkdir problematic                                                     
/home/dq$ mv crime_rates.json problematic                                       
/home/dq$ mv forest_fires.cssv problematic                                      
/home/dq$ mv legislators problematic 
```



---
#3: Fixing File Extensions
Now that you've quarantined the files with problematic file extensions into their own folder, let's fix the file extensions.  

##Instructions  
 - Change all of the file extensions of the files in the problematic folder to .csv.
 - Display the files in problematic to confirm.
 
```bash
cd problematic
mv crime_rates.json crime_rates.csv
mv forest_fires.cssv forest_fires.csv
mv legislators legislators.csv
```

####Results: 
```bash  
/home/dq$ cd problematic                                                        
/home/dq/problematic$ ls -l                                                     
total 544                                                                       
-rwxrwxrwx 1 dq dq   1030 Feb 25 17:04 crime_rates.json                         
-rwxrwxrwx 1 dq dq  25478 Feb 25 17:04 forest_fires.cssv                        
-rwxrwxrwx 1 dq dq 520300 Feb 25 17:04 legislators                              
/home/dq/problematic$ mv ^C                                                     
/home/dq/problematic$ mv crime_rates.json crime_rates.csv                       
/home/dq/problematic$ mv forest_fires.cssv forest_fires.csv                     
/home/dq/problematic$ mv legislators legislators.csv                            
/home/dq/problematic$ ls -l                                                     
total 544                                                                       
-rwxrwxrwx 1 dq dq   1030 Feb 25 17:04 crime_rates.csv                          
-rwxrwxrwx 1 dq dq  25478 Feb 25 17:04 forest_fires.csv                         
-rwxrwxrwx 1 dq dq 520300 Feb 25 17:04 legislators.csv 
```



---
#4: Consolidating Files
Now that the files are fixed, consolidate all of the CSV files into one folder.  

##Instructions  
 - Move the remaining files into the problematic folder.
 - Rename the folder problematic to csv_datasets.
 
```bash
mv nfl.csv problematic
mv titanic_survival.csv problematic
mv problematic csv_datasets
```

####Results: 
```bash  
/home/dq/problematic$ cd ..                                                     
/home/dq$ ls                                                                    
nfl.csv  problematic  titanic_survival.csv                                      
/home/dq$ mv nfl.csv problematic                                                
/home/dq$ mv titanic_survival.csv problematic                                   
/home/dq$ cd problematic                                                        
/home/dq/problematic$ ls                                                        
crime_rates.csv   legislators.csv  titanic_survival.csv                         
forest_fires.csv  nfl.csv                                                       
/home/dq/problematic$ cd ..                                                     
/home/dq$ mv problematic csv_datasets                                           
/home/dq$ ls                                                                    
csv_datasets                                                                    
/home/dq$ cd csv_datasets                                                       
/home/dq/csv_datasets$ ls -l                                                    
total 708                                                                       
-rwxrwxrwx 1 dq dq   1030 Feb 25 17:04 crime_rates.csv                          
-rwxrwxrwx 1 dq dq  25478 Feb 25 17:04 forest_fires.csv                         
-rwxrwxrwx 1 dq dq 520300 Feb 25 17:04 legislators.csv                          
-rwxrwxrwx 1 dq dq  54145 Feb 25 17:04 nfl.csv                                  
-rwxrwxrwx 1 dq dq 108283 Feb 25 17:04 titanic_survival.csv
```



---
#5: Restricting Permissions
Let's now change the permissions of these files so nobody else can mess with the file extensions!  

##Instructions  

Change the file permissions for all of the CSV files in the csv_datasets folder to:  

- owner: read, write, and execute.
- group: read.
- everyone: no permissions.

Display the list of files in the csv_datasets directory to confirm the permissions.  
 
```bash
chmod 0740 *
```

####Results: 
```bash  
/home/dq/csv_datasets$ chmod 0740 *                                             
/home/dq/csv_datasets$ ls -l                                                    
total 708                                                                       
-rwxr----- 1 dq dq   1030 Feb 25 17:04 crime_rates.csv                          
-rwxr----- 1 dq dq  25478 Feb 25 17:04 forest_fires.csv                         
-rwxr----- 1 dq dq 520300 Feb 25 17:04 legislators.csv                          
-rwxr----- 1 dq dq  54145 Feb 25 17:04 nfl.csv                                  
-rwxr----- 1 dq dq 108283 Feb 25 17:04 titanic_survival.csv 
```



---
#6: Next Steps
In this challenge, you practiced working with the file system and managing file permissions using the command line. Solidifying these basics will prepare you well for the next mission, where we'll explore how to work with variables and programs.  