02/2017  
Dataquest : Data Analyst Path  
Step 3: The Command Line  
SubStep : Command Line: Beginner : Working with files
samedi, 25. février 2017 01:47 

---
#1: Making A File
We explored directories and looked at files in the last mission. In this mission, we'll look more closely at files, and how to interact with them.  

The first step in this process is creating a file. We can create files in several ways, but one is the touch command. This will create an empty file with a given name. touch file.txt will create a new file called file.txt in the current directory. We can later open the file and edit it if we want.  

Touch can also be used to update the date that a file was last accessed if we have a need to change that time. You can read more about the touch command here.  

##Instructions  
 . Use the touch command to create a file named test.txt in the home directory for the user dq.
 
```bash
touch text.txt
```

####Results: 
```bash  
/home/dq$ touch text.txt                                                        
/home/dq$ ls                                                                    
text.txt 
```


---
#2: Standard Streams
Now that you created the test.txt file, you can add text to it in a few different ways. The first is the echo command. The echo command will just print whatever you tell it to as output. If you type echo "Dataquest is awesome", it will print Dataquest is awesome.  

This text is printed into a stream called standard output, or stdout. Every program writes to standard output, and gets input through standard input (stdin). Whenever a program has an error while running, it writes the error message to standard error (stderr). These standard streams are how output is shown to you in the terminal, and how you enter input.  

Usually, stdout and stderr are shown on the monitor, and stdin is the input from the keyboard. In this case, echo is taking a string from stdin, and printing that string to stdout. By default, we see the message that is printed to stdout, because it shows on the monitor.  

The interfaces look something like this:   

see img/im1.png  

The reason for stdout, stderr, and stdin is that the standard streams allow the interfaces to be abstract. A program doesn't need to care if it's getting input from a keyboard, from a file, or from somewhere else. A program also doesn't need to care if it's outputting to the display, to a file, or to somewhere else. The standard streams allow us to hook up various inputs and outputs to programs without the programs having to worry about what those inputs and outputs are.

##Instructions  
 . Type echo "All bears should juggle" to write All bears should juggle to stdout.
 
```bash
echo "All bears should juggle"
```

####Results: 
```bash  
/home/dq$ echo "All bears should juggle"                                        
All bears should juggle 
```



---
#3: Redirection
We can redirect standard streams in order to connect them to different sources. One example is that we can connect stdout to a file. After doing this, the program it's connected to will write to a file instead of the screen.  

To redirect, we use the greater than sign (>). For example, echo "Dataquest is awesome" > dataquest.txt will write Dataquest is awesome to stdout, then redirect stdout to the file dataquest.txt. The end result is that Dataquest is awesome will be written to the file dataquest.txt.    

##Instructions  
 . Echo All bears should juggle into the test.txt file that we created earlier.
 
```bash
echo "All bears should juggle" > test.txt
```

####Results: 
```bash  
/home/dq$ echo "All bears should juggle" > test.txt                             
/home/dq$ nano test.txt
```



---
#4: Editing A File
We can also edit a file directly from the terminal, without redirection. There are a few programs that let us do this, but the simplest is called nano. Nano is a command-line text editor that lets us edit and save files all from the terminal.  

To run nano, type nano, followed by the name of the file you want to edit. nano test.txt will open the test.txt file for editing.  

After a file is open, you can make whatever changes you want, then hit ctrl+x to quit. When you quit, you'll be prompted to save your work. Typing Y, then hitting enter will save all your changes.  

##Instructions  
 . Open test.txt with nano, delete the text in the file, and save the file.
 
```bash
nano test.txt
```

####Results: 
```bash  
open nano text editor
```


---
#5: File Permissions
In Unix, every file and folder has associated permissions. These permissions have three scopes:  

- owner -- the user who created the file or folder.
- group -- users in the owner's group. Users on unix systems can be placed into groups.
- everyone -- all other users on the system who aren't the user or in the user's group.
- Each scope can have any of three permissions (a scope can have multiple permissions at once):

---

- read -- The ability to see what's in a file. If defined on a folder, the ability to see what files are in a folder.
- write -- The ability to modify a file. If a folder, the ability to delete, modify, and rename files in the folder.
- execute -- The ability to run a file. Some files are executable, and need this permission to be run.
Each permission can be granted or denied to each scope.

You can view the permissions on files and folders using ls -l. This shows the permissions on the left of each file. Here's an example:  

```bash 
~$ ls -l                                                                                   
    total 4                                                                                    
    -rw-r--r-- 1 dq dq 10 Nov 14 00:08 test.txt
```
In the example above, the permissions for the file test.txt are -rw-r--r--. There are 10 characters in that string.  

see img.img2.png

We can ignore the first character for now. Starting at the second character, the permissions are split into three groups, one for user, one for group, and one for everyone. The owner has the permissions rw-, going from character 2 to character 4. This means that the owner can read and write the file, but not execute it. The first character represents read permissions, the second represents write permissions, and the third execute permissions. The character for read is r, the character for write is w, and the character for execute is x. If a scope doesn't have a permission, it shows as a dash -- -. If the permissions for the owner were instead rwx, they would be able to execute as well.  

The permissions for group are from character 5 to character 7. This is r--. People in the owner's group can only read the file.  

The permissions for everyone are r--. Anyone who has an account on this machine can read the file.  

##Instructions  
 . Type ls -l to see the file permissions in the /home/dq directory.
 
```bash
ls -l
```

####Results: 
```bash  
/home/dq$ ls -l                                                                 
total 4                                                                         
-rw-r--r-- 1 dq dq 1 Feb 25 12:52 test.txt                                      
-rw-r--r-- 1 dq dq 0 Feb 25 12:40 text.txt 
```



---
#6: Octal Notation
We just looked at file permissions that looked like -rw-r--r--. This is known as symbolic notation for permissions, because it expresses each permission as a symbol. The downside to symbolic notation is that if we want to change permissions, it takes a long time to type out. Another way to represent permissions is using octal notation.  

Octal notation lets us represent the permissions for all scopes in 4 digits instead of 10 characters like in symbolic notation. There are 8 possible combinations of the 3 permissions r, w, and x. We can express each combination as a single digit in an octal (base 8) counting system. Thus, we can represent each scope as a single digit in base 8.  

Here are the combinations and their corresponding digits:  

- --- -- no permissions, corresponds to 0.
- --x -- execute only permission, corresponds to 1.
- -w- -- write only permissions, corresponds to 2.
- -wx -- write and execute permissions, corresponds to 3.
- r-- -- read only permissions, corresponds to 4.
- r-x -- read and execute permissions, corresponds to 5.
- rw- -- read and write permissions, corresponds to 6.
- rwx -- grants read, write, and execute permissions, corresponds to 7.  

We can turn the permissions string -rw-r--r-- into 0644. Just like with symbolic notation, don't worry about the first digit in octal notation right this second -- we'll get to it later.  

You can see the octal permissions of a file by using the stat command. Typing stat test.txt will show you some information about the file test.txt, including the octal permissions.   

```bash
~$ stat test.txt                                                                           
File: ‘test.txt’                                                                         
Size: 10              Blocks: 8          IO Block: 4096   regular file                   
Device: 60h/96d Inode: 2625        Links: 1                                                
Access: (0644/-rw-r--r--)  Uid: ( 1000/      dq)   Gid: ( 1000/      dq)                   
Access: 2015-11-14 00:08:58.299959914 +0000                                                
Modify: 2015-11-14 00:08:57.930008711 +0000                                                
Change: 2015-11-14 00:08:57.930008711 +0000                                                
Birth: -
```

The stat command returns quite a bit of detailed information about the file. At the moment, we'll focus on the permissions, which can be found in the Access section.  


##Instructions  
 . Type stat test.txt to see the file permissions of the test.txt file.
 
```bash
stat test.txt
```

####Results: 
```bash  
/home/dq$ stat test.txt                                                         
  File: ‘test.txt’                                                              
  Size: 1               Blocks: 8          IO Block: 4096   regular file        
Device: ca01h/51713d    Inode: 22939178    Links: 1                             
Access: (0644/-rw-r--r--)  Uid: ( 1000/      dq)   Gid: ( 1000/      dq)        
Access: 2017-02-25 12:43:52.774134765 +0000                                     
Modify: 2017-02-25 12:52:38.717979560 +0000                                     
Change: 2017-02-25 12:52:38.717979560 +0000                                     
 Birth: -
```



---
#7: Modifying File Permissions
Now that we understand file permissions, we can modify them using the chmod command. We pass in an octal permissions string and a file name, and it modifies the file we specify to have the permissions reflected by that string.  

Typing chmod 0664 test.txt will give the owner read and write permissions, the group read and write permissions, and everyone read only permissions.    

##Instructions  
Modify test.txt so it has the following permissions:  

-  owner -- read, write, and execute
-  group -- read and write
-  everyone -- no permissions

 Remember to add a 0 in front of the octal permissions string.  
```bash
chmod 0760 test.txt
```

####Results: 
```bash  
/home/dq$ chmod 0760 test.txt                                                   
/home/dq$ ls -l                                                                 
total 4                                                                         
-rwxrw---- 1 dq dq 1 Feb 25 12:52 test.txt                                      
-rw-r--r-- 1 dq dq 0 Feb 25 12:40 text.txt
```


---
#8: Moving Files
You can move files with the mv command. Typing mv test.txt /dq will move the test.txt file to the /dq folder.   
This assume that test.txt is in your current directory.   

##Instructions  
Make a directory called test in the home directory of dq.  

 - The full path should be /home/dq/test.
 
Type mv test.txt test to move the test.txt file to the test folder.  
 
```bash
mkdit test 
mv test.txt test
```

####Results: 
```bash  
/home/dq$ mkdit test                                                            
bash: mkdit: command not found                                                  
/home/dq$ mv test.tx /test                                                      
mv: cannot stat ‘test.tx’: No such file or directory                            
/home/dq$ mv test.txt /test                                                     
mv: cannot move ‘test.txt’ to ‘/test’: Permission denied                        
/home/dq$ mv test.txt test  
```



---
#9: Copying Files
Sometimes, instead of moving a file, you'll want to make a copy, and move that copy somewhere else. The cp command is useful for this. cp test.txt test2.txt will copy the test.txt file, and create a new file called test2.txt with the contents of test.txt.   

##Instructions  
 . Copy the file at /home/dq/test/test.txt to /home/dq/test/test2.txt.
 
```bash
cp ~/test/test.txt ~/test/test2.txt
```

####Results: 
```bash  
/home/dq/test$ cd ..                                                            
/home/dq$ cp ~/test/test.txt ~/test/test2.txt                                   
/home/dq$ ls -l                                                                 
total 4                                                                         
drwxr-xr-x 2 dq dq 4096 Feb 25 15:33 test                                       
-rw-r--r-- 1 dq dq    0 Feb 25 12:40 text.txt                                   
/home/dq$ cd test                                                               
/home/dq/test$ ls -l                                                            
total 0                                                                         
-rw-r--r-- 1 dq dq 0 Feb 25 15:34 test2.txt                                     
-rw-r--r-- 1 dq dq 0 Feb 25 15:33 test.txt
```



---
#10: File Extensions
Typically, files have extensions, such as .txt and .csv, that indicate the type of the file, and are used to determine the default program to open these files in Windows. For instance, on Windows, a text editor will be the default program to open files with the .txt extension.  

Rather than relying on extensions to determine file type, Unix-based operating systems such as Linux use media types, also called MIME types. The MIME type application/pdf indicates that a file is a pdf, and the MIME type image/png indicates that a file is a png image. The first part of a MIME type string is the type, such as application, or image, and the second part is the subtype, such as pdf, or png.  

There are MIME types for every type of file. MIME types are stored in the file metadata, which is stored as part of the file. Because of this, Linux can figure out the type of a file and open it properly even if it doesn't have an extension.  

You can rename files and remove extensions whenever you want, and you'll often run across files without extensions, such as test.  

Specifying a folder as the second argument to mv will preserve the file name, and move it into the folder. If you instead specify a full path, including filename, it will move the original file to the new file name, essentially renaming it. For example, mv test.txt test2.txt will move the file test.txt to test2.txt. This will basically rename test.txt.   

##Instructions  
 . Rename test.txt in the /home/dq/test folder to test_no_extension.
 
```bash
mv ~/test/test.txt ~/test/test_no_extension
```

####Results: 
```bash  
/home/dq/test$ cd ..                                                            
/home/dq$ mv ~/test/test.txt ~/test/test                                        
/home/dq$ mv ~/test/test ~/test/test_no_extension    
```


---
#11: Deleting A File
You can delete a file with the rm command. Typing rm test.txt will remove the test.txt file, provided it's in the same folder that you're in.  

##Instructions  
 . Remove the /home/dq/test/test2.txt file.
 
```bash
rm ~/test/test2.txt
```

####Results: 
```bash  
home/dq$ rm ~/test/test2.txt
```



---
#12: The Root User
Unix systems have a special user, called the root user. You can run commands as the root user using sudo. Adding sudo to the beginning of any command will run that command as the root user. Typing sudo rm test.txt will switch to the root user, then delete the test.txt file as the root user. This is useful in situations where the current user doesn't have permission to delete the file. The root user has access to all files and has all permissions by default.  

You typically will need a password to switch to the root user -- for security reasons, you don't want anyone to be able to switch to the root user whenever they want.  

In the Dataquest terminal, access to the root user is restricted for security reasons. Adding sudo to a command will result in an error.  

##Instructions  
 . Try adding sudo to a command and seeing what happens.
 
```bash
sudo
```

####Results: 
```bash  
/home/dq$ sudo                                                                  
sudo: unable to change to root gid: Operation not permitted
```