import streamlit as st
from gtts import gTTS
from gradio_client import Client
import os

def alpha_audio_studio():
    st.title("🎙️ Alpha AI Audio Studio")
    st.write("සල්ලි යන්නේ නැති, API Keys ඕනෙම නැති අලුත්ම Audio පද්ධතිය.")

    # Tabs දෙකක් හදමු Voice සහ Music වලට
    tab_voice, tab_music = st.tabs(["AI Voice (gTTS)", "AI Music Creator (MusicGen)"])

    # --- 1. AI Voice Tab (gTTS) ---
    with tab_voice:
        st.subheader("අසීමිතව හඬවල් නිර්මාණය කරන්න")
        text_to_speak = st.text_area("කියවිය යුතු දේ ලියන්න:", "Hello Hasith, welcome to Alpha AI Voice Lab!")
        
        # භාෂාව තෝරාගැනීම (සිංහලත් ඇතුළුව)
        langs = {"English": "en", "Sinhala (සිංහල)": "si", "Hindi": "hi", "Japanese": "ja"}
        selected_lang = st.selectbox("භාෂාව තෝරන්න:", list(langs.keys()))

        if st.button("Generate Voice 🔊"):
            if text_to_speak:
                with st.spinner("හඬ සකස් කරමින් පවතී..."):
                    tts = gTTS(text=text_to_speak, lang=langs[selected_lang], slow=False)
                    tts.save("voice.mp3")
                    st.audio("voice.mp3")
                    st.success("හඬ සාර්ථකව නිර්මාණය වුණා!")
            else:
                st.warning("කරුණාකර යමක් ලියන්න.")

    # --- 2. AI Music Creator Tab (MusicGen) ---
    with tab_music:
        st.subheader("AI එක ලවා අලුත්ම සින්දු නිර්මාණය කරන්න")
        st.info("සටහන: මෙතනදී AI එක සින්දුවක් බින්දුවේ ඉඳන් හදන නිසා විනාඩියක් පමණ ගතවිය හැක.")
        
        music_prompt = st.text_input("සින්දුවේ ස්වභාවය ලියන්න (English):", "Slow acoustic guitar with flute")
        duration = st.slider("කාලය (තත්පර):", 5, 20, 10)

        if st.button("Generate Original Music ✨"):
            if music_prompt:
                with st.spinner("AI එක සින්දුව නිර්මාණය කරමින් පවතී... කරුණාකර රැඳී සිටින්න."):
                    try:
                        # කිසිම API Token එකක් නැතිව කෙලින්ම Public Space එකකට සම්බන්ධ වීම
                        client = Client("facebook/MusicGen")
                        result = client.predict(
                            task="text2audio",
                            text=music_prompt,
                            model_name="facebook/musicgen-small",
                            api_name="/predict"
                        )
                        st.audio(result)
                        st.success("AI එක ඔයාටම වෙන්වුණු අලුත්ම තාලයක් හැදුවා!")
                    except Exception as e:
                        st.error("දැනට සර්වර් එක කාර්යබහුලයි. විනාඩියකින් නැවත උත්සාහ කරන්න.")
            else:
                st.warning("සින්දුව ගැන විස්තරයක් ලියන්න.")

# App එකේ මේක run කරන්න
alpha_audio_studio()
