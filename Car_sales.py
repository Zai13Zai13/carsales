import streamlit as st
import pandas as pd
import pickle

st.write("""
# Car Sales Performance

This app predicts the **Car Sales Perfromance** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features(): 
    Manufacturer = st.sidebar.selectbox ('Select the Manufacturer Type',['Acura', 'Audi', 'BMW', 'Buick', 'Cadillac', 'Chevrolet',
       'Chrysler', 'Dodge', 'Ford', 'Honda', 'Hyundai', 'Infiniti',
       'Jaguar', 'Jeep', 'Lexus', 'Lincoln', 'Mercedes-B', 'Mercury',
       'Mitsubishi', 'Nissan', 'Oldsmobile', 'Plymouth', 'Pontiac',
       'Porsche', 'Saab', 'Saturn', 'Subaru', 'Toyota', 'Volkswagen',
       'Volvo'])
    Model = st.sidebar.selectbox ('Select the Model Type',['3-Sep', '3000GT', '300M', '323i', '328i', '4Runner', '5-Sep',
       '528i', 'A4', 'A6', 'A8', 'Accent', 'Accord', 'Alero', 'Altima',
       'Aurora', 'Avalon', 'Avenger', 'Beetle', 'Bonneville', 'Boxter',
       'Bravada', 'Breeze', 'C-Class', 'C70', 'CL', 'CL500', 'CLK Coupe',
       'CR-V', 'Cabrio', 'Camaro', 'Camry', 'Caravan', 'Carrera Cabrio',
       'Carrera Coupe', 'Catera', 'Cavalier', 'Celica', 'Century',
       'Cherokee', 'Cirrus', 'Civic', 'Concorde', 'Continental',
       'Contour', 'Corolla', 'Corvette', 'Cougar', 'Crown Victoria',
       'Cutlass', 'Dakota', 'DeVille', 'Diamante', 'Durango', 'E-Class',
       'ES300', 'Eclipse', 'Elantra', 'Eldorado', 'Escalade', 'Escort',
       'Expedition', 'Explorer', 'F-Series', 'Firebird', 'Focus',
       'Forester', 'Frontier', 'GS300', 'GS400', 'GTI', 'Galant', 'Golf',
       'Grand Am', 'Grand Cherokee', 'Grand Marquis', 'Grand Prix', 'I30',
       'Impala', 'Integra', 'Intrepid', 'Intrigue', 'Jetta', 'LHS', 'LS',
       'LS400', 'LW', 'LX470', 'Land Cruiser', 'LeSabre', 'Lumina',
       'M-Class', 'Malibu', 'Maxima', 'Metro', 'Mirage', 'Montana',
       'Monte Carlo', 'Montero', 'Montero Sport', 'Mountaineer',
       'Mustang', 'Mystique', 'Navigator', 'Neon', 'Odyssey', 'Outback',
       'Park Avenue', 'Passat', 'Passport', 'Pathfinder', 'Prizm',
       'Prowler', 'Quest', 'RAV4', 'RL', 'RX300', 'Ram Pickup', 'Ram Van',
       'Ram Wagon', 'Ranger', 'Regal', 'S-Class', 'S-Type', 'S40', 'S70',
       'S80', 'SC', 'SL', 'SL-Class', 'SLK', 'SLK230', 'SW', 'Sable',
       'Sebring Conv.', 'Sebring Coupe', 'Sentra', 'Seville', 'Sienna',
       'Silhouette', 'Sonata', 'Stratus', 'Sunfire', 'TL', 'Tacoma',
       'Taurus', 'Town & Country', 'Town car', 'V40', 'V70', 'Villager',
       'Viper', 'Voyager', 'Windstar', 'Wrangler', 'Xterra'])
    Vehicle_type = st.sidebar.selectbox ('Select the Vehicle Type',['Car','Passenger'])
    Resale_Value = st.sidebar.slider('Resale_Value', 5.16, 67.55, 30.0)
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
    data = {'Manufacturer': Manufacturer,
            'Model': Model,
            'Vehicle_type': Vehicle_type,
            'Resale_Value': Resale_Value,
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

loaded_model = pickle.load(open("Car_salesmodel (2).h5", "rb"))

prediction = loaded_model.predict(df)

st.subheader('Prediction')
st.write(prediction)
