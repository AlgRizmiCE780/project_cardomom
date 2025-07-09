# Cardamom Disease Classification using EfficientNet & ResNet

This repository presents a deep learning project focused on classifying diseases in cardamom plants using EfficientNet and ResNet architectures. The models are trained on a curated dataset in collaboration with scientists at ICRI Idukki.

> ⚠️ **NOTE**: Due to data-sharing restrictions, the dataset is not included in this repository. Usage of this project is restricted to academic purposes only.

---

## 🔍 Project Overview

This work implements and compares EfficientNet-based classifiers with custom ResNet-based architectures to detect cardamom diseases with high accuracy.

### ✅ Achievements:
- Achieved up to *88.31*% accuracy** with `EfficientNetB1`.
- Trained multiple versions using Adam, SGD, and RMSprop optimizers.
- Built custom ResNet9 architecture for benchmarking.

---
# 🌿 Cardamom Disease Detection using Deep Learning

This repository presents a deep learning project focused on classifying cardamom plant diseases using advanced CNN architectures (EfficientNet and ResNet). The dataset was collected in collaboration with the Indian Cardamom Research Institute (ICRI), Mayladumpara, Idukki, over a span of 65 days during summer.

> ⚠️ **Note:** Due to data-sharing restrictions, the dataset is not included in this repository. The project is strictly for academic and research purposes.

---

## 📸 Dataset Overview

The dataset was built from real-world field images captured under expert supervision from ICRI. It consists of three classes:
- **Healthy**
- **Leaf Blight**
- **Leaf Spot**

**Data Collection Duration:** 65 days  
**Conditions:** Outdoor summer lighting  
**Preprocessing Techniques:**  
- Image normalization  
- Augmentation (rotation, flipping, zoom)  
- Stratified train-validation split  
- Label encoding and resizing to uniform dimensions

---

## 🧠 Model Architectures

We experimented with the following models:

### ✅ EfficientNet Models

| Model Name                      | Optimizer  | Batch Size | LR    | Weight Decay | Clip Val | Epochs | Accuracy |
|--------------------------------|------------|------------|-------|--------------|----------|--------|----------|
| `my_efv_epoch25_batchsize8.pt` | Adam       | 8          | 0.01  | 1e-4         | 0.01     | 25     | 87.3%    |
| `my_efv_cardamom_update2.pt`   | SGD        | 4          | 0.01  | 1e-6         | 0.1      | 25     | 79%      |
| `my_efv_cardamom_update3.pt`   | RMSprop    | 4          | 0.01  | 1e-6         | 0.1      | 25     | N/A      |
| `EfficientNetB4 (latest)`      | Adam       | 8          | 0.001 | 1e-2         | 1.0      | 50     | 88.31%   |

### 🏗️ Custom ResNet9

Developed a simplified ResNet9 variant for benchmarking with fewer parameters but competitive performance for edge deployment scenarios.

---

## 🔍 Project Highlights

- Built the dataset from scratch in a real-world agricultural setting.
- Focused on lightweight CNNs for mobile/edge deployment.
- Model designed for ONNX conversion and integration into drones/rovers for autonomous field scanning.
- Implemented real-time webcam inference prototype (proof-of-concept).
- Tested with multiple optimizers (Adam, SGD, RMSprop) and learning configurations.
## 🚀 Future Work

- Real-time drone integration for automated disease monitoring.
- Expand dataset with more disease categories and seasonal variations.
- Edge deployment using ONNX and NVIDIA Jetson/Coral TPU boards.

## 📚 Tech Stack

- Python, PyTorch
- torchvision, albumentations
- EfficientNet, ResNet
- matplotlib, seaborn
- OpenCV (for webcam inference)

## 📝 License
This project is licensed for **academic use only**. Please contact the author for any commercial or field deployment inquiries.
