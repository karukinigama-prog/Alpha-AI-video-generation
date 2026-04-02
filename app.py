import streamlit as st
import urllib.parse

# 1. Secrets වලින් API Key එක ලබා ගැනීම
POLL_API_KEY = st.secrets["POLLINATIONS_API_KEY"]

def generate_voice_ui():
    st.subheader("🎙️ Alpha Voice Lab")
    st.write("ඔයා දෙන ඕනෑම වාක්‍යයක් AI හඬකින් කියවන්න මෙතනින් පුළුවන්.")

    # කතා කළ යුතු දේ
    input_text = st.text_area("කියවිය යුතු දේ ලියන්න:", "Hello Hasith, welcome to Alpha AI Voice Lab!")
    
    # හඬවල් (Voices) තෝරාගැනීම - Docs වල තියෙන ඒවා
    voice_choice = st.selectbox("හඬ තෝරන්න:", 
                                ["nova", "alloy", "echo", "fable", "onyx", "shimmer", "ballad", "coral"])
    
    # Output format එක (MP3 තමයි හොඳම)
    out_format = st.selectbox("Format එක:", ["mp3", "wav", "aac"])

    if st.button("Generate Voice 🔊"):
        if input_text:
            with st.spinner("Alpha AI හඬ සකස් කරමින් පවතී..."):
                try:
                    # පෙළ URL එකකට ගැලපෙන සේ සැකසීම
                    encoded_text = urllib.parse.quote(input_text)
                    
                    # Pollinations Audio API URL එක
                    voice_url = (
                        f"https://gen.pollinations.ai/audio/{encoded_text}?"
                        f"voice={voice_choice}&"
                        f"response_format={out_format}&"
                        f"key={POLL_API_KEY}"
                    )
                    
                    # හඬ ප්ලේ කිරීම
                    st.audio(voice_url)
                    st.success("හඬ සාර්ථකව නිර්මාණය වුණා!")
                    
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("කරුණාකර කියවිය යුතු පෙළක් ඇතුළත් කරන්න.")

# App එකේ Tab එකක් ඇතුළේ මේක පාවිච්චි කරන්න
generate_voice_ui()
