import streamlit as st
import urllib.parse
import requests

# 1. Streamlit secrets වලින් API Key එක ලබා ගැනීම
# ඔයා secrets.toml එකේ POLLINATIONS_API_KEY කියලා මේක දාලා තියෙන්න ඕනේ
POLL_API_KEY = st.secrets["POLLINATIONS_API_KEY"]

def generate_video_url(prompt, model="veo", duration=4):
    # Prompt එක URL එකකට ගැලපෙන සේ encode කිරීම
    encoded_prompt = urllib.parse.quote(prompt)
    
    # Pollinations Documentation එකේ විදිහට URL එක සැකසීම
    # මෙතනදී key එක query parameter එකක් ලෙස යවනවා (ලේසිම ක්‍රමය)
    video_url = f"https://gen.pollinations.ai/video/{encoded_prompt}?model={model}&duration={duration}&key={POLL_API_KEY}"
    
    return video_url

# UI කොටස
st.title("🎬 Alpha AI Video Lab")

video_prompt = st.text_input("වීඩියෝවට අවශ්‍ය දේ ලියන්න:", "a sunset timelapse")

if st.button("Generate Video"):
    if video_prompt:
        with st.spinner("Alpha AI is generating your video..."):
            # URL එක සාදා ගැනීම
            final_url = generate_video_url(video_prompt)
            
            # පරීක්ෂා කිරීම සඳහා URL එක පෙන්වන්න (විකල්ප)
            # st.write(f"Debug URL: {final_url}")
            
            # වීඩියෝව පෙන්වීම
            st.video(final_url)
            st.success("වීඩියෝව සාර්ථකව නිර්මාණය වුණා!")
    else:
        st.warning("කරුණාකර prompt එකක් ඇතුළත් කරන්න.")
