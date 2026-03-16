import streamlit as st
from docx import Document
from fpdf import FPDF
import io

# Branding
st.set_page_config(page_title="Word to PDF | One Pilot Tools", page_icon="📄")

# UI Style
st.markdown("""
    <style>
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 3.5em; 
        background: linear-gradient(45deg, #12c2e9, #c471ed, #f64f59);
        color: white; font-weight: bold; border: none;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📄 WORD to PDF Converter")
st.write("Bahi, ab blank page ka masla hal ho gaya hai. Check karen!")

uploaded_file = st.file_uploader("Upload .docx file", type=["docx"])

if uploaded_file:
    if st.button("⬇️ CONVERT & DOWNLOAD PDF"):
        try:
            with st.spinner("Converting..."):
                # Word file read karen
                doc = Document(uploaded_file)
                
                # FPDF Setup
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("helvetica", size=12)
                
                # Content add karen
                for para in doc.paragraphs:
                    if para.text.strip():
                        # Unicode handling
                        clean_text = para.text.encode('utf-8', 'replace').decode('utf-8')
                        pdf.multi_cell(0, 10, txt=clean_text)
                        pdf.ln(2)
                
                # Bytes mein convert karen
                pdf_output = pdf.output() # fpdf2 handles bytes better
                
                st.balloons()
                st.download_button(
                    label="📂 SAVE PDF NOW",
                    data=pdf_output,
                    file_name=uploaded_file.name.replace(".docx", ".pdf"),
                    mime="application/pdf"
                )
        except Exception as e:
            st.error(f"Error: {e}")

st.divider()
st.caption("Developed with ❤️ in Multan - One Pilot Tools")
