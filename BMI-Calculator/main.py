
import streamlit as st

# Streamlit App Title
st.title("BMI Calculator")

# Taking user input
weight = st.number_input("Enter your weight (kg):", min_value=1.0, format="%.2f")
height = st.number_input("Enter your height (meters):", min_value=0.5, format="%.2f")

# Function to calculate BMI
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Calculate BMI on button click
if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        st.write(f"Your BMI is: *{bmi:.2f}*")

        # Categorizing BMI
        if bmi < 18.5:
            st.warning("You are *Underweight*.")
        elif 18.5 <= bmi < 24.9:
            st.success("You are *Healthy (Normal weight)*.")
        elif 25 <= bmi < 29.9:
            st.warning("You are *Overweight*.")
        else:
            st.error("You are *Obese*. Consider consulting a doctor.")