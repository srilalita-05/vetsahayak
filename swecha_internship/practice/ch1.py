import streamlit as st

st.title("programming language picker!!")
st.subheader("Please select your programming language")
lang=st.selectbox("programming language",["c","c++","java","python","c#","r"])
st.success(f"you have picked {lang} language")
