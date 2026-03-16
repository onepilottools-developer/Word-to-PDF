import streamlit as st
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import io

# Page Config
st.set_page_config(page_title="Word to PDF | One Pilot Tools", page_icon="📄")

# UI Styling
st.markdown("""
    <style>
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 3.5em; 
        background: linear-gradient(45deg, #FF4B2B, #FF416C);
        color: white; font-weight: bold; border: none;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📄 WORD to PDF Converter")
st.write("Bahi, ab file download bhi hogi aur sahi khulegi bhi!")

uploaded_file = st.file_uploader("Upload .docx file", type=["docx"])

if uploaded_file:
    if st.button("⬇️ CONVERT & DOWNLOAD PDF"):
        try:
            with st.spinner("PDF ban rahi hai..."):
                doc = Document(uploaded_file)
                pdf_buffer = io.BytesIO()
                
                # Styles setup
                styles = getSampleStyleSheet()
                style_n = styles['Normal']
                
                # PDF building
                pdf_doc = SimpleDocTemplate(pdf_buffer, pagesize=letter)
                story = []
                
                for para in doc.paragraphs:
                    if para.text.strip():
                        p = Paragraph(para.text, style_n)
                        story.append(p)
                        story.append(Spacer(1, 12))
                
                pdf_doc.build(story)
                
                # CRITICAL STEP: Rewind the buffer
                pdf_buffer.seek(0) 
                
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
st.caption("One Pilot Tools - Multan")
