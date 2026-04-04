import streamlit as st
import requests
import base64
import io

def alpha_ultimate_full_song_studio():
    st.markdown("<h2 style='text-align: center;'>🔥 Alpha AI: Ultimate Full Song Studio</h2>", unsafe_allow_html=True)
    st.write("Hasith, මෙතනින් ඔයාගේ සම්පූර්ණ සින්දුවම කිසිම අඩුවක් නැතිව නිර්මාණය කරගන්න.")

    # 1. පද පේළි ඇතුළත් කිරීම (සෑම පේළියක්ම අලුත් පේළියක ලියන්න)
    lyrics = st.text_area("සින්දුවේ පද පේළි (Lyrics):", 
                          "Yo, Alpha AI is coming to town,\n"
                          "Hasith is the one who wears the crown.\n"
                          "From the code to the rhythm, we never slow down,\n"
                          "The best AI system that can be found.",
                          height=150)

    # 2. ඔයා ඉල්ලපු සින්දු විලාසයන් (Styles)
    music_styles = {
        "🎧 Hip-Hop / Rap (Lobby)": "en_male_m03_lobby",
        "🎸 Rock Style (Sunshine)": "en_male_m03_sunshine",
        "✨ Pop Style (Twinkle)": "en_female_f08_twinkle",
        "🎻 Classic Style (Salute)": "en_female_f08_salut_damour",
        "🎙️ Deep Narration (Gembira)": "en_male_narration"
    }
    
    selected_style = st.selectbox("සින්දුවේ විලාසය (Select Style):", list(music_styles.keys()))
    voice_id = music_styles[selected_style]

    if st.button("Generate Full Song & Download 🎤", use_container_width=True):
        if lyrics:
            # පේළි වෙන් කරගැනීම
            lines = [line.strip() for line in lyrics.split('\n') if line.strip()]
            
            # සියලුම Audio කෑලි එකතු කරන තැන
            combined_audio = io.BytesIO()
            
            with st.spinner(f"Alpha AI {selected_style} විලාසයෙන් සම්පූර්ණ සින්දුව සකස් කරයි..."):
                success_count = 0
                for line in lines:
                    try:
                        # TikTok TTS Engine එකට සම්බන්ධ වීම
                        url = "https://tiktok-tts.weilnet.workers.dev/api/generation"
                        payload = {"text": line, "voice": voice_id}
                        
                        response = requests.post(url, json=payload)
                        data = response.json()

                        if "data" in data:
                            audio_bytes = base64.b64decode(data["data"])
                            # හැම Audio කොටසක්ම එක පෙළට අලවනවා
                            combined_audio.write(audio_bytes)
                            success_count += 1
                    except:
                        continue # එකක් වැරදුණොත් ඊළඟ එකට යනවා

                if success_count > 0:
                    # Pointer එක මුලට අරගෙන Full Data එක කියවීම
                    combined_audio.seek(0)
                    full_audio_data = combined_audio.read()
                    
                    st.success(f"නියමයි හසීත්! පේළි {success_count} කින් යුත් සම්පූර්ණ සින්දුව සූදානම්.")
                    
                    # එකම ප්ලේයර් එකකින් මුළු සින්දුවම අහන්න
                    st.audio(full_audio_data, format='audio/mp3')
                    
                    # 📥 මුළු සින්දුවම එකවර Download කරන්න බට්න් එක
                    st.download_button(
                        label="Download Full Song MP3 📥",
                        data=full_audio_data,
                        file_name="Alpha_Ultimate_Song.mp3",
                        mime="audio/mp3",
                        use_container_width=True
                    )
                else:
                    st.error("සර්වර් එකේ පොඩි ප්‍රශ්නයක්. නැවත උත්සාහ කරන්න.")
        else:
            st.warning("කරුණාකර පද පේළි ඇතුළත් කරන්න.")

    st.markdown("<hr>", unsafe_allow_html=True)
    st.caption("Created by Hasith | Alpha AI Elite Project")

# App එක ප්ලේ කරන්න
alpha_ultimate_full_song_studio()
