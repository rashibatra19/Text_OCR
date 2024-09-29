
import streamlit as st
from PIL import Image
import re
import io
import torch
from transformers import AutoModel, AutoTokenizer
import tempfile

# Function to load model and tokenizer
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained('ucaslcl/GOT-OCR2_0', trust_remote_code=True)
    model = AutoModel.from_pretrained('ucaslcl/GOT-OCR2_0', trust_remote_code=True, low_cpu_mem_usage=True, use_safetensors=True, pad_token_id=tokenizer.eos_token_id)
    model = model.eval()
    return tokenizer, model

def search_keyword(extracted_text, keyword):
    if not keyword:
        return extracted_text
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    highlighted_text = pattern.sub(lambda m: f'<span style="color: red; font-weight: bold;">{m.group()}</span>', extracted_text)
    return highlighted_text


def main():
    st.title("Simplified OCR Application")

    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    # Placeholder for extracted text (simulating OCR result)
    extracted_text = None
    # Load model and tokenizer
    tokenizer, model = load_model()

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Simulate OCR extraction (replace this with actual OCR in your full app)
        if st.button('Extract Text'):
            # Save the uploaded file to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
                temp_filename = temp_file.name
                image.save(temp_filename, format='PNG')

            # Perform OCR
            with st.spinner('Extracting text...'):
                res = model.chat(tokenizer, temp_filename, ocr_type='ocr')

            # Display result
          
            extracted_text = res
            st.session_state['extracted_text'] = extracted_text
            st.subheader("Extracted Text:")
            st.write(extracted_text)


    # Search functionality
    if 'extracted_text' in st.session_state:
        keyword = st.text_input("Enter a keyword to search:")
        if st.button("Search"):
            if keyword:
                highlighted_text = search_keyword(st.session_state['extracted_text'], keyword)
                st.subheader("Search Results:")
                st.write(highlighted_text, unsafe_allow_html=True)
                st.download_button(
                    label="Download highlighted text",
                    data=highlighted_text.encode('utf-8'),
                    file_name="highlighted_text.txt",
                    mime="text/plain"
                )
            else:
                st.warning("Please enter a keyword to search.")

if __name__ == "__main__":
    main()