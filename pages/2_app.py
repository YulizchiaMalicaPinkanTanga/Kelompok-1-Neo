import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import pickle
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
from sklearn.linear_model import Ridge
from sklearn.preprocessing import LabelEncoder

st.title("SolarGuard : Energy Anomaly Maintenance Scheduling for Solar Power Plant")

with st.container():
    st.write('Please Upload Data File')
    uploaded_file = st.file_uploader('Choose a CSV file')
    save_button = st.button('save file')
    if save_button:
        if uploaded_file is not None:
            with open(os.path.join("./save_folder",uploaded_file.name),mode='wb') as f:
               f.write(uploaded_file.getbuffer())
               st.success(f"File {uploaded_file.name} saved successfully")



with st.container():
    display_button = st.button('Display Data')  
    if display_button:         
        data = pd.read_csv('./save_folder/plant_generation_data.csv')
        # Menampilkan tabel dengan nama
        st.write("## Plant Generation Data")
        st.table(data.head())
        data['DATE_TIME'] = pd.to_datetime(data["DATE_TIME"])
        #Plant generation data
        fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 10))
        # Plot histogram DC_POWER
        data['DC_POWER'].hist(ax=axes[0, 0], bins=20, color='blue', alpha=0.7)
        axes[0, 0].set_title('DC_POWER')
        # Plot histogram AC_POWER
        data['AC_POWER'].hist(ax=axes[0, 1], bins=20, color='green', alpha=0.7)
        axes[0, 1].set_title('AC_POWER')
        # Plot histogram DAILY_YIELD
        data['DAILY_YIELD'].hist(ax=axes[1, 0], bins=20, color='orange', alpha=0.7)
        axes[1, 0].set_title('DAILY_YIELD')
        # Plot histogram TOTAL_YIELD
        data['TOTAL_YIELD'].hist(ax=axes[1, 1], bins=20, color='red', alpha=0.7)
        axes[1, 1].set_title('TOTAL_YIELD')
        st.write("Generation Data Feature Distribution")
        st.pyplot(fig)

        #Memvisualisasikan tren deret waktu untuk fitur-fitur utama
        fig = plt.figure(figsize=(15,20))
        ax1 = fig.add_subplot(4, 1, 1)
        ax2 = fig.add_subplot(4, 1, 2)
        ax3 = fig.add_subplot(4, 1, 3)
        ax4 = fig.add_subplot(4, 1, 4)
        fig.subplots_adjust(hspace=0.5)
        st.write("DC POWER, AC POWER, and TOTAL YIELD Over Time")
        # Plot DC_POWER
        data.plot(x='DATE_TIME', y='DC_POWER', ax=ax1, title="DC_POWER Over Time")
        # Plot AC_POWER
        data.plot(x='DATE_TIME', y='AC_POWER', ax=ax2, title="AC_POWER Over Time")
        # Plot DAILY_YIELD
        data.plot(x='DATE_TIME', y='DAILY_YIELD', ax=ax3, title="DAILY_YIELD Over Time")
        # Plot TOTAL_YIELD
        data.plot(x='DATE_TIME', y='TOTAL_YIELD', ax=ax4, title="TOTAL_YIELD Over Time")
        # Menampilkan plot menggunakan st.pyplot()
        st.pyplot(fig)

with st.container():
    predict_button = st.button('Predict Data')
    if predict_button:
        data = pd.read_csv('./save_folder/plant_generation_data.csv')
        data['DATE_TIME'] = pd.to_datetime(data["DATE_TIME"])
        encoder = LabelEncoder()
        data['SOURCE_KEY_NUMBER'] = encoder.fit_transform(data['SOURCE_KEY'])
        PLANT_ID_mode = data['PLANT_ID'].mode()
        SOURCE_KEY_mode = data['SOURCE_KEY'].mode()
        DC_POWER_median = data['DC_POWER'].median()
        AC_POWER_median = data['AC_POWER'].median()
        DAILY_YIELD_median = data['DAILY_YIELD'].median()
        TOTAL_YIELD_median = data['TOTAL_YIELD'].median()
        #Preprocess
        data['PLANT_ID'].fillna(PLANT_ID_mode[0], inplace=True)
        data['SOURCE_KEY'].fillna(SOURCE_KEY_mode[0], inplace=True)
        data['DC_POWER'].fillna(DC_POWER_median, inplace=True)
        data['AC_POWER'].fillna(AC_POWER_median, inplace=True)
        data['DAILY_YIELD'].fillna(DAILY_YIELD_median, inplace=True)
        data['TOTAL_YIELD'].fillna(TOTAL_YIELD_median, inplace=True)
        data_real = data[['AC_POWER', 'DAILY_YIELD', 'TOTAL_YIELD']]
        #Import model
        file = open('model.pkl', 'rb')

        #dump information to that file
        model = pickle.load(file)
        Data_Prediction = model.predict(data_real)
        # Menampilkan plot hasil prediksi
        fig, ax = plt.subplots()
        plt.plot(Data_Prediction)                                  # Line chart hasil prediksi model
        plt.title('Next-Day DC Power Prediction Graph')             # Judul plot
        plt.xlabel("Data Every 15 minutes")                            # Nama sumbu X
        plt.ylabel("DC Power")                                     # Nama sumbu Y
        plt.legend(labels=['Prediction'])                          # Menambahkan legenda pada plot
        plt.show()
        st.pyplot(fig)

with st.container():
    anomaly_detector_and_warning_button= st.button('Anomaly Detector and Maintenance Warning')
    if anomaly_detector_and_warning_button:
        data = pd.read_csv('./save_folder/plant_generation_data.csv')
        data['DATE_TIME'] = pd.to_datetime(data["DATE_TIME"])
        encoder = LabelEncoder()
        data['SOURCE_KEY_NUMBER'] = encoder.fit_transform(data['SOURCE_KEY'])
        PLANT_ID_mode = data['PLANT_ID'].mode()
        SOURCE_KEY_mode = data['SOURCE_KEY'].mode()
        DC_POWER_median = data['DC_POWER'].median()
        AC_POWER_median = data['AC_POWER'].median()
        DAILY_YIELD_median = data['DAILY_YIELD'].median()
        TOTAL_YIELD_median = data['TOTAL_YIELD'].median()
        #Preprocess
        data['PLANT_ID'].fillna(PLANT_ID_mode[0], inplace=True)
        data['SOURCE_KEY'].fillna(SOURCE_KEY_mode[0], inplace=True)
        data['DC_POWER'].fillna(DC_POWER_median, inplace=True)
        data['AC_POWER'].fillna(AC_POWER_median, inplace=True)
        data['DAILY_YIELD'].fillna(DAILY_YIELD_median, inplace=True)
        data['TOTAL_YIELD'].fillna(TOTAL_YIELD_median, inplace=True)
        data_real = data[['AC_POWER', 'DAILY_YIELD', 'TOTAL_YIELD']]
        #Import model
        file = open('model.pkl', 'rb')

        #dump information to that file
        model = pickle.load(file)
        Data_Prediction = model.predict(data_real)

        # Menghitung perubahan relatif DC Power
        data['DC_Power_Change'] = data['DC_POWER'].pct_change()

        # Menetapkan batas ambang untuk mendeteksi penurunan drastis (gantilah sesuai kebutuhan)
        threshold = -0.3
    
        # Mendeteksi anomali
        anomaly_indices = data[data['DC_Power_Change'] < threshold].index

        fig, ax = plt.subplots()
        plt.plot(Data_Prediction)
        ax.scatter(anomaly_indices, data.loc[anomaly_indices, 'DC_POWER'], color='red', label='Anomaly')    
        ax.set(title='Anomaly Detection in Next-Day DC Power Prediction Graph', xlabel='Every 15 Minutes', ylabel='DC Power')
        ax.legend()
        plt.show()
        st.pyplot(fig)
        
        if not anomaly_indices.empty:
            anomaly_times = data.loc[anomaly_indices, 'DATE_TIME']
            anomaly_times_str = anomaly_times.dt.strftime('%H:%M:%S').tolist()
            st.warning(f"ANOMALIES DETECTED! THERE WILL BE A SIGNIFICANT DECREASE IN DC POWER AT  {', '.join(anomaly_times_str)}.")
        
