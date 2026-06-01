import streamlit as st
import requests

# 1. Page Configuration
st.set_page_config(page_title="PlayerSync AI Portal", page_icon="⚽", layout="wide")

# Custom CSS styling for glowing cards and neon accents
st.markdown("""
    <style>
    .big-title { font-size: 42px !important; font-weight: 800; color: #00FF66; margin-bottom: 0px; }
    .subtitle { font-size: 18px !important; color: #8A99AD; margin-bottom: 30px; }
    div[data-testid="stMetricValue"] { color: #00FF66 !important; font-size: 48px !important; font-weight: 700; }
    div[data-testid="stMetricLabel"] { color: #FFFFFF !important; font-size: 16px !important; }
    </style>
""", unsafe_allow_html=True)

# 2. Main Header Banner
st.markdown('<p class="big-title">⚽ PLAYERSYNC AI ENGINE</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Next-Generation Athletic Intelligence & Predictive Performance Clustering</p>', unsafe_allow_html=True)

# 3. Sidebar Metric Controller Panel
st.sidebar.markdown("<h2 style='color: #00FF66; margin-top: 0;'>🏃‍♂️ Player Metrics</h2>", unsafe_allow_html=True)
st.sidebar.markdown("Adjust the feature sliders below to capture live raw field tracking performance data.")

f1 = st.sidebar.slider("🔥 Feature 1: Speed & Pace", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
f2 = st.sidebar.slider("🎯 Feature 2: Accuracy & Passing", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
f3 = st.sidebar.slider("🛡️ Feature 3: Defensive Positioning", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
f4 = st.sidebar.slider("🔋 Feature 4: Stamina & Workrate", min_value=0.0, max_value=10.0, value=5.0, step=0.1)

st.sidebar.markdown("---")

# 4. Triggering the AI Analysis
if st.sidebar.button("RUN ML ENGINE", type="primary", use_container_width=True):
    # Package slider data values into JSON formatting
    payload = {
        "feature_1": f1,
        "feature_2": f2,
        "feature_3": f3,
        "feature_4": f4
    }
    
    with st.spinner("Decoding multidimensional array matrices..."):
        try:
            # Make an HTTP request call to your backend running FastAPI script
            response = requests.post("http://127.0.0.1:8000/predict", json=payload)
            
            if response.status_code == 200:
                result = response.json()
                cluster_id = result.get("assigned_cluster")
                prediction_id = result.get("prediction_id")
                
                st.markdown("### 📊 Live Predictive Analysis Result")
                
                # Render sleek responsive stat cards
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric(label="ASSIGNED PRO PROFILE", value=f"GROUP {cluster_id}")
                with col2:
                    st.metric(label="DATABASE ID LOGGED", value=f"#{prediction_id}")
                with col3:
                    st.metric(label="SYSTEM ENGINE NODE", value="ACTIVE ✅")
                    
                st.success(f"⚡ Success! {result.get('msg')}")
                
            else:
                st.error(f"❌ Backend Cluster Error: {response.text}")
        except Exception as e:
            st.error("🔌 Connectivity Failure: Could not establish a link to the FastAPI core backend engine. Make sure your server is activated on port 8000!")
else:
    # Default instruction block before clicking the main action trigger
    st.markdown("### 🎛️ System Status: Awaiting Matrix Input")
    st.info("Adjust the performance metrics inside the left control panel and click 'RUN ML ENGINE' to fire up the live cluster prediction engine.")