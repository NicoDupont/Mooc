03/2017  
Dataquest : Data Analyst Path  
Step 3: The Command Line  
SubStep :  Git and Version Control  : Git branches  
mercredi, 01. mars 2017 08:52 



---
# 1: Git Branches  

As you may recall from the last mission, it's very common for git to be used in large teams, when collaboration is necessary between many programmers all making changes to a repo at the same time.  

In cases like this, it quickly becomes difficult for everyone to work off of the master branch. Let's imagine that we start with two files, bot.py, and README.md:  

see img/im15.png  

Let's say we have three people working on a team: Seashell Sally, Rocky Raccoon, and Superman. Each of them makes the following changes:  

see img/im16.png  

Each of them commits their changes. Since they're all working on the master branch, this results in this commit history:  

see img/im17.png  

Each of them has a different most recent commit. Even worse, all of the commits make changes to the same files. There's no way for git to determine what changes are the "correct" ones, so they will have issues if they all try to push to the remote. Let's see what happens if Superman pushes to the remote:    

see img/im18.png  

NNow Rocky and Sally can't push to the remote, because commits 456 and 765 conflict with Superman's commit b53. Rocky, Sally, and Superman edited the same lines in the same files. This results in something called a merge conflict, which is painful to fix, and something we'll talk about in the next mission.  

Luckily, git gives us a few ways to both avoid merge conflicts. The best way is a concept called branches. With branches, you can create several different work areas within the same repo. It's common for a new branch to be created whenever you want to make a change to a project, and then the branch to be merged into the master branch when it's done.  

Here's an example, where Superman, Rocky, and Sally each make their own branches:  

see img/im19.png  

Each of them originally pulled the master branch, which has the commit f34. They then created separate branches: Superman created enchancement, Rocky created rocky, and Sally created shells. They each made a commit on their own branch.  

This way, when each of them pushes their branch to the remote, it's stored separately, and doesn't conflict with everyone else's changes. The remote would then have the branches master, enhancement, rocky, and shells. They'd eventually want to merge the branches into master, but having branches enables each of them to make changes to the repo separately without their changes conflicting with everyone else's.  

Imagine if Sally wants to make 10 more commits before merging, and Rocky wants to make 2. Branches make it much faster and more flexible to develop.  

You can create a branch with the git branch command. git branch rocky will create a branch called rocky. You can then switch to the branch using the git checkout command, by typing git checkout rocky. If you want to save a command, you can combine them with git checkout -b rocky, which will create a branch rocky then switch to it.  

### Instructions :

 - Clone the repo chatbot from /dataquest/user/git/chatbot to /home/dq/chatbot.
 - Create a branch called more-speech in the repo chatbot.
 - Switch to the branch more-speech.
 - Run bot.py using python to see what happens.

```bash
git clone /dataquest/user/git/chatbot
ls
cd chatbot
git branch -b more-speed
python bot.py
```

#### Results :

```bash
/home/dq$ git clone /dataquest/user/git/chatbot                                 
Cloning into 'chatbot'...                                                       
done.                                                                           
/home/dq$ cd chatbot                                                            
/home/dq/chatbot$ git checkout -b more-speech                                   
Switched to a new branch 'more-speech'                                        
/home/dq/chatbot$ python bot.py                                                 
Hello, let's chat!
```



---
# 2: Switching Branches  

Once we create a branch, we can make changes to it the same way that we can with the master branch. We just have to alter the files, add them to the staging area, and then commit them.  

The main wrinkles come into play when we switch branches. Switching to a branch will change the working directory to reflect the latest commit in that branch. Switching to a new branch, making a new commit, then switching back to master will switch our working directory to the state of the latest commit in master.   

see img/im20.png

In the example above, the branch enhancement has one commit more than master. When we switch to the enhancement branch, the working directory will contain a file called bot.py that contains the code print('2'). If we switch to the master branch, the working directory will be altered by git to contain a file called bot.py that contains the code print('1').  

This is very useful when we want to work on additions to a project that require different amounts of testing or development time. By separating them into separate branches, we can save the state of each addition, without them conflicting with each other.  

The git checkout command will let you switch branches. When you change branches but still have changes in the working directory that aren't committed yet, git checks to see if there's a potential merge conflict with the branch you're switching to. If there is, git won't let you change branches.  

### Instructions :

 - Switch to the more-speech branch.
 - Edit bot.py to print more output when it's run.
 - Make a commit with the message Added more output.

```bash
git checkout more-speech
git add *
git commit
```

#### Results :

```bash
/home/dq/chatbot$ python bot.py                                                 
Hello, let's chat!                                                              
/home/dq/chatbot$ git checkout more-speech                                      
Already on 'more-speech'                                                        
/home/dq/chatbot$ nano bot.py                                                   
/home/dq/chatbot$ git add *                                                     
/home/dq/chatbot$ git commit                                                    
[more-speech 36b58e3] more output on bot.py                                     
 1 file changed, 2 insertions(+), 1 deletion(-)
```




---
# 3: Pushing A Branch To A Remote  

Once we've created a branch and added a commit, we can push the branch to the remote repo. This allows other people to see our changes, and to collaborate with us.  

As you'll recall from the previous mission, it's possible to push a branch to a remote using git push. Once you've pushed a branch to a remote, you can use git branch -r to show all the branches on the remote. git branch -a will show all the branches available locally.  

git branch -r might result in the following output:  

 > origin/HEAD -> origin/master                                                  
 > origin/master                                                                 
 > origin/more-speech
 
This shows that there are two branches, master, and more-speech on the remote called origin, and the currently selected branch (the HEAD branch) is master. HEAD is used by git to refer to both the currently selected branch, and the latest commit in the current branch.  


### Instructions :

 - Push the more-speech branch to the remote origin.
 - List the branches available on the remote.

```bash
git push origin more-speech
```

#### Results :

```bash
/home/dq/chatbot$ git push origin more-speech                                   
Counting objects: 5, done.                                                      
Delta compression using up to 16 threads.                                       
Compressing objects: 100% (3/3), done.                                          
Writing objects: 100% (3/3), 347 bytes | 0 bytes/s, done.                       
Total 3 (delta 0), reused 0 (delta 0)                                           
To /dataquest/user/git/chatbot                                                  
 * [new branch]      more-speech -> more-speech
```


---
# 4: Merging Branches  

When creating a project, it's typical for users to download and use a single version of the project. One example is Django, a popular web framework for Python, which is developed using git and Github. When a user installs Django, they install a single version, not dozens or hundreds of separate branches. However, if you look at the Github repo for Django, there are many different branches that have been used for development of features. Here's one such example, where a feature was developed on a separate branch.  

Typically, the release that is downloaded and used is from the master branch. This means that all the changes made in other branches need to be pulled into the master branch. This can be done through a git concept called merging. Merging allows us to copy commits from one branch into another. This enables us to efficiently develop features for projects on their own branches, without conflicts, then merge them into master so that they're ready to be released and used.  

In order to merge a branch into another branch, we can use the git merge command. Here's an example of a merge:  

see img/im21.png

As you can see above, merging the branch enhancement into the branch master will pull the commit b53 into master, and make b53 the latest commit in master. Whenever anyone switches to the branch master, their working directory will contain the file bot.py, which has the contents print(2).  

In order to merge branch b into branch a, we first have to switch to branch a, then run git merge.  

Merging allows us to efficiently combine changes from multiple branches into one, and have a working directory that reflects all the changes in all of the branches.   

### Instructions :

 - Switch to the master branch of chatbot.
 - Merge more-speech into master.
 - Push master to the remote repo.

```bash
git checkout master
git merge more-speech
git push origin master
```

#### Results :

```bash
/home/dq/chatbot$ git checkout master                                           
Switched to branch 'master'                                                     
Your branch is up-to-date with 'origin/master'.                                 
/home/dq/chatbot$ git merge more-speech                                         
Updating 927e9fb..8150de2                                                       
Fast-forward                                                                    
 bot.py | 3 ++-                                                                 
 1 file changed, 2 insertions(+), 1 deletion(-)                                 
/home/dq/chatbot$ git push origin master                                        
Total 0 (delta 0), reused 0 (delta 0)                                           
To /dataquest/user/git/chatbot                                                  
   927e9fb..8150de2  master -> master
```

---
# 5: Deleting Branches  

A good way to think of a branch is as a collection of commits. Here's an example: 

see img/im22.png

In the above example, both master and enhancement have the commit b53 as the latest commit. Both branches have identical commits. This isn't necessarily bad, but it does mean that the original branch is redundant -- it no longer contains any unique commits. It's typical to use a branch to develop a single feature, merge than branch into master, then delete that branch.  

It's possible to delete branches once all of the commits in them have been merged into another branch. This can be done via the git branch -d command. git branch -d requires you to specify the name of a branch when you call it.  

The branch will be removed completely from your local repo. If a branch has unmerged commits inside it, git will prevent it from being deleted, so its generally safe to delete branches that you think are old or unnecessary.  

Having too many branches can make the repo hard to use, so most software teams tend to delete branches once they've been merged. For example, if you have many branches, listing all the branches in a repo can print hundreds or thousands of lines, making it hard to find the branches you want. It also makes cloning or updating the repo more difficult, because git needs to download information on all of the branches.  


### Instructions :

 - Delete the more-speech branch.

```bash
git branch -d more-speech
```

#### Results :

```bash
/home/dq/chatbot$ git branch -d more-speech                                     
Deleted branch more-speech (was 8150de2).
```




---
# 6: Checking Out Branches From The Remote  

In order to see what other collaborators in the remote repo are working on, we can checkout their branches. This will automatically create a local branch with the same name, and copy any commits from the remote branch to the local branch.  

Let's say we want to checkout a branch called angry-bot from the remote. Doing this will require two steps:  

git fetch will fetch all the current branches and commits from the remote. This won't make any changes to the working directory, but will update git's list of branch names and commits.  
git checkout angry-bot will look for the branch in the local repo and remote repo. Because it only exists in the remote repo, it will be copied into the local repo. angry-bot will also be made the current branch.    


### Instructions :

 - Simulate a second collaborator working on the remote:
	- Clone /dataquest/user/git/chatbot into /home/dq/chatbot2.
	- cd into chatbot2.
	- Create a new branch called happy-bot.
	- Edit bot.py to output happy messages.
	- Commit your changes with the message Made the bot 20% happier!.
	- Push the happy-bot branch to the remote.
 - In your local repo /home/dq/chatbot, checkout the branch.
	- Run git fetch to update the git history.
	- Checkout the happy-bot branch.
	- Run bot.py to make sure the file changed.

```bash
cd ..
git branch -d more-speech
ls
cd chatbot2
git branch -l happy-bot
git checkout happy-bot
nano bot.py
git add *
git commit
git push origin happy-bot
cd ~/chatbot
git fetch
git checkout happy-bot
python bot.py
```

#### Results :

```bash
/home/dq/chatbot$ cd ..
/home/dq/chatbot$ git branch -d more-speech                                     
Deleted branch more-speech (was 8150de2).                                       
/home/dq/chatbot$ cd ..                                                         
/home/dq$ git clone /dataquest/user/git/chatbot chatbot2                        
Cloning into 'chatbot2'...                                                      
done.                                                                           
/home/dq$ ls                                                                    
chatbot  chatbot2                                                               
/home/dq$ cd chatbot2
/home/dq/chatbot2$ git branch -l happy-bot                                      
/home/dq/chatbot2$ git checkout happy-bot                                       
Switched to branch 'happy-bot'                                                  
/home/dq/chatbot2$ nano bot.py                                                  
/home/dq/chatbot2$ git add *                                                    
/home/dq/chatbot2$ git commit                                                   
[happy-bot 4607993] Made the bot 20% happier!.                                  
 1 file changed, 2 insertions(+), 1 deletion(-)
/home/dq/chatbot2$ git push origin happy-bot                                    
Counting objects: 5, done.                                                      
Delta compression using up to 16 threads.                                       
Compressing objects: 100% (3/3), done.                                          
Writing objects: 100% (3/3), 342 bytes | 0 bytes/s, done.                       
Total 3 (delta 1), reused 0 (delta 0)                                           
To /dataquest/user/git/chatbot                                                  
 * [new branch]      happy-bot -> happy-bot                                     
/home/dq/chatbot2$ cd ~/chatbot                                                 
/home/dq/chatbot$ git fetch                                                     
remote: Counting objects: 5, done.                                              
remote: Compressing objects: 100% (3/3), done.                                  
remote: Total 3 (delta 1), reused 0 (delta 0)                                   
Unpacking objects: 100% (3/3), done.                                            
From /dataquest/user/git/chatbot                                                
 * [new branch]      happy-bot  -> origin/happy-bot                             
/home/dq/chatbot$ git checkout happy-bot                                        
Branch happy-bot set up to track remote branch happy-bot from origin.           
Switched to a new branch 'happy-bot'                                            
/home/dq/chatbot$ python bot.py                                                 
Hello, let's chat!                                                              
Kind of dull in here, right?                                                    
Made the bot 20% happier!
```




---
# 7: Finding Differences Across Branches  

A very common development workflow when using git looks like this:  

 - Create a branch off of master with the name of your feature. Let's say feature/better-algo.  
 - Make your changes on the branch, and create commits.
 - Push the branch to the remote repo.
 - Get others to look at and evaluate your branch.
 - Merge the branch into master when everyone thinks it looks okay.
 - Delete the branch.
 
This is how most teams of developers work, and a critical piece of this workflow is being able to see the differences between the feature branch and master. When you use Github as your remote repo, there's a feature called Pull Requests that shows the differences between branches in a nice interface and lets other developers add comments.  

If you're not using Github, you can use git diff to see the differences between branches. This allows you to see line by line what the changes in the branch are. If the changes are additions, they will be colored green and start with a +. If they are deletions, they will be colored red, and start with a -. New files will be shown as additions.  

The order in which you specify the two branches as arguments to git diff influences if the changes are seen as additions or deletions. It's generally prefer to put the "older" branch first, and the one that builds on it second.    


### Instructions :

 - Use git diff to see the differences between happy-bot and master.

```bash
git diff happy-bot master
```

#### Results :

```bash
/home/dq/chatbot$ git diff happy-bot master                                     
diff --git a/bot.py b/bot.py                                                    
index deaed62..4b7412e 100755                                                   
--- a/bot.py                                                                    
+++ b/bot.py                                                                    
@@ -1,4 +1,3 @@                                                                 
 if __name__ == "__main__":                                                     
     print("Hello, let's chat!")                                                
-print('Kind of dull in here, right?')                                          
-print("Made the bot 20% happier!")                                             
+print('Kind of dull in here, right?')                                          
\ No newline at end of file
```



---
# 8: Branch Naming Conventions  

When naming branches, it's common to use a prefix that describes the type of branch, then a slash, then the name of the feature or fix you're making. Here are some typical prefixes, along with example branch names:  

 - Feature -- feature/happy-bot
 - Fix -- fix/remove-error
 - Chore -- chore/add-analytics

Features tend to be commits that add some functionality to the project, fixes resolve bugs and other issues, and chores are things that users of the project won't necessarily notice, but will help you reorganize the project or make the code more efficient.  

By naming branches this way, it makes it easier to organize them, and to figure out what each branch does without having to look at the full diff.    


### Instructions :

 - Create a new branch called feature/random-messages.
 - Edit bot.py to output one of several possible messages based on a random number generator.
 - Commit and push your branch to the remote.

```bash
git branch -l feature/random-message
git checkout feature/random-messages
nano bot.py
git add *
git commit
git push origin feature/random-messages
```

#### Results :

```bash                                                    
/home/dq/chatbot$ git branch -l feature/random-messages                         
/home/dq/chatbot$ git ckeckout feature/random-messages                          
git: 'ckeckout' is not a git command. See 'git --help'.                         
                                                                                
Did you mean this?                                                              
        checkout                                                                
/home/dq/chatbot$ git checkout feature/random-messages                          
Switched to branch 'feature/random-messages'                                    
/home/dq/chatbot$ nano bot.py                                                   
/home/dq/chatbot$ git add *                                                     
/home/dq/chatbot$ git commit                                                    
[feature/random-messages feec51a] delete                                        
 1 file changed, 1 insertion(+), 1 deletion(-)                                  
/home/dq/chatbot$ git push origin feature/random-messages                       
Counting objects: 7, done.                                                      
Delta compression using up to 16 threads.                                       
Compressing objects: 100% (3/3), done.                                          
Writing objects: 100% (3/3), 289 bytes | 0 bytes/s, done.                       
Total 3 (delta 1), reused 0 (delta 0)                                           
To /dataquest/user/git/chatbot                                                  
 * [new branch]      feature/random-messages -> feature/random-messages
```




---
# 9: Branch History  

When you create a branch, the branch will take on the commit history of whatever branch you started from. Here's an example:    

see img/im22.png

In the above example, we have two branches, master, and feature/new-interface. feature/new-interface has one more commit than master, 45g. If our current branch is feature/new-interface, and we create a new branch, the most recent commit in the branch we create will be 45g. If our current branch is master, then we create a new branch, the most recent commit in the new branch will be 67f.  

### Instructions :

 - Checkout the feature/random-messages branch.
 - Create a new branch called feature/spam-messages.
 - Verify that the history of feature/random-messages and feature/spam-messages is the same, and different from master.

```bash
git branch -l feature/random-messages
git checkout feature/random-messages
```

#### Results :

```bash
/home/dq/chatbot$ git checkout feature/random-messages                          
Already on 'feature/random-messages'                                            
/home/dq/chatbot$ git checkout -b feature/spam-messages                         
fatal: A branch named 'feature/spam-messages' already exists.
```