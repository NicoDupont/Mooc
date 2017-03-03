02/2017  
Dataquest : Data Analyst Path  
Step 3: The Command Line  
SubStep : Command Line: Beginner : Command line basics

---
#1: Introduction  
Many people interact with a computer through a graphical user interface(GUI).   
A GUI looks like this:  
![desktop ui](https://dq-content.s3.amazonaws.com/P8qZfFC.jpg  "desktop ui")https://dq-content.s3.amazonaws.com/P8qZfFC.jpg

This is the desktop from a Mac. It has icons, and you can click on programs to launch them. Before GUIs were invented, the most common way to interact with a computer was through something called a command-line interface. It can also be called a shell or terminal. A command-line interface lets you switch between folders and launch programs by typing commands. A command-line interface is often faster and more powerful than a GUI for programming tasks.  

Virtually all programmers and data scientists make extensive use of the terminal, and knowing how to interact with it is a critical skill. Every operating system has a slightly different terminal, with different commands and syntax. Linux and OSX, because they're both based on an older operating system called Unix, both have very similar terminals. Windows isn't, so it has different commands. It's more common to use Linux and OSX for data science work, so our terminal missions will be using Linux. In particular, we'll be running Ubuntu 14.04.  

To the right is a terminal interface. The dollar sign is called the command prompt. Anything you type to the right of it is a shell command, and will be executed immediately when you hit enter.  

##Instructions  
 . Type pwd into the terminal to the right, and press the Enter key on your keyboard.  
 . This command returns the current directory and stands for print working directory.  
 
```bash
 pwd
```

####Results: 
```bash  
 /home/dq$ pwd                                                                   
/home/dq
```
---
#2: Filesystem  
When we typed pwd in the last screen, the terminal printed out what folder we were in. The terminal is built around being able to navigate and switch between directories. You've probably browsed through directories using a GUI, like Explorer in Windows, or Finder in OSX. The terminal lets you do the same thing, except you type a command instead of clicking on a folder name. Once you learn the terminal, navigating through folders is much faster with it than using a GUI.  

Files are stored in directories. Each directory can have subdirectories or files inside of it. Right now, we're in the dq folder. This is a subfolder of the home folder. Our folder path is /home/dq. home is a folder that exists at the root of the filesystem -- it isn't in any folders itself. We indicate that dq is in home folder by separating them with a forward slash -- home/dq. We indicate that home is at the root of the filesystem with the leading slash -- /home.  

A special directory is the root directory, or /. This will navigate to the root of the filesystem. If we think of our filesystem like a tree, it looks like this.  


/
|__home
    |
    |__dq
home is a folder at the root of the filesystem, and dq is a folder inside the home folder.  

We can use the cd command to switch directories. You can type cd / to switch to the root directory.  

##Instructions  
 . Type cd / to switch to the root directory.  
 
```bash
 /home/dq$ cd /                                                                  
```

####Results:
```bash  
 /home/dq$ pwd                                                                   
/home/dq
```



---
#3: Absolute Vs Relative Paths  
When you typed /, it switched to the root directory. Any path that starts with / is an absolute path. An absolute path is in relation to the root of the filesystem. No matter what folder you're in, typing cd /home/dq will switch to the dq folder, inside the home folder, which is at the root of the filesystem.  

On the other hand, relative paths are relative to the directory you're in. These don't start with a forward slash. If you're in the home folder, typing cd dq will move you to /home/dq. However, if you're in the root (/) of the filesystem, typing cd dq will cause an error because the dq folder doesn't exist at the root of the filesystem -- it's inside the home folder.  


##Instructions   
Type cd home to move into the home folder.
 . This is a relative path not an absolute path.
 . This works since the home folder is located in the root of the filesystem and you're currently in the root folder.
 
```bash
cd home
```

####Results:   
```bash
/home $
```

---
#4: Getting Back To The Dq Folder  
Now that we're in the home folder, let's navigate back to the /home/dq folder.   

##Instructions  
 . Type cd dq to get into the /home/dq folder.
 
```bash
cd dq
```

####Results: 
```bash  
/home/dq $
```


---
#5: Users  
Most popular operating systems have a concept of users. Users have certain permissions within the system, and can create their own files, and run their own programs. Users can restrict other users from accessing their files and running programs.  

Right now, we're logged in as a user called dq (short for Dataquest). We can check which user we are using the whoami command.  


##Instructions  
 . Type whoami to check your username.
 
```bash
whoami
```

####Results: 
```bash  
/home/dq$ whoami                                                                
dq
```


---
#6: The Home Directory
Every user has a home directory, where they can add files specific to their user. Every home directory is at /home. The home directory for dq is /home/dq. A shortcut for referring to the home directory is ~. Typing cd ~ will automatically take you to the current user's home directory.   


##Instructions  
 . Type cd / to switch to the root directory.
 . Then, type cd ~ to switch back to the home directory for dq.
 
```bash
cd /
cd ~
```

####Results:   
```bash
/home/dq$ cd /                                                                  
/$ cd ~                                                                         
/home/dq$                                                                       
```            



---
#7: Making A Directory  
We can create files and directories with the terminal. We'll explore making a directory first. We can make directories with the mkdir command. We just have to type mkdir test to make a directory called test. Note that rules about absolute and relative paths apply here, and in almost every command involving paths. If you type mkdir test it will make a directory called test in the current folder, because it's a relative path. If you type mkdir /home/dq/test it will make a folder called test inside the /home/dq folder, because it's an absolute path.  

##Instructions  
 . Type mkdir test to make a directory called test inside the user dqs home folder.
 
```bash
mkdir test
```

####Results:
```bash  
/home/dq$ mkdir test                                                            
/home/dq$ ls                                                                    
test  
```


---
#8: Command Options
Commands have options that can modify their behavior. We specify these options by adding them, preceded by one dash, after we invoke the command.  

For example, adding the -v option after the mkdir command will turn on "verbose" mode, and print output when it makes the folder.  


##Instructions  
 . Type mkdir -v test2 to check out the verbose option.
 
```bash
mkdir -v test2
```

####Results:
```bash  
home/dq$ mkdir -v test2                                                        
mkdir: created directory ‘test2’ 
```


---
#9: Checking Possible Options
Most commands will let you use the --help flag to understand what all the possible options are. A flag comes after a command. When you use the --help flag, you don't need to specify a directory.  

##Instructions  
 . Type mkdir --help to get help on the mkdir command.
 
```bash
mkdir --help
```

####Results:   
```bash
/home/dq$ mkdir --help                                                          
Usage: mkdir [OPTION]... DIRECTORY...                                           
Create the DIRECTORY(ies), if they do not already exist.                        
                                                                                
Mandatory arguments to long options are mandatory for short options too.        
  -m, --mode=MODE   set file mode (as in chmod), not a=rwx - umask              
  -p, --parents     no error if existing, make parent directories as needed     
  -v, --verbose     print a message for each created directory                  
  -Z, --context=CTX  set the SELinux security context of each created           
                      directory to CTX                                          
      --help     display this help and exit                                     
      --version  output version information and exit                            
                                                                                
Report mkdir bugs to bug-coreutils@gnu.org                                      
GNU coreutils home page: <http://www.gnu.org/software/coreutils/>               
General help using GNU software: <http://www.gnu.org/gethelp/>                  
For complete documentation, run: info coreutils 'mkdir invocation'  
```


---
#10: Listing The Contents Of A Directory
Now that we've made a couple of directories, let's see what's in our home folder. We can use the ls command for this. It lists all the files and folders in a directory. If we pass in the -l option, it will print a nicely formatted table of everything.   



##Instructions  
 . Type ls -l to see the contents of the home folder for dq.
 
```bash
ls -l
```

####Results:   
```bash
/home/dq$ ls -l                                                                 
total 8                                                                         
drwxr-xr-x 2 dq dq 4096 Feb 25 12:32 test                                       
drwxr-xr-x 2 dq dq 4096 Feb 25 12:33 test2 
```



---
#11: Removing A Directory
There's two directories, test and test2. Let's clean up the clutter by removing a directory. We can use the rmdir command to delete a directory.  

##Instructions  
 . 
 
```bash
rmdir test2
```

####Results:   
```bash
/home/dq$ rmdir test2                                                           
/home/dq$ ls                                                                    
test 
```