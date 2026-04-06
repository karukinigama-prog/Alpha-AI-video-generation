import streamlit as st
import requests

# --- CONFIGURATION ---
# මෙතනට ඔයාගේ Colab එකෙන් ලැබුණු URL එක දාන්න (අගට /generate කෑල්ල අමතක කරන්න එපා)
COLAB_URL = "https://revolution-functions-toolbar-christ.trycloudflare.com/generate"

# --- UI SETTINGS ---
st.set_page_config(page_title="Alpha AI Video Gen", page_icon="🎬", layout="centered")

st.title("🎬 Alpha AI Video Generator")
st.markdown("Created by **Hasith**") # ඔයාගේ බ්‍රෑන්ඩින් එක මෙතන තියෙනවා
st.write("රූපයක් ලබා දී එය සජීවීකරණය කරන්න (Image-to-Video)")

# --- INPUT ---
image_url = st.text_input("ඔබේ Image URL එක ඇතුළත් කරන්න (උදා: Unsplash ලින්ක් එකක්):")

if st.button("Generate Video ✨"):
    if image_url:
        with st.spinner("Colab සර්වර් එකෙන් වීඩියෝව හදනවා... මේකට විනාඩියක් පමණ ගත විය හැක."):
            try:
                # Colab API එකට රික්වෙස්ට් එක යැවීම
                response = requests.post(COLAB_URL, json={"image_url": image_url}, timeout=120)
                
                if response.status_code == 200:
                    # වීඩියෝ එක සාර්ථකව ලැබුණොත් එය save කර පෙන්වීම
                    with open("temp_video.mp4", "wb") as f:
                        f.write(response.content)
                    
                    st.success("වීඩියෝව සාර්ථකව නිපදවා ඇත!")
                    st.video("temp_video.mp4")
                    
                    # Download කරන්න බටන් එකක්
                    with open("temp_video.mp4", "rb") as file:
                        st.download_button(
                            label="Download Video",
                            data=file,
                            file_name="alpha_ai_video.mp4",
                            mime="video/mp4"
                        )
                else:
                    st.error(f"සර්වර් එකේ ගැටලුවක්! (Error Code: {response.status_code})")
                    st.info("ඔබේ Colab එක රන් වෙනවාද කියා නැවත පරීක්ෂා කරන්න.")
                    
            except Exception as e:
                st.error(f"සම්බන්ධ වීමට නොහැකි විය: {e}")
    else:
        st.warning("කරුණාකර රූපයක URL එකක් ඇතුළත් කරන්න.")

st.divider()
st.caption("සටහන: මෙම සේවාව ක්‍රියාත්මක වීමට ඔබේ Google Colab සර්වර් එක 'Running' තත්වයේ තිබිය යුතුය.")
