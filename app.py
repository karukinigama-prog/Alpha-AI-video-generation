import streamlit as st
import requests
import base64

def alpha_fast_lyrics_singer():
    st.subheader("🎸 Alpha Fast Lyrics Singer")
    st.write("වචන දුන්නම AI එක ලවා සින්දුවක් කරවන්න (gTTS වගේම ලේසියි).")

    # සින්දුවේ පද (English)
    lyrics = st.text_area("සින්දුවේ පද පේළි (English):", 
                          "In the stars of Alpha AI, We reach for the neon sky.")

    if st.button("Sing This Now! 🎶"):
        if lyrics:
            with st.spinner("AI එක සින්දුව නිර්මාණය කරමින් පවතී..."):
                try:
                    # මේක තමයි නොමිලේම සින්දු කියන TikTok API එක
                    # මෙතන 'en_female_f08_twinkle' කියන්නේ සින්දු කියන හඬක්
                    url = "https://tiktok-tts.weilnet.workers.dev/api/generation"
                    payload = {
                        "text": lyrics,
                        "voice": "en_female_f08_twinkle" # මේක Singing voice එකක්
                    }
                    
                    response = requests.post(url, json=payload)
                    data = response.json()

                    if "data" in data:
                        # ලැබෙන base64 audio එක ප්ලේ කිරීම
                        audio_base64 = data["data"]
                        audio_bytes = base64.b64decode(audio_base64)
                        st.audio(audio_bytes, format='audio/mp3')
                        st.success("ඔන්න AI එක ලස්සනට සින්දුව කිව්වා!")
                    else:
                        st.error("සර්වර් එකේ පොඩි ප්‍රශ්නයක්. වෙනත් හඬක් උත්සාහ කරමු.")
                        
                except Exception as e:
                    st.error("සම්බන්ධතාවයේ දෝෂයක්. කරුණාකර නැවත උත්සාහ කරන්න.")
        else:
            st.warning("කරුණාකර පද පේළි ඇතුළත් කරන්න.")

alpha_fast_lyrics_singer()
