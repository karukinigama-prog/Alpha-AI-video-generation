import streamlit as st
import requests
import base64
import io

def alpha_full_song_only():
    st.markdown("<h2 style='text-align: center;'>🎶 Alpha Full Song Studio</h2>", unsafe_allow_html=True)
    
    # 1. පද පේළි ඇතුළත් කරන තැන
    lyrics = st.text_area("සින්දුවේ පද පේළි (එක් පේළියකට එක බැගින් ලියන්න):", 
                          "In the stars of Alpha AI,\nWe reach for the neon sky.\nHasith leads the way today,\nTo a brighter digital day.",
                          height=150)

    # 2. හඬ තෝරන තැන
    voice_options = {
        "Female (Twinkle)": "en_female_f08_twinkle",
        "Male (Lobby)": "en_male_m03_lobby"
    }
    selected_voice = st.selectbox("ගායකයා තෝරන්න:", list(voice_options.keys()))

    if st.button("Generate Full Song 🎧", use_container_width=True):
        if lyrics:
            # පද පේළි ටික ලිස්ට් එකකට වෙන් කර ගැනීම
            lines = [line.strip() for line in lyrics.split('\n') if line.strip()]
            
            # සියලුම audio කොටස් එකතු කරන තැන (Buffer)
            combined_audio = io.BytesIO()
            
            with st.spinner(f"Alpha AI පද්ධතිය සම්පූර්ණ සින්දුව නිර්මාණය කරමින් පවතී..."):
                success_count = 0
                for line in lines:
                    try:
                        url = "https://tiktok-tts.weilnet.workers.dev/api/generation"
                        payload = {"text": line, "voice": voice_options[selected_voice]}
                        
                        response = requests.post(url, json=payload)
                        data = response.json()

                        if "data" in data:
                            audio_bytes = base64.b64decode(data["data"])
                            # හැම කෑල්ලක්ම එක දිගට අලවනවා
                            combined_audio.write(audio_bytes)
                            success_count += 1
                    except:
                        continue # පොඩි වැරදීමක් වුණොත් ඊළඟ පේළියට යනවා

                if success_count > 0:
                    combined_audio.seek(0)
                    full_audio_data = combined_audio.read()
                    
                    st.success("සම්පූර්ණ සින්දුව සාර්ථකව සකස් කළා!")
                    
                    # 🎧 එකම එක Player එකක් පමණයි පෙන්වන්නේ
                    st.audio(full_audio_data, format='audio/mp3')
                    
                    # 📥 මුළු සින්දුවම Download කරන්න බට්න් එක
                    st.download_button(
                        label="Download Full Song MP3 📥",
                        data=full_audio_data,
                        file_name="Alpha_Full_Song.mp3",
                        mime="audio/mp3",
                        use_container_width=True
                    )
                else:
                    st.error("සින්දුව සෑදීමට නොහැකි වුණා. කරුණාකර පේළි පරීක්ෂා කරන්න.")
        else:
            st.warning("කරුණාකර පද පේළි කිහිපයක් ඇතුළත් කරන්න.")

    st.markdown("<hr>", unsafe_allow_html=True)
    st.caption("Created by Hasith | Alpha AI Elite Project")

alpha_full_song_only()
