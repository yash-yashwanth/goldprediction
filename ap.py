import streamlit as st
import numpy as np
import pickle

# -------------------------------------------------
# 🌟 Page configuration
# -------------------------------------------------
st.set_page_config(
    page_title="💰 Gold Price Predictor",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------
# 🎨 Custom CSS styling (Swiggy-inspired look)
# -------------------------------------------------
st.markdown("""
    <style>
    body {
        background-color: #FFF8DC;
        color: #333333;
    }
    .main {
        background-color: #FFF8DC;
        padding: 2rem;
        border-radius: 15px;
    }
    h1, h2, h3 {
        color: #DAA520;
    }
    .stButton>button {
        background-color: #FFD700;
        color: black;
        border-radius: 10px;
        font-weight: bold;
        padding: 0.5em 1em;
        border: none;
    }
    .stButton>button:hover {
        background-color: #FFB700;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# 🧠 Load the trained model
# -------------------------------------------------
try:
    model = pickle.load(open("gold_price_model.pkl", "rb"))
except FileNotFoundError:
    st.error("Model file not found. Please make sure 'gold_price_model.pkl' is in the same folder.")
    st.stop()

# -------------------------------------------------
# 🏷️ App title and description
# -------------------------------------------------
st.title("💰 Gold Price Prediction App")
st.write("""
Welcome to the **Gold Price Predictor**!  
Enter market values below (like SPX, USO, SLV, and EUR/USD) to predict the **GLD (Gold ETF) price**.
""")

# -------------------------------------------------
# 📊 Input Section
# -------------------------------------------------
st.subheader("📥 Enter Market Data")

col1, col2, col3, col4 = st.columns(4)

with col1:
    SPX = st.number_input("S&P 500 (SPX)", min_value=0.0, value=2700.0, step=10.0)
with col2:
    USO = st.number_input("Crude Oil (USO)", min_value=0.0, value=14.0, step=0.5)
with col3:
    SLV = st.number_input("Silver Price (SLV)", min_value=0.0, value=15.5, step=0.1)
with col4:
    EURUSD = st.number_input("EUR/USD Exchange Rate", min_value=0.0, value=1.18, step=0.01)

# -------------------------------------------------
# 🧮 Prediction Button
# -------------------------------------------------
if st.button("🔮 Predict Gold Price"):
    input_data = np.array([[SPX, USO, SLV, EURUSD]])
    prediction = model.predict(input_data)[0]
    
    st.success(f"✨ Predicted Gold ETF (GLD) Price: **{prediction:.2f} USD**")

# -------------------------------------------------
# 📈 Footer info
# -------------------------------------------------
st.markdown("---")
st.markdown(
    "<center>Built with ❤️ using Streamlit | Inspired by Swiggy’s clean design</center>",
    unsafe_allow_html=True
)
