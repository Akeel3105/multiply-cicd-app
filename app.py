import streamlit as st
from utils import multiply_number

st.title("Mini CI/CD Demo App 🚀")

num_1 = st.number_input("Enter First number:", value=2)
num_2 = st.number_input("Enter Second number:", value=5)
if st.button("Multiply it"):
    result = multiply_number(num_1,num_2)
    st.success(f"The multiplication value of {num_1} and {num_2} is {result}")
