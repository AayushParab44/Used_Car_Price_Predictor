import streamlit as st
import joblib

try:
    with open("random_forest_model1.pkl", "rb") as f:
        model = joblib.load(f)
except Exception as e:
    st.error(f"❌ Model failed to load: {e}")
    model = None

if model is not None:
    st.success("✅ Model loaded successfully!")
    # continue with prediction code here
else:
    st.stop()  # stop Streamlit execution safely
