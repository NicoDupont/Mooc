02/2017  
Dataquest : Data Analyst Path  
Step 3: The Command Line  
SubStep :  Git and Version Control  : Introduction to Git Integration  
lundi, 27. février 2017 06:29  

---
# 1: Version Control Systems    

When you're working with teams, you'll generally be making changes to the same files. Imagine you're working on a project to make a Python script, and have a folder with the following two files:  

- script.py
- README.md

Here are the contents of script.py:  

```python
if __name__ == "__main__":
    print("Welcome to a script!")
```

Imagine that you and a coworker are both working on the project at the same time. You modify script.py like this:  

```python
if __name__ == "__main__":
    print("Welcome to a script!")
    print("Here's my amazing contribution to this project!")
```    

And your coworker does this:  

```python
import math
print(10 + 10)
if __name__ == "__main__":
    print("Welcome to a script!")
```

Imagine you both have the folder on your local machine. To modify files, you make changes, then upload the entire folder to a centralized location, like Dropbox or Google Drive, to enable collaboration. If you didn't have a distributed version control system, whoever changed the file last will overwrite the changes of the other person. This gets extremely frustrating and impossible to manage as you start dealing with larger and larger chunks of code. What if the folder had 100 files, and you modified 10, and your coworker modified 30 at the same time? You don't want to lose your changes every time your coworker uploads his version of the folder. Now, imagine that instead of just you and a coworker, it's a project with 10 or 100 contributors.  

Companies face this problem every day, which is why distributed version control systems exist. With a distributed version control system, software will "merge" changes together intelligently, and enable multiple developers to work on a project at the same time.  

Going back to the script.py file, if we intelligently merged the two versions, it would end up looking like this:  

```python
import math
print(10 + 10)
if __name__ == "__main__":
    print("Welcome to a script!")
    print("Here's my amazing contribution to this project!")
```

There are a few distributed version control systems, including Mercurial, and Subversion. However, Git is by far the most popular.  

Git is a command line tool that we can access by typing git in the shell. The first step in using Git is to initialize a folder as a repository. A repository tracks multiple versions of the files in the folder, and enables collaboration.  

You can initialize a repository by typing git init inside the folder you want to initialize as a repository.  

### Instructions :

 - Create a folder named random_numbers.
 - Navigate into this folder and initialize a git repository.

```bash
mkdir random_numbers
cd random_numbers
git init
```

#### Results :

```bash
/home/dq$ mkdir random_numbers                                                  
/home/dq$ cd random_numbers                                                     
/home/dq/random_numbers$ git init                                               
Initialized empty Git repository in /home/dq/random_numbers/.git/
```


---
# 2: The .Git Folder  

Initializing a Git repository will create a folder called .git inside the repository folder. There should now be a folder called .git inside our random_numbers folder. Typically, when folders and files are prefixed with a period (.), it means that they are private, and they don't show up by default when you list the files in the folder.  

Let's verify that it's there with ls -al. As you may recall, the -a flag will show everything in a folder, even if it starts with ..  


### Instructions :    

 - Run ls -al to check the contents of the random_numbers folder.

```bash
ls -al
```

#### Results :  

```bash
/home/dq/random_numbers$ ls -al                                                 
total 12                                                                        
drwxr-xr-x 3 dq dq 4096 Feb 27 17:38 .                                          
drwxr-xr-x 1 dq dq 4096 Feb 27 17:38 ..                                         
drwxr-xr-x 7 dq dq 4096 Feb 27 17:38 .git
```


---
# 3: Creating Some Files    

Git works on the principle of adding files, making changes, then storing a checkpoint of those changes. These checkpoints are called commits.  

Instead of storing every file in every commit, Git stores the diff, or the difference between the file in one commit and the next commit.  

For example, if you created a file called README.md with this content:  

>Welcome to my readme!

Then made a commit with it, Git would store the file. Let's say you later added another line to the file and made another commit:  

>Welcome to my readme!
>Here's another line.

Git would only store the difference between the file in the two commits, which is Here's another line.. Every project is a sequence of commits. Commits give us a powerful way to merge changes together from others, and to rewind time and reset to an earlier state of the repository.  

Before we make a commit, let's add some files to our folder.  


### Instructions :  

Create a file named README.md with the following content:  

>Random number generator

Create a file named script.py with the following content:  

```python
if __name__ == "__main__":
    print("10")
```

```bash
echo "Random number generator" > README.md
nano script.py
```

#### Results :  

```bash
/home/dq/random_numbers$ echo "Random number generator" > README.md             
/home/dq/random_numbers$ nano script.py
```



---
# 4: Git Status    

Files can have 3 states in Git:  

 - committed -- the current version of the file has been added to a commit, and is stored by git.
 - staged -- the file is currently staged for the next commit, but isn't yet stored by git.
 - modified -- the file has been modified since the last commit, but isn't staged yet.

After we make any changes to a Git repository, we can run git status to see which state each file in the repository is in. Any files that don't show up in git status are in the committed state.  

Git will automatically show us which files have been modified since the last commit. If we're ready to commit the modified files, we can add them to the staging area using git add. Typing git add script.py will add script.py to the staging area, where it will be staged for the next commit.  


### Instructions :  

 - Check the status of the repo.
 - Add script.py to the staging area.
 - Add README.md to the staging area.

```bash
git status
git add script.py
git add README.md
```

#### Results :  

```bash
/home/dq/random_numbers$ git status                                             
On branch master                                                                

Initial commit                                                                  

Untracked files:                                                                
  (use "git add <file>..." to include in what will be committed)                

        README.md                                                               
        script.py                                                               

nothing added to commit but untracked files present (use "git add" to track)    
/home/dq/random_numbers$ git add script.py                                      
/home/dq/random_numbers$ git add README.md
```


---
# 5: Configuring Git  

Before we can make our first commit, we need to tell Git who we are so it can store that information along with the commit. This ensures that different team members can tell who made which commit.  

We can do this by running git config. This only needs to be run once per computer, as Git saves your details.  

Git needs two pieces of information about you -- your email and your name. You can configure your email with:  

```bash
git config --global user.email "your.email@domain.com"
```

You can configure your name with:  

```bash
git config --global user.name "Your name"
```

### Instructions :  

 - Configure Git with your email and name.

```bash
git config --global user.email "nicolas.dupont@outlook.com"
git config --global user.name "Nicolas"
```

#### Results :  

```bash
/home/dq/random_numbers$ git config --global user.email "nicolas.dupont@outlook.
com"                                                                            
/home/dq/random_numbers$ git config --global user.name "Nicolas"
```



---
# 6: Committing  
Now that we have files that are staged, we can make our first commit. A commit is a way to store a snapshot of the files in the folder at a certain point in time. By building a history of these snapshots, we can easily rewind to an earlier point in time, or merge someone else's changes to files with ours.  

To make a commit, just use git commit -m "Commit message here". It's customary to make the commit message something informative, so if you do have to rewind or merge code, it's obvious what changes were made when.  


### Instructions :  

 - Type git commit -m "Initial commit. Added script.py and README.md" to make the first commit in the repository with an informative message.

```bash
git commit -m "Initial commit. Added script.py and README.md"
```

#### Results :  

```bash
/home/dq/random_numbers$ git commit -m "Initial commit. Added script.py and READ
ME.md"                                                                          
[master (root-commit) fb804b0] Initial commit. Added script.py and README.md    
 2 files changed, 3 insertions(+)                                               
 create mode 100644 README.md                                                   
 create mode 100644 script.py
```


---
# 7: File Differences      

Let's modify our files and make another commit to see how the process works. Before files are placed in the staging area, you can use git diff to see the line differences between the current versions of files in the folder, and the versions in the last commit. You can scroll up and down with the arrow keys, and exit git diff with the q key. If you want to see the differences after files are staged, you can use git diff --staged.  


### Instructions :    

script.py isn't exactly a random number generator right now.  

 - Modify it so that it prints a random integer from 0 to 10. You can import and use random.randint for this.

Type git diff afterwards to see how Git is tracking modifications.  
Finally, type git status to see the status of the modified file.  

```bash
nano script.py
python script.py
git diff
git status
```

#### Results :  

```bash
/home/dq/random_numbers$ nano script.py
/home/dq/random_numbers$ python script.py                                       
9                                                                               
/home/dq/random_numbers$ git diff                                               
diff --git a/script.py b/script.py                                              
index 9bf7d31..0262b9d 100644                                                   
--- a/script.py                                                                 
+++ b/script.py                                                                 
@@ -1,2 +1,3 @@                                                                 
+import random                                                                  
 if __name__ == "__main__":                                                     
-    print("10")                                                                
+    print(random.randint(0,10))                                                
/home/dq/random_numbers$ git status                                             
On branch master                                                                
Changes not staged for commit:                                                  
  (use "git add <file>..." to update what will be committed)                    
  (use "git checkout -- <file>..." to discard changes in working directory)     
                                                                                
        modified:   script.py                                                   
                                                                                
no changes added to commit (use "git add" and/or "git commit -a") 
```



---
# 8: Making A Second Commit  

Now that we have a modified file, we can add the changes to the staging area using git add script.py, and then commit them using git commit.  


### Instructions :  

 - Add the script.py file to the staging area, then make a new commit with an informative message.

```bash
git add script.py
git commit 
```

#### Results :  

```bash
/home/dq/random_numbers$ git add script.py                                      
/home/dq/random_numbers$ git commit                                             
[master 4c64850] step 8                                                         
 1 file changed, 2 insertions(+), 1 deletion(-)
```


---
# 9: Looking At The Commit History  

You can look at the commit history of a repository using the git log command. This will show you a list of all the commits to the repository, in descending order of creation date. If the output is very long, it will allow you to scroll. You can scroll the log with the up and down arrows, and use the q key to exit.  


### Instructions :  

 - Run git log to explore the commit history of the repository.

```bash
git log
```

#### Results :  

```bash
/home/dq/random_numbers$ git log                                                
commit 4c64850006977fc4eee5bfac440077d71ac75356                                 
Author: Dataquest User <user@dataquest.io>                                      
Date:   Wed Mar 1 18:37:56 2017 +0000                                           
                                                                                
    step 8                                                                      
                                                                                
commit 1e196b4e3f6a6913a687982bbe6ceb5fd8b43c89                                 
Author: Dataquest User <user@dataquest.io>                                      
Date:   Wed Mar 1 18:33:05 2017 +0000                                           
                                                                                
    Initial commit.  Added script.py and README.md
```



---
# 10: Seeing Commit Differences  

You can use git log --stat to see more details about the commits in the git log output.  


### Instructions :  

 - Run git log --stat to explore the commit history of the repository.
 - Press q to exit the screen once you have finished exploring.

```bash
git log --stat
```

#### Results :  

```bash
/home/dq/random_numbers$ git log --stat                                         
commit 4c64850006977fc4eee5bfac440077d71ac75356                                 
Author: Dataquest User <user@dataquest.io>                                      
Date:   Wed Mar 1 18:37:56 2017 +0000                                           
                                                                                
    step 8                                                                      
                                                                                
 script.py | 3 ++-                                                              
 1 file changed, 2 insertions(+), 1 deletion(-)                                 
                                                                                
commit 1e196b4e3f6a6913a687982bbe6ceb5fd8b43c89                                 
Author: Dataquest User <user@dataquest.io>                                      
Date:   Wed Mar 1 18:33:05 2017 +0000                                           
                                                                                
    Initial commit.  Added script.py and README.md                              
                                                                                
 README.md | 1 +                                                                
 script.py | 2 ++                                                               
 2 files changed, 3 insertions(+) 
```