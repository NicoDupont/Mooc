02/2017  
Dataquest : Data Analyst Path  
Step 3: The Command Line  
SubStep : Command Line: Beginner : Command line Python scripting  
samedi, 25. février 2017 06:34 


---
#1: Command Line Python
We looked at the command line Python interpreter in the last mission. The interpreter lets you run Python commands and see their results immediately. It's very useful for quickly testing snippets of code and debugging. But it's not a good way to develop Python programs, because the commands aren't saved anywhere.  

In order to develop Python programs, we'll need to make files containing Python code. We'll then be able to use the interpreter to run them from the command line. This way, we can save all our commands, but still see what's happening.  

This is a very common way to develop using Python -- use an IDE or text editor to create Python files, then run them from the command line.  

In order to make a file that Python can execute on the command line, we'll need to add some lines to a blank file:  

```python
if __name__ == "__main__":
    print("Welcome to a Python script")
```

The code above will print Welcome to a Python script when it's run from the command line. To run it, we just need to put those lines into a file, and then call it with python file.py (assuming the file is called file.py).  

This works because the __name__ variable in Python scripts is automatically set to the name of the module. If the module is being run from the command line, it will be set to __main__. Checking this allows us to tell if a script is being run from the command line or not.  

##Instructions  
 
 Create a file called script.py in the /home/dq folder that contains the following code:
 
```python
if __name__ == "__main__":
    print("Welcome to a Python script")
```

Finally, save the file and run it using python script.py.


```bash  
touch script.py
nano script.py
python script.py
```

####Results: 

```bash  
/home/dq$ touch script.py                                                       
/home/dq$ nano script.py                                                        
/home/dq$ python script.py                                                      
Welcome to a Python script
```



---
#2: Python Versions
There are actually two versions of Python on this machine. We ran the last script using the default python executable, which is Python version 2. We'll instead want to use Python 3, which we can access with the python3 executable.  


##Instructions  
 - Type python3 script.py to run the file script.py using python 3.
 
```bash
python3 script.py
```

####Results: 

```bash  
/home/dq$ python3 script.py                                                     
Welcome to a Python script
```



---
#3: Installing Packages
Packages are an important way to extend the functionality of Python. We've worked with packages like matplotlib and pandas. The best way to install packages is to use the command line, and a program called pip. The newest versions of Python include pip by default, so installing Python will automatically give you access to pip.  

In order to install a package with pip, we just use pip install. pip install requests will install the requests package, which can be used to interact with websites and APIs.  


##Instructions  
Type pip install requests to install the requests package.

 - Since the library is already installed, you'll receive an appropriate message to reflect that.
 
```bash
pip install requests
```

####Results: 

```bash  
/home/dq$ pip install requests                                                  
Requirement already satisfied: requests in /dataquest/system/env/python3/lib/pyt
hon3.4/site-packages
```




---
#4: Virtual Environments
In the previous screen, we used the default version of pip, which installed requests for the python executable, which is Python version 2.  

What if we had instead wanted to install requests for Python 3? This type of version switching can get confusing, and different projects can require different packages and Python versions. A nice way to avoid issues with different package versions are virtual environments. By default, the system has one python executable, and you have to install all packages and libraries globally. This means that every single project on your machine has to use the same version of Python, and the same versions of every package.  

By default, you can't use different versions of Python without some hacks. One such hack is renaming python to python3 so we can have access to both Python 2 and Python 3.  

A better solution for this is for each project we write to have its own version of Python, along with its own packages. This way, we don't need to worry that upgrading the version of a package will affect other projects on the system and cause them to stop working.  

Virtual environments, or virtualenvs, let us do this. You can create a new virtualenv with the virtualenv command. In order to access this, you normally have to install the virtualenv package, but we've already installed it to simplify the process.  

Typing virtualenv main will create a virtualenv named main. It will create a folder in the current directory called main that will hold all the packages you install into the virtual environment.  


##Instructions  
Type virtualenv python2 in the /home/dq directory to create a new virtual environmented named python2.
 - Note how it makes a folder called python2.
 
```bash
virtualenv python2
```

####Results: 

```bash  
/home/dq$ virtualenv python2                                                    
New python executable in /home/dq/python2/bin/python                            
Installing setuptools, pip, wheel...done.  
```



---
#5: Python 3 Virtualenv
By default, virtualenv will use the python executable when it makes a new virtualenv, which means that it has the same version of Python as the system. In this case, we want to use python3 instead for our virtualenv. In order to do this, we pass the -p flag to the virtualenv command, which will allow us to change the Python interpreter that virtualenv uses.  

In this case, we can type virtualenv -p /usr/bin/python3 python3 to use Python 3 instead of Python 2.  


##Instructions  
 - Create a virtualenv called python3 in the /home/dq folder that uses Python 3.
 
```bash
virtualenv -p /usr/bin/python3 python3
```

####Results: 

```bash  
/home/dq$ virtualenv -p /usr/bin/python3 python3                                
Running virtualenv with interpreter /usr/bin/python3                            
Using base prefix '/usr'                                                        
New python executable in /home/dq/python3/bin/python3                           
Also creating executable in /home/dq/python3/bin/python                         
Installing setuptools, pip, wheel...done.
```



---
#6: Activating A Virtualenv
Once a virtualenv is created, you can activate it using source python3/bin/activate (this assumes that the virtualenv is called python3, and the folder for the virtualenv is in our current directory).  

When a virtualenv is activated, the Python version and packages installed in the virtualenv will become the default Python version and packages when you type python.  


##Instructions  
 - Activate the python3 virtualenv.
 
```bash
source python3/bin/activate
```

####Results: 

```bash  
/home/dq$ source python3/bin/activate                                           
(python3) /home/dq$
```




---
#7: Checking The Installed Packages
You can check the version of Python you're using with python -V. You can check which packages are currently installed and their versions with pip freeze. If you activate a virtualenv, all the packages, including pip, will be from the virtualenv instead of the main system Python executable.  


##Instructions  
 - Type python -V to verify that Python 3 is the current Python version after activating the virtualenv.
 - Type pip freeze to check which packages are installed and their versions.
 
```bash
python -V
pip freeze
```

####Results: 

```bash  
(python3) /home/dq$ python -V                                                   
Python 3.4.3                                                                    
(python3) /home/dq$ pip freeze                                                  
appdirs==1.4.0                                                                  
backports-abc==0.5                                                              
backports.shutil-get-terminal-size==1.0.0                                       
basemap==1.1.0                                                                  
beautifulsoup4==4.4.1                                                           
bleach==1.5.0                                                                   
click==6.7                  
...
```



---
#8: Importing A File
One of the great things about Python is that we can import functions from one package into a file. We can also import functions and classes from one file into another file. This gives us a powerful way to structure larger projects without having to put everything into one file.  

We'll experiment with this style of import by writing a function in a file, and then importing it from another file.  

If there's a file named utils.py, we can import it from another file in the same directory using import utils. All the functions and classes defined in utils.py will then be available using dot notation. If there's a function called keep_time in utils.py, we can access it with utils.keep_time() after importing it.  


##Instructions  
Create a file called utils.py that contains the following code:  
 
```python
def print_message():
    print("Hello from another file!")
```

Modify the original script.py file to instead contain this code:  

```python
import utils

if __name__ == "__main__":
    utils.print_message()
```

Both script.py and utils.py should be in the same folder.  
Finally, run python script.py to print out the message.  

```bash  
nano utils.py
nano script.py
python script.py
```

####Results: 

```bash  
(python3) /home/dq$ nano utils.py                                               
(python3) /home/dq$ nano script.py                                              
(python3) /home/dq$ python script.py                                            
Hello from another file!
```



---
#9: Command Line Arguments
You can also pass command line options into Python scripts. They can be retrieved inside the script using the sys package. The argv list allows you to retrieve the positional arguments passed into the script. We learned about positional arguments in the last mission -- they are any arguments that come after the command name. An example is python script.py 82. The first positional argument is script.py, and the second is 82.  

```python
import sys
​
if __name__ == "__main__":
    print(sys.argv[1])
```

The above code will read input from the command line, and print it back out. If the code is saved to script.py, you'd call python script.py "Hello from the command line" to pass in the text you want displayed.  

You'll notice that we print the second item in the argv list (sys.argv[1]). This is because the arguments start after the python command, so the first argument is the name of the file we want to run. The second argument is the actual text that we want to print.  

##Instructions  
 - Modify script.py to accept and print a command line argument.
 - Then, call the script and pass in "Hello from the command line".
 
```bash
nano script.py
python script.py "Hello from the command line"
```

####Results: 

```bash  
(python3) /home/dq$ python script.py "Hello from the command line"              
Hello from the command line
```




---
#10: Deactivating A Virtualenv
When you want to switch a virtualenv off so you can move to a different project, you can deactivate it with the deactivate command. You don't have to pass in the virtualenv name to the deactivate command -- just typing deactivate will deactivate the current virtualenv.  


##Instructions  
 - Deactivate the virtualenv.
 
```bash
deactivate
```

####Results: 

```bash  
(python3) /home/dq$ deactivate                                                  
/home/dq$
```