import streamlit as st
import requests
import io
from PIL import Image

# --- API CONFIGURATION (Using Streamlit Secrets) ---
# මෙහිදී කෙලින්ම Token එක ලියනවා වෙනුවට Secrets වලින් ලබා ගනී
if "HF_TOKEN" in st.secrets:
    HF_TOKEN = st.secrets["HF_TOKEN"]
else:
    st.error("කරුණාකර Streamlit Cloud Settings -> Secrets වල HF_TOKEN එකතු කරන්න!")
    st.stop()

# Hugging Face Model URL (Stable Diffusion XL)
# පරණ එක අයින් කරලා මේක දාන්න
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

# --- UI SETTINGS ---
st.set_page_config(page_title="Alpha AI - Elite Edition", page_icon="💎", layout="centered")

# Custom CSS for Professional Dark UI
st.markdown("""
    <style>
    .main { background-color: #000000; color: white; }
    .stTextArea textarea { 
        background-color: #111; 
        color: #00ffcc; 
        border: 1px solid #00ffcc;
        border-radius: 10px;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #7000ff, #00ffcc);
        color: white;
        font-weight: bold;
        border: none;
        height: 3.5em;
        border-radius: 10px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 20px rgba(0, 255, 204, 0.4);
        color: white;
    }
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("💎 Alpha AI Elite Image Gen")
st.markdown("### Created by **Hasith Karunarathna**")
st.write("Hugging Face API හරහා ක්‍රියාත්මක වන සීමා රහිත Ultra HD රූප ජෙනරේටරය.")

# --- INPUT SECTION ---
prompt = st.text_area(
    "ඔබේ සිතුවිල්ල ඉංග්‍රීසියෙන් ලියන්න (Prompt):", 
    placeholder="e.g. A realistic Iron Man suit with Sri Lankan traditional patterns, 8k, highly detailed, cinematic lighting...",
    height=150
)

if st.button("Generate Ultra HD Image 🚀"):
    if prompt:
        with st.spinner("Elite සර්වර් එකෙන් රූපය නිර්මාණය කරමින් පවතී..."):
            try:
                # API එකට Request එක යැවීම
                response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
                
                if response.status_code == 200:
                    image_bytes = response.content
                    image = Image.open(io.BytesIO(image_bytes))
                    
                    # රූපය පෙන්වීම
                    st.image(image, use_container_width=True, caption=f"Alpha AI Result: {prompt}")
                    
                    # Download Button
                    st.download_button(
                        label="Download Image 📥",
                        data=image_bytes,
                        file_name="alpha_ai_elite.png",
                        mime="image/png"
                    )
                elif response.status_code == 503:
                    st.warning("සර්වර් එක දැනට කාර්යබහුලයි (Model Loading). කරුණාකර තත්පර කිහිපයකින් නැවත උත්සාහ කරන්න.")
                else:
                    st.error(f"Error {response.status_code}: සම්බන්ධ වීමේ ගැටලුවක්. කරුණාකර පසුව උත්සාහ කරන්න.")
                    
            except Exception as e:
                st.error(f"දෝෂයක් සිදු විය: {e}")
    else:
        st.warning("කරුණාකර රූපය පිළිබඳ විස්තරයක් ඇතුළත් කරන්න.")

# --- FOOTER ---
st.divider()
st.caption("Alpha AI Elite Edition | Status: Online ✅ | Secured by Secrets")
