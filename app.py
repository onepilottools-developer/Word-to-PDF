import streamlit as st
from docx import Document
from fpdf import FPDF
import io

# Page Configuration
st.set_page_config(page_title="Word to PDF | One Pilot Tools", page_icon="📄")

# White UI Styling
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 3.5em; 
        background-color: #FF4B4B; color: white; font-weight: bold; border: none;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📄 WORD to PDF Converter")
st.write("Bahi, ye version bilkul sahi chalay ga. Insha'Allah!")

uploaded_file = st.file_uploader("Upload .docx file", type=["docx"])

if uploaded_file:
    if st.button("🚀 CONVERT & DOWNLOAD PDF"):
        try:
            with st.spinner("Processing..."):
                # Word file read karen
                doc = Document(uploaded_file)
                
                # FPDF2 setup
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("helvetica", size=12)
                
                # Content convert karen
                for para in doc.paragraphs:
                    if para.text.strip():
                        # Unicode handling
                        text = para.text.encode('utf-8', 'replace').decode('utf-8')
                        pdf.multi_cell(0, 10, txt=text)
                        pdf.ln(2)
                
                # Fix: Output as bytes directly
                pdf_bytes = pdf.output() 
                
                st.balloons()
                st.download_button(
                    label="📥 DOWNLOAD PDF NOW",
                    data=bytes(pdf_bytes), # Force conversion to bytes
                    file_name="OnePilot_Converted.pdf",
                    mime="application/pdf"
                )
        except Exception as e:
            st.error(f"Error: {str(e)}")

st.divider()
st.caption("One Pilot Tools - Multan, Pakistan")
