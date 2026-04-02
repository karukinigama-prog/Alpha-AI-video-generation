import streamlit as st
import urllib.parse

def generate_video_ui():
    st.subheader("🎬 Alpha Cinema Lab (Powered by Veo)")
    
    # වීඩියෝවට අවශ්‍ය විස්තරය (Prompt)
    video_prompt = st.text_area("වීඩියෝවේ විය යුතු දේ විස්තර කරන්න:", 
                                placeholder="A futuristic city with flying cars, sunset, 4k cinematic style...")
    
    # Models තෝරාගැනීම (Pollinations docs වල ඇති ඒවා)
    model_choice = st.selectbox("Model එක තෝරන්න:", ["veo", "wan", "ltx-2", "p-video"])
    
    # වීඩියෝවේ කාලය
    duration = st.slider("කාලය (තත්පර):", 2, 10, 4)

    if st.button("Generate Video ✨"):
        if video_prompt:
            with st.spinner("Alpha AI is rendering your masterpiece..."):
                try:
                    # Prompt එක URL එකකට ගැලපෙන සේ සැකසීම
                    encoded_prompt = urllib.parse.quote(video_prompt)
                    
                    # Pollinations Video API URL එක
                    # ඔයාට API Key එකක් තියෙනවා නම් අන්තිමට &key=YOUR_KEY ලෙස එකතු කරන්න
                    video_url = f"https://gen.pollinations.ai/video/{encoded_prompt}?model={model_choice}&duration={duration}"
                    
                    # වීඩියෝව පෙන්වීම
                    st.video(video_url)
                    st.success("ඔයාගේ වීඩියෝව සූදානම්!")
                    
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("කරුණාකර විස්තරයක් (Prompt) ඇතුළත් කරන්න.")

# Tab එක ඇතුළේ call කරන්න
generate_video_ui()
