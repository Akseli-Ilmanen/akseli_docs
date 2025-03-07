---
title: 2025-02-27 Intan headstage, electrodes & channel maps
layout: default 
mathjax: true
tags: #project
---
Tags:  <br>
- 📚 ADXL355 accelerometer: [Accelerometer Calibration](https://intantech.com/files/Intan_RHD2000_accelerometer_calibration.pdf) & [ADXL354/ADXL355 (Rev. A)](https://www.analog.com/media/en/technical-documentation/data-sheets/adxl354_355.pdf) <br>
- 📚 RHD 2132: https://intantech.com/files/Intan_RHD2000_series_datasheet.pdf<br>
- 📚 Cambridge Neurotech dimensions: [Cambridge NeuroTech Product Catalog | PDF](https://www.scribd.com/document/771039846/Cambridge-NeuroTech-Product-Catalog)<br>
<br>
| Name              | Num channels | Company             | Manual                                                                                             |<br>
| ----------------- | ------------ | ------------------- | -------------------------------------------------------------------------------------------------- |<br>
| ASSY-79 E-1 & E-2 | 16           | Cambridge Neurotech | [ASSY-79-E-1-E-2-map.pdf](https://www.cambridgeneurotech.com/assets/files/ASSY-79-E-1-E-2-map.pdf) |<br>
| ASSY-79 P-1 & P-2 | 16           | Cambridge Neurotech | [ASSY-79-P-1-P-2-map.pdf](https://www.cambridgeneurotech.com/assets/files/ASSY-79-P-1-P-2-map.pdf) |<br>
<br>
![image](images/Pasted image 20250227185300.png)<br>
<br>
<br>
![image](images/Pasted image 20250227185346.png)<br>
<br>
![image](images/2025-02-27 Intan headstage and channel maps 2025-02-27.excalidraw)<br>
- ⚠️ P-1 & P-2/E-1 & E-2 $$\rightarrow$$ have the same contact ID configuration in terms of how they are organized above "omnetics print side" (electrode plugs)<br>
<br>
| ASSY-79 P-1 & P-2/E-1 & E-2 (contact ID) | Channelmap (inXX/A-0XX) |<br>
| ---------------------------------------- | ----------------------- |<br>
| 1                                        | in20                    |<br>
| 2                                        | in19                    |<br>
| 3                                        | in21                    |<br>
| 4                                        | in18                    |<br>
| 5                                        | in22                    |<br>
| 6                                        | in17                    |<br>
| 7                                        | in23                    |<br>
| 8                                        | in16                    |<br>
| 9                                        | in8                     |<br>
| 10                                       | in15                    |<br>
| 11                                       | in9<br>                 |<br>
| 12                                       | in14                    |<br>
| 13                                       | in10                    |<br>
| 14                                       | in13                    |<br>
| 15                                       | in11                    |<br>
| 16                                       | in12                    |<br>
<br>
<br>
- ⚠️ Channelmap column (if contact ID col sorted from 1-16) $$\rightarrow$$ <br>
```python<br>
# ASSY-79 P-1 & P-2/E-1 & E-2<br>
chanMap = np.array([20, 19, 21, 18, 22, 17, 23, 16, 8, 15, 9, 14, 10, 13, 11, 12])<br>
```<br>
<br>
<br>
![image](images/Pasted image 20250227185402.png)<br>
<br>
<br>
