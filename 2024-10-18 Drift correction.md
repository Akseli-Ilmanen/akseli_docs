---
mathjax: true
title: 2024-10-18 Drift correction
tags: #conceptual
---
   
- 📚 (Steinmetz, 2021)
- See supplementary material:  [Neuropixels 2.0: A miniaturized high-density probe for stable, long-term brain recordings | Science](https://www.science.org/doi/10.1126/science.abf4588#supplementary-materials)

<br>
### Outcome of ("vertical") drift correction
<br>

<br>
### Algorithm 

1. Detect **spikes** for drift correction (fluctuations in the LFP have long spatial correlations, and thus cannot be used to determine micron-scale shifts of the probe), 
	1. When detecting spikes, both the vertical position $$y$$ (along the probe) and horizontal position $$x$$ (parallel to surface) is considered, plus a few other parameters, for following steps $$x$$ is then discarded.
2. Split data into batches (default ~2 sec)
3. Log-transform + Gaussian smoothing filter each batch, to get a matrices $$f_{ij}^{t}$$, where $$i$$ indexes the depth bins (depth along probe), and $$j$$ indexes the amplitude bins (amplitude = sum over spikes in batch per y_position)
4. One could use a single batch $$d_{t}$$ to adjust all other batches, but better approach is to jointly optimize on registration target $$F$$ (see image below - in red highlighted)
	1. $$\text{Cost}(D, F) = \sum_{tij} |F_{ij} - f^t_{ij}(d_t)|^2$$
	2. The function $$f_{ij}^{t}(d_{t})$$ describes the "fingerprint" of neural activity for batch $$d_t$$
	3. Choose arbitrary $$t$$ batches from middle of recording $$\rightarrow$$ initialize $$F =f^{t}$$. We first optimize each batch $$d_{t}$$ individually with initialized $$F$$ ($$F$$ is fixed). We only do this for a subset of bins (e.g. $$\approx 20$$) $$\rightarrow$$ then hold $$d_{t}$$ for all $$t$$, and optimize $$F$$ by averaging over all batches $$d_{t}$$ (see image below)
5. Then the batches are adjusted ("drift correction") using [Kriging](https://en.wikipedia.org/wiki/Kriging) interpolation

 - ⚠️ There are two drift estimation strategies: One can assume that there is 1) consistent drift across the probe (**rigid estimation**) or it  2) varies as a function of depth (**nonrigid** **estimation**). E.g. drift may differ in cortical vs sub-cortical regions, therefore nonrigid estimation is useful here.
 - The steps above are for rigid estimation, but to do nonrigid estimation, the steps can be adapted by splitting the batches into segments by vertical position $$y$$ (along the probe), 

<br>
![image](images/Pasted image 20241019203516.png | 400)
[Kriging - Wikipedia](https://en.wikipedia.org/wiki/Kriging)
- ⚠️ see further in  