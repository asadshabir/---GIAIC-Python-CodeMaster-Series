import streamlit as st
from datetime import datetime

# App title with emojis and color
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🧮 Welcome to BMI Calculator 💪</h1>", unsafe_allow_html=True)

# Add current date/time
st.markdown(f"<p style='text-align: center;'>📅 {datetime.now().strftime('%A, %d %B %Y')}</p>", unsafe_allow_html=True)

# Input: Weight
weight = st.number_input("⚖️ Enter your weight (in kilograms):", min_value=1.0)

# Input: Height Format Selection
status = st.radio('📏 Select your height format:', ('Centimeters', 'Meters', 'Feet'))

# Input: Height
if status == 'Centimeters':
    height = st.number_input('📏 Height (in cm):', min_value=1.0)
    height_m = height / 100

elif status == 'Meters':
    height = st.number_input('📏 Height (in meters):', min_value=0.1)
    height_m = height

else:
    height = st.number_input('📏 Height (in feet):', min_value=0.1)
    height_m = height / 3.28

# Button: Calculate
if st.button('🚀 Calculate BMI'):
    try:
        bmi = round(weight / (height_m ** 2), 2)
        st.markdown(f"<h3 style='color: #2196F3;'>📊 Your BMI is: {bmi}</h3>", unsafe_allow_html=True)

        # BMI interpretation
        if bmi < 16:
            st.error("😟 You are **Extremely Underweight**. Please take care!")
        elif bmi >= 16 and bmi < 18.5:
            st.warning("⚠️ You are **Underweight**. Time to fuel up!")
        elif bmi >= 18.5 and bmi < 25:
            st.success("✅ You are **Healthy**! Keep it up 🏃‍♂️💚")
        elif bmi >= 25 and bmi < 30:
            st.warning("⚠️ You are **Overweight**. Little control can go a long way.")
        else:
            st.error("🚨 You are **Extremely Overweight**. Health is wealth, friend!")

    except:
        st.error("❌ Please make sure height is valid.")
