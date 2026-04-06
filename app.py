import streamlit as st

# --- UI SETTINGS ---
st.set_page_config(page_title="Alpha AI - Pro Edition", page_icon="🚀", layout="centered")

# Custom CSS for a Professional Dark UI
st.markdown("""
    <style>
    .main { background-color: #050505; color: white; }
    .stTextInput > div > div > input { background-color: #111; color: #00ffcc; border: 1px solid #00ffcc; }
    .stButton>button {
        width: 100%;
        background: linear-gradient(45deg, #00ffcc, #0099ff);
        color: black;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.02); color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Alpha AI Pro Generator")
st.markdown("### Created by **Hasith Karunarathna**")
st.write("මෙය කිසිම විටක **Lock නොවන**, Unlimited සහ API Key රහිත අනුවාදයයි.")

# --- INPUT SECTION ---
with st.container():
    prompt = st.text_input("ඔබේ සිතුවිල්ල ඉංග්‍රීසියෙන් ලියන්න (Prompt):", placeholder="e.g. Iron Man in Sri Lankan traditional dress, 8k...")
    
    col1, col2 = st.columns(2)
    with col1:
        category = st.selectbox("වර්ගය (Type):", ["Artistic", "Cinematic", "Anime", "Cyberpunk"])
    with col2:
        seed = st.number_input("Seed (වෙනස් රූප ලබා ගැනීමට):", value=42)

if st.button("Generate Unlimited Image ✨"):
    if prompt:
        with st.spinner("Alpha AI විසින් රූපය සකසමින් පවතී..."):
            try:
                # සීමා රහිතව රූප ලබා දෙන නවතම API එක
                # මෙහි seed එක වෙනස් කිරීමෙන් එකම prompt එකට විවිධ රූප ගත හැක
                final_prompt = f"{prompt}, {category} style, ultra detailed, masterpiece"
                encoded_prompt = final_prompt.replace(" ", "%20")
                
                image_url = f"https://pollinations.ai/p/{encoded_prompt}?width=1024&height=1024&seed={seed}&nologo=true"
                
                st.image(image_url, use_container_width=True, caption=f"Alpha AI Result: {prompt}")
                
                # Download Button
                st.markdown(f'''
                    <a href="{image_url}" target="_blank">
                        <button style="width:100%; padding:12px; border-radius:8px; background-color:#28a745; color:white; border:none; cursor:pointer; font-size:16px;">
                            Download High Quality Image 📥
                        </button>
                    </a>
                ''', unsafe_allow_html=True)
                
            except Exception as e:
                st.error("දත්ත ලබා ගැනීමේදී ගැටලුවක් ඇති විය.")
    else:
        st.warning("කරුණාකර යම් විස්තරයක් ඇතුළත් කරන්න.")

st.divider()
st.caption("Alpha AI Elite Edition | Status: Online ✅ | No API Key Required")
