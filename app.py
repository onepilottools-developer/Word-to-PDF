import streamlit as st
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import io

# Page Branding & UI
st.set_page_config(page_title="Word to PDF Converter", page_icon="📄", layout="centered")

# Attractive White UI Styling
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button { 
        width: 100%; 
        border-radius: 12px; 
        height: 3.5em; 
        background-color: #FF4B4B; 
        color: white; 
        font-weight: bold;
        border: none;
        font-size: 18px;
    }
    .stButton>button:hover {
        background-color: #ff3333;
        box-shadow: 0px 4px 15px rgba(255, 75, 75, 0.3);
    }
    .upload-text {
        font-size: 24px;
        font-weight: bold;
        color: #1E1E1E;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📄 WORD to PDF Converter")
st.write("Bahi, apni `.docx` file upload karen aur foran PDF download karen.")

# 1. File Upload Section
uploaded_file = st.file_uploader("Choose a Word File", type=["docx"])

if uploaded_file is not None:
    st.success(f"✅ File Loaded: {uploaded_file.name}")
    
    # Big Attractive Button
    if st.button("⬇️ CONVERT & DOWNLOAD PDF"):
        try:
            with st.spinner("Bahi wait karen, PDF tayyar ho rahi hai..."):
                
                # Load Word Document from memory
                doc = Document(uploaded_file)
                
                # Create a BytesIO buffer for PDF
                pdf_buffer = io.BytesIO()
                pdf_doc = SimpleDocTemplate(pdf_buffer, pagesize=letter)
                
                story = []
                styles = getSampleStyleSheet()
                
                # Process Paragraphs
                for paragraph in doc.paragraphs:
                    if paragraph.text.strip():
                        # Word ka text PDF ke paragraph mein convert karna
                        p = Paragraph(paragraph.text, styles['Normal'])
                        story.append(p)
                        story.append(Spacer(1, 12))
                
                # Build PDF
                pdf_doc.build(story)
                pdf_output = pdf_buffer.getvalue()
                
                # Final Success & Download Button
                st.balloons()
                st.download_button(
                    label="📂 CLICK HERE TO SAVE PDF",
                    data=pdf_output,
                    file_name=uploaded_file.name.replace(".docx", ".pdf"),
                    mime="application/pdf"
                )
                
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
else:
    st.info("Awaiting Word File... Browse button par click karen.")

st.divider()
st.caption("One Pilot Tools - Professional & Simple Utilities")
