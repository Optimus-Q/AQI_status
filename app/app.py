import streamlit as st

# addition 
def add(a, b):
    return a+b

st.title("Simple Addition App")

a = st.number_input("Enter the first number: ", 0, 100, key="First element")
b = st.number_input("Enter the second number: ", 0, 100, key="Second element")

if st.button("Add", key="Add button"):
    result = add(a, b)
    st.markdown(f"The result is: {result}")