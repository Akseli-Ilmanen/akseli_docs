---<br>
title: 2024-12-16 Sync zotero with overleaf over onedrive<br>
layout: default <br>
mathjax: true<br>
tags: #conceptual<br>
---<br>
Steps<br>
<br>
1. Zotero export specific folder as bibtext file to onedrive folder<br>
2. onedrive share "can view", you get a link looking like https://1drv.ms/u/s!AsIihgq-8O6rzrMHILGKy5joGZ9nrw?e=c1vAgi<br>
3. Extract the `key identifier`, e.g. extract `s!AsIihgq-8O6rzrMHILGKy5joGZ9nrw` from `https://1drv.ms/u/s!AsIihgq-8O6rzrMHILGKy5joGZ9nrw?e=c1vAgi`<br>
4. Create a link by combining<br>
<br>
Part 1:<br>
- ❌ keep the same<br>
```python<br>
https://api.onedrive.com/v1.0/shares/<br>
```<br>
<br>
Part 2: (add your key, everything after )<br>
```python<br>
s!AsIihgq-8O6rzrMSdSO1KLn2a7vFWw<br>
```<br>
<br>
Part 3: add suffix root/content <br>
- ❌ keep the same<br>
```python<br>
/root/content<br>
```<br>
<br>
5. in overleaf, go to upload - from external URL - add link, and as filename references.bib<br>
- ⚠️ important: the filename has to be references.bib not just references