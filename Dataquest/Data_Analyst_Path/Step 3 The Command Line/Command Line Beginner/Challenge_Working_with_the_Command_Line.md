02/2017  
Dataquest : Data Analyst Path  
Step 3: The Command Line  
SubStep : Command Line: Beginner : Challenge: Working with the Command Line  
samedi, 25. février 2017 06:54 

---
#1: Command Line Python
In the past few missions, you learned how to navigate the filesystem, create and modify files, and work with Python on the command line. You learned that it isn't enough to just know how to program in Python -- you also have to know how to modify and execute Python programs on your computer.

In this challenge, you'll pull all of the concepts from the past few missions together to create and run a Python script on the command line. Here's a rough outline of what you'll do:

- Create a Python script.
- Create a virtual environment.
- Change file permissions.
- Execute a Python script from the command line.


##Instructions  
- Familiarize yourself with the current folder.
	- Change out of the current directory, then back in.
 	- Print the path of the current folder to the standard output.
 
```bash  
pwd
```

####Results: 

```bash  
/home/dq$ pwd                                                                   
/home/dq
```



---
#2: Creating A Script
You'll now be able to create a Python script in the current folder.  


##Instructions  
 - Create a Python script that takes in a command line argument and prints it.
	 - Use output redirection or a command line editor to create a Python script called script.py in the /home/dq/ folder.
	 - Add code to the file that will read the first command line argument passed in and print it out.
 
```bash  
nano script.py
python script.py "test"
```

####Results: 

```bash  
/home/dq$ nano script.py                                                        
/home/dq$ python script.py "test"                                               
test
```



---
#3: Change File Permissions
You don't want just anyone to be able to run your script. By editing permissions, you can make it so that only you can run the script.  


##Instructions  
 - Edit the file permissions for script.py so that only the current user can access it.
	- Assign read, write, and execute permissions to the current user.
	- Assign no permissions to your group, or other users.
 
```bash  
chmod 0700 script.py
```

####Results: 

```bash  
/home/dq$ chmod 0700 script.py                                                  
/home/dq$ ls -l                                                                 
total 4                                                                         
-rwx------ 1 dq dq 58 Feb 25 21:45 script.py 
```




---
#4: Create A Virtualenv
You'll want to isolate the Python environment that your script is in by creating a virtual environment. This will allow you to install Python packages with the versions that the script expects.  


##Instructions  
 - Create a Python 3 virtualenv called script.
 - Activate the script virtualenv.
 
```bash  
virtualenv -p /usr/bin/python3 python3
source python3/bin/activate
```

####Results: 

```bash  
/home/dq$ virtualenv -p /usr/bin/python3 python3                                
Running virtualenv with interpreter /usr/bin/python3                            
Using base prefix '/usr'                                                        
New python executable in /home/dq/python3/bin/python3                           
Also creating executable in /home/dq/python3/bin/python                         
Installing setuptools, pip, wheel...done.
/home/dq$ source python3/bin/activate                                           
(python3) /home/dq$
```



---
#5: Move The Script
Moving the script to its own folder will keep your home directory clean, and enable you to more easily tell which program is which if you create more scripts.  

##Instructions  
 - Create a folder called printer in the current user's home directory (/home/dq/).
 - Move script.py into the printer folder.
 
```bash  
mkdir printer
mv script.py printer/script.py
```

####Results: 

```bash  
(python3) /home/dq$ mkdir printer                                               
(python3) /home/dq$ mv script.py printer/script.py  
```



---
#6: Execute The Script
Now you're ready to execute the Python script.  


##Instructions  
 - Change the current directory to be the printer directory.
 - Execute script.py, and pass in the string I'm so good at challenges!.
 
```bash  
cd printer
python3 script.py "I'm so good at challenges!"
```

####Results: 

```bash  
(python3) /home/dq$ cd printer                                                  
(python3) /home/dq/printer$ script.py "I'm so good at challenges!"              
bash: script.py: command not found                                              
(python3) /home/dq/printer$ python3 script.py "I'm so good at challenges!"      
I'm so good at challenges! 
```


