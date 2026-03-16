import streamlit as st
from docx import Document
from fpdf import FPDF
import io

# Branding
st.set_page_config(page_title="Word to PDF | One Pilot Tools", page_icon="📄")

# UI Style (Aapka favorite minimalist theme)
st.markdown("""
    <style>
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 3.5em; 
        background: linear-gradient(45deg, #ee0979, #ff6a00);
        color: white; font-weight: bold; border: none;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📄 Professional Word to PDF")
st.write("Bahi, ab binary data aur blank page dono ka masla hal ho gaya hai.")

uploaded_file = st.file_uploader("Upload .docx file", type=["docx"])

if uploaded_file:
    # File name handle karna (Urdu names handle karne ke liye)
    safe_filename = "converted_document.pdf"
    
    if st.button("🚀 CONVERT TO PDF"):
        try:
            with st.spinner("Processing..."):
                # Word file load karen
                doc = Document(uploaded_file)
                
                # FPDF Setup
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                
                # Content extract aur add karen
                for para in doc.paragraphs:
                    if para.text.strip():
                        # Latin-1 safe conversion
                        text = para.text.encode('latin-1', 'ignore').decode('latin-1')
                        pdf.multi_cell(0, 10, txt=text)
                        pdf.ln(2)
                
                # Binary Stream handle karna
                pdf_str = pdf.output(dest='S')
                # Convert string output to actual bytes
                pdf_bytes = pdf_str.encode('latin-1')
                
                st.balloons()
                st.download_button(
                    label="📥 DOWNLOAD NOW",
                    data=pdf_bytes,
                    file_name=safe_filename,
                    mime="application/pdf"
                )
        except Exception as e:
            st.error(f"Error: {str(e)}")

st.divider()
st.caption("Powered by One Pilot Tools - Multan, Pakistan")
