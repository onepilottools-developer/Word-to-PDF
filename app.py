import streamlit as st
from docx import Document
from fpdf import FPDF
import io

# Page Config
st.set_page_config(page_title="Word to PDF | One Pilot Tools", page_icon="📄")

# UI Styling (Bahi, attractive white UI)
st.markdown("""
    <style>
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 3.5em; 
        background: linear-gradient(45deg, #00c6ff, #0072ff);
        color: white; font-weight: bold; border: none;
    }
    .main { background-color: #ffffff; }
    </style>
    """, unsafe_allow_html=True)

st.title("📄 WORD to PDF Converter")
st.write("Bahi, ye version 100% working hai. Try karen!")

uploaded_file = st.file_uploader("Upload .docx file", type=["docx"])

if uploaded_file:
    if st.button("⬇️ CONVERT & DOWNLOAD PDF"):
        try:
            with st.spinner("Converting..."):
                # Word file read karen
                doc = Document(uploaded_file)
                
                # FPDF Setup
                pdf = FPDF()
                pdf.set_auto_page_break(auto=True, margin=15)
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                
                # Text extract karke PDF mein dalen
                for para in doc.paragraphs:
                    if para.text.strip():
                        # Latin-1 encoding ka masla hal karne ke liye encode/decode
                        text = para.text.encode('latin-1', 'ignore').decode('latin-1')
                        pdf.multi_cell(0, 10, txt=text)
                        pdf.ln(5)
                
                # Output to Buffer
                pdf_output = pdf.output(dest='S').encode('latin-1')
                pdf_buffer = io.BytesIO(pdf_output)
                
                st.balloons()
                st.download_button(
                    label="📂 SAVE PDF NOW",
                    data=pdf_buffer,
                    file_name=uploaded_file.name.replace(".docx", ".pdf"),
                    mime="application/pdf"
                )
        except Exception as e:
            st.error(f"Error: {e}")

st.divider()
st.caption("One Pilot Tools - Multan, Pakistan")
