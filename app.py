import streamlit as st
from gtts import gTTS
import requests
import urllib.parse
import os

def alpha_audio_lab():
    st.title("🎙️ Alpha Ultimate Audio Lab")
    
    # Tabs දෙකක් හදමු Voice සහ Music වලට
    tab_voice, tab_music = st.tabs(["Voice Generation (gTTS)", "Music Explorer (Jamendo)"])

    # --- 1. Voice Generation (gTTS) ---
    with tab_voice:
        st.subheader("අසීමිතව හඬවල් නිර්මාණය කරන්න")
        text_input = st.text_area("කියවිය යුතු දේ ලියන්න:", "Hello Hasith, Welcome to Alpha AI!")
        
        # භාෂාව තෝරාගැනීම
        lang_options = {
            "English": "en",
            "Sinhala (සිංහල)": "si",
            "Hindi (हिन्दी)": "hi",
            "Tamil (தமிழ்)": "ta",
            "Japanese": "ja"
        }
        selected_lang = st.selectbox("භාෂාව තෝරන්න (Language):", list(lang_options.keys()))
        
        if st.button("Generate Voice 🔊"):
            if text_input:
                with st.spinner("හඬ සකස් කරමින් පවතී..."):
                    tts = gTTS(text=text_input, lang=lang_options[selected_lang], slow=False)
                    tts.save("alpha_voice.mp3")
                    st.audio("alpha_voice.mp3")
                    st.success(f"{selected_lang} හඬ සාර්ථකව නිර්මාණය වුණා!")
            else:
                st.warning("කරුණාකර පෙළක් ඇතුළත් කරන්න.")

    # --- 2. Music Explorer (Jamendo) ---
    with tab_music:
        st.subheader("නොමිලේ සංගීතය සොයාගන්න")
        music_query = st.text_input("සංගීත වර්ගය (Genre):", "Lo-fi beats")
        
        if st.button("Search Music 🔍"):
            if music_query:
                with st.spinner("සින්දු සොයමින් පවතී..."):
                    # Jamendo Free Client ID
                    client_id = "56d30cce"
                    url = f"https://api.jamendo.com/v3.0/tracks/?client_id={client_id}&format=json&limit=3&namesearch={music_query}"
                    
                    try:
                        response = requests.get(url)
                        data = response.json()
                        
                        if data['results']:
                            for track in data['results']:
                                with st.container():
                                    st.markdown(f"### 🎶 {track['name']}")
                                    st.caption(f"Artist: {track['artist_name']}")
                                    st.audio(track['audio'])
                                    st.markdown(f"[⬇️ Download MP3]({track['audio']})")
                                    st.write("---")
                        else:
                            st.error("ගැලපෙන සින්දු හමු වුණේ නැහැ.")
                    except Exception as e:
                        st.error(f"Error: {e}")

# App එකේ මේක run කරන්න
alpha_audio_lab()
