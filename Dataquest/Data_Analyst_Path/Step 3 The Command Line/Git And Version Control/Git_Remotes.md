03/2017  
Dataquest : Data Analyst Path  
Step 3: The Command Line  
SubStep :  Git and Version Control  : Git Remotes  
mercredi, 01. mars 2017 07:41 


---
# 1: Git Remotes  

One of the most useful ways to use git is to use it in conjunction with Github. Using git with Github allows you to push your code to remote repositories. This enables you to:  

 - Share your code with others and build a portfolio.
 - Collaborate with others on your project and build your code together.
 - Download and use code others have created.
 
Here's an example of a remote repository on Github. Repositories can be viewed on your Github profile, and are a great way to build a portfolio and get noticed by recruiters.  

Remote repositories aren't just useful for building a portfolio. Pushing to Github also allows you to collaborate with others on your code. For example, linux is developed on Github, and has thousands of different contributors. Many companies, including Google and Facebook, also use Github to work on code projects across teams.  

Remote repositories also enable you to access and use code you didn't write. For instance, this repo will let you download Amazon's Deep Learning tools and start training models. Since the reposistory is public, it's accessible by anyone, and can be downloaded and used by anyone. Repositories on Github can also be private, in which case they are hidden, and not accessible by others.  

In order to get a remote repository onto your own computer, you'll need to do something called cloning. cloning copies a repository from one location to a folder on your computer. The repository retains all of its git history, and you can work with it just like you would work with a git repository you created yourself.  

In order to clone a remote repository, we'll use the git clone command. If we were cloning from Github, we'd specify a Github URL to clone a repository from.  

Here's how we'd clone the Amazon Deep Learning repo from Github:  

```bash
git clone https://github.com/amznlabs/amazon-dsstne.git
```

https://github.com/amznlabs/amazon-dsstne.git is the URL of the git repository that we're cloning. This will automatically create a folder called amazon-dsstne in our current folder, and place the repository there.  

Since we're working with a simplified remote repository for the purposes of this mission, we'll clone a repository slightly differently:  

```bash
git clone /dataquest/user/git/chatbot
```

This will clone the repository from /dataquest/user/git/chatbot, a path on our local computer, to our current folder, and place it into a folder called chatbot.  

If we specify a second argument to git clone, we can change the folder the repository is saved to:  

```bash
git clone /dataquest/user/git/chatbot silentbot
```

The above code will place the chatbot repository into a folder called silentbot.    


### Instructions :

 - Clone the /dataquest/user/git/chatbot repository into the home folder of the current user.   
 
 This should create a folder called chatbot in /home/dq.

```bash
git clone /dataquest/user/git/chatbot chatbot
```

#### Results :

```bash
/home/dq$ git clone /dataquest/user/git/chatbot chatbot                       
Cloning into 'chatbot'...                                                     
done.                                                                           
/home/dq$ ls                                                                    
chatbot                                                                       
/home/dq$ cd chatbot                                                          
/home/dq/chatbot$ ls                                                          
README.md
```




---
# 2: Making Changes To Cloned Repositories  

Now that we've cloned a repository (or repo for short), we can makes changes in the same way that we did in the last mission. We'll be able to edit files, add them to the staging area, and then commit the changes. These changes will be reflected in the local version of the repo, but not the remote version.  

Here's a diagram showing how the local repo and the remote repo are separate:   

see img/im1.png

After making the commit in the diagram, the local repo will have one more commit than the remote repo, and the file README.md will be different.  

The README.md file is one you'll often see in projects on Github. A README file helps people understand what the project is about and how to install it. It's common for the README file to be in Markdown format, which is a way to create lists and other complex but useful structures using plain text. The markdown format has the .md extension.  

Similar to the diagram above, we'll edit the README.md file to add a line, then commit it to the repository. When updating shared repositories, it's important to add informative messages when comitting, so other people can easily figure out what each commit is doing without reading through the code. This gets really important when debugging issues with code that multiple people are working on.  

### Instructions :

 - cd into the /home/dq/chatbot folder to get into the chatbot repo.
 - Add the line This project needs no installation to the bottom of README.md.
 - Add your changes to the staging area using git add.
 - Commit your changes using git commit, with the commit message Updated README.md.
 - Run git status to see that status of the repo.

```bash
nano README.md
git add
git status
```

#### Results :

```bash
/home/dq/chatbot$ nano README.md                                                
/home/dq/chatbot$ git add                                                       
Nothing specified, nothing added.                                               
Maybe you wanted to say 'git add .'?                                            
/home/dq/chatbot$ git add .                                                     
/home/dq/chatbot$ git commit                                                    
[master 724e166] Updated README.md                                              
 1 file changed, 2 insertions(+), 2 deletions(-)                                
/home/dq/chatbot$ git status                                                    
giOn branch master                                                              
Your branch is ahead of 'origin/master' by 1 commit.                            
  (use "git push" to publish your local commits)                                
                                                                                
nothing to commit, working directory clean                                      
/home/dq/chatbot$ git status                                                    
On branch master                                                                
Your branch is ahead of 'origin/master' by 1 commit.                            
  (use "git push" to publish your local commits)                                
                                                                                
nothing to commit, working directory clean
```




---
# 3: The Master Branch  

In the last screen, when you ran git status, your output looked something like this:    

>On branch master                                                                
>Your branch is ahead of 'origin/master' by 1 commit.                            
>  (use "git push" to publish your local commits)

The first two lines mention the terms branch, master, and origin, all of which may be unfamiliar. We'll look at branch and master in this screen, and origin in the next screen.  

Every git repository consists of one or more branches. Each branch is a slightly different version of the code. We'll dive more into branches and how they work in the next mission, but the important fact to know now is that the main branch of a git repo is typically called master. Developers will create separate branches when they want to work on new features for a project, then add the commits in those branches back into master when the features are ready.  

All of the changes we've made so far have been on the master branch of the chatbot repo. The master branch is usually the most up-to-date shared version of any code project.  

We can check what branch we're on by using git branch. This will list all of the branches in the repo, along with the branch that is currently active.  

nothing to commit, working directory clean   

### Instructions :

 - Use git branch to see what branches exist in the chatbot repo.

```bash
git branch
```

#### Results :

```bash
/home/dq/chatbot$ git branch                                                    
* master
```





---
# 4: Pushing Changes To The Remote  

Once you've made changes to the local version of the repo, you can push those changes to the remote repo so that your changes can be viewed by everyone. Changes you make locally are only reflected in your local repo. Unless you push these changes to the remote, the remote repo doesn't change.  

To do this, you'll need to use the git push command, which pushes commits from your local repo to the remote repo. Here's a diagram showing what happens when you run git push:    

see img/im2.png  

As you can see, until you push the branch to the remote repo, the changes are only in your local repo. Once you push to the remote, it's updated with your latest changes. Anyone else who pulls from the remote repo will then have access to the same two commits as you do in your local repo.  

When you run git push, you'll need to specify both the name of a remote to push to, and the name of a branch to push. When you clone a repo, git automatically names the remote repo origin. This means that the following command will push the master branch to the remote repo:  

```bash
git push origin master
```

It's possible, but rare, that a remote will have a name other than origin. In cases where you're unsure, you can list remotes using git remote.  

git remote will list all of the remotes. If you specify the -v option, you'll get additional information about where the remote repos are located.  


### Instructions :

 - Push the master branch of the local chatbot repo to the remote origin.

```bash
it push origin master
```

#### Results :

```bash
/home/dq/chatbot$ git push origin master                                        
Counting objects: 5, done.                                                      
Delta compression using up to 16 threads.                                       
Compressing objects: 100% (2/2), done.                                          
Writing objects: 100% (3/3), 319 bytes | 0 bytes/s, done.                       
Total 3 (delta 1), reused 0 (delta 0)                                           
To /dataquest/user/git/chatbot                                                  
   20bf682..724e166  master -> master
```




---
# 5: Viewing Individual Commits  

If you'll recall from the previous mission, git stores the history of the repo as a series of commits. Each commit contains the difference between the current commit and the previous commit. This allows git to very efficiently store history, and replay that history to reconstruct the working directory. The working directory is the folder on your computer where you edit files, then add the changes, then make commits. Commits are separate from the working directory, and are a snapshot of all the files in the working directory at a specific point in time.  

You can see the full commit history of the master branch of the local chatbot repo with git log. Here's the output you might get from git log:  


	commit 6a95e94ea10caa28013b767510d4bc59369d83fa                                 
	Author: Dataquest <me@dataquest.io>                                             
	Date:   Wed May 18 21:56:27 2016 +0000                                          
	​
	    Updated README.md                                                           
	​
	commit 8a1ca35dd5c5de8f93aa6cbbd153caa40233386c                                 
	Author: Dataquest <me@dataquest.io>                                             
	Date:   Wed May 18 21:55:33 2016 +0000                                          
	​
	    Add the initial version of README.md    
	</me@dataquest.io></me@dataquest.io>

This history shows two commits, the first one with the message Add the initial version of README.md, and the second with the message Updated README.md. The great thing about git is that it stores both commits, so we can easily revert back to a previous commit if we want to.  

In order to do this, we'll need to use the hash of the commit. The hash is a unique identifier for each commit, and allows us to perform operations like reverting to a specific commit. In the above output, the first commit has the id 8a1ca35dd5c5de8f93aa6cbbd153caa40233386c, and the second commit has the id 6a95e94ea10caa28013b767510d4bc59369d83fa.  

We can use the git show command, along with a hash, to see what changed in a specific commit. Running git show 6a95e94ea10caa28013b767510d4bc59369d83fa in the above example would result in:  


	commit 6a95e94ea10caa28013b767510d4bc59369d83fa                                 
	Author: Dataquest <me@dataquest.io>                                             
	Date:   Wed May 18 21:56:27 2016 +0000                                          
	​
	    Updated README.md                                                           
	​
	diff --git a/README.md b/README.md                                              
	index f4871de..9c05964 100644                                                   
	--- a/README.md                                                                 
	+++ b/README.md                                                                 
	@@ -1,3 +1,3 @@                                                                 
	 README
	​
	-This is a README file.  It's typical for Github projects to have a README.  A README gives information about what the project is about, and usually how to install and use it.
	\ No newline at end of file                                                     
	+This is a README file.  It's typical for Github projects to have a README.  A README gives information about what the project is about, and usually how to install and use it.This project needs no installation!
	</me@dataquest.io>

This indicates that the README.md file was changed in this commit, and the line This project needs no installation! was added. a/README.md is the file state before the commit, and b/README.md is the file state after the commit.  

git show will allow you to scroll up and down and side to side. You'll need to type q to exit it.    


### Instructions :

 - Use the git log command to find the commit hash corresponding to the most recent commit in the chatbot repo.
 - Use the commit hash, along with git show to see what the commit did.


```bash
git log
git show
```

#### Results :

```bash
/home/dq/chatbot$ git log                                                       
commit 724e1663a39e6338a3da8c623b4800b854db03f3                                 
Author: Dataquest <me@dataquest.io>                                             
Date:   Wed Mar 1 19:25:44 2017 +0000                                           
                                                                                
    Updated README.md                                                           
                                                                                
commit 20bf682963a38c8e58bae9d444b903f8b65f2018                                 
Author: Dataquest <me@dataquest.io>                                             
Date:   Wed Mar 1 19:24:06 2017 +0000                                           
                                                                                
    Add the initial version of README.md
    
/home/dq/chatbot$ git show                                                      
commit 724e1663a39e6338a3da8c623b4800b854db03f3                                 
Author: Dataquest <me@dataquest.io>                                             
Date:   Wed Mar 1 19:25:44 2017 +0000                                           
                                                                                
    Updated README.md                                                           
                                                                                
diff --git a/README.md b/README.md                                              
index f4871de..f53e7f2 100755                                                   
--- a/README.md                                                                 
+++ b/README.md                                                                 
@@ -1,3 +1,3 @@                                                                 
 README                                                                         
-                                                                               
-This is a README file.  It's typical for Github projects to have a README.  A R
EADME gives information about what the project is about, and usually how to inst
all and use it.                                                                 
\ No newline at end of file                                                     
+This project needs no installation                                             
+This is a README file.  It's typical for Github projects to have a README.  A R
EADME gives information about what the project is about, and usually how to inst
all and use it.This project needs no installation
```




---
# 6: Commits And The Working Directory  

Before we dive more into commits, let's take a closer look at the working directory and how it interacts with commits. As you may recall from the previous mission, the git commit workflow has three main components:  

- The working directory
- The staging area
- Commits

The working directory is the folder that you're version controlling with git, and the contents of the working directory are what you see when you list the contents of the folder with ls. In our case, /home/dq/chatbot is the working directory. You can edit the working directory by changing or adding files.  

So let's say our working directory looks like this:    

see img/im3.png  

In the above example, we have one file, called README.md, in the working directory. There are no files in the staging area, and no commits.  

When we run git add, git adds the changes between the most recent commit and our working directory into the staging area, like this:  

see img/im4.png  

When we run git commit, we create a commit that contains all of the changes in the staging area. The commit also has a unique commit hash, so we can refer to it later. Note how making a commit removes all changes from the staging area:  

see img/im5.png  

We now have a commit, with the hash 53d, that is a snapshot of the working directory at the moment, when it contains a file called README.md, with the contents This is a README!.  

We can then add a file to the working directory, and edit README.md. This will only affect the working directory, where we're making changes:  

see img/im6.png  

We can then use git add to stage our changes:  

see img/im7.png  

In this case, git adds both the new and the changed file into the staging area. We can then commit the change:  

see img/im8.png  

We now have two commits, each storing a snapshot of our working directory at a different point in time. In the next screen, we'll cover how to switch between commits to change the files in our working directory.  

You can see the difference between two commits by using git diff. Just pass the two commit hashes as arguments to git diff. If you want to save yourself typing time, you can also use the first few characters of the commit hash (usually 4 is enough) to uniquely identify the commit. The order in which you pass the two hashes to git diff influences whether changes appear as deletions or additions.  

You'll need to use q to exit git diff when you're done.  

### Instructions :

 - Use git diff to find the difference between your two commits.

```bash
git diff 
```

#### Results :

```bash

```




---
# 7: Switching To A Specific Commit  

Now that we know about commit hashes, we can use them to switch to a specific commit. Switching between commits allows us to easily move between different historical versions of the project. For example, if you introduce a change that causes issues, and you want to use an earlier version, switching between commits will let you do so.  

Commit hashes are preserved between the local repo and the remote repo. For instance, let's say we have two commits, c12 and c53:    

see img/im9.png  

c12 originally existed on the remote, but when we pulled it locally, the commit kept the same hash. This is because the commit is the same on both the remote and locally -- the same changes were made to the same files. When we changed a file and made a commit locally, it was given the hash c53. When we later pushed this commit to the remote, it kept the same hash, because it was still the same commit. In the above diagram, both the local repo and the remote repo have two commits, c12 and c53. We can switch between commits in the local repo without changing what commits are in the remote repo. We can do this with the git reset command:  

see img/im10.png  

As you can see above, the commit is on the left, and what your working directory looks like on the right. If you use git reset --hard c12, it switches back to the commit c12, and changes all the files in the working directory so that they are the exact same as the files in the commit. This will essentially let you rewind the repo to past commits if there are problems with commits, or if you want to see what the project looked like at an earlier point in time.  

The --hard flag resets the working directory and the git history to a specific state. If we omitted the flag, or instead used the --soft flag, it would keep the working directory the same, and only reset the git history.  

### Instructions :

 - Use the git log command to find the commit hash corresponding to the oldest commit in the chatbot repo.
 - Use git reset to reset the chatbot repo to the oldest commit.
 - Explore README.md, and see what text is contained in it.

```bash
git log
git reset --hard 20bf682963a38c8e58bae9d444b903f8b65f2018
```

#### Results :

```bash
/home/dq/chatbot$ git log                                                       
commit 724e1663a39e6338a3da8c623b4800b854db03f3                                 
Author: Dataquest <me@dataquest.io>                                             
Date:   Wed Mar 1 19:25:44 2017 +0000                                           
                                                                                
    Updated README.md                                                           
                                                                                
commit 20bf682963a38c8e58bae9d444b903f8b65f2018                                 
Author: Dataquest <me@dataquest.io>                                             
Date:   Wed Mar 1 19:24:06 2017 +0000                                           
                                                                                
    Add the initial version of README.md
/home/dq/chatbot$ git reset --hard 20bf682963a38c8e58bae9d444b903f8b65f2018     
HEAD is now at 20bf682 Add the initial version of README.md
```





---
# 8: Pulling From A Remote Repo  

Now that we reverted our local chatbot repo to an older version, the remote repo actually has a newer commit than our local repo. This happens often in projects when other people make changes to code, and push it to a remote repo. Here's a diagram showing which commits exist in which locations:    

see img/im11.png  

In cases where the latest commit in your local repo is older than the latest commit in the remote repo, you can use git pull to update the current branch with the latest commits. git pull will also update your working directory to have the same files as the latest commit.  

In our case, we'll be updating the master branch, since the chatbot repo only has a single branch.  

### Instructions :

 - Pull the latest commits from the chatbot remote repo.
 - Inspect the working directory and git history to see what happened.

```bash
git log
git pull
git log
```

#### Results :

```bash
/home/dq/chatbot$ git log                                                       
commit 20bf682963a38c8e58bae9d444b903f8b65f2018                                 
Author: Dataquest <me@dataquest.io>                                             
Date:   Wed Mar 1 19:24:06 2017 +0000                                           
                                                                                
    Add the initial version of README.md                                        
/home/dq/chatbot$ git pull                                                      
Updating 20bf682..724e166                                                       
Fast-forward                                                                    
 README.md | 4 ++--                                                             
 1 file changed, 2 insertions(+), 2 deletions(-)                                
/home/dq/chatbot$ git log                                                       
commit 724e1663a39e6338a3da8c623b4800b854db03f3                                 
Author: Dataquest <me@dataquest.io>                                             
Date:   Wed Mar 1 19:25:44 2017 +0000                                           
                                                                                
    Updated README.md                                                           
                                                                                
commit 20bf682963a38c8e58bae9d444b903f8b65f2018                                 
Author: Dataquest <me@dataquest.io>                                             
Date:   Wed Mar 1 19:24:06 2017 +0000                                           
                                                                                
    Add the initial version of README.md
```



---
# 9: Referring To The Most Recent Commit  

There are many times when using git that you'll want to refer to the most recent commit. It's cumbersome to always use the full commit hash. Git has a special variable, called HEAD, that always refers to the most recent commit in the current branch.  

We can use the HEAD variable to switch to the most recent commit easily. Let's say we modify a file, and we want to undo our changes -- resetting using HEAD will change the working directory to the state of the most recent commit.  

You can also use shortcuts to get older commit hashes. HEAD~1 will get the second newest commit in the local repo, and HEAD~2 will get the third newest commit, and so on. Here's a diagram of a local repo where 646 is the newest hash, and c12 is the oldest on the master branch:   

see img/im12.png

You can use git rev-parse along with the HEAD variable to find the commit hash corresponding to a particular commit number. In the diagram above, git rev-parse HEAD will return 646, and git rev-parse HEAD~3 will return c53.  


### Instructions :

 - Use git reset, along with HEAD, to reset the chatbot repo to the oldest commit.
 - Use git rev-parse, along with HEAD, to get the commit hash of the current commit.

```bash
git reset --hard HEAD~1
git rev-parse HEAD
```