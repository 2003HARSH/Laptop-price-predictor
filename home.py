import pickle
import streamlit as st
import numpy as np
import base64


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)


def app():
    set_background("./bg_photo.jpg")
    
    pipe = pickle.load(open('pipe1.pkl', 'rb'))
    df = pickle.load(open('df.pkl', 'rb'))
    
    st.title("Laptop Price Pridector")
    
    company = st.selectbox('Brand', df['Company'].unique())
    
    type = st.selectbox('Type', df['TypeName'].unique())
    
    ram = st.selectbox('RAM (in GB)', df['Ram'].unique())
    
    weight = st.number_input("Weight of the Laptop (in kg)",value=1.5,min_value=1.0,max_value=4.0)
    
    touchscreen = st.selectbox('TouchScreen', ['No', "Yes"])
    
    ips = st.selectbox('IPS Display', ['No', "Yes"])
    
    screen_size = st.number_input('Screen Size (in inches)',value=14.0,min_value=14.0,max_value=16.0)
    
    resolution = st.selectbox('Screen Resolution', [
                              '1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'])
    
    cpu = st.selectbox('CPU', df['Cpu brand'].unique())
    
    hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])
    
    ssd = st.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024])
    
    gpu = st.selectbox('GPU', df['Gpu brand'].unique())
    
    os = st.selectbox('OS', df['os'].unique())
    
    if st.button("Predict"):
    
        if touchscreen == 'Yes':
            touchscreen = 1
        else:
            touchscreen = 0
    
        if ips == 'Yes':
            ips = 1
        else:
            ips = 0
    
        X_res = int(resolution.split('x')[0])
        Y_res = int(resolution.split('x')[1])
        ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
        query = np.array([company, type, ram, weight, touchscreen,
                         ips, ppi, cpu, hdd, ssd, gpu, os])
        query = query.reshape(1, 12)
        st.text("The predicted price of this configuration is Rs. " +
                 str(int(np.exp(pipe.predict(query)[0]))))
    
