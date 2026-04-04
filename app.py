import streamlit as st
import urllib.parse

def alpha_custom_song_gen():
    st.subheader("🎸 Alpha Custom Lyrics Song Creator")
    
    # 1. සින්දුවේ පද පේළි ටික මෙතන ලියන්න
    user_lyrics = st.text_area("සින්දුවේ පද පේළි (English):", 
                                "In the stars of Alpha AI,\nWe reach for the neon sky.\nHasith leads the way,\nTo a brighter digital day.")

    # 2. සංගීත වර්ගය (Genre)
    genre = st.selectbox("සංගීත වර්ගය:", ["Pop", "Rock", "Electronic", "Lo-fi", "Hip-hop"])

    if st.button("Generate My Song 🎶"):
        if user_lyrics:
            with st.spinner("ඔයාගේ පද පේළි වලට තාලයක් දමමින් පවතී..."):
                try:
                    # Prompt එක සකස් කරන ආකාරය (Style + Lyrics)
                    full_prompt = f"Style: {genre}. Lyrics: {user_lyrics}"
                    encoded_prompt = urllib.parse.quote(full_prompt)
                    
                    # Sunopollination model එක පාවිච්චි කිරීම
                    song_url = f"https://gen.pollinations.ai/audio/{encoded_prompt}?model=sunopollination"
                    
                    # සින්දුව ප්ලේ කිරීම
                    st.audio(song_url)
                    st.success("ඔන්න ඔයාගේ පද පේළි වලට අනුව සින්දුව හැදුවා!")
                    
                except Exception as e:
                    st.error("සර්වර් එකේ පමාවක්. නැවත උත්සාහ කරන්න.")
        else:
            st.warning("කරුණාකර සින්දුවේ පද ඇතුළත් කරන්න.")

alpha_custom_song_gen()
