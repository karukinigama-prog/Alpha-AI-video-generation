import streamlit as st
from gtts import gTTS
import os

def generate_free_voice_ui():
    st.subheader("🎙️ Alpha Voice Lab (Unlimited & Free)")
    st.write("මෙය Google Translate තාක්ෂණයෙන් ක්‍රියා කරයි. API Keys අවශ්‍ය නැත.")

    # කියවිය යුතු දේ
    text_to_speak = st.text_area("කියවිය යුතු දේ ලියන්න:", "Hello Hasith, Alpha AI is now using free voice engine.")
    
    # භාෂාව තෝරාගැනීම (සිංහලත් පුළුවන්!)
    lang_choice = st.selectbox("Language / භාෂාව:", 
                                ["en (English)", "si (Sinhala)", "hi (Hindi)", "fr (French)"])
    
    lang_code = lang_choice.split(" ")[0]

    if st.button("Generate Voice 🔊"):
        if text_to_speak:
            with st.spinner("හඬ සකස් කරමින් පවතී..."):
                try:
                    # gTTS මගින් හඬ නිර්මාණය කිරීම
                    tts = gTTS(text=text_to_speak, lang=lang_code, slow=False)
                    
                    # හඬ file එකක් ලෙස save කිරීම
                    audio_file = "alpha_voice.mp3"
                    tts.save(audio_file)
                    
                    # ප්ලේ කිරීම
                    st.audio(audio_file)
                    st.success("සාර්ථකයි!")
                    
                    # පාවිච්චි කරලා ඉවර වුණාම file එක අයින් කරන්න පුළුවන් (Optional)
                    # os.remove(audio_file)
                    
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("කරුණාකර යමක් ලියන්න.")

generate_free_voice_ui()
