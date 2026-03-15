# VisionGuard AI

**Note:** The trained model files and dataset are not included in this repository due to size constraints. These components can be added locally for running and testing the system.

---

## Project Overview

VisionGuard AI is an artificial intelligence–based medical assistance system designed to help in the early detection of Diabetic Retinopathy using retinal fundus images. The system allows users to upload retinal images, after which a deep learning model analyzes the image and predicts the severity level of the disease. Based on the prediction, a virtual assistant chatbot interacts with the patient and provides basic guidance, lifestyle suggestions, and precautionary steps.

The aim of the project is to demonstrate how artificial intelligence can assist in preliminary medical screening and patient awareness, especially in conditions where early detection plays a crucial role in preventing vision loss.

---

## Key Features

* Upload retinal fundus images through a simple user interface
* CNN-based deep learning model for disease severity prediction
* Automated analysis workflow
* Virtual doctor chatbot that communicates results and guidance
* Clean and simple medical-themed user interface
* Modular architecture separating backend, model, and frontend

---

## System Workflow

1. The user uploads a retinal fundus image through the interface.
2. The image is processed and passed to the trained CNN model.
3. The model predicts the severity level of Diabetic Retinopathy.
4. The prediction is sent to a chatbot module.
5. The chatbot interacts with the user and provides basic advice and precautionary steps.

---

## Project Structure

```
VisionGuard_AI
│
├── backend
│   └── Backend logic and API components
│
├── frontend
│   └── UI components for image upload and interaction
│
├── model
│   ├── notebooks
│   │   └── Training and experimentation notebooks
│   └── trained_models
│       └── Model files (not included in repository)
│
├── scripts
│   └── Supporting scripts such as chatbot integration
│
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python
* TensorFlow / Keras
* OpenCV
* NumPy
* Deep Learning (Convolutional Neural Networks)
* Basic Web UI for interaction

---

## Setup Instructions

1. Clone the repository

```
git clone https://github.com/yourusername/VisionGuard_AI.git
cd VisionGuard_AI
```

2. Create a virtual environment

```
python -m venv vg_env
```

3. Activate the environment

Windows:

```
vg_env\Scripts\activate
```

4. Install dependencies

```
pip install -r requirements.txt
```

---

## Educational Purpose

This project is developed as part of an academic semester project focusing on the practical application of artificial intelligence in healthcare assistance systems.

---

## Authors

Devansh Tyagi
Artificial Intelligence Society (AIS)

---
