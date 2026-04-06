import streamlit as st
import fal_client
import os

# --- API CONFIGURATION ---
# ඔයා දුන්න Key එක මෙතන තියෙනවා. 
# පසුව ආරක්ෂාව සඳහා මෙය Streamlit Secrets වලට දාන්න.
os.environ["FAL_KEY"] = "e17aeca9-b41e-4cac-95f0-996370af31ff:10878663de189655b7340d51c1518534"

# --- UI SETTINGS ---
st.set_page_config(page_title="Alpha AI - Fast Video Gen", page_icon="⚡", layout="centered")

# Custom CSS for Branding
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ Alpha AI Video Generator")
st.subheader("Created by Hasith")
st.write("විනාඩියකටත් අඩු කාලයකින් ඕනෑම රූපයක් වීඩියෝවක් බවට පත් කරන්න.")

# --- INPUT SECTION ---
image_url = st.text_input("ඔබේ Image URL එක මෙතනට ලබා දෙන්න:", placeholder="https://unsplash.com/photo-xxx")

if st.button("Generate AI Video ✨"):
    if image_url:
        with st.spinner("Fal.ai Cloud සර්වර් එක හරහා වීඩියෝව සකසමින් පවතී..."):
            try:
                # Fal.ai API එක හරහා Stable Video Diffusion භාවිතා කිරීම
                handler = fal_client.submit(
                    "fal-ai/stable-video-diffusion/img2vid",
                    arguments={
                        "image_url": image_url,
                        "motion_bucket_id": 127,
                        "fps": 24
                    },
                )
                
                result = handler.get()
                video_url = result['video']['url']
                
                if video_url:
                    st.success("වීඩියෝව සාර්ථකව නිපදවා ඇත!")
                    st.video(video_url)
                    
                    # Download පහසුකම
                    st.download_button(
                        label="Download Video 📥",
                        data=video_url,
                        file_name="alpha_ai_video.mp4",
                        mime="video/mp4"
                    )
                else:
                    st.error("වීඩියෝව ලබා ගැනීමට නොහැකි විය.")
                    
            except Exception as e:
                st.error(f"දෝෂයක් සිදු විය: {str(e)}")
    else:
        st.warning("කරුණාකර රූපයක URL එකක් ඇතුළත් කරන්න.")

st.divider()
st.caption("© 2026 Alpha AI | Created by Hasith Karunarathna")
