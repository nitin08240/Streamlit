import streamlit as st
from dotenv import load_dotenv
import io
import os
import pandas as pd
import google.generativeai as genai



load_dotenv()

st.title("AI Financial Analyzer")
st.divider()
st.badge("chai and code")
st.markdown("Make better decision with AI in finance")


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key = GEMINI_API_KEY)

uploaded_file = st.file_uploader("Upload your financial data ",type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    tab1,tab2,tab3 = st.tabs(["Raw Data","Cleaned Data", "AI insights"])
    
    with tab1:
        st.subheader("Raw Data")
        st.dataframe(df)
    with tab2:
        st.subheader("Cleaned Data")
        df['Amount'] = pd.to_numeric(df['Amount'],errors = "coerce")
        df.dropna(subset=['Amount'],inplace=True)
        
        
        st.dataframe(df)
        
        
    with tab3:
        st.subheader("Gemini AI Analysis")
        
        prompt = f""" 
        Analyze the following financial data provided in CSV format. The data includes columns for 'Date', 'Category', 'Description', 'Amount', and 'Payment Method'.

    Provide insights based on this data, including:
    1.  A summary of total income and total expenses.
    2.  A breakdown of expenses by category.
    3.  Identification of the most frequently used payment methods.
    4.  Any other interesting observations or patterns you can find in the data.

    Here is the data : {df.to_csv(index=False)}
        
        """  
        
        try:
               model = genai.GenerativeModel("models/gemini-2.5-flash")
               response =  model.generate_content(prompt)
               st.markdown("### AI Suggestions")
               st.write(response.text)
        
        except Exception as e:
            st.error(f"Error from Gemini {str(e)}")  



    

    


         