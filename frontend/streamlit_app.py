import streamlit as st
import requests

st.title("🎬 Movie Rating Predictor")

user = st.number_input("User ID", 0)
movie = st.number_input("Movie ID", 0)
genre = st.number_input("Genre ID", 0)

if st.button("Predict Rating"):
    payload = {"User_Id": user, "Movie_Name": movie, "Genre": genre}
    response = requests.post("https://<your-app-name>.azurewebsites.net/predict", json=payload)

    if response.status_code == 200:
        st.success(f"Predicted Rating: ⭐ {response.json()['predicted_rating']}")
    else:
        st.error("Prediction failed.")
