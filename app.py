import streamlit as st
import urllib.parse

# 1. Secrets වලින් API Key එක ගන්න (වීඩියෝ වලට පාවිච්චි කරපු එකම තමයි)
POLL_API_KEY = st.secrets["POLLINATIONS_API_KEY"]

def generate_music_ui():
    st.subheader("🎵 Alpha Music Lab")
    st.write("ඔයාට අවශ්‍ය ඕනෑම වර්ගයක සින්දුවක් මෙතනින් නිර්මාණය කරගන්න.")

    # සින්දුව ගැන විස්තරය (Prompt)
    music_prompt = st.text_input("සින්දුවේ ස්වභාවය ලියන්න:", placeholder="Upbeat jazz with saxophone, Lo-fi hip hop for studying, Cinematic epic drums...")
    
    col1, col2 = st.columns(2)
    # සින්දුවේ කාලය (තත්පර 3 සිට 300 දක්වා පුළුවන්)
    duration = col1.slider("කාලය (තත්පර):", 3, 60, 30)
    # Instrumental ද නැද්ද යන්න
    is_instrumental = col2.toggle("Instrumental Only", value=True)

    if st.button("Generate Music 🎧"):
        if music_prompt:
            with st.spinner("Alpha AI ඔයාගේ සින්දුව හදමින් පවතිනවා..."):
                try:
                    # Prompt එක URL එකකට ගැලපෙන සේ encode කිරීම
                    encoded_text = urllib.parse.quote(music_prompt)
                    
                    # Pollinations Music API URL එක
                    # model=elevenmusic එක අනිවාර්යයි
                    music_url = (
                        f"https://gen.pollinations.ai/audio/{encoded_text}?"
                        f"model=elevenmusic&"
                        f"duration={duration}&"
                        f"instrumental={'true' if is_instrumental else 'false'}&"
                        f"key={POLL_API_KEY}"
                    )
                    
                    # සින්දුව ප්ලේ කරන්න player එකක් පෙන්වීම
                    st.audio(music_url)
                    st.success("ඔන්න සින්දුව හදලා ඉවරයි!")
                    
                    # Download කරගන්න link එකක්
                    st.markdown(f"[⬇️ Download MP3]({music_url})")
                    
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("කරුණාකර සින්දුව ගැන විස්තරයක් ඇතුළත් කරන්න.")

# App එකේ Music Tab එක ඇතුළේ මේක call කරන්න
generate_music_ui()
