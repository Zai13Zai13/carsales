import streamlit as st
import pandas as pd
import pickle

st.write("""
# Car Sales Performance

This app predicts the **Car Sales Perfromance** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    st.write('The Manufacturers are 0=Acura, 1=Audi, 2=BMW, 3=Buick, 4=Cadillac, 5=Chevrolet,6=Chrysler, 7=Dodge, 8=Ford, 9=Honda, 10=Hyundai, 11=Infiniti, 12=Jaguar, 13=Jeep, 14=Lexus, 15=Lincoln, 16=Mercedes-B, 17=Mercury,18=Mitsubishi, 19=Nissan, 20=Oldsmobile, 21=Plymouth,22=Pontiac,23=Porsche, 24=Saab, 25=Saturn, 26=Subaru, 27=Toyota, 28=Volkswagen,29=Volvo')
    Manufacturer = st.sidebar.selectbox ('Select the Manufacturer Type',[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 18,
    17, 16, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29])
    st.write('The Models are 79=3-Sep, 143=3000GT, 25=300M, 115=323i, 8=328i, 9=4Runner, 10=5-Sep, 3=528i, 4=A4, 7=A6, 38=A8, 121=Accent, 107=Accord, 89=Alero, 51=Altima, 137=Aurora, 58=Avalon, 35=Avenger, 59=Beetle, 36=Bonneville, 92=Boxter, 90=Bravada, 97=Breeze, 30=C-Class, 46=C70, 111=CL, 94=CL500, 78=CLK Coupe, 135=CR-V, 134=Cabrio, 42=Camaro, 40=Camry, 83=Caravan, 146=Carrera Cabrio, 2=Carrera Coupe, 104=Catera, 17=Cavalier, 141=Celica, 80=Century, 151=Cherokee, 117=Cirrus, 119=Civic, 118=Concorde, 50=Continental, 53=Contour, 32=Corolla, 60=Corvette, 101=Cougar, 44=Crown Victoria, 145=Cutlass, 65=Dakota, 48=DeVille, 62=Diamante, 153=Durango, 61=E-Class, 120=ES300, 63=Eclipse, 41=Elantra, 12=Eldorado, 28=Escalade, 109=Escort, 105=Expedition, 11=Explorer, 57=F-Series, 140=Firebird, 77=Focus, 123=Forester, 154=Frontier, 39=GS300, 74=GS400, 55=GTI, 68=Galant, 69=Golf, 85=Grand Am, 87=Grand Cherokee, 116=Grand Marquis, 43=Grand Prix, 147=I30, 103=Impala, 95=Integra, 56=Intrepid, 71=Intrigue, 52=Jetta, 1=LHS, 98=LS, 99=LS400, 102=LW, 47=LX470, 133=Land Cruiser, 75=LeSabre, 100=Lumina, 150=M-Class, 23=Malibu, 54=Maxima, 122=Metro, 129=Mirage, 130=Montana, 131=Monte Carlo, 27=Montero, 26=Montero Sport, 91=Mountaineer, 136=Mustang, 14=Mystique, 93=Navigator, 113=Neon, 110=Odyssey, 155=Outback, 67=Park Avenue, 49=Passat, 81=Passport, 13=Pathfinder, 15=Prizm, 21=Prowler, 139=Quest, 22=RAV4, 152=RL, 112=RX300, 142=Ram Pickup, 73=Ram Van, 64=Ram Wagon, 76=Ranger, 19=Regal, 96=S-Class, 20=S-Type, 34=S40, 33=S70, 6=S80, 0=SC, 128=SL, 127=SL-Class, 132=SLK, 86=SLK230, 84=SW, 106=Sable, 66=Sebring Conv., 45=Sebring Coupe, 31=Sentra, 16=Seville, 37=Sienna, 144=Silhouette, 138=Sonata, 114=Stratus, 5=Sunfire, 88=TL, 72=Tacoma, 82=Taurus, 108=Town & Country, 29=Town car, 70=V40, 18=V70, 124=Villager, 148=Viper, 125=Voyager, 149=Windstar, 24=Wrangler, 126=Xterra') 
    Model = st.sidebar.selectbox ('Select the Model Type',[ 79, 143,  25, 115,   8,   9,  10,   3,   4,   7,  38, 121, 107,
    89,  51, 137,  58,  35,  59,  36,  92,  90,  97,  30,  46, 111,
    94,  78, 135, 134,  42,  40,  83, 146,   2, 104,  17, 141,  80,
    151, 117, 119, 118,  50,  53,  32,  60, 101,  44, 145,  65,  48,
    62, 153,  61, 120,  63,  41,  12,  28, 109, 105,  11,  57, 140,
    77, 123, 154,  39,  74,  55,  68,  69,  85,  87, 116,  43, 147,
    103,  95,  56,  71,  52,   1,  98,  99, 102,  47, 133,  75, 100,
    150,  23,  54, 122, 129, 130, 131,  27,  26,  91, 136,  14,  93,
    113, 110, 155,  67,  49,  81,  13,  15,  21, 139,  22, 152, 112,
    142,  73,  64,  76,  19,  96,  20,  34,  33,   6,   0, 128, 127,
    132,  86,  84, 106,  66,  45,  31,  16,  37, 144, 138, 114,   5,
    88,  72,  82, 108,  29,  70,  18, 124, 148, 125, 149,  24, 126])
    st.write('The Vehicles are 1=Car , 0=Passenger)
    Vehicle_type = st.sidebar.selectbox ('Select the Vehicle Type',[ 1,  0])
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
    Power_perf_factor = st.sidebar.slider('Power_perf_factor', 23.27, 188.14, 130.0)
    Vehicle_type_Car = st.sidebar.slider('Vehicle_type_Car', 0.0, 1.0, 0.5)
    Vehicle_type_Passenger = st.sidebar.slider('Vehicle_type_Passenger', 0.0, 1.0, 0.5)
    data = {'Manufacturer': Manufacturer,
            'Model': Model,
            'Vehicle_type': Vehicle_type,
            '__year_resale_value':  __year_resale_value,
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

loaded_model = pickle.load(open("Car_salesmodel.h5", "rb"))

prediction = loaded_model.predict(df)

st.subheader('Prediction')
st.write(prediction)
