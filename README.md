# SaID
This repository is the official implementation of the paper SaID: Simulation-aware Image Denoising Pre-trained Model for Cryo-EM Micrographs.
## v0.1.0
Complete training, testing, and an example micrograph of SaID is available now. <br>
The simulated dataset will be available soon. 
## 1 Operating System
Ubuntu 18.04 or Centos 7 is preferred.
## 2 Requirements
Python >= 3.6.13 <br>
Pytorch >= 1.7.1 <br>
opencv-python 4.5.1 <br>
numpy 1.19.2 <br>
scikit-image 0.17.1 <br>
scikit-learn 0.24.2 <br>
mrcfile 1.3.0 <br>
torchvision >= 0.8.2 <br>
## 3 Test Data
Example real dataset can be found at: <br>
Google Drive: https://drive.google.com/file/d/1ECWjwu7GO55oAQRxKSvF-sP8JMoh8nWr/view?usp=sharing <br>
## 4 Usage
#### The directory is advised to build as follows
```
./SaID
./SaID/denoised_micrographs
./SaID/test_data
./SaID/pre_trained_models
```
#### Run training/testing script
    sh run_test.sh
#### For detailed parameter settings, please run
    python denoise_cmd.py -h
## Acknowledgement
We sinceresly thank following work with their open-sourced code. Code is modified from following work: <br>
Bepler, T., Kelley, K., Noble, A.J., Berger, B. Topaz-Denoise: general deep denoising models for cryoEM and cryoET. Nat Commun 11, 5208 (2020).
