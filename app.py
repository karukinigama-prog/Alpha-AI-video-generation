import streamlit as st
from gradio_client import Client
import os

# --- UI SETTINGS ---
st.set_page_config(page_title="Alpha AI - Ultimate Video", page_icon="🎬", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #050505; color: white; }
    .stTextArea textarea { background-color: #111; color: #ff0055; border: 1.5px solid #ff0055; }
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #ff0055, #ffcc00);
        color: black;
        font-weight: bold;
        font-size: 18px;
        height: 3.5em;
        border-radius: 12px;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎬 Alpha AI Ultimate Video")
st.markdown("### Created by **Hasith Karunarathna**")
st.write("මෙය කිසිම API Key එකක් අවශ්‍ය නොවන, සීමා රහිත වෘත්තීය මට්ටමේ වීඩියෝ ජෙනරේටරයයි.")

# --- INPUT SECTION ---
prompt = st.text_area("ඔබට අවශ්‍ය වීඩියෝවේ විස්තරය ලියන්න (English Prompt):", 
                     placeholder="Example: A cinematic drone shot of a tropical island, 4k, realistic...")

if st.button("Generate High-End Video 🚀"):
    if prompt:
        with st.spinner("ලෝකයේ වේගවත්ම සර්වර් එකකට සම්බන්ධ වී වීඩියෝව නිර්මාණය කරමින් පවතී... (විනාඩි 1-2ක් ගතවිය හැක)"):
            try:
                # Gradio Client හරහා ලෝකයේ ප්‍රබලම Space එකකට සම්බන්ධ වීම
                # මෙහිදී කිසිම API Key එකක් අවශ්‍ය නොවේ
                client = Client("tencent/HunyuanVideo")
                
                result = client.predict(
                    prompt=prompt,
                    api_name="/generate_video"
                )
                
                # වීඩියෝවේ පාත් එක ලබා ගැනීම
                video_path = result
                
                if video_path:
                    st.success("වීඩියෝව සාර්ථකව නිපදවා ඇත!")
                    st.video(video_path)
                    
                    # Download Button
                    with open(video_path, "rb") as f:
                        st.download_button("Download Video 📥", f, file_name="alpha_ai_video.mp4")
                
            except Exception as e:
                st.error("දැනට සර්වර් එකේ පෝලිමක් (Queue) පවතී. කරුණාකර මොහොතකින් නැවත උත්සාහ කරන්න.")
    else:
        st.warning("කරුණාකර වීඩියෝව ගැන විස්තරයක් ලියන්න.")

st.divider()
st.caption("Alpha AI Ultimate | No API Key Required | Powered by HunyuanVideo")
