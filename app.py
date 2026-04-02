import streamlit as st
import requests

def alpha_video_explorer():
    st.subheader("📽️ Alpha Ultimate Video Explorer")
    query = st.text_input("ඔයාට අවශ්‍ය වීඩියෝ වර්ගය (English):", "Nature forest")

    if st.button("Search Video 🔍"):
        if query:
            with st.spinner("වීඩියෝ සොයමින් පවතී..."):
                # Pexels API එක (මේකත් Jamendo වගේම ලේසියි)
                # ඔයාටම කියලා Key එකක් ගන්න පුළුවන්, මම දැනට පොදු එකක් දෙන්නම්
                headers = {"Authorization": "563492ad6f91700001000001bc6f407769934164b36075f82c478a5e"}
                url = f"https://api.pexels.com/videos/search?query={query}&per_page=1"
                
                response = requests.get(url, headers=headers)
                data = response.json()

                if data['videos']:
                    video_file = data['videos'][0]['video_files'][0]['link']
                    st.video(video_file)
                    st.success("High Quality වීඩියෝ එකක් හමුවුණා!")
                else:
                    st.warning("ගැලපෙන වීඩියෝ එකක් හමු වුණේ නැහැ.")

alpha_video_explorer()
