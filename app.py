import streamlit as st
import joblib
import numpy as np

model = joblib.load('placement_model.pkl')

st.title("Student Placement Predictor")

internships = st.number_input("Number of Internships", min_value=0, max_value=5, value=1)
cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, value=7.5)
backlogs = st.selectbox("History of Backlogs", [0, 1])

if st.button("Predict"):
    features = np.array([[internships, cgpa, backlogs]])
    prediction = model.predict(features)[0]
    if prediction == 1:
        st.success("Likely to be Placed! 🎉")
    else:
        st.error("Likely Not Placed")
