import streamlit as st

def find_largest_number(num1, num2, num3):
    return max(num1, num2, num3)

st.title("Largest Number Finder")

# Get user input
num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")
num3 = st.number_input("Enter the third number:")

if st.button("Find Largest Number"):
    result = find_largest_number(num1, num2, num3)
    st.success(f"The largest number among {num1}, {num2}, and {num3} is: {result}")
