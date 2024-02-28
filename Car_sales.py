%%writefile Car_sales.py
import streamlit as st
import pandas as pd
import pickle

st.write("""
# Car Sales Performance

This app predicts the **Car Sales Perfromance** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    Manufacturer = st.sidebar.slider('Manufacturer', 0.0, 1.0, 0.5)
    Model = st.sidebar.slider('Model', 0.0, 1.0, 0.5)
    __year_resale_value = st.sidebar.slider('__year_resale_value', 0.0, 1.0, 0.5)
    Vehicle_type = st.sidebar.slider('Vehicle_type', 0.0, 1.0, 0.5)
    Price_in_thousands = st.sidebar.slider('Price_in_thousands', 0.0, 1.0, 0.5)
    Engine_size = st.sidebar.slider('Engine_size', 0.0, 1.0, 0.5)
    Horsepower = st.sidebar.slider('Horsepower', 0.0, 1.0, 0.5)
    Wheelbase = st.sidebar.slider('Wheelbase', 0.0, 1.0, 0.5)
    Width = st.sidebar.slider('Width', 0.0, 1.0, 0.5)
    Length = st.sidebar.slider('Length', 0.0, 1.0, 0.5)
    Curb_weight = st.sidebar.slider('Curb_weight', 0.0, 1.0, 0.5)
    Fuel_capacity = st.sidebar.slider('Fuel_capacity', 0.0, 1.0, 0.5)
    Fuel_efficiency = st.sidebar.slider('Fuel_efficiency', 0.0, 1.0, 0.5)
    Power_perf_factor = st.sidebar.slider('Power_perf_factor', 0.0, 1.0, 0.5)
    data = {'Manufacturer': Manufacturer,
            'Model': Model,
            'Vehicle_type': Vehicle_type,
            'Price_in_thousands': Price_in_thousands,
            'Engine_size': Engine_size,
            'Horsepower': Horsepower,
            'Wheelbase': Wheelbase,
            'Width': Width,
            'Length': Length,
            'Curb_weight': Curb_weight,
            'Fuel_capacity': Fuel_capacity,
            'Fuel_efficiency': Fuel_efficiency,
            'Power_perf_factor': Power_perf_factor}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

loaded_model = pickle.load(open("Car_sales.h5", "rb"))

prediction = loaded_model.predict(df)

st.subheader('Prediction')
st.write(prediction)
