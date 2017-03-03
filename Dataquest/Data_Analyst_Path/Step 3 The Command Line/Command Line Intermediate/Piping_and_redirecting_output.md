02/2017  
Dataquest : Data Analyst Path  
Step 3: The Command Line  
SubStep : Command Line: Intermediate : Piping and redirecting output  
dimanche, 26. février 2017 12:42 


---
#1: Appending
In an earlier mission, we looked at how to redirect output from a command to a file using >. Here's an example:  

```bash
echo "This is all a dream..." > dream.txt
```

If the file dream.txt already exists, the above code will overwrite the file with the string This is all a dream.... If the file dream.txt doesn't exist, it will be created, and the string This is all a dream... will be used as the content. This involves redirecting from the standard output of the command to the standard input of the file.  

If we don't want to overwrite dream.txt, and we instead want to add to it, we can use >>.  

```bash
echo "Wake up!" >> dream.txt
```

The above code will append This is all a dream... to the file dream.txt. The file will still be created if it didn't exist.  


##Instructions  
- Overwrite the file beer.txt with the string 99 bottles of beer on the wall....
- Append the string Take one down, pass it around, 98 bottles of beer on the wall... to the file beer.txt.

```bash  
echo "99 bottles of beer on the wall..." > beer.txt
echo "Take one down, pass it around, 98 bottles of beer on the wall.." >> beer.txt
nano beer.txt
```

####Results: 

```bash  
/home/dq$ echo "99 bottles of beer on the wall..." > beer.txt                  
/home/dq$ echo "Take one down, pass it around, 98 bottles of beer on the wall.." >> beer.txt
```



---
#2: Redirecting From A File
We've seen how to redirect from a command to a file. We can also redirect the other way, from a file to a command. This involves redirecting from the standard output of the file to the standard input of the command.  

In our last screen, the file beer.txt ends up looking like this:  

>99 bottles of beer on the wall...
	
Take one down, pass it around, 98 bottles of beer on the wall...  
The Linux sort command will sort the lines of a file in alphabetical order. If we pass the -r flag, the lines will be sorted in reverse order.  

```bash
sort < beer.txt
```

The above code will sort each of the lines in beer.txt in order.  


##Instructions  
 - Use the sort command to sort the lines of beer.txt in reverse order.


```bash  
sort -r < beer.txt
```

####Results: 

```bash  
/home/dq$ sort -r < beer.txt                                                    
Take one down, pass it around, 98 bottles of beer on the wall...                
99 bottles of beer on the wall...
```




---
#3: The Grep Command
Sometimes, we'll want to search through the contents of a set of files to find a specific line of text. We can use the grep command for this.  

```bash
grep "pass" beer.txt
```

The above command will print any lines in beer.txt where the string pass appears, and highlight the string pass.  

We can specify multiple files by passing in more arguments:  

```bash
grep "beer" beer.txt coffee.txt
```

This will show all lines from either file that contain the string beer.  


##Instructions  
 - Make a file called coffee.txt that has two lines of text in it:

>Coffee is almost as good as beer,
>But I could never drink 99 bottles of it

 - Use the grep command to search beer.txt and coffee.txt for the string bottles of.


```bash  
echo "Coffee is almost as good as beer," > coffee.txt
echo "But I could never drink 99 bottles of it" >> coffee.txt
grep "bottles of" beer.txt coffee.txt
```

####Results: 

```bash  
/home/dq$ echo "Coffee is almost as good as beer," > coffee.txt                 
/home/dq$ echo "But I could never drink 99 bottles of it" >> coffee.txt         
/home/dq$ grep "bottles of" beer.txt coffee.txt                                 
beer.txt:99 bottles of beer on the wall...                                      
beer.txt:Take one down, pass it around, 98 bottles of beer on the wall...       
coffee.txt:But I could never drink 99 bottles of it
```



---
#4: Special Characters
Like we did in the last screen, sometimes we'll want to execute commands on a set of files. There were only 2 files in the last screen though, beer.txt and coffee.txt. But what if we wanted to search through all 1000 files in a folder? We definitely wouldn't want to type out all of the names. Let's say we have the following files in a directory:  

>beer.txt
>beer1.txt
>beer2.txt
>coffee.txt
>better_coffee.txt

If we wanted to search for a string in beer1.txt and beer2.txt, we could use this command:  

```bash
grep "beer" beer1.txt beer2.txt
```

We could also use a wildcard character, ?. ? is used to represent a single, unknown character. We could perform the same search we did above like this:  

```bash
grep "beer" beer?.txt
```

The wildcard above will match both beer1.txt and beer2.txt. We can use as many wildcards as we want in a filename.  


##Instructions  
- Create empty files called beer1.txt and beer2.txt.
- Use grep and the ? wildcard character to search for beer in both beer1.txt and beer2.txt.

```bash  
touch beer1.txt beer2.txt 
grep "beer" beer?.txt 
```

####Results: 

```bash  
/home/dq$ touch beer1.txt beer2.txt                                             
/home/dq$ ls                                                                    
beer1.txt  beer2.txt  beer.txt  coffee.txt                                       
/home/dq$ grep "beer" beer?.txt 
```



---
#5: The Star Wildcard
We learned about the ? wildcard character in the last screen, but there are also other wildcard characters. Let's say we again have the following files in a directory:  

>beer.txt
>beer1.txt
>beer2.txt
>coffee.txt
>better_coffee.txt

We can use the * character to match any number of characters, including 0.  

```bash
grep "beer" beer*.txt
```

The above command will search for the string beer in beer.txt, beer1.txt, and beer2.txt. We can also use the wildcard to match more than 1 character:  

```bash
grep "beer" *.txt
```

The above command will search for the string beer in any file that has a name ending in .txt.  

We can use wildcards anytime we would otherwise enter a filename. For example:  

```bash
ls *.txt
```

The above command will list any files with names ending in .txt in the current directory.  


##Instructions  
- Use grep and the * wildcard character to search for beer in all the files ending in .txt in the home directory.

```bash  
grep "beer" *.txt
```

####Results: 

```bash  
/home/dq$ grep "beer" *.txt                                                     
beer.txt:99 bottles of beer on the wall...                                      
beer.txt:Take one down, pass it around, 98 bottles of beer on the wall...       
coffee.txt:Coffee is almost as good as beer,
```




---
#6: Piping Output
The pipe character, |, allows you to send the standard output from one command to the standard input of another command. This can be very useful for chaining together commands.  

For example, let's say we had a file called logs.txt with 100000 lines. We only want to search the last 10 lines for the string Error. We can use the tail -n 10 logs.txt to get the last 10 lines of logs.txt. We can then use the pipe character to chain it with a grep command to perform the search:  

```bash
tail -n 10 logs.txt | grep "Error"
```

The above command will search the last 10 lines of logs.txt for the string Error.  

We can also pipe the output of a Python script. Let's say we had this script called rand.py:  

```python 
import random
for i in range(10000):
    print(random.randint(1,10))
```    
    
The above script will use the random library to generate a sequence of random integers, ranging in value from 0 to 10, and will print them to the standard output.  

This command will run the script, and search each line of output to see if a 9 occurs:  

```bash
python rand.py | grep 9
```

Any lines that output a 9 will be printed.  


##Instructions  
- Make a Python script that generates output.
- Use pipes and grep to search the output of the script.

```python  
import random
for i in range(10000):
    print(random.randint(1,10))
```

```bash  
python script.py | grep *
```

####Results: 

```bash  
/home/dq$ python script.py | grep *                                             
Traceback (most recent call last):                                              
  File "script.py", line 3, in <module>                                         
    print(random.randint(1,10))                                                 
BrokenPipeError: [Errno 32] Broken pipe
```



---
#7: Chaining Commands
If we want to run two commands sequentially, but not pass output between them, we can use && to chain them. Let's say we want to add some content to a file, then print the whole file:  

```bash
echo "All the beers are gone" >> beer.txt && cat beer.txt
```

This will first add the string All the beers are gone to the file beer.txt, then print the entire contents of beer.txt. The && only runs the second command if the first command doesn't return an error. If we instead tried this:  

```bash
echo "All the beers are gone" >> beer.txt && cat beer.txt
```

We'd get an error, and nothing would be printed, because we used the command ec instead of echo.  


##Instructions  
- Add a line to beer.txt, and then print the contents of the file with cat.

```bash  
echo "add line to beer.txt" > beer.txt && cat beer.txt
```

####Results: 

```bash  
/home/dq$ echo "add line to beer.txt" > beer.txt && cat beer.txt                
add line to beer.txt
```



---
#8: Escaping Characters
There are quite a few special characters that bash uses. A full list can be found here. When you use these characters in a string or a command, and you don't want them to have a special effect, you may have to escape them.  

Escaping tells the shell to not treat the character as special, but to treat it as a plain character instead. Here's an example:  

```bash
echo ""Get out of here," said Neil Armstrong to the moon people." >> famous_quotes.txt
```

The above command won't work as we intend because the quotes inside the string will be treated as special. But what we want to do is add the quotes into the file.  

We use a backslash (\) as an escape character -- if you add a backslash before a special character, the special character is treated like plain text.  

```bash
echo "\"Get out of here,\" said Neil Armstrong to the moon people." >> famous_quotes.txt
```

The command above has the double quotes escaped with a backslash, so it will work as we intend.  


##Instructions  
- Use the echo command to add a double quote character into a file.

```bash  
echo "\"Get out of here,\" said Neil Armstrong to the moon people." >>
 beer.txt
```

####Results: 

```bash  
/home/dq$ echo "\"Get out of here,\" said Neil Armstrong to the moon people." >>
 beer.txt
```