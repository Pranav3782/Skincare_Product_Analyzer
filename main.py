import streamlit as st
from PIL import Image
import pytesseract

from langchain_groq import ChatGroq

from langchain.schema import HumanMessage

# Set the Tesseract OCR path (Windows only)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Setup LLaMA via Groq
llm = ChatGroq(

    api_key="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",  # Replace with your key
    model="llama-3.3-70b-versatile",
    temperature=0
)

# Define the analysis function
def analyze_ingredients(text, product_type):
    prompt = f"""
    You are a skincare expert. Analyze the following ingredients for a {product_type}.

    1. For each ingredient, tell if it's Healthy ✅, Harmful ❌, or Neutral ⚠️, and give a short reason.
    2. Based on the product type, recommend which skin/hair type this is best for.
    3. Return in bullet points for clarity.

    Ingredients:
    {text}
    """
    response = llm.invoke([HumanMessage(content=prompt)])  # ✅ Preferred

    return response.content

# Streamlit UI
st.title("🧴 Skincare Product Analyzer")

uploaded_file = st.file_uploader("Upload a product label image", type=["jpg", "jpeg", "png"])
product_type = st.selectbox("Select product type", ["Moisturizer", "Shampoo", "Sunscreen", "Face Wash"])

if uploaded_file:
    image = Image.open(uploaded_file)
    extracted_text = pytesseract.image_to_string(image)
    st.text_area("Extracted Text", value=extracted_text)

    if st.button("Analyze Ingredients"):
        with st.spinner("Analyzing with LLaMA..."):
            analysis_result = analyze_ingredients(extracted_text, product_type)
            st.markdown("### 🔍 Ingredient Analysis")
            st.write(analysis_result)
