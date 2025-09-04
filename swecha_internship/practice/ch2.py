import streamlit as st
import datetime as dt
from dateutil.relativedelta import relativedelta

st.title("Exact Age Calculator")
st.write("This is a simple and accurate age calculator")

# Define a wide date range
min_date = dt.date(1900, 1, 1)
max_date = dt.date.today()

# Date input with custom range
dob = st.date_input("Select your date of birth", min_value=min_date, max_value=max_date)
today = dt.date.today()

# Prevent future date input
if dob > today:
    st.error("Date of birth cannot be in the future.")
else:
    # Use relativedelta to get exact age
    diff = relativedelta(today, dob)
    age = f"{diff.years} years, {diff.months} months, {diff.days} days"
    st.write(f"Your exact age is: {age}")
