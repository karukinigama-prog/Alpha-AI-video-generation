import streamlit as st
from huggingface_hub import InferenceClient
import time

# --- API CONFIGURATION ---
if "HF_TOKEN" in st.secrets:
    client = InferenceClient(token=st.secrets["HF_TOKEN"])
else:
    st.error("Secrets වල HF_TOKEN එකතු කරන්න!")
    st.stop()

# --- UI SETTINGS ---
st.set_page_config(page_title="Alpha AI - Pro Video", page_icon="🎬", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #000000; color: white; }
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #ff0055, #7000ff);
        color: white;
        font-weight: bold;
        border-radius: 12px;
        height: 3.5em;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎬 Alpha AI Pro Video Gen")
st.markdown("### Created by **Hasith Karunarathna**")

# --- INPUT ---
prompt = st.text_area("වීඩියෝවේ විස්තරය ලියන්න (Prompt):", placeholder="e.g. A cinematic shot of a robot walking through a rainy street, neon lights, 4k...")

if st.button("Generate Pro Video 🚀"):
    if prompt:
        with st.spinner("Hugging Face සර්වර් එකෙන් වීඩියෝව නිර්මාණය කරමින් පවතී... (මෙයට විනාඩියක් පමණ ගත විය හැක)"):
            try:
                # ලෝකයේ දැනට තියෙන හොඳම Open Source Video Model එකක් (HunyuanVideo)
                # මෙය Hugging Face API හරහා කැඳවීම
                video_data = client.text_to_video(
                    prompt,
                    model="hunyuanvideo-community/HunyuanVideo" # හෝ "THUDM/CogVideoX-5b"
                )
                
                # වීඩියෝව පෙන්වීම
                st.video(video_data)
                
                st.success("වීඩියෝව සාර්ථකව නිපදවා ඇත!")
                
            except Exception as e:
                st.error("දැනට මෙම මාදිලිය කාර්යබහුලයි හෝ සම්බන්ධ වීමේ ගැටලුවක් ඇත. කරුණාකර මොහොතකින් නැවත උත්සාහ කරන්න.")
    else:
        st.warning("කරුණාකර Prompt එකක් ඇතුළත් කරන්න.")

st.divider()
st.caption("Alpha AI Elite | Professional Video Mode | Created by Hasith")
