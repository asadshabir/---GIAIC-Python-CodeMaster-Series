import streamlit as st

# '''Function'''
# For Distance Converter 
def distance_Converter(from_unit,to_unit,value):
    units = {
        "Meters" : 1,
        "Kilometers" : 1000,
        "Feet" : 0.3048,
        "Miles" : 1609.34
        }
    result = value * units[from_unit] / units[to_unit]
    return result

# Tempreture Converter
def tempreture_Converter(from_Unit,to_Unit,value):
    if from_Unit == "Celsius" and to_Unit == "Fahrenhiet" :
        result = (value *9/5)+32
    elif from_Unit == "Fahrenhiet" and to_Unit == "Celsius" :
        result = (value -32) *5/9
    else :
        return value    
    return result

# Weight Converter
def weight_Converter(from_Unit,to_Unit,value):
    units = {
        "Kilograms":1,
        "Grams" :0.001,
        "Pounds":0.453592,
        "Ounces" :0.0283495
        }
    result = value * units[from_Unit] / units[to_Unit]
    return result

# Pressure Converter

def pressure_Converter(from_Unit,to_Unit,value) :
    values = {
        "Pascals" : 1,
        "Hactopascals" : 100,
        "Kilopascals" : 100,
        "Bar" : 100000
    }
    result = value * values[from_Unit] / values[to_Unit]
    return result
# Titles
st.title("Unit Convertor")
st.write("WelCome to Unit-Converter")

# UI
catagory = st.selectbox("Catagory",["Distace","Tempreture","Weight","Pressure"])

# Distance converter :
if catagory == "Distace" :
    from_Unit = st.selectbox("From",["Meters","Kilometers","Feet","Miles"])
    to_Unit =st.selectbox("To",["Meters","Kilometers","Feet","Miles"])
    value=  st.number_input("Enter Value")
    if st.button("Convert") :
       result =  distance_Converter(from_Unit ,to_Unit,value)
       st.success(f"{value} {from_Unit} = {result:.2f} {to_Unit}")

# Tempreture Converter
elif catagory =="Tempreture" :
    from_Unit = st.selectbox("From",["Celsius","Fahrenhiet"])
    to_Unit =st.selectbox("To",["Celsius","Fahrenhiet"])
    value=  st.number_input("Enter Value")
    if st.button("Convert") :
       result =  tempreture_Converter(from_Unit ,to_Unit,value)
       st.success(f"{value} {from_Unit} = {result:.2f} {to_Unit}")

# Weight Converter
elif catagory =="Weight" :
    from_Unit = st.selectbox("From",["Kilograms","Grams","Pounds","Ounces"])
    to_Unit = st.selectbox("To",["Kilograms","Grams","Pounds","Ounces"])
    value = st.number_input("Enter Value")
    if st.button("Convert") :
        result = weight_Converter(from_Unit,to_Unit,value)
        st.success(f"{value} {from_Unit} = {result:.2f} {to_Unit}")
elif catagory == "Pressure" :
    from_Unit = st.selectbox("From",["Pascals","Hactopascals","Kilopascals","Bar"])
    to_Unit = st.selectbox("To",["Pascals","Hactopascals","Kilopascals","Bar"])
    value = st.number_input("Enter Value")
    if st.button("Convert"):
        result = pressure_Converter(from_Unit,to_Unit,value)
        st.success(f"{value} {from_Unit} = {result} {to_Unit} ")
