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

## 🧠 Model Architectures

### 1. EfficientNet Models

#### `my_efv_epoch25_batchsize8.pt`
- Epochs: 25
- Batch Size: 8
- Optimizer: `torch.optim.Adam`
- Weight Decay: `1e-4`
- Learning Rate: `0.01`
- Gradient Clipping: `0.01`
- Accuracy: **87.3%**

#### `my_efv_cardamom_update2.pt`
- Epochs: 25
- Batch Size: 4
- Optimizer: `torch.optim.SGD`
- Weight Decay: `1e-6`
- Learning Rate: `0.01`
- Gradient Clipping: `0.1`
- Accuracy: **79%**

#### `my_efv_cardamom_update3.pt`
- Epochs: 25
- Batch Size: 4
- Optimizer: `torch.optim.RMSprop`
- Weight Decay: `1e-6`
- Learning Rate: `0.01`
- Gradient Clipping: `0.1`
- Accuracy: *Not recorded*

#### Latest Training (EfficientNetB4)
- Epochs: 50
- Batch Size: 8
- Optimizer: `torch.optim.Adam`
- Weight Decay: `1e-2`
- Learning Rate: `0.001`
- Gradient Clipping: `1.0`
- Accuracy: **88.31%**

---


