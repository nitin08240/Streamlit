import streamlit as st
from dotenv import load_dotenv
import io
import os
import PyPDF2
import google.generativeai as genai



load_dotenv()

st.title("AI Resume roaster")
st.divider()
st.badge("chai and code")
st.markdown("Upload your resume and get AI roasting feedback")


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key = GEMINI_API_KEY)


    

uploaded_file = st.file_uploader("Upload your resume here (PDF and txt only)",type=["pdf","txt"])
job_role = st.text_input("Enter the job role that you are Targeting")

analyze = st.button("Analze resume")
print(analyze)

def extract_text_from_pdf(file_bytes):
    reader = PyPDF2.PdfReader(file_bytes)
    return "\n".join(page.extract_text() or "" for page in reader.pages)
    
    



def extract_text(uploaded_file):
    """Extracts text from an uploaded pdf or text file"""
    file_type = uploaded_file.type

    if file_type == "application/pdf":
        file_bytes = io.BytesIO(uploaded_file.read())
        return extract_text_from_pdf(file_bytes)
    elif file_type == "text/plain":
        return uploaded_file.read().decode("utf-8")
    else:
        return ""
if analyze and uploaded_file:
    try:
        file_content = extract_text(uploaded_file)
        
        if not file_content or not file_content.strip():
            st.error("File does not have any content")
            st.stop()
        
        ##AI CALLING    
        prompt = f"""
        You are brutally honest, no non-sense HR except who's been reviewing resume for decades
        Roast this resume like you are on a comedy stages but still give some useful insights feedback.
        Don't hold back -be sarcastic,witty and critical where needed.
        Would would make this resume actually land a job in {job_role} for a good company
        
        here is the resume ,go wild:
        {file_content}
        
        Make it string and make sure to keep it in 150 words Answer everthing in Hinglish"""
        
        # Use a valid Gemini model name, e.g., "gemini-pro"
        models = genai.GenerativeModel("models/gemini-2.5-flash")

        response = models.generate_content(prompt)
        st.markdown("## Analysis Results ")
        st.markdown(response.text)
    except Exception as e:
        st.error(f"An error occurred: {e}")   
    
          
         