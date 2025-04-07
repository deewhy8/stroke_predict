import streamlit as st
import joblib

model = joblib.load('stroke_pred.pkl')

st.title('Stroke Prediction Tool')
st.write('Predict likelihood of having a stroke based on certain demographics')
st.write()
st.write('Enter 1 for yes or 0 for no when applicable')

age = st.number_input('Enter age:')
hypertension = st.number_input('Has hypertension:')
heart_disease = st.number_input('Has heart disease:')
avg_glucose_level = st.number_input('Enter average blood glucose level:')
bmi = st.number_input('Enter BMI:')
ever_married = st.number_input('Ever married:')
gender = st.number_input('Gender (enter 1 for male, or 0 for female):')
residence_type_rural = st.number_input('Rural residence type:')
residence_type_urban = st.number_input('Urban residence type:')
work_type_govt_job = st.number_input('Work type government job:')
work_type_never_worked = st.number_input('Work type never worked')
work_type_private = st.number_input('Work type private:')
work_type_self_employed = st.number_input('Work type self-employed:')
work_type_child = st.number_input('Work type child:')
smoking_status_unknown = st.number_input('Smoking status unknown:')
smoking_status_former_smoker = st.number_input('Smoking status former smoker:')
smoking_status_never_smoked = st.number_input('Smoking status never smoked:')
smoking_status_smokes = st.number_input('Smoking status smokes:')

if st.button('Predict stroke likelihood'):
    
    features = [
    age,
    hypertension,
    heart_disease,
    avg_glucose_level,
    bmi,
    ever_married,
    gender,
    residence_type_rural,
    residence_type_urban,
    work_type_govt_job,
    work_type_never_worked,
    work_type_private,
    work_type_self_employed,
    work_type_child,
    smoking_status_unknown,
    smoking_status_former_smoker,
    smoking_status_never_smoked,
    smoking_status_smokes
    ]
    
    prediction = model.predict([features])[0]
    st.write(f'Are you likely to have a stroke: {prediction}')
