# -*- coding: utf-8 -*-
"""app

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AicAMepeYrF4EVXdFfYtiNS_4rHTsKVA
"""

import streamlit as st
import pickle
import numpy as np

# Load the model
with open('model_prediksi.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Prediksi Hasil Produksi Padi Provinsi Jawa Tengah")  # Mengganti judul

# Informasi Akurasi Model
st.markdown("**Berisi 3 Variabel yaitu Luas Tanam (Ha), Luas Panen (Ha), dan Produktivitas (Ku/Ha).**")

# Luas Tanam dengan batasan minimal dan maksimal, dan satuan hektar
Luas_Tanam = st.number_input("Luas Tanam (Ha) (min: 0, maks: 1000000) ", min_value=0.0, max_value=1000000.0, format="%.2f")
# Luas Panen dengan satuan hekta
Luas_Panen = st.number_input("Luas Panen (Ha) (min: 0, maks: 1000000) ", min_value=0.0, max_value=1000000.0, format="%.2f")
# Produktivitas dengan satuan Ku/Ha
Produktivitas = st.number_input("Produktivitas (Ku/Ha) (min: 0, maks: 100) ", min_value=0.0, max_value=10000.0, format="%.2f")

if st.button("Prediksi"):
    features = np.array([[Luas_Tanam, Luas_Panen, Produktivitas]])
    prediction = model.predict(features)
    st.write(f"Hasil Prediksi Produksi Padi : {prediction[0]:.2f} ton")
