---
title: 2024-12-16 Sync zotero with overleaf over onedrive
layout: default 
mathjax: true
tags: #conceptual
---
Steps
<br>
1. Zotero export specific folder as bibtext file to onedrive folder
2. onedrive share "can view", you get a link looking like https://1drv.ms/u/s!AsIihgq-8O6rzrMHILGKy5joGZ9nrw?e=c1vAgi
3. Extract the `key identifier`, e.g. extract `s!AsIihgq-8O6rzrMHILGKy5joGZ9nrw` from `https://1drv.ms/u/s!AsIihgq-8O6rzrMHILGKy5joGZ9nrw?e=c1vAgi`
4. Create a link by combining
<br>
Part 1:
- ❌ keep the same
```python
https://api.onedrive.com/v1.0/shares/
```
<br>
Part 2: (add your key, everything after )
```python
s!AsIihgq-8O6rzrMSdSO1KLn2a7vFWw
```
<br>
Part 3: add suffix root/content 
- ❌ keep the same
```python
/root/content
```
<br>
5. in overleaf, go to upload - from external URL - add link, and as filename references.bib
- ⚠️ important: the filename has to be references.bib not just references