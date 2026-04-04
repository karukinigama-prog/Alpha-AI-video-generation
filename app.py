import streamlit as st
import requests
import base64

def alpha_long_song_studio():
    st.subheader("🎤 Alpha Long Song Studio")
    
    # පද පේළි ගොඩක් ලියන්න ඉඩ දෙනවා
    lyrics = st.text_area("සින්දුවේ පද පේළි (දිගට ලියන්න):", 
                          "In the stars of Alpha AI, We reach for the neon sky.\n"
                          "Hasith leads the way today, To a brighter digital day.\n"
                          "We are coding every night, Making dreams and making light.")

    voice_options = {
        "Female (Twinkle)": "en_female_f08_twinkle",
        "Male (Lobby)": "en_male_m03_lobby"
    }
    selected_voice = st.selectbox("Singer:", list(voice_options.keys()))

    if st.button("Generate Full Song 🎧"):
        if lyrics:
            # 1. පද පේළි ටික කොටස් වලට කඩනවා (පේළියෙන් පේළියට)
            lines = [line.strip() for line in lyrics.split('\n') if line.strip()]
            
            with st.spinner(f"කොටස් {len(lines)} කින් සින්දුව නිර්මාණය කරයි..."):
                for i, line in enumerate(lines):
                    try:
                        url = "https://tiktok-tts.weilnet.workers.dev/api/generation"
                        payload = {"text": line, "voice": voice_options[selected_voice]}
                        
                        response = requests.post(url, json=payload)
                        data = response.json()

                        if "data" in data:
                            audio_bytes = base64.b64decode(data["data"])
                            # හැම පේළියකටම වෙන වෙනම Player එකක් පෙන්වනවා
                            st.write(f"🎶 Part {i+1}: {line}")
                            st.audio(audio_bytes, format='audio/mp3')
                        
                    except:
                        st.error(f"Part {i+1} එකේදී පොඩි අවුලක් වුණා.")
        else:
            st.warning("කරුණාකර පද ලියන්න.")

alpha_long_song_studio()
