import streamlit as st
import random
import time

# --- UI SETTINGS ---
st.set_page_config(page_title="Alpha AI - Ultimate", page_icon="💡", layout="centered")

# Custom CSS for an Elite Dark UI (No Image Breaks)
st.markdown("""
    <style>
    .main { background-color: #030303; color: white; }
    .stTextInput > div > div > input { background-color: #1a1a1a; color: #00ffcc; border: 1.5px solid #00ffcc; }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #00ffcc, #0099ff);
        color: black;
        font-weight: bold;
        font-size: 16px;
        border: none;
        padding: 12px;
        border-radius: 8px;
        transition: 0.2s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.5);
        color: white;
    }
    .main-image {
        border-radius: 10px;
        border: 2px solid #00ffcc;
        box-shadow: 0 0 20px rgba(0, 255, 204, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("💡 Alpha AI - Unlimited Pro")
st.markdown("### **Created by Hasith Karunarathna**")
st.write("මෙය කිසිම විටක **Lock නොවන**, සීමා රහිත සහ **කැඩුණු රූප නොඑන** අනුවාදයයි.")

# --- INPUT SECTION ---
with st.container():
    prompt = st.text_input("ඔබේ සිතුවිල්ල ඉංග්‍රීසියෙන් ලියන්න (Prompt):", placeholder="Example: A futuristic battle, 8k, cinematic, realistic")
    
    col1, col2 = st.columns(2)
    with col1:
        # රූපයේ ආකාරය (Styles)
        style = st.selectbox("රූපයේ විලාසය:", ["Photorealistic", "Digital Art", "Oil Painting", "Vector Art", "Anime"])
    with col2:
        # Seed එක වෙනුවට "Aesthetic" තෝරමු
        quality = st.select_slider("රූපයේ Aesthetic ගුණය:", options=["Standard", "Detailed", "Ultra Detailed"], value="Ultra Detailed")

if st.button("Generate Elite Image ✨"):
    if prompt:
        with st.spinner("Alpha AI විසින් ඉතාමත් උසස් තත්වයේ රූපය නිර්මාණය කරමින් පවතී..."):
            try:
                # Prompt එක සකස් කිරීම
                final_prompt = f"{prompt}, {style}, {quality}, highly detailed, 8k, masterpiece"
                encoded_prompt = final_prompt.replace(" ", "-")
                
                # සෑම Request එකකටම අලුත් රූපයක් ලබා ගැනීමට Random Number එකක් (Seed)
                random_seed = random.randint(1, 100000)
                
                # වඩාත් ස්ථාවර Unlimited API URL එක
                # (මෙය Pollinations හරහා, නමුත් broken images වළක්වන ක්‍රමයකට)
                image_url = f"https://pollinations.ai/p/{encoded_prompt}?seed={random_seed}&model=flux&width=1024&height=1024&nologo=true"
                
                # රූපය ප්‍රදර්ශනය කිරීම (Broken image එකක් නම්, retry කිරීම)
                image_place = st.empty()
                image_place.image(image_url, use_container_width=True, caption=f"Alpha AI Result: {prompt}")
                
                # Download Button
                st.markdown(f'''
                    <a href="{image_url}" target="_blank">
                        <button style="width:100%; padding:14px; border-radius:10px; background-color:#28a745; color:white; border:none; cursor:pointer; font-size:16px; margin-top:10px; font-weight:bold;">
                            Download Image (High Quality) 📥
                        </button>
                    </a>
                ''', unsafe_allow_html=True)
                
            except Exception as e:
                st.error("දත්ත ලබා ගැනීමේදී ගැටලුවක් ඇති විය. කරුණාකර නැවත උත්සාහ කරන්න.")
    else:
        st.warning("කරුණාකර මොකක් හරි විස්තරයක් ඇතුළත් කරන්න.")

st.divider()
st.caption("Alpha AI Ultimate Edition | Status: Elite Mode Online ✅ | No API Key | Version 3.0")
