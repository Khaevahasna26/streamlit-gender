import pickle
import streamlit as st

# load save model 
model = pickle.load(open('gender_model.sav', 'rb'))

# Judul Untuk Web
st.title('Data Mining Prediksi Jenis Kelamin')
st.subheader('Nama : Khaeva Hasna') 
st.subheader('Nim : 191351047')


# Form Input
long_hair = st.text_input('Masukan Nilai Long Hair')

forehead_width_cm = st.text_input('Masukan Nilai Forehead Width (cm)') 

forehead_height_cm = st.text_input('Masukan  Nilai Forehead Height (cm)')

nose_wide = st.text_input('Masukan Nilai Nose Wide')

nose_long = st.text_input('Masukan Nilai Nose Long')

lips_thin = st.text_input('Masukan Nilai Lips Thin')

distance_nose_to_lip_long = st.text_input('Masukan Nilai Distance Nose To Lip Long')


# kode Prediksi

gend_diagnosis = ' '

#Button Prediksi
if st.button('Test'):
    gend_prediction = model.predict([[long_hair, forehead_width_cm, forehead_height_cm, nose_wide, nose_long, lips_thin, distance_nose_to_lip_long]])

    if(gend_prediction[0]==0):
        gend_diagnosis = 'Jenis Kelamin Wanita'

    else:
         gend_diagnosis = 'Jenis Kelamin Pria'

st.success(gend_diagnosis)
