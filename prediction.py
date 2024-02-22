import streamlit as st
import pickle
import numpy as np
from streamlit_option_menu import option_menu

def load_model():
    with open('saved.pkl','rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

rf = data["model"]

with st.sidebar:
    selected = option_menu('The Doctor\'s Guide',['Liver Cirrhosis Prediction'],default_index=0)

if(selected=='Liver Cirrhosis Prediction'):

    st.title("Liver Cirrhosis Stage Prediction")

    col1,col2,col3 = st.columns(3)

    with col1:
        age = st.number_input("Age")
    with col1:
        bilirubin = st.number_input("Bilirubin[mg/dl]")
    with col1:
        cholestrol = st.number_input("Cholestrol[mg/dl]")
    with col1:
        albumin = st.number_input("Albumin[gm/dl]")
    with col1:
        copper = st.number_input("Copper[ug/day]")
    with col1:
        alk_phos = st.number_input("Alk_Phos[U/liter]")
    with col2:
        sgot = st.number_input("SGOT[U/ml]")
    with col2:
        tryglicerides = st.number_input("Tryglicerides[mg/dl]")
    with col2:
        platelets = st.number_input("Platelets[ml/1000]")
    with col2:
        prothombin = st.number_input("Prothrombin[s]")

    drug_val = (1,0)
    sex_val = (1,0)
    ascites_val = (1,0)
    hepatomegaly_val = (1,0)
    spiders_val = (1,0)
    edema_with_diuretic_val = (1,0)
    edema_with_no_diuretic_val =(1,0)

    with col2:
        drug = st.selectbox("Drug Used - Placebo(1) D-Penicilamine(0)",drug_val)
    with col2:
        sex = st.selectbox("Sex - Male(1) Female(0)",sex_val)
    with col3:
        ascites = st.selectbox("Ascites - Present(1) Absent(0)",ascites_val)
    with col3:
        hepatomegaly = st.selectbox("Hepatomegaly - Present(1) Absent(0)",hepatomegaly_val)
    with col3:
        spiders = st.selectbox("Spiders - Present(1) Absent(0)",spiders_val)
    with col3:
        edema_with_diuretic = st.selectbox("Edema_with_diuretic - Present(1) Absent(0)",edema_with_diuretic_val)
    with col3:
        edema_with_no_diuretic = st.selectbox("Edema_with_no_diuretic - Present(1) Absent(0)",edema_with_no_diuretic_val)

    result = ''

    user_input_float_val = [age,bilirubin,cholestrol,albumin,copper,alk_phos,sgot,tryglicerides,platelets,prothombin]
    user_input_int_val = [drug,sex,ascites,hepatomegaly,spiders,edema_with_diuretic,edema_with_no_diuretic]

    all_inputs = user_input_float_val + user_input_int_val

    if st.button('Predict the result'):
        predicton = rf.predict([all_inputs])

        if(predicton[0]==1):
            result = 'The patient is in 1st stage'
        elif(predicton[0]==2):
            result = 'The patient is in 2nd stage'
        elif(predicton[0]==3):
            result = 'The patient is in 3rd stage'
        else:
            result = 'The patient is in 4th stage'
        
    st.success(result)


