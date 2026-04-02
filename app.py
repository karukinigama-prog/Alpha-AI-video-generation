import streamlit as st
import urllib.parse

def alpha_free_music_gen():
    st.subheader("🎵 Alpha AI Music Studio (No Limits)")
    st.write("සල්ලි යන්නේ නැති, API Keys ඕනෙම නැති අලුත්ම Music Generator එක.")

    # සින්දුවේ විස්තරය (English වලින් ලියන්න)
    music_prompt = st.text_input("සංගීතයේ ස්වභාවය ලියන්න:", "Dark cinematic drums with orchestra")
    
    # කාලය තෝරන්න (තත්පර 10-30 හොඳයි)
    duration = st.slider("කාලය (තත්පර):", 5, 30, 15)

    if st.button("Generate Original Music ✨"):
        if music_prompt:
            with st.spinner("Alpha AI ඔයාගේ සින්දුව අලුතින්ම නිර්මාණය කරමින් පවතී..."):
                try:
                    # Prompt එක URL එකට ගැලපෙන සේ සැකසීම
                    encoded_prompt = urllib.parse.quote(music_prompt)
                    
                    # මේක තමයි Pollinations වල තියෙන නොමිලේම දෙන Music URL එක
                    # මෙතන model=audiocraft පාවිච්චි කරන නිසා සල්ලි (Pollen) යන්නේ නැහැ
                    free_music_url = (
                        f"https://gen.pollinations.ai/audio/{encoded_prompt}?"
                        f"model=audiocraft&"
                        f"duration={duration}"
                    )
                    
                    # සින්දුව ප්ලේ කිරීම
                    st.audio(free_music_url)
                    st.success("ඔන්න අලුත්ම සින්දුව හැදුවා!")
                    
                    # Download කරගන්න link එක
                    st.markdown(f"[⬇️ Download MP3]({free_music_url})")
                    
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("කරුණාකර සංගීතය ගැන විස්තරයක් ඇතුළත් කරන්න.")

alpha_free_music_gen()
