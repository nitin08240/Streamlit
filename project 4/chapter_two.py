import streamlit as st
from datetime import date

st.title("Chai Maker App")

if st.button("Make Chai"):
    st.success("Your chai is being brewed")


add_masala = st.checkbox("Add Masala")

if add_masala:
    st.write("Masala added to your chai")
    
tea_type = st.radio("Pick your chai base:",['Milk','Water','Honey'])

st.write(f"Selected base {tea_type}")  

flavour = st.selectbox("Choose flavour :",["Adrak","Kesar","Tulsi"])  
st.write(f"Selected Flavour {flavour}")


sugar = st.slider("Sugar Level Spoon", 0,5,4)
st.write(f"Selected Sugar Level Spoon {sugar}")


cups = st.number_input("How many cups",min_value = 1,max_value=10,step=1)
st.write(f"Selected cups Level {cups}")


name = st.text_input("Enter your name")
if name:
    st.write(f"Welcome: {name} ! Your chai is on the ways")
    
    
# import datetime

# dob = st.date_input("Select your date of birth")
# if dob >= datetime.date(2006, 7, 4):
#     st.write(f"You are eligible to vote")   

 
st.title("Voter Eligibility Checker by Date of Birth")
st.divider()

# Date input for DOB
dob = st.date_input("Enter your Date of Birth:", min_value=date(1900, 1, 1), max_value=date.today())

# Button to check eligibility
if st.button("Check Eligibility"):
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    st.write(f"Your age is: **{age}**")

    if age >= 18:
        st.success("✅ You are eligible to vote!")
    else:
        st.error("❌ You are not eligible to vote yet.")