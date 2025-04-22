import streamlit as st
st.set_page_config(page_title="Unit Converter", layout="centered")
st.title("🔄 Universal Unit Converter")

# Categories
category = st.selectbox("Choose a category", ["Length", "Weight", "Temperature"])

# Conversion logic
def convert_units(category, from_unit, to_unit, value):
    # Length conversions
    if category == "Length":
        factors = {
            "Meter": 1,
            "Kilometer": 1000,
            "Mile": 1609.34,
            "Foot": 0.3048
        }
        return value * factors[from_unit] / factors[to_unit]

    # Weight conversions
    elif category == "Weight":
        factors = {
            "Kilogram": 1,
            "Gram": 0.001,
            "Pound": 0.453592,
            "Ounce": 0.0283495
        }
        return value * factors[from_unit] / factors[to_unit]

    # Temperature conversions
    elif category == "Temperature":
        if from_unit == to_unit:
            return value
        elif from_unit == "Celsius":
            return {
                "Fahrenheit": (value * 9/5) + 32,
                "Kelvin": value + 273.15
            }[to_unit]
        elif from_unit == "Fahrenheit":
            return {
                "Celsius": (value - 32) * 5/9,
                "Kelvin": (value - 32) * 5/9 + 273.15
            }[to_unit]
        elif from_unit == "Kelvin":
            return {
                "Celsius": value - 273.15,
                "Fahrenheit": (value - 273.15) * 9/5 + 32
            }[to_unit]

# Unit options
unit_options = {
    "Length": ["Meter", "Kilometer", "Mile", "Foot"],
    "Weight": ["Kilogram", "Gram", "Pound", "Ounce"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

# UI elements
from_unit = st.selectbox("From Unit", unit_options[category])
to_unit = st.selectbox("To Unit", unit_options[category])
value = st.number_input(f"Enter value in {from_unit}", value=0.0, step=0.1)

if st.button("Convert"):
    try:
        result = convert_units(category, from_unit, to_unit, value)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
    except:
        st.error("Conversion not supported.")
