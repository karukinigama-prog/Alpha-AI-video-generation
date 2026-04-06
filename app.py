import streamlit as st
import requests
import io
from PIL import Image

# --- API KEYS FROM SECRETS ---
try:
    HF_TOKEN = st.secrets["HF_TOKEN"]
    PIXABAY_KEY = st.secrets["PIXABAY_KEY"]
except:
    st.error("කරුණාකර Streamlit Secrets වල API Keys ඇතුළත් කරන්න!")
    st.stop()

# --- UI CONFIGURATION ---
st.set_page_config(page_title="Alpha AI - Multimedia Elite", page_icon="🚀", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #050505; color: white; }
    .stTextInput > div > div > input, .stTextArea textarea { 
        background-color: #111; color: #00ffcc; border: 1px solid #00ffcc; 
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #00ffcc, #0055ff);
        color: white; font-weight: bold; border-radius: 10px; height: 3.5em;
    }
    .result-card {
        border: 1px solid #333; padding: 15px; border-radius: 15px; margin-bottom: 20px;
        background-color: #111;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Alpha AI Multimedia Elite")
st.markdown("### Created by **Hasith Karunarathna**")

# --- TABS FOR DIFFERENT FEATURES ---
tab1, tab2 = st.tabs(["🎨 AI Image Generator", "🎥 Real Video Finder"])

# --- TAB 1: AI IMAGE GENERATOR (Hugging Face) ---
with tab1:
    st.header("AI Image Generator")
    img_prompt = st.text_area("මොන වගේ රූපයක්ද ඕනේ? (Prompt):", key="img_p", placeholder="e.g. A robotic lion, neon lights, 8k...")
    
    if st.button("Generate AI Image ✨"):
        if img_prompt:
            with st.spinner("AI රූපය සකසමින් පවතී..."):
                API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"
                headers = {"Authorization": f"Bearer {HF_TOKEN}"}
                response = requests.post(API_URL, headers=headers, json={"inputs": img_prompt})
                
                if response.status_code == 200:
                    image = Image.open(io.BytesIO(response.content))
                    st.image(image, use_container_width=True)
                    st.download_button("Download Image 📥", response.content, "alpha_ai.png", "image/png")
                else:
                    st.error("සර්වර් එකේ ගැටලුවක්. පසුව උත්සාහ කරන්න.")

# --- TAB 2: REAL VIDEO FINDER (Pixabay) ---
with tab2:
    st.header("Real Video Search")
    vid_query = st.text_input("සොයන වීඩියෝව ගැන ලියන්න:", key="vid_q", placeholder="e.g. Nature, Space, Cars...")
    
    if st.button("Search Videos 🔍"):
        if vid_query:
            with st.spinner("වීඩියෝ සොයමින් පවතී..."):
                v_url = f"https://pixabay.com/api/videos/?key={PIXABAY_KEY}&q={vid_query.replace(' ', '+')}&per_page=5"
                v_res = requests.get(v_url).json()

                if v_res.get('hits'):
                    for video in v_res['hits']:
                        st.markdown('<div class="result-card">', unsafe_allow_html=True)
                        v_link = video['videos']['medium']['url']
                        st.video(v_link)
                        st.write(f"품질: {video['width']}x{video['height']}")
                        st.markdown(f"[Direct Download 📥]({v_link})")
                        st.markdown('</div>', unsafe_allow_html=True)
                else:
                    st.warning("වීඩියෝ හමු වූයේ නැත.")

st.divider()
st.caption("Alpha AI Elite Edition | Status: Fast & Secure ✅")
