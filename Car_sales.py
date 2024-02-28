import streamlit as st
import pandas as pd
import pickle

st.write("""
# Car Sales Performance

This app predicts the **Car Sales Perfromance** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    __year_resale_value = st.sidebar.slider('__year_resale_value', 5.16, 67.55, 30.0)
    Price_in_thousands = st.sidebar.slider('Price_in_thousands', 9.24, 85.5, 40.0)
    Engine_size = st.sidebar.slider('Engine_size', 1.0, 8.0, 4.0)
    Horsepower = st.sidebar.slider('Horsepower', 55.0, 450.0, 300.0)
    Wheelbase = st.sidebar.slider('Wheelbase', 92.6, 138.70, 100.0)
    Width = st.sidebar.slider('Width', 62.60, 79.90, 68.0)
    Length = st.sidebar.slider('Length', 149.4, 224.5, 200.0)
    Curb_weight = st.sidebar.slider('Curb_weight', 1.9, 5.57, 3.0)
    Fuel_capacity = st.sidebar.slider('Fuel_capacity', 10.30, 32.0, 20.0)
    Fuel_efficiency = st.sidebar.slider('Fuel_efficiency', 15.00, 45.0, 20.0)
    Power_perf_factor = (st.sidebar.slider'Power_perf_factor', 23.27, 188.14, 130.0)
    Manufacturer_Acura = st.sidebar.slider ('Manufacturer_Acura', 0.0, 1.0, 0.5)
    Manufacturer_Audi = st.sidebar.slider('Manufacturer_Audi', 0.0, 1.0, 0.5)
    Manufacturer_BMW = st.sidebar.slider('Manufacturer_BMW', 0.0, 1.0, 0.5)
    Manufacturer_Buick = st.sidebar.slider('Manufacturer_Buick', 0.0, 1.0, 0.5)
    Manufacturer_Cadillac = st.sidebar.slider('Manufacturer_Buick', 0.0, 1.0, 0.5)
    Manufacturer_Chevrolet = st.sidebar.slider('Manufacturer_Chevrolet', 0.0, 1.0, 0.5) 
    Manufacturer_Chrysler = st.sidebar.slider('Manufacturer_Chrysler', 0.0, 1.0, 0.5) 
    Manufacturer_Dodge = st.sidebar.slider('Manufacturer_Dodge', 0.0, 1.0, 0.5)
    Manufacturer_Ford = st.sidebar.slider('Manufacturer_Ford', 0.0, 1.0, 0.5) 
    Manufacturer_Honda = st.sidebar.slider('Manufacturer_Honda', 0.0, 1.0, 0.5) 
    Manufacturer_Hyundai = st.sidebar.slider('Manufacturer_Hyundai', 0.0, 1.0, 0.5) 
    Manufacturer_Infiniti = st.sidebar.slider('Manufacturer_Infiniti', 0.0, 1.0, 0.5) 
    Manufacturer_Jaguar = st.sidebar.slider('Manufacturer_Jaguar', 0.0, 1.0, 0.5) 
    Manufacturer_Jeep = st.sidebar.slider('Manufacturer_Jeep', 0.0, 1.0, 0.5) 
    Manufacturer_Lexus = st.sidebar.slider('Manufacturer_Lexus', 0.0, 1.0, 0.5)
    Manufacturer_Lincoln = st.sidebar.slider('Manufacturer_Lincoln', 0.0, 1.0, 0.5) 
    Manufacturer_Mercedes-B = st.sidebar.slider('Manufacturer_Mercedes-B', 0.0, 1.0, 0.5)
    Manufacturer_Mercury = st.sidebar.slider('Manufacturer_Mercury', 0.0, 1.0, 0.5) 
    Manufacturer_Mitsubishi = st.sidebar.slider('Manufacturer_Mitsubishi', 0.0, 1.0, 0.5) 
    Manufacturer_Nissan = st.sidebar.slider('Manufacturer_Nissan', 0.0, 1.0, 0.5) 
    Manufacturer_Oldsmobile = st.sidebar.slider('Manufacturer_Oldsmobile', 0.0, 1.0, 0.5)
    Manufacturer_Plymouth = st.sidebar.slider('Manufacturer_Plymouth', 0.0, 1.0, 0.5) 
    Manufacturer_Pontiac = st.sidebar.slider('Manufacturer_Pontiac', 0.0, 1.0, 0.5) 
    Manufacturer_Porsche = st.sidebar.slider('Manufacturer_Porsche', 0.0, 1.0, 0.5)
    Manufacturer_Saab = st.sidebar.slider('Manufacturer_Saab', 0.0, 1.0, 0.5) 
    Manufacturer_Saturn = st.sidebar.slider('Manufacturer_Saturn', 0.0, 1.0, 0.5) 
    Manufacturer_Subaru = st.sidebar.slider('Manufacturer_Subaru', 0.0, 1.0, 0.5) 
    Manufacturer_Toyota = st.sidebar.slider('Manufacturer_Toyota', 0.0, 1.0, 0.5) 
    Manufacturer_Volkswagen = st.sidebar.slider('Manufacturer_Volkswagen', 0.0, 1.0, 0.5)
    Manufacturer_Volvo = st.sidebar.slider('Manufacturer_Volvo', 0.0, 1.0, 0.5)
    Vehicle_type_Car = st.sidebar.slider('Vehicle_type_Car', 0.0, 1.0, 0.5) 
    Vehicle_type_Passenger = st.sidebar.slider('Vehicle_type_Passenger', 0.0, 1.0, 0.5) 
    data = {' __year_resale_value':  __year_resale_value,
            'Price_in_thousands': Price_in_thousands,
            'Engine_size': Engine_size,
            'Horsepower': Horsepower,
            'Wheelbase': Wheelbase,
            'Width': Width,
            'Length': Length,
            'Curb_weight': Curb_weight,
            'Fuel_capacity': Fuel_capacity,
            'Fuel_efficiency': Fuel_efficiency,
            'Power_perf_factor': Power_perf_factor,
            'Manufacturer_Acura': Manufacturer_Acura,
            'Manufacturer_Audi': Manufacturer_Audi,
            'Manufacturer_BMW': Manufacturer_BMW,
            'Manufacturer_Buick':Manufacturer_Buick,
            'Manufacturer_Cadillac' : Manufacturer_Cadillac,
            'Manufacturer_Chevrolet': Manufacturer_Chevrolet,
            'Manufacturer_Chrysler': Manufacturer_Chrysler,
            'Manufacturer_Dodge': Manufacturer_Dodge,
            'Manufacturer_Ford': Manufacturer_Ford,
            'Manufacturer_Honda': Manufacturer_Honda,
            'Manufacturer_Hyundai': Manufacturer_Hyundai,
            'Manufacturer_Infiniti': Manufacturer_Infiniti,
            'Manufacturer_Jaguar': Manufacturer_Jaguar,
            'Manufacturer_Jeep': Manufacturer_Jeep,
            'Manufacturer_Lexus': Manufacturer_Lexus,
            'Manufacturer_Lincoln': Manufacturer_Lincoln,
            'Manufacturer_Mercedes-B': Manufacturer_Mercedes-B,
            'Manufacturer_Mercury': Manufacturer_Mercury,
            'Manufacturer_Mitsubishi': Manufacturer_Mitsubishi,
            'Manufacturer_Nissan': Manufacturer_Nissan,
            'Manufacturer_Oldsmobile': Manufacturer_Oldsmobile,
            'Manufacturer_Plymouth': Manufacturer_Plymouth,
            'Manufacturer_Pontiac': Manufacturer_Pontiac,
            'Manufacturer_Porsche': Manufacturer_Porsche,
            'Manufacturer_Saab': Manufacturer_Saab,
            'Manufacturer_Saturn': Manufacturer_Saturn,
            'Manufacturer_Subaru': Manufacturer_Subaru,
            'Manufacturer_Toyota': Manufacturer_Toyota,
            'Manufacturer_Volkswagen': Manufacturer_Volkswagen,
            'Manufacturer_Volvo': Manufacturer_Volvo,
            'Vehicle_type_Car' : Vehicle_type_Car,
            'Vehicle_type_Passenger': Vehicle_type_Passenger}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

loaded_model = pickle.load(open("Car_sales.h5", "rb"))

prediction = loaded_model.predict(df)

st.subheader('Prediction')
st.write(prediction)
