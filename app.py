### first version of app.py

import streamlit as st
from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


st.title("🧴 Skincare Product Analyzer")

# Upload image
uploaded_file = st.file_uploader("Upload a product label image", type=["jpg", "jpeg", "png"])
product_type = st.selectbox("Select product type", ["Moisturizer", "Shampoo", "Sunscreen", "Face Wash"])

# Process the uploaded image
if uploaded_file:
    image = Image.open(uploaded_file)
    extracted_text = pytesseract.image_to_string(image)
    st.text_area("Extracted Ingredients", value=extracted_text)

### first implemented
    # # Add button to analyze the ingredients
    # if st.button("Analyze Ingredients"):
    #     # Example dummy analysis for now
    #     st.markdown("### 🔍 Analysis")
    #     st.write(f"Analyzing ingredients for a **{product_type}**...")
    #     st.write(f"Extracted Text: {extracted_text}")
    #     # Call your analyze_ingredients function here
    if st.button("Analyze Ingredients"):
        with st.spinner("Analyzing with LLaMA..."):
            analysis_result = analyze_ingredients(extracted_text, product_type)
            st.markdown("### 🔍 Ingredient Analysis")
            st.write(analysis_result)

