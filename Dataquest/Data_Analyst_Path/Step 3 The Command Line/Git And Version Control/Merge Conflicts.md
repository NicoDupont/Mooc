03/2017  
Dataquest : Data Analyst Path  
Step 3: The Command Line  
SubStep :  Git and Version Control  : Merge Conflicts




---
# 1: Merge Conflicts  

When you merge a branch into another, it can sometimes conflict with commits others have added. Let's say that you're working on a project with another developer named Ninja Jane. You both edit the same file on your own branch, then Jane pushes her branch to the remote and merges it into master:    

see img/im23.png  

This results in the following:  

see img/im24.png  

At this point, the commit history for each branch looks like this:  

see img/im25.png  

Since you and Jane branched off of master at the same time, and you both made one commit, the history of the branches is almost identical. However, the latest commit for master and shuriken is 45g, and the latest commit for superbot is 782.  

When you try to merge superbot into master, git will notice that 45g and 782 both come immediately after 67f, and both edit the same lines in the same files. Because both commits are based on 67f, they are equally valid, and this causes a merge conflict. Git can't overwrite the changes in master with the changes from superbot, because git doesn't know which changes are the "correct" ones. Git is based around the principle of not losing anyone's work. Because you and Jane both worked on your features, git won't cause the loss of effort by intentionally overwriting one commit with the other.  

It's not possible to just layer the commits on top of each other, because both 782 and 45g both come immediately after commit 67f. If git layered the changes on top of each other, and applied commit 782 from superbot, Jane's changes in commit 45g would be overwritten and lost. If commit782insuperbotinstead came after the commit45g` in the git history, there would be no conflict.  

In situations where commits can't be merged automatically, git informs the user of a merge conflict, and asks them to sort it out. Sorting out a merge conflict involves editing the code that conflicts to create the "correct" version. This way, the person who wrote the code is in charge of resolving the issue, and git isn't intentionally overwriting anyone's changes.  

### Instructions :

 - Clone the repo chatbot from /dataquest/user/git/chatbot to /home/dq/chatbot.
 - Create a branch.
	- Create a branch called feature/king-bot in the repo chatbot.
	- Switch to the branch feature/king-bot.
	- Edit bot.py and add an appropriately kingly print statement at the end of the file.
Commit your changes.
 - Create another branch with conflicts.
	- Switch to the master branch.
	- Create a branch called feature/queen-bot in the repo chatbot.
	- Switch to the branch feature/queen-bot.
	- Edit bot.py and add an appropriately queenly print statement at the end at the end of the file.
	- Commit your changes.
 - Create a merge conflict.
	- Merge feature/king-bot into master.
	- Try merging feature/queen-bot into master.
	- At this point, you should trigger a conflict.
 
```bash
git clone /dataquest/user/git/chatbot
cd chatbot
git branch -l feature/king-bot
git checkout feature/king-bot
nano bot.py
git add .
git commit
git checkout master 
git branch -l feature/queen-bot
git checkout feature/queen-bot 
nano bot.py
git add .
git commit
git merge feature/king-bot master
git merge feature/queen-bot  master
```

#### Results :

```bash
/home/dq$ git clone /dataquest/user/git/chatbot                         
Cloning into 'chatbot'...                                               
done.
/home/dq$ cd chatbot                                                    
/home/dq/chatbot$ git branch -l feature/king-bot                        
/home/dq/chatbot$ git checkout feature/king-bot                         
Switched to branch 'feature/king-bot'                                   
/home/dq/chatbot$ nano bot.py                                           
/home/dq/chatbot$ git add                                               
Nothing specified, nothing added.                                       
Maybe you wanted to say 'git add .'?                                    
/home/dq/chatbot$ git add .                                             
/home/dq/chatbot$ git commit                                            
[feature/king-bot cdd240d] first add                                    
 1 file changed, 2 insertions(+), 1 deletion(-)                         
/home/dq/chatbot$ git checkout master                                   
Switched to branch 'master'                                             
Your branch is up-to-date with 'origin/master'.                         
/home/dq/chatbot$ git branch -l feature/queen-bot                       
/home/dq/chatbot$ git checkout feature/queen-bot                        
Switched to branch 'feature/queen-bot'                                  
/home/dq/chatbot$ nano bot.py                                           
/home/dq/chatbot$ git add .                                             
/home/dq/chatbot$ git commit                                            
[feature/queen-bot 6d24da2] second add                                  
 1 file changed, 2 insertions(+), 1 deletion(-)
 git merge feature/king-bot master
/home/dq/chatbot$ git merge feature/queen-bot  master                   
error: 'merge' is not possible because you have unmerged files.         
hint: Fix them up in the work tree,                                     
hint: and then use 'git add/rm <file>' as                               
hint: appropriate to mark resolution and make a commit,                 
hint: or use 'git commit -a'.                                           
fatal: Exiting because of an unresolved conflict. 
```



---
# 2: Aborting A Merge  

When a merge conflict occurs, git adds markup lines to the files that have conflicts that identify where the conflicts are. These lines can prevent code from executing properly, because they can't be interpreted by the Python interpreter. Because of this, it's important to immediately resolve conflicts and remove the markup.  

One way to resolve a conflict is to abort the merge. This doesn't actually merge the files together, but instead stops attempting to merge them. This can be done with git merge --abort.  

Aborting the merge is usually an action you would take if you merged one branch into another by accident, or want to deal with large merge conflicts another way. When you abort a merge, git resets the state of the working directory and git history to the state before you tried to merge.    

 

### Instructions :

 - Abort the merge from the last screen that had conflicts.
 
```bash
git merge --abort
```

#### Results :

```bash
/home/dq/chatbot$ git merge --abort
```



---
# 3: Fixing The Conflicts  

When a merge conflict occurs, git will edit the file that contains the conflicts and add markup that indicates what the conflicts are. Here's an example from bot.py in the first screen, when we tried to merge feature/queen-bot into master:  

see img/im26.png    

 This conflict markup indicates that the current branch (or HEAD branch) contains the line print('I am the king'), but the branch we're trying to merge, feature/queen-bot contains the line print('I am the queen'). Since the last commit in each branch is exclusive to that branch, git cannot automatically determine which line is the most recent edit. This means that you have to manually edit the file to remove the lines that git added, and just leave what the line actually should be.  

Here's how you might remove the conflict markup and only keep the code you want:  

```bash
print('I am the queen')
```

In the above example, we removed all the git confict markup, and just left the line print('I am the queen). After doing this for each section of conflict markup, we would then commit the file, which would conclude the merge.  

### Instructions :

 - Swich to the master branch of the chatbot repo.
 - Merge feature/queen-bot into master.
 - Fix the merge markup so the lines from feature/queen-bot are the ones that are retained.
 - Add the changes to the staging area and merge them with the commit message Fixed conflicts.
 - Push master to the remote.
 
```bash
git merge feature/queen-bot
echo "print('I am the queen')" > bot.py
git add .
git commit -m "Fixed conflicts"
git push origin master
```

#### Results :

```bash
/home/dq/chatbot$ git checkout master                                   
Already on 'master'                                                     
Your branch is ahead of 'origin/master' by 1 commit.                    
  (use "git push" to publish your local commits)                        
/home/dq/chatbot$ git merge feature/queen-bot                           
Auto-merging bot.py                                                     
CONFLICT (content): Merge conflict in bot.py                            
Automatic merge failed; fix conflicts and then commit the result.       
/home/dq/chatbot$ echo "print('I am the queen')" > bot.py               
/home/dq/chatbot$ git add .                                             
/home/dq/chatbot$ git commit -m "Fixed conflicts"                       
[master 8788c45] Fixed conflicts                                        
/home/dq/chatbot$ git push origin master                                
Counting objects: 11, done.                                             
Delta compression using up to 16 threads.                               
Compressing objects: 100% (8/8), done.                                  
Writing objects: 100% (9/9), 813 bytes | 0 bytes/s, done.               
Total 9 (delta 2), reused 0 (delta 0)
```



---
# 4: Multi-Line Conflicts  

In the previous example, only one line conflicted. However, when you're working with larger teams and bigger features, it's possible to have a conflict across multiple lines.  

Let's say bot.py in the master branch contains the following code:  

```python
for i in range(4,20):
    print("This is the {0}th time I've complimented you!".format(i))
```

bot.py in the feature/king-bot branch contains the following code:  

```python
for i in range(0,3):
    print("Off with his head!")
for i in range(4,20):
    print("This is the {0}th time I've complimented you!".format(i))
```

bot.py in the feature/queen-bot branch contains the following code:  

```python
print("Hello")
print("Off with your head!")
for i in range(4,20):
    print("This is the {0}th time I've complimented you!".format(i))
```

In this case, the first two lines of bot.py would conflict if we tried to merge both feature/king-bot and feature/queen-bot into master. We'd get conflict markup that looked like this:   

```python
<<<<<<< HEAD                                                                    
for i in range(0,3):
    print("Off with his head!")                                                          
=======                                                                         
print("Hello")
print("Off with your head!")                                                         
>>>>>>> feature/queen-bot 
for i in range(4,20):
    print("This is the {0}th time I've complimented you!".format(i))
```    

When git detects a multi-line conflict, it will place the entire block into one merge conflict. This makes it much easier to handle larger merge conflicts, such as when a whole function is edited.  

Resolving these merge conflicts is the same as resolving single-line merge conflicts. You'll just need to remove the conflict markup and keep whatever code lines you want to keep.    

 

### Instructions :

 - Switch into the /home/dq/chatbot repo.
 - Switch to the master branch.
 - Create a branch that randomly prints statements.
	- Create a branch called feature/random-printing in the repo chatbot.
	- Switch to the branch feature/random-printing.
	- Edit bot.py and add a block that prints one of three random messages at the end.
	- Commit your changes.
 - Create another branch with conflicts.
	- Switch to the master branch.
	- Create a branch called feature/dice-roller in the repo chatbot.
	- Switch to the branch feature/dice-roller.
	- Edit bot.py and add a block that generates and displays two random numbers at the end.
	- Commit your changes.
 - Create a merge conflict.
	- Merge feature/random-printing into master.
	- Try merging feature/dice-roller into master.
	- At this point, you should trigger a conflict.
 - Resolve the merge conflict.
	- Resolve the conflict by editing bot.py
	- Remove the merge conflict markup.
	- Keep whatever code lines you want.
	- Commit bot.py with the message Resolved multi-line conflict.
 - Push the master branch of chatbot to the remote repo.

 
```bash
cd chatbot
git checkout -b feature/random-printing
printf "\nmessages=['I am great', 'You are great', 'I need more outside time']\nimport random\nmsg=random.choice(messages)\nprint(msg)" >> bot.py
git add .
git commit -m "Add random printing"
git checkout master
git checkout -b feature/dice-roller
printf "\nimport random\nd1=random.randint(1,6)\nd2=random.randint(1,6)\nprint('D1: {0} D2: {1}'.format(d1, d2)" >> bot.py
git add .
git commit -m "Add dice rolling"
git checkout master
git merge feature/random-printing
git merge feature/dice-roller
printf "\nimport random\nd1=random.randint(1,6)\nd2=random.randint(1,6)\nprint('D1: {0} D2: {1}'.format(d1, d2)" > bot.py
git add .
git commit -m "Resolved multi-line conflict"
git push origin master
```

#### Results :

```bash
/home/dq/chatbot$ git checkout -b feature/random-printing               
Switched to a new branch 'feature/random-printing'                      
/home/dq/chatbot$ printf "\nmessages=['I am great', 'You are great', 'I 
need more outside time']\nimport random\nmsg=random.choice(messages)\npr
int(msg)" >> bot.py                                                     
/home/dq/chatbot$ git add .                                             
/home/dq/chatbot$ git commit -m "Add random printing"                   
[feature/random-printing 5a5d46b] Add random printing                   
 1 file changed, 5 insertions(+)                                        
/home/dq/chatbot$ git checkout master                                   
Switched to branch 'master'                                             
Your branch is up-to-date with 'origin/master'.                         
/home/dq/chatbot$ git checkout -b feature/dice-roller                   
Switched to a new branch 'feature/dice-roller'                          
/home/dq/chatbot$ printf "\nimport random\nd1=random.randint(1,6)\nd2=ra
ndom.randint(1,6)\nprint('D1: {0} D2: {1}'.format(d1, d2)" >> bot.py
/home/dq/chatbot$ git checkout master                                   
Switched to branch 'master'                                             
Your branch is up-to-date with 'origin/master'.                         
/home/dq/chatbot$ git merge feature/random-printing                     
Updating 454e2a1..5a5d46b                                               
Fast-forward                                                            
 bot.py | 5 +++++                                                       
 1 file changed, 5 insertions(+)                                        
/home/dq/chatbot$ git merge feature/dice-roller                         
Auto-merging bot.py                                                     
CONFLICT (content): Merge conflict in bot.py                            
Automatic merge failed; fix conflicts and then commit the result.
/home/dq/chatbot$ printf "\nimport random\nd1=random.randint(1,6)\nd2=ra
ndom.randint(1,6)\nprint('D1: {0} D2: {1}'.format(d1, d2)" > bot.py     
/home/dq/chatbot$ git add .                                             
/home/dq/chatbot$ git commit -m "Resolved multi-line conflict"          
[master 45730e9] Resolved multi-line conflict                           
/home/dq/chatbot$ git push origin master                                
Counting objects: 11, done.                                             
Delta compression using up to 16 threads.                               
Compressing objects: 100% (9/9), done.                                  
```



---
# 5: Multiple Conflicts  

When working with a larger team, it's possible to have multiple merge conflicts; both multiple conflicts in a single file, and conflicts in multiple files. When working on large projects, with many files, it's common for a single branch to alter dozens of files. When this happens, you may face merge conflicts that are tricky to resolve.  

Although we won't be using them here, this is where git's graphical merge tools can be useful. To use them, you'll need to run the git mergetool command. You'll also generally want to specify the --tool option flag to specify which graphical tool to use. You can see a full list of available tools on your system by running git mergetool --tool-help.  

A graphical merge tool will show you the branches side by side, and highlight differences visually, like this:    

see img/im27.png  

In this particular tool, the HEAD branch is on the right, and called the REMOTE branch, the branch we're merging is on the left and called the LOCAL branch, and the final version is in the center. We need to edit the center version to get the result we want, then save it.  

In the absence of a graphical tool, it's still possible to sort through multiple merge conflicts, it's just a bit more work. All of the merge conflict markup must be removed before committing if there are multiple conflicts.  

### Instructions :

 - Switch into the /home/dq/chatbot repo.
 - Switch to the master branch.
 - Create a branch that inserts print statements into bot.py.
	- Create a branch called feature/more-printing in the repo chatbot.
	- Switch to the branch feature/more-printing.
	- Edit bot.py and add multiple lines that print whatever text you want.
	- Commit your changes.
 - Create another branch that inserts print statements into bot.py.
	- Switch to the master branch.
	- Create a branch called feature/more-printing-2 in the repo chatbot.
	- Switch to the branch feature/more-printing-2.
	- Edit bot.py and add different print statements to the same lines you edited in feature/more-printing.
	- Commit your changes.
 - Create a merge conflict.
	- Merge feature/more-printing into master.
	- Try merging feature/more-printing2 into master.
	- At this point, you should trigger multiple conflicts.
 - Resolve the merge conflict.
	- Resolve the conflicts by editing bot.py and keeping whatever lines you want.
	- Commit bot.py with the message Resolved multiple conflicts.
 - Push the master branch of chatbot to the remote repo.
 
```bash
cd ~
cd chatbot
git checkout -b feature/more-printing
printf "\nmessages=['I am great', 'You are great', 'I need more outside time']\nimport random\nmsg=random.choice(messages)\nprint(msg)" >> bot.py
git add .
git commit -m "Add more printing"
git checkout master
git checkout -b feature/more-printing-2
printf "\nimport random\nd1=random.randint(1,6)\nd2=random.randint(1,6)\nprint('D1: {0} D2: {1}'.format(d1, d2))" >> bot.py
git add .
git commit -m "Add even more printing"
git checkout master
git merge feature/more-printing
git merge feature/more-printing-2
printf "\nimport random\nd1=random.randint(1,6)\nd2=random.randint(1,6)\nprint('D1: {0} D2: {1}'.format(d1, d2))" > bot.py
git add .
git commit -m "Resolved multiple conflicts"
git push origin master
```

#### Results :

```bash
/home/dq/chatbot$ git checkout master                                           
Already on 'master'                                                             
Your branch is up-to-date with 'origin/master'.                                 
/home/dq/chatbot$ git checkout -b feature/more-printing                         
Switched to a new branch 'feature/more-printing'                                
/home/dq/chatbot$ printf "\nmessages=['I am great', 'You are great', 'I need mor
e outside time']\nimport random\nmsg=random.choice(messages)\nprint(msg)" >> bot
.py                                                                             
/home/dq/chatbot$ git add .                                                     
/home/dq/chatbot$ git commit -m "Add more printing"                             
[feature/more-printing f9f14f2] Add more printing                               
 1 file changed, 5 insertions(+), 1 deletion(-)                                 
/home/dq/chatbot$ git checkout master                                           
Switched to branch 'master'                                                     
Your branch is up-to-date with 'origin/master'.                                 
/home/dq/chatbot$ git checkout -b feature/more-printing-2                       
Switched to a new branch 'feature/more-printing-2'                              
/home/dq/chatbot$ printf "\nimport random\nd1=random.randint(1,6)\nd2=random.ran
dint(1,6)\nprint('D1: {0} D2: {1}'.format(d1, d2))" >> bot.py                   
/home/dq/chatbot$ git add .                                                     
/home/dq/chatbot$ git commit -m "Add even more printing"                        
[feature/more-printing-2 cceb3a3] Add even more printing                        
 1 file changed, 5 insertions(+), 1 deletion(-)                                 
/home/dq/chatbot$ git checkout master                                           
Switched to branch 'master'                                                     
Your branch is up-to-date with 'origin/master'.
/home/dq/chatbot$ git merge feature/more-printing                               
Updating 00df578..f9f14f2                                                       
Fast-forward                                                                    
 bot.py | 6 +++++-                                                              
 1 file changed, 5 insertions(+), 1 deletion(-)                                 
/home/dq/chatbot$ git merge feature/more-printing-2                             
Auto-merging bot.py                                                             
CONFLICT (content): Merge conflict in bot.py                                    
Automatic merge failed; fix conflicts and then commit the result.               
/home/dq/chatbot$ printf "\nimport random\nd1=random.randint(1,6)\nd2=random.ran
dint(1,6)\nprint('D1: {0} D2: {1}'.format(d1, d2))" > bot.py                    
/home/dq/chatbot$ git add .
/home/dq/chatbot$ git commit -m "Resolved multiple conflicts"                   
[master 198dbf3] Resolved multiple conflicts                                    
/home/dq/chatbot$ git push origin master                                        
Counting objects: 11, done.                                                     
Delta compression using up to 16 threads.                                       
Compressing objects: 100% (9/9), done.                                          
Writing objects: 100% (9/9), 921 bytes | 0 bytes/s, done.                       
Total 9 (delta 3), reused 0 (delta 0)                                           
To /dataquest/user/git/chatbot                                                  
   00df578..198dbf3  master -> master
```



---
# 6: Accepting Changes From Only One Branch  

There are times during the merge process when you'll know that one branch has the "correct" changes, and only want to keep the changes from that branch, ignoring the other.  

After a merge conflict comes up, you can use git checkout, along with the --ours and --theirs options to keep files from one of the conflicting branches only.  

For example, if you were trying to merge files from feature/queen-bot into master, you could use git checkout --ours . to only keep files from master, and git checkout --theirs . to only keep files from feature/queen-bot. In general, --ours will keep files from the current branch, and --theirs will keep files from the branch being merged in.    

see img/im28.png  

After running git checkout, you'll need to commit the files to complete the merge.  

### Instructions :

 - Switch into the /home/dq/chatbot repo.
 - Switch to the master branch.
 - Create a branch.
	- Create a branch called feature/remove-bot in the repo chatbot.
	- Switch to the branch feature/remove-bot.
	- Delete bot.py.
	- Stage the deleted file using the command git rm bot.py.
	- Commit your changes with the commit message Remove bot.
 - Create another branch with conflicts.
	- Switch to the master branch.
	- Create a branch called feature/keep-bot in the repo chatbot.
	- Switch to the branch feature/keep-bot.
	- Edit bot.py and add a print statement to the end of the file.
	- Commit your changes with the message Keeping bot.py.
 - Create a merge conflict.
	- Merge feature/remove-bot into master.
	- Try merging feature/keep-bot into master.
	- At this point, you should trigger a conflict.
 - Keep only the files from feature/keep-bot.
 - Finish the merge by committing with the message Keeping bot.py
 - Push the branch master to the remote.
 
```bash
cd ~
cd chatbot
git checkout -b feature/remove-bot
git rm bot.py
git commit -m "Remove bot"
git checkout master
git checkout -b feature/keep-bot
printf "\nprint('I want to live')" >> bot.py
git add .
git commit -m "Keep the bot around"
git checkout master
git merge feature/remove-bot
git merge feature/keep-bot
git checkout --theirs .
git add .
git commit -m "Keeping bot.py"
git push origin master
```

#### Results :

```bash
/home/dq/chatbot$ cd ~                                                          
/home/dq$ cd chatbot                                                            
/home/dq/chatbot$ git checkout -b feature/remove-bot                            
Switched to a new branch 'feature/remove-bot'                                   
/home/dq/chatbot$ git rm bot.py                                                 
rm 'bot.py'                                                                     
/home/dq/chatbot$ git commit -m "Remove bot"                                    
[feature/remove-bot 7d00ed3] Remove bot                                         
 1 file changed, 5 deletions(-)                                                 
 delete mode 100755 bot.py                                                      
/home/dq/chatbot$ git checkout master                                           
Switched to branch 'master'                                                     
Your branch is up-to-date with 'origin/master'.                                 
/home/dq/chatbot$ git checkout -b feature/keep-bot                              
Switched to a new branch 'feature/keep-bot'                                     
/home/dq/chatbot$ printf "\nprint('I want to live')" >> bot.py                  
/home/dq/chatbot$ git add .                                                     
/home/dq/chatbot$ git commit -m "Keep the bot around"                           
[feature/keep-bot 41c7d02] Keep the bot around                                  
 1 file changed, 2 insertions(+), 1 deletion(-)
 /home/dq/chatbot$ git checkout master                                           
Switched to branch 'master'                                                     
Your branch is up-to-date with 'origin/master'.                                 
/home/dq/chatbot$ git merge feature/remove-bot                                  
Updating 198dbf3..7d00ed3                                                       
Fast-forward                                                                    
 bot.py | 5 -----                                                               
 1 file changed, 5 deletions(-)                                                 
 delete mode 100755 bot.py                                                      
/home/dq/chatbot$ git merge feature/keep-bot                                    
CONFLICT (modify/delete): bot.py deleted in HEAD and modified in feature/keep-bo
t. Version feature/keep-bot of bot.py left in tree.                             
Automatic merge failed; fix conflicts and then commit the result.               
/home/dq/chatbot$ git checkout --theirs .
/home/dq/chatbot$ git add .                                                     
/home/dq/chatbot$ git commit -m "Keeping bot.py"                                
[master 9543c46] Keeping bot.py                                                 
/home/dq/chatbot$ git push origin master                                        
Counting objects: 8, done.                                                      
Delta compression using up to 16 threads.                                       
Compressing objects: 100% (5/5), done.                                          
Writing objects: 100% (6/6), 584 bytes | 0 bytes/s, done.                       
Total 6 (delta 3), reused 0 (delta 0)                                           
To /dataquest/user/git/chatbot                                                  
   198dbf3..9543c46  master -> master
```



---
# 7: Ignoring Files  
  
There are some files that change very often, and aren't very useful to a project. One example is the .DS_Store file OSX puts in directories. Another is the .pyc files that Python produces when it compiles source files. Neither of these are necessary for the project to work properly, but because they change rapidly, they can create merge conflicts and other problems.  

The best thing to do with these types of files is to tell git to ignore them. By ignoring them, they aren't added to commits, and therefore aren't tracked by git. This means that you don't have to deal with merge conflicts and other issues caused by them.  

In order to tell git to ignore files, we have to first create a file called .gitignore, then add lines to this file to tell git what files to ignore when adding to the staging area and committing. These lines make use of wildcard characters, so you can ignore all files with a certain extension.  

For example, the following lines in .gitignore will ignore all files called .DS_Store, and all files ending with .pyc:  

 > .DS_Store
 > *.pyc
 
By adding the above two lines, any new files named .DS_Store or ending in .pyc won't be added to the staging area or committed in future commits. Existing files that have already been added to a commit will still have their changes tracked and added to new commits.  

There's a git repo with good default .gitignore configurations for popular languages that you can find here.    

### Instructions :

 - Switch into the /home/dq/chatbot repo.
 - Switch to the master branch.
 - Create a file called .gitignore.
 - Add the following lines to .gitignore:
	- .DS_Store
	- *.pyc
 - Commit the changes with the message Added gitignore.
 - Push the master branch to the remote.
 
```bash
cd ~
cd chatbot
git checkout master
printf ".DS_Store\n*.pyc" > .gitignore
git add .
git commit -m "Added gitignore"
git push origin master
```

#### Results :

```bash
/home/dq/chatbot$ cd ..                                                         
/home/dq$ cd chatbot                                                            
/home/dq/chatbot$ git checkout master                                           
Already on 'master'                                                             
Your branch is up-to-date with 'origin/master'.                                 
/home/dq/chatbot$ printf ".DS_Store\n*.pyc" > .gitignore                        
/home/dq/chatbot$ git add .                                                     
/home/dq/chatbot$ git commit -m "Added gitignore"                               
[master 3124e6b] Added gitignore                                                
 1 file changed, 2 insertions(+)                                                
 create mode 100644 .gitignore                                                  
/home/dq/chatbot$ git push origin master                                        
Counting objects: 4, done.                                                      
Delta compression using up to 16 threads.                                       
Compressing objects: 100% (2/2), done.                                          
Writing objects: 100% (3/3), 322 bytes | 0 bytes/s, done.                       
Total 3 (delta 0), reused 0 (delta 0)                                           
To /dataquest/user/git/chatbot                                                  
   3d45b85..3124e6b  master -> master
```



---
# 8: Removing Cached Files
As mentioned in the previous screen, adding files to .gitignore doesn't remove any files that have already been added to a git commit. Any changes to these files will still be tracked by git, and added to future commits. This can be frustrating, especially when those files cause merge conflicts that take effort to resolve.  

In situations like this, removing files from the git cache can be helpful. This will prevent git from tracking changes in those files, and adding them into future commits.  

This can be done with the git rm command, and the --cached flag. For example, the below command will remove any file called .DS_Store from the git cache, and prevent it from being tracked:  

```bash
git rm --cached .DS_Store
```

This will remove any files called .DS_Store from your git repo, but not from your working directory. The files will still exist on your computer, but be invisible to git for version tracking purposes.      

### Instructions :

 - Switch into the /home/dq/chatbot repo.
 - Switch to the master branch.
 - Remove bot.py from the git cache.
 - Commit your changes with the message Removed bot.py. Remember not use git add here, as this will add bot.py back in!
 - Push the master branch to the remote.
 
```bash
cd ~
cd chatbot
git checkout master
git rm --cached bot.py
git commit -m "Removed bot.py"
git push origin master
```

#### Results :

```bash
/home/dq/chatbot$ cd ..                                                         
/home/dq$ cd chatbot                                                            
/home/dq/chatbot$ gi checkout master                                            
bash: gi: command not found                                                     
/home/dq/chatbot$ git checkout master                                           
Already on 'master'                                                             
Your branch is up-to-date with 'origin/master'.                                 
/home/dq/chatbot$ git rm --cached bot.py                                        
rm 'bot.py'                                                                     
/home/dq/chatbot$ git commit -m "Removed bot.py"                                
[master 3324b50] Removed bot.py                                                 
 1 file changed, 6 deletions(-)                                                 
 delete mode 100755 bot.py                                                      
/home/dq/chatbot$ git push origin master                                        
Counting objects: 3, done.                                                      
Delta compression using up to 16 threads.                                       
Compressing objects: 100% (2/2), done.                                          

```