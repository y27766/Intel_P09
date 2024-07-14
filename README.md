# P09 DETECT PIXELATED IMAGES AND DEPIXELATE IT 
### Project Final Report
- [Link to Project Final Report](https://docs.google.com/document/d/1b3h0-VPKK3YG0TWc7Td-sR7nVRxzqkAE/edit?usp=drive_link&ouid=108268979758453571814&rtpof=true&sd=true)

This project involves detecting pixelated images and restoring them to their original quality using machine learning techniques. The project is part of the curriculum for the 2nd year, Department of Computer Science and Engineering at Nitte Meenakshi Institute of Technology.

## Project Overview

The project aims to:
1. Automatically detect pixelation in images.
2. Restore pixelated images to their original state.

## Author

- **Name:** Yashas C Raju
- **Year:** 2nd Year
- **Department:** Computer Science and Engineering
- **Institution:** Nitte Meenakshi Institute of Technology

## Dataset

The dataset consists of images categorized into 'Original' and 'Pixelated' labels. The images are loaded and preprocessed for training and evaluation of the models.

## Objectives

1. **Detect Pixelation:** 
   - Train a Convolutional Neural Network (CNN) to classify images as pixelated or non-pixelated.
   - Evaluate the model using accuracy, precision, recall, and F1-score metrics.

2. **Depixelate Images:** 
   - Use a Generative Adversarial Network (GAN) to restore pixelated images.
   - Evaluate the restoration quality using metrics such as LPIPS and PSNR.

## Workflow

1. **Data Preparation:**
   - Load image paths from the CSV file.
   - Preprocess images (resizing, normalization, etc.).

2. **Model Training:**
   - Train the CNN model for pixelation detection.
   - Train the GAN model for image restoration.

3. **Model Evaluation:**
   - Evaluate the performance of the CNN model on the test set.
   - Evaluate the restoration quality of the GAN model.

4. **Inference:**
   - Use the trained models to detect and depixelate new images.

## Requirements

- Python 3.x
- TensorFlow or PyTorch
- OpenCV
- NumPy
- Pandas
- Matplotlib


