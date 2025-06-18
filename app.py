import streamlit as st
import pandas as pd
import joblib
import base64

# 🌿 Custom Page Config
st.set_page_config(page_title="Skincare Recommender", page_icon="💧", layout="centered")


# 🌊 Add Background Image CSS
def set_background(image_path):
    with open(image_path, "rb") as img:
        encoded_string = base64.b64encode(img.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# 🖼️ Set the background
set_background("background.jpg")  # Make sure your image is in the same directory

st.markdown("""
    <style>
        /* Glassmorphic container */
        .main > div {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 2rem;
            margin-top: 2rem;
        }

        /* White font color for text and titles */
        h1, h2, h3, p, label, .stTextInput label, .stSelectbox label {
            color: white !important;
        }

        /* White button text */
        .stButton>button {
            background-color: rgba(255, 255, 255, 0.2);
            color: white;
            border: 1px solid rgba(255,255,255,0.4);
        }

        .stButton>button:hover {
            background-color: rgba(255, 255, 255, 0.3);
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Load model and encoders
model = joblib.load('skincare_model.pkl')
le_skin = joblib.load('le_skin.pkl')
le_climate = joblib.load('le_climate.pkl')
le_preference = joblib.load('le_preference.pkl')
le_product = joblib.load('le_product.pkl')

# 🌼 App Title
st.title("💧 Skincare Product Recommender")
st.write("Discover the *perfect skincare* based on your skin type, climate, and beauty goals. 🌿")

# 🌸 User Inputs
skin_type = st.selectbox("Select your skin type:", ["oily", "dry", "combination", "sensitive", "normal"])
climate = st.selectbox("Select your climate:", ["humid", "dry", "cold", "moderate"])
preference = st.selectbox("Select your preference:", ["matte", "glowing", "natural", "hydrated"])

# 🌟 Predict Button
if st.button("Get Recommendation 💡"):
    try:
        input_features = [[
            le_skin.transform([skin_type])[0],
            le_climate.transform([climate])[0],
            le_preference.transform([preference])[0]
        ]]
        prediction = model.predict(input_features)
        result = le_product.inverse_transform(prediction)[0]
        st.success(f"🌸 Recommended Skincare: **{result}**")
    except Exception as e:
        st.error("Oops! Something went wrong. Please try again.")