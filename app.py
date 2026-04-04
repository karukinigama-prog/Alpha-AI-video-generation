import streamlit as st
import requests
import base64

def alpha_pro_singer():
    st.subheader("🎸 Alpha Pro Lyrics Singer")
    st.write("කැමති හඬක් තෝරාගෙන පද පේළි සින්දුවක් බවට පත් කරන්න.")

    # 1. සින්දුවේ පද පේළි (English)
    lyrics = st.text_area("සින්දුවේ පද පේළි (English):", 
                          "In the stars of Alpha AI, We reach for the neon sky.")

    # 2. හඬවල් තෝරන ලිස්ට් එක (Selectbox)
    voice_options = {
        "Female (Twinkle) - ලස්සන කාන්තා හඬක්": "en_female_f08_twinkle",
        "Male (Lobby) - ගම්භීර පිරිමි හඬක්": "en_male_m03_lobby",
        "Classic (Salute d'Amour) - පැරණි පන්නයේ හඬක්": "en_female_f08_salut_damour"
    }
    
    selected_voice_name = st.selectbox("ගායනා කරන හඬ තෝරන්න:", list(voice_options.keys()))
    voice_id = voice_options[selected_voice_name]

    if st.button("Start Singing 🎶"):
        if lyrics:
            with st.spinner(f"{selected_voice_name} හඬින් සින්දුව නිර්මාණය කරමින් පවතී..."):
                try:
                    # TikTok TTS API එකට සම්බන්ධ වීම
                    url = "https://tiktok-tts.weilnet.workers.dev/api/generation"
                    payload = {
                        "text": lyrics,
                        "voice": voice_id
                    }
                    
                    response = requests.post(url, json=payload)
                    data = response.json()

                    if "data" in data:
                        # ලැබෙන base64 audio එක ප්ලේ කිරීම
                        audio_base64 = data["data"]
                        audio_bytes = base64.b64decode(audio_base64)
                        
                        st.audio(audio_bytes, format='audio/mp3')
                        st.success(f"ඔන්න {selected_voice_name} හඬින් සින්දුව හැදුවා!")
                    else:
                        st.error("සර්වර් එකේ පොඩි ප්‍රශ්නයක්. පසුව උත්සාහ කරන්න.")
                        
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("කරුණාකර පද පේළි ඇතුළත් කරන්න.")

    st.caption("Created by Hasith | TikTok Singing Engine")

alpha_pro_singer()
