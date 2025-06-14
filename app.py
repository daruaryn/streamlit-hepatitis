import streamlit as st
import joblib

# Load model
model = joblib.load("model_hepatitis.pkl")

st.title("Prediksi Penyakit Hepatitis")

# Input dari pengguna (harus sesuai urutan training)
sex = st.selectbox("Jenis Kelamin (0 = Pria, 1 = Wanita)", [0, 1])
age = st.number_input("Umur", min_value=0)
steroid = st.selectbox("Pernah pakai steroid?", [0, 1])
antivirals = st.selectbox("Pernah pakai antivirus?", [0, 1])
fatigue = st.selectbox("Sering lelah?", [0, 1])
malaise = st.selectbox("Lemas?", [0, 1])
anorexia = st.selectbox("Anoreksia?", [0, 1])
liver_big = st.selectbox("Hati membesar?", [0, 1])
liver_firm = st.selectbox("Hati mengeras?", [0, 1])
spleen_palpable = st.selectbox("Limpa teraba?", [0, 1])
spiders = st.selectbox("Spider angioma?", [0, 1])
ascites = st.selectbox("Ascites?", [0, 1])
varices = st.selectbox("Varises esofagus?", [0, 1])
bilirubin = st.number_input("Bilirubin", min_value=0.0)
alk_phosphate = st.number_input("Alk Phosphate", min_value=0.0)
sgot = st.number_input("SGOT", min_value=0.0)
albumin = st.number_input("Albumin", min_value=0.0)
protime = st.number_input("Protime", min_value=0.0)
histology = st.selectbox("Hasil Histologi?", [0, 1])

# Tombol prediksi
if st.button("Prediksi"):
    input_data = [[
        sex, age, steroid, antivirals, fatigue, malaise, anorexia,
        liver_big, liver_firm, spleen_palpable, spiders, ascites, varices,
        bilirubin, alk_phosphate, sgot, albumin, protime, histology
    ]]
    hasil = model.predict(input_data)
    st.success(f"Hasil Prediksi: {'POSITIF Hepatitis' if hasil[0] == 1 else 'NEGATIF Hepatitis'}")
