import streamlit as st
import joblib

# Load model and encoders
model = joblib.load("career_model.pkl")
le_interest = joblib.load("le_interest.pkl")
le_skill = joblib.load("le_skill.pkl")
le_personality = joblib.load("le_personality.pkl")
le_career = joblib.load("le_career.pkl")

st.title("Smart Career Guide")
st.write("Get the best career recommendation based on your interests, skills, and personality.")

# Dropdowns for user input
interest = st.selectbox("Select your Interest", le_interest.classes_)
skill = st.selectbox("Select your Skill Level", le_skill.classes_)
personality = st.selectbox("Select your Personality", le_personality.classes_)

# Predict button
if st.button("Suggest Career"):
    try:
        input_data = [[
            le_interest.transform([interest])[0],
            le_skill.transform([skill])[0],
            le_personality.transform([personality])[0]
        ]]
        result = model.predict(input_data)
        career = le_career.inverse_transform(result)[0]
        st.success(f" Recommended Career: **{career}**")
    except:
        st.error("Something went wrong! Please check your inputs.")
