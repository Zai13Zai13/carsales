import streamlit as st
import pandas as pd
import pickle

col1, col2, col3 = st.columns(3)

with col1:
    st.header("User Input Parameters")
    def user_input_features(): 
        Manufacturer = st.sidebar.selectbox ('Select the Manufacturer Type', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18, 17, 16, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29])
        Model = st.sidebar.selectbox ('Select the Model Type', [79, 143, 25, 115, 8, 9, 10, 3, 4, 7, 38, 121, 107, 89, 51, 137, 58, 35, 59, 36, 92, 90, 97, 30, 46, 111, 94, 78, 135, 134, 42, 40, 83, 146, 2, 104, 17, 141, 80, 151, 117, 119, 118, 50, 53, 32, 60, 101, 44, 145, 65, 48, 62, 153, 61, 120, 63, 41, 12, 28, 109, 105, 11, 57, 140, 77, 123, 154, 39, 74, 55, 68, 69, 85, 87, 116, 43, 147, 103, 95, 56, 71, 52, 1, 98, 99, 102, 47, 133, 75, 100, 150, 23, 54, 122, 129, 130, 131, 27, 26, 91, 136, 14, 93, 113, 110, 155, 67, 49, 81, 13, 15, 21, 139, 22, 152, 112, 142, 73, 64, 76, 19, 96, 20, 34, 33, 6, 0, 128, 127, 132, 86, 84, 106, 66, 45, 31, 16, 37, 144, 138, 114, 5, 88, 72, 82, 108, 29, 70, 18, 124, 148, 125, 149, 24, 126])
        Resale_Value = st.sidebar.slider('Resale_Value', 5.16, 67.55, 30.0)
        Vehicle_type = st.sidebar.selectbox ('Select the Vehicle Type', [1, 0])
        Price_in_thousands = st.sidebar.slider('Price_in_thousands', 9.24, 85.5, 40.0)
        Engine_size = st.sidebar.slider('Engine_size', 1.0, 8.0, 4.0)
        Horsepower = st.sidebar.slider('Horsepower', 55.0, 450.0, 300.0)
        Wheelbase = st.sidebar.slider('Wheelbase', 92.6, 138.70, 100.0)
        Width = st.sidebar.slider('Width', 62.60, 79.90, 68.0)
        Length = st.sidebar.slider('Length', 149.4, 224.5, 200.0)
        Curb_weight = st.sidebar.slider('Curb_weight', 1.9, 5.57, 3.0)
        Fuel_capacity = st.sidebar.slider('Fuel_capacity', 10.30, 32.0, 20.0)
        Fuel_efficiency = st.sidebar.slider('Fuel_efficiency', 15.00, 45.0, 20.0)
        Power_perf_factor = st.sidebar.slider('Power_perf_factor', 23.27, 188.14, 130.0)

    with col2:
        st.header("Description")
        st.write('The Manufacturers are 0=Acura, 1=Audi, 2=BMW, ...')
        st.write('The Models are 79=3-Sep, 143=3000GT, 25=300M, ...')
        st.write('The Vehicles are 1=Car, 0=Passenger')

    with col3:
        st.header("Car Performance Sale")
        st.write("# Car Sales Performance")
        st.write("This app predicts the **Car Sales Performance** type!")
        st.image('CarSales.png', caption='CAR SALES')

df = user_input_features()

st.subheader('User Input parameters value')
st.write(df)

loaded_model = pickle.load(open("Car_salesmodel (2).h5", "rb"))

prediction = loaded_model.predict(df)

st.subheader('Prediction of Sales in Thousand')
st.write(prediction)
