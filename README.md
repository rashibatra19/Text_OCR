# OCR Application and GOT Model Fine-Tuning

## Overview
This repository contains an OCR application that performs Optical Character Recognition (OCR) on images containing text in both Hindi and English. It also includes a Jupyter Notebook for fine-tuning the GOT OCR model using a custom Hindi dataset, resulting in 81% accuracy for Hindi text extraction.

Although the application was fully developed and fine-tuned, due to hardware (GPU) limitations, the fine-tuned model could not be deployed to Streamlit Cloud or Hugging Face Spaces. However, the complete code, model fine-tuning steps, and screenshots showcasing the application's functionality and performance are provided in this repository.

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
  

4.**Keyword Search**: Once text is extracted, users can enter a keyword, and matching sections will be highlighted.

### **2.Model Fine-Tuning (final.ipynb)**:
The final.ipynb notebook contains code for fine-tuning the GOT OCR model using a custom Hindi dataset. 
Despite the model achieving 81% accuracy on Hindi text extraction, deployment was constrained due to the lack of GPU support on platforms like Streamlit Cloud or Hugging Face Spaces.

Dataset Used:https://www.kaggle.com/datasets/prathmeshzade/hindi-ocr-synthetic-line-image-text-pair
- **Fine-Tuning Process**
    - **Dataset Preparation**: The notebook guides you through loading and preparing a custom Hindi dataset for OCR tasks.
    - **Model Fine-Tuning**: The GOT OCR model is fine-tuned on the Hindi dataset to enhance its performance on Hindi text recognition.
    - **Evaluation**: The fine-tuned model achieved an 81% accuracy on extracting Hindi text from images.
      
### 3. Known Issue: Deployment Constraints
Despite the successful completion of both the English and Hindi OCR models, the fine-tuned Hindi GOT OCR model could not be deployed online due to the hardware limitations (lack of GPU on the Streamlit Cloud and Hugging Face Spaces). The model requires GPU support for loading and real-time inference, which was not available on these platforms).

### Alternative: Screenshots for Demonstration
To demonstrate the full functionality of the OCR application and the fine-tuned model's performance, I have attached screenshots showing the:

  - Successful extraction of Hindi and English text from images.
  - Results of the keyword search feature on the extracted text.
  - Performance metrics for the fine-tuned Hindi OCR model.
  - Screenshots
    
**The screenshots include:**
  - Image upload interface.
  - Text extraction results (both Hindi and English).
  - Keyword search functionality.
  - Model fine-tuning results and performance metrics (81% accuracy on Hindi).
    **Step-1:Upload the image :**
 ![img 1 ](https://github.com/user-attachments/assets/1c102b5e-4b8c-4dac-b999-2a708825fea1)
    **Step-2:Click on Extract Text to get the extracted text**
![img 2](https://github.com/user-attachments/assets/6cb1ba67-0521-4e14-ae89-28464b6c7e3e)
    **Step-3:Search a keyword and get the highlighted output**
![img 3](https://github.com/user-attachments/assets/3a76ba0c-440f-4734-ae81-d87bd1e15f81)



**Fine-tuned model**:


**input_image**:

![2 1](https://github.com/user-attachments/assets/76951b89-bf67-4bf4-bdab-71d4ef6a5763)

**output_text**:

![WhatsApp Image 2024-09-30 at 19 33 14_73f2b5eb](https://github.com/user-attachments/assets/ae2b7888-267c-4345-a602-7313ba645ced)

3.**Requirements**:
  The project requires the following Python packages, which are listed in requirements.txt:
```bash
    streamlit
    transformers
    torch
    Pillow
```
**Future Work**
Once suitable GPU resources are available, the fine-tuned model can be deployed online to allow real-time inference for Hindi and English text extraction. This will enable full functionality of the web application.

**Conclusion**:
This project demonstrates my proficiency in OCR, deep learning model fine-tuning, and web application development. Despite deployment limitations, the complete functionality of the application can be reviewed via the attached screenshots and the well-documented codebase.
