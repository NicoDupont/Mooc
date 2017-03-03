02/2017  
Dataquest : Data Analyst Path  
Step 3: The Command Line  
SubStep : Command Line: Beginner : Working with programs  
samedi, 25. février 2017 06:19 


---
#1: Setting Variables
In these shell tutorials, we've been interacting with a computer through the command line. In order to interact with it, we type commands in, those commands are executed, and we're shown the results. That interaction is happening within a shell called bash. A shell is a way to access and control a computer. Command line shells have a text interface for typing commands and seeing results, versus graphical shells which allow you to click on icons with a mouse. There are many unix shells, but Bash is one of the most popular. Bash is the default shell on most Linux and OSX computers.  

Bash is essentially a program that lets us run other programs. To do this, Bash implements a command language. This language specifies how we can type and structure commands that will be executed. A command language is a special kind of programming language through which we can control applications and the system. Just like other programming languages, like Python, we can create scripts, set variables, and more. Because it is a language, bash is far more powerful than a graphical shell.  
  
We can set variables by assigning to them. Variables consist entirely of uppercase characters, numbers, and underscores. You can assign any datatype to a variable. Here are some examples:  

```bash
OS=linux
OPERATING_SYSTEM="linux"
```

Both of the above variables OS and OPERATING_SYSTEM will actually be assigned the same value. Quotes are optional when using strings in bash, unless there's a space in the string -- bash is sensitive to spaces, and strings with spaces won't work properly if they aren't surrounded with quotes.  

This assignment won't work:  

```bash
ANIMAL=Shark with a laser beam on its head
```

But this will:  

```bash
ANIMAL="Shark with a laser beam on its head"
```

It's also important not to add in stray spaces. This won't work:  

```bash
ANIMAL = "Shark with a laser beam on its head"
```

##Instructions  
 - Create a variable FOOD containing the value Shrimp gumbo.
 
 
```bash
FOOD="Shrimp gumbo"
```

####Results: 

```bash  
/home/dq$ FOOD="Shrimp gumbo"
```


---
#2: Accessing Variables
Variables in bash work similarly to variables in other languages such as Python in that we can access the values again after we set them. One major difference is that in order to access the value of a variable, you have to add a dollar sign to the beginning of the variable name.  

For example, if you create a variable named FOOD with the value Shrimp gumbo, you'll need to use $FOOD when you want to access the value again later. This is because typing FOOD at the command prompt will attempt to call the command FOOD, and will return an error, because there is no executable named FOOD in PATH.  

Another difference between Python variables and bash variables is that when you type $FOOD at the command prompt, it will resolve to the value of the variable, or Shrimp gumbo. By default, bash will try to turn this into a command, and will try to call the command Shrimp. Since there is no executable named Shrimp in PATH, this will cause an error.  

If you want to see the value of a variable named FOOD, you'll need to type echo $FOOD. This will turn into echo "Shrimp gumbo", which will print Shrimp gumbo to stdout.  


##Instructions  
 - Type echo $FOOD to print the value of the FOOD variable.
 
 
```bash
echo $FOOD
```

####Results: 

```bash  
/home/dq$ echo $FOOD                                                            
Shrimp gumbo
```



---
#3: Environment Variables
So far, we've been creating shell variables. These variables can be accessed only within the bash shell.  

Another type of variable is an environment variable. These can be accessed by any program that is run from the shell.  

We can create environment variables using the export command. export FOOD="Chicken and waffles" will create an environment variable called FOOD.  


##Instructions  
 - Type export FOOD="Chicken and waffles" to create an environment variable called FOOD.
 
 
```bash
export FOOD="Chicken and waffles"
```

####Results: 

```bash  
/home/dq$ export FOOD="Chicken and waffles"
```



---
#4: Accessing Environment Variables
We can run many programs from bash, including Python. To run the Python interpreter from the bash shell, just type python at the command prompt.  

Once inside the command prompt, you can access environment variables like this:  

```python
import os
print(os.environ["FOOD"])
```

The os package is built into the Python standard library, and contains many useful functions for working with the operating system.  

os.environ is a dictionary containing all of the values of environment variables. You can access any environment variable by specifying it as a key, just like with any Python dictionary.  

This shows you a hint of the power of environment variables -- we can use them to set configuration in Python scripts and in other places. This is useful when configuration is secret (like access keys), or is changing quickly.  


##Instructions  
Type python to fire up the Python interpreter.  
 - In the interpreter, you can run Python commands by typing them in and hitting enter at the end of each line.
 - Run the following code in the interpreter:
 
```python
import os
print(os.environ["FOOD"])
```

 - When you're done, type exit() to exit the interpreter.
 
 Finally, type echo $FOOD to verify that the value of the FOOD variable is the same in Python and in the shell.
 
 
```bash
python
import os
print(os.environ["FOOD"])
exit()
echo $FOOD
```

####Results: 

```bash  
/home/dq$ python                                                                
Python 3.4.3 (default, Nov 17 2016, 01:08:31)                                   
[GCC 4.8.4] on linux                                                            
Type "help", "copyright", "credits" or "license" for more information.          
>>> import os                                                                   
>>> print(os.environ["FOOD"])                                                   
Chicken and waffles                                                             
>>> exit()                                                                      
/home/dq$ echo $FOOD                                                            
Chicken and waffles 
```


---
#5: Calling Programs
In the last screen, we accessed Python by typing python in the shell. We can run many programs this way. There's nothing special about a program -- it's a file somewhere on the system.  

Any program can be accessed by typing its full path. The full path for Python, which itself is a program, is /usr/bin/python.  


##Instructions  
 - Type /usr/bin/python to get to the Python interpreter.
 - Type exit() to leave the interpreter.
 
 
```bash
/usr/bin/python 
exit()
```

####Results: 

```bash  
/home/dq$ /usr/bin/python                                                       
Python 2.7.6 (default, Oct 26 2016, 20:30:19)                                   
[GCC 4.8.4] on linux2                                                           
Type "help", "copyright", "credits" or "license" for more information.          
>>> exit()
```



---
#6: The PATH Variable
In the last screen, we typed /usr/bin/python to access the Python interpreter. If the Python interpreter is at that location, how come we can also access it by typing python? We can do this because of the PATH variable. The PATH environment variable contains several folders. Any program in any one of these folders can be run simply by typing the name of the program. Since /usr/bin is one of the folders in PATH, we can access python, which is in the folder, by just typing python instead of the full path.  


##Instructions  
 - Type echo $PATH to see what folders are in PATH.
 
 
```bash
echo $PATH
```

####Results: 

```bash  
/home/dq$ echo $PATH                                                            
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```



---
#7: Flags
Some of the programs we've been running have arguments, and some don't. When you type echo $FOOD, you're passing the value of the $FOOD variable as a positional argument to the echo program. This is similar to a function in Python, which has positional and keyword arguments. Programs can have any number of positional arguments, including zero. python is an example of a program that doesn't require any positional arguments.  

cp is an example of a command with two positional arguments -- you need to pass the file, and the path to which you want it to be copied.  

Programs can also have flags, which are akin to keyword arguments in Python. These are optional, and modify program behavior. Flags sometimes have values specified. If they don't have a value specified, then they're boolean. Boolean flags are true when they appear, and false when they don't. For example, the -l flag, when passed to ls, will list the files in the directory in long mode, and show more information about them.  


##Instructions  
 - Type ls -l to see how ls works with the -l flag set to true.
 
 
```bash
ls -l                                                                 
```

####Results: 

```bash  
/home/dq$ ls -l                                                                 
total 0
```


---
#8: Combining Flags
There are many times when you'll want to specify multiple flags. Most flags have short, single-character names, as well as longer names. See the ls manual page for a closer look at this.  

For example, specifying ls -a, and ls --all will both list all of the files in a directory, instead of hiding anything that starts with .. The commands are equivalent.  

When we have multiple flags with short, single-character names, we can chain them together to save time. ls -la will list all of the files in a long format, and is equivalent to ls -a -l. The order of the l and the a don't matter. This is commonly done by experienced programmers, and can be a bit confusing to parse at first.  


##Instructions  
 - Use ls -al to list all of the files in a long format.
 
 
```bash
ls -al
```

####Results: 

```bash  
/home/dq$ ls -al                                                                
total 48                                                                        
drwxr-xr-x 1 dq   dq   4096 Feb 25 17:18 .                                      
drwxr-xr-x 1 root root 4096 Feb 23 02:22 ..                                     
-rw-rw-rw- 1 dq   dq   4496 Feb 25 17:18 .bashrc                                
drwxr-xr-x 1 dq   dq   4096 Feb 23 02:22 .byobu                                 
drwxr-xr-x 1 dq   dq   4096 Feb 23 02:22 .cache                                 
drwxr-xr-x 1 dq   dq   4096 Feb 23 02:22 .config                                
-rw-r--r-- 1 dq   dq     25 Feb 23 02:22 .gitconfig                             
drwxr-xr-x 1 dq   dq   4096 Feb 25 17:18 .ipython                               
drwxr-xr-x 2 dq   dq   4096 Feb 23 02:22 .jupyter                               
drwx------ 3 dq   dq   4096 Feb 23 02:22 .local                                 
-rw-rw-rw- 1 dq   dq     17 Feb 23 02:19 .tmux.conf 
```



---
#9: Long Flags
You can specify longer flags with two dashes. One such longer flag for ls is --ignore. Using ls --ignore=test.txt won't list any files named test.txt in the output of ls.  


##Instructions  
 - Use ls -al with the --ignore flag to ignore any files named .ipython.
 
 
```bash
ls -al --ignore=.ipython
```

####Results: 

```bash  
/home/dq$ ls -al --ignore=.ipython                                              
total 44                                                                        
drwxr-xr-x 1 dq   dq   4096 Feb 25 17:18 .                                      
drwxr-xr-x 1 root root 4096 Feb 23 02:22 ..                                     
-rw-rw-rw- 1 dq   dq   4496 Feb 25 17:18 .bashrc                                
drwxr-xr-x 1 dq   dq   4096 Feb 23 02:22 .byobu                                 
drwxr-xr-x 1 dq   dq   4096 Feb 23 02:22 .cache                                 
drwxr-xr-x 1 dq   dq   4096 Feb 23 02:22 .config                                
-rw-r--r-- 1 dq   dq     25 Feb 23 02:22 .gitconfig                             
drwxr-xr-x 2 dq   dq   4096 Feb 23 02:22 .jupyter                               
drwx------ 3 dq   dq   4096 Feb 23 02:22 .local                                 
-rw-rw-rw- 1 dq   dq     17 Feb 23 02:19 .tmux.conf 
```