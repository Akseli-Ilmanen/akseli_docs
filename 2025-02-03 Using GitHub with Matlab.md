---
title: 2025-02-03 Using GitHub with Matlab
layout: default 
mathjax: true
tags: #project
---
Tags:  
<br>
![image](images/Pasted image 20250203171701.png)
<br>
<br>
### Set up github repository from folder
<br>
-  `cd` to folder which you would like to upload to github
```cmd
cd C:\Akseli\Pipeline
```
<br>
<br>
 - Initialize the repo
```git
git init
```
<br>
- Make a change to the folder
```git
git add .
```
<br>
- Commit this change
```git
git commit -m "Initial commit"
```
<br>
<br>
- Login to GitHub. Create New repository. For coherency, name the repository the same way your local folder is named (e.g. `Pipeline`). Copy the URL of your new repository.
<br>
- In command window, connect your local repo to the remote GitHub repo
```git
git remote add origin https://github.com/your-username/my-project.git
```
- ❌ replace URL with that of your github repo
<br>
- Push your local changes to github
```git
git push -u origin main
```
<br>
### Push and commit
<br>
- ⚠️ Use the `push_commit.bat` file to update commit and push changes from your local folder to the remote repository
<br>
<br>
### Compare versions & revert to earlier version
<br>
- Option 1: The benefit of running `push_commit.bat` very regularly is that you can compare previous versions of your code with your current code side-by-side.
- Option 2: You can also compare local folders with other local folders. E.g. you could `clone` and `pull` a version of your colleague's code to a separate folder, and then compare specific files with the `compare against` option.
- ❌ You can also revert to earlier versions of your code with the `Revert using Git` option
<br>
![image](images/Pasted image 20250203173949.png)
<br>
<br>
<br>
![image](images/2025-02-03 Init from local folder 2025-02-03_0.excalidraw)
<br>
<br>
### Clone and pull
<br>
- Navigate to the folder, where you would like the remote repository to be copied in
```cmd
cd C:\Documents
```
<br>
- ``Clone`` the remote repository. 
- ❌ This step only needs to be done once.
```cmd
git clone https://github.com/Akseli-Ilmanen/Pipeline_Akseli
```
<br>
<br>
- If the remote repository is updated by another user, you can `pull` an updated version of this repository to your local folder. You can perform this step very easily by just clicking on the `pull_repo_this_folder.bat` file in the file explorer.
<br>
- ❌ This step only makes sense if you would like to discard local changes, and update your local folder with the remote version. If you would like to keep parts of your local folder and only get parts of the remote version, you can explore commands such as `fetch` and `merge`.
<br>
<br>
