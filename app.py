import streamlit as st
import requests

def alpha_video_explorer_v3():
    st.subheader("📽️ Alpha Ultimate Video Explorer (V1)")
    
    # 1. පියවර: ඔයාගේ Pexels API Key එක මෙතනට දාන්න
    PEXELS_API_KEY = "ඔයාගේ_API_KEY_එක_මෙතනට_දාන්න" 

    query = st.text_input("ඔයාට අවශ්‍ය වීඩියෝ වර්ගය (English):", "Sci-fi robot animation")

    if st.button("Search Video 🔍"):
        if query:
            with st.spinner("අලුත්ම Pexels V1 පද්ධතියෙන් වීඩියෝ සොයමින් පවතී..."):
                headers = {"Authorization": PEXELS_API_KEY}
                
                # මෙන්න අලුත් URL එක (api.pexels.com/v1/videos/search)
                url = f"https://api.pexels.com/v1/videos/search?query={query}&per_page=1"
                
                try:
                    response = requests.get(url, headers=headers)
                    data = response.json()

                    # දත්ත ලැබෙනවද කියලා චෙක් කිරීම
                    if 'videos' in data and len(data['videos']) > 0:
                        # වීඩියෝ ලින්ක් එක ලබාගැනීම
                        video_file = data['videos'][0]['video_files'][0]['link']
                        
                        st.video(video_file)
                        st.success("High Quality වීඩියෝ එකක් සාර්ථකව හමුවුණා!")
                    else:
                        st.error("වීඩියෝවක් හමුවුණේ නැහැ. කරුණාකර API Key එක හෝ සෙවුම් වචනය පරීක්ෂා කරන්න.")
                        # මොකක්ද වෙලා තියෙන ප්‍රශ්නය කියලා බලන්න මේක පාවිච්චි කරන්න
                        # st.write(data) 
                
                except Exception as e:
                    st.error(f"පද්ධතියේ දෝෂයක්: {e}")
        else:
            st.warning("කරුණාකර සෙවිය යුතු දෙයක් ලියන්න.")

    st.caption("Updated to V1 API | Created by Hasith")

alpha_video_explorer_v3()
