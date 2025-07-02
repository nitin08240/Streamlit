import streamlit as st

st.title("Hello Chai App")
st.subheader("Brewed with streamlit")

st.title("Welcome to your first interative app")

st.write("Choose your favourite variety of chai")


chai = st.selectbox("Your fav chai: ", {"Masal Chai", "Lemon Tea", "Protein Chai","Kesar Chai"})


st.write(f"Your choose {chai} Excellent Choice")

st.success("Your chai has been ready ")