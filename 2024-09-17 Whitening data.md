
 title: 2024-09-17 Whitening data.md
 layout: default 
mathjax: true
tags: #conceptual
---
Tags:  ,  ,  ,  

<br>
### ZCA whitening matrix.

Steps:
1. Zero-center data (Divide by mean $$\mathbf{\bar{x}}$$)

$$\mathbf{x}_\text{centered} = \mathbf{x} - \bar{\mathbf{x}}
$$

2. Decorrelate data:

$$\mathbf{x}_\text{decorrelated} = E^T \mathbf{x}_\text{centered}
$$


3. Create ZCA Whitening matrix:

$$W_{\text{ZCA}} = E D^{-1/2} E^T
$$


4. Apply Whitening matrix: (Matrix multiplication)

$$\mathbf{y} = W_{ZCA} \mathbf{x}_\text{centered}
$$



where:
- $$\mathbf{x}$$ is data
- $$E$$ is matrix of eigenvectors of original $$\mathbf{x}$$
- $$D^{-1/2}$$ is the diagonal matrix of the inverse square roots of the eigenvalues
- $$W_{ZCA}$$ is the whitening matrix

- ❌ Note how, step 2 can be skipped, since ZCA implicitly does decorrelation + sphering in one step


![image](images/Pasted image 20250307171156.png)

<br>

- bottom:  
- ⚠️ Note during decorrelation step, covariance $$\rightarrow$$ 0 (implicit in definition of  ) and during ZCA whitening step $$\rightarrow$$ variance of each diagonal equals 1


<br>
### Kilosort implementation

`wrot` $$\rightarrow$$ $$W_{\text{ZCA}}$$

- ⚠️ A separate whitening vector (`wrot`) is estimated for each channel based on its nearest 32 channels $$\rightarrow$$ for 16ch all our channels

```python
def whitening_from_covariance(CC):
    """Whitening matrix for a covariance matrix CC.
    This is the so-called ZCA whitening matrix.

    """
    E,D,V =  torch.linalg.svd(CC)
    eps = 1e-6
    Wrot =(E / (D+eps)**.5) @ E.T
    return Wrot

```



<br>
### For me

#todo 
- [ ]   understand relationship between eigenvector and change of basis and and dot product

 