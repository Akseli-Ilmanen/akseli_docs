---
mathjax: true
title: 2025-05-08 Crow lab - set up new PC
tags: #project
---
<br>
### General
- Install Matlab
	- Install the following toolboxes: Signal Processing Toolbox, Curve fitting toolbox, Statistics and Machine Learning Toolbox
- Install Anaconda
	- Recommendation: In case you don't use Python already on this machine, I would during the installation "Add Anaconda to the Path Environment Variable"
- Install Git 
	- See also: [2025-02-03 Using GitHub with Matlab - Akseli Docs](https://akseli-ilmanen.github.io/akseli_docs/2025-02-03%20Using%20GitHub%20with%20Matlab.html)
- Install VSCode or another Python code editor

<br>
### File management
- ⚠️ For an overview, of how we maintain our files, see: [2025-04-08 File management in crow lab - Akseli Docs](https://akseli-ilmanen.github.io/akseli_docs/2025-04-08%20File%20management%20in%20crow%20lab)
- This file structure is also (partially compatible) with the [datashuttle libary](https://datashuttle.neuroinformatics.dev/) 

- Add `user_paths.json` to file location `Desktop/user_paths.json`
- [Here](https://drive.google.com/file/d/1MoUN2TgFkYdIDaFjV-jUbFFC26eJfYpq/view?usp=sharing) is a template for `user_paths.json`. Make sure to end each line with `\\",`, except for the last key value pair where the `,` is omitted. 



To install S, please follow the following steps in the terminal:
```cmd
conda create --name files python=3.9
conda activate files
pip install datashuttle ipykernel
conda install -c conda-forge rclone
```

- ⚠️ For further steps, see: [Pipeline_Akseli/functions/file_utils/new_user.iypnb](https://github.com/Akseli-Ilmanen/Pipeline_Akseli/blob/main/functions/file_utils/new_user_datteshuttle.ipynb) and documentation of [datashuttle libary](https://datashuttle.neuroinformatics.dev/) 



<br>
### Phy
- Documentation: [Introduction - phy](https://phy.readthedocs.io/en/latest/)
- Install Phy: See steps in [phy installation](https://github.com/cortex-lab/phy#installation-instructions)
- Plugins: [petersenpeter/phy2-plugins: Plugins for Phy2](https://github.com/petersenpeter/phy2-plugins)
- To download the specific version of May 2025 with plugins, see steps in: [kilosort_pipeline/bat files/open_phy.bat at main · Akseli-Ilmanen/kilosort_pipeline](https://github.com/Akseli-Ilmanen/kilosort_pipeline/blob/main/bat%20files/open_phy.bat)



