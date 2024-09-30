# OCR Application and GOT Model Fine-Tuning

## Overview
This repository contains an OCR application that performs Optical Character Recognition (OCR) on images containing text in both Hindi and English. Additionally, it includes a Jupyter Notebook for fine-tuning the GOT OCR model using custom datasets.

## Components

### 1. OCR Application (`app.py`)
The OCR application is built using Streamlit and utilizes the Hugging Face Transformers library to load a pre-trained OCR model for extracting text from uploaded images.

### GOT_OCR_2 Model 
- The GOT OCR Model (General OCR Theory) is an advanced Optical Character Recognition (OCR) model designed to extract text from images with a focus on high accuracy and adaptability to various types of text, including different fonts and languages. Here are some key features and details:
- Architecture: The GOT model employs a deep learning architecture optimized for OCR tasks, leveraging techniques such as convolutional neural networks (CNNs) and transformer-based models for effective feature extraction and text recognition.
- Multi-Language Support: This model is capable of recognizing text in multiple languages, including Hindi and English, making it versatile for applications in multilingual environments.
- End-to-End Learning: The model is trained in an end-to-end fashion, meaning it learns to process images directly and output recognized text without needing separate steps for feature extraction and classification.
- Pre-Trained Weights: The model comes with pre-trained weights that have been fine-tuned on a diverse dataset, allowing it to generalize well to various text styles and formats.
- Performance: The GOT model has been evaluated for its accuracy and efficiency in recognizing text from images, making it suitable for real-time applications, such as document scanning and automated transcription.

  
#### Features
- **Image Upload**: Allows users to upload images in common formats (JPEG, PNG).
- **Text Extraction**: Extracts text from the uploaded image using a pre-trained OCR model.
- **Keyword Search**: Users can search for specific keywords in the extracted text, with matching keywords highlighted.

#### Running the Application
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/rashibatra19/Text_OCR.git
   cd your-repo-name
2.**Install Dependencies**:
  Create a virtual environment (optional but recommended) and install the required packages:
  ```bash
      python -m venv ocr_env
      source ocr_env/bin/activate  # On Windows use: ocr_env\Scripts\activate
      pip install -r requirements.txt
```
3.**Run the Application**: 
  Execute the following command in your terminal:
    ```bash
      streamlit run app.py
      ```
      Access the application via the URL provided in the terminal (usually http://localhost:8501).
  

2. **Model Fine-Tuning (final.ipynb)**:
    The final.ipynb notebook contains code for fine-tuning the GOT OCR model on a custom dataset. Fine-tuning allows the model to adapt better to specific types of     text or fonts present in the dataset.

- Dataset Preparation: The notebook guides you through loading and preparing a dataset suitable for OCR tasks.
- Model Fine-Tuning: Fine-tunes the pre-trained GOT model using the provided dataset, adjusting the model's weights based on new data.
- Evaluation: Includes steps for evaluating the model's performance on a validation dataset.

3.**Requirements**:
  The project requires the following Python packages, which are listed in requirements.txt:
```bash
    streamlit
    transformers
    torch
    Pillow
```
