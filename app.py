import streamlit as st
import time
import re
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Nexo AI",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
    --bg:       #070712;
    --card:     #0f0f26;
    --border:   rgba(255,255,255,0.07);
    --purple:   #7c3aed;
    --plt:      #a855f7;
    --pxt:      #c084fc;
    --cyan:     #06b6d4;
    --text:     #f0f0ff;
    --dim:      #3a3a5c;
    --mid:      #7a80a0;
    --green:    #22c55e;
    --red:      #ef4444;
}

html, body, .stApp {
    font-family: 'Outfit', sans-serif !important;
    background: var(--bg) !important;
    color: var(--text) !important;
    overflow-x: hidden !important;
}

/* Kill all streamlit chrome */
#MainMenu, header, footer,
[data-testid="stToolbar"],
[data-testid="collapsedControl"],
[data-testid="stSidebarCollapsedControl"],
[data-testid="stDecoration"],
section[data-testid="stSidebar"],
.stDeployButton { display: none !important; }

.block-container {
    padding: 0 16px !important;
    max-width: 100% !important;
    overflow-x: hidden !important;
}

/* Glow */
.stApp::before {
    content: '';
    position: fixed; inset: 0; z-index: 0; pointer-events: none;
    background:
        radial-gradient(ellipse 80% 40% at 50% 0%, rgba(124,58,237,0.15) 0%, transparent 60%),
        radial-gradient(ellipse 50% 30% at 80% 80%, rgba(6,182,212,0.06) 0%, transparent 60%);
}

/* ── SPLASH ── */
.splash {
    position: fixed; inset: 0; z-index: 999;
    background: var(--bg);
    display: flex; flex-direction: column;
    align-items: center; justify-content: center; gap: 16px;
}
.s-logo {
    font-size: 4.5rem; font-weight: 900; letter-spacing: -3px;
    background: linear-gradient(135deg, #c084fc, #7c3aed, #06b6d4);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text; line-height: 1;
    animation: zoomIn .8s cubic-bezier(.16,1,.3,1) both;
    filter: drop-shadow(0 0 32px rgba(124,58,237,0.5));
}
@keyframes zoomIn {
    from { opacity:0; transform:scale(.6) translateY(16px); }
    to   { opacity:1; transform:scale(1) translateY(0); }
}
.s-tag {
    font-size: 0.6rem; letter-spacing: 4px; text-transform: uppercase;
    color: var(--dim); animation: fadeIn .6s .3s both;
}
.s-bar-wrap {
    width: 160px; height: 2px;
    background: rgba(255,255,255,0.05); border-radius: 10px; overflow: hidden;
}
.s-bar {
    height: 100%; width: 0%;
    background: linear-gradient(90deg, #7c3aed, #06b6d4);
    border-radius: 10px; animation: loadBar 1.8s ease forwards;
}
@keyframes loadBar { to { width:100%; } }
@keyframes fadeIn  { from{opacity:0} to{opacity:1} }

/* ── LOGIN PAGE ── */
.login-page {
    position: relative; z-index: 1;
    width: 100%; padding: 24px 16px 24px;
    display: flex; flex-direction: column;
    align-items: center; gap: 0;
    animation: fadeIn .4s ease both;
}
.l-header { text-align: center; margin-bottom: 20px; width: 100%; }
.l-logo {
    font-size: 2.6rem; font-weight: 900; letter-spacing: -2px;
    background: linear-gradient(135deg, #c084fc, #7c3aed, #06b6d4);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text; line-height: 1;
    filter: drop-shadow(0 0 20px rgba(124,58,237,0.35));
}
.l-sub {
    font-size: 0.6rem; letter-spacing: 3px; text-transform: uppercase;
    color: var(--dim); margin-top: 4px;
}
.l-card {
    width: 100%; max-width: 400px;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 22px 18px;
    box-shadow: 0 6px 32px rgba(0,0,0,0.4), 0 0 0 1px rgba(124,58,237,0.07);
}
.l-title { font-size: 1.1rem; font-weight: 700; margin-bottom: 3px; }
.l-desc  { font-size: 0.75rem; color: var(--mid); margin-bottom: 18px; }
.l-footer {
    text-align: center; margin-top: 14px;
    font-size: 0.65rem; color: var(--dim); line-height: 1.6;
}
.l-footer span { color: var(--purple); }

/* ── WELCOME BACK ── */
.wb-page {
    position: relative; z-index: 1;
    width: 100%; padding: 30px 16px 24px;
    display: flex; flex-direction: column;
    align-items: center; text-align: center;
    animation: fadeIn .4s ease both;
}
.wb-av {
    width: 66px; height: 66px; border-radius: 50%;
    background: linear-gradient(135deg, #7c3aed, #06b6d4);
    display: flex; align-items: center; justify-content: center;
    font-size: 1.6rem; margin-bottom: 12px;
    box-shadow: 0 0 0 3px rgba(124,58,237,0.2), 0 6px 24px rgba(124,58,237,0.3);
    animation: popIn .6s cubic-bezier(.16,1,.3,1) both;
}
@keyframes popIn {
    from{opacity:0;transform:scale(.4)} to{opacity:1;transform:scale(1)}
}
.wb-name  { font-size: 1.4rem; font-weight: 800; margin-bottom: 3px; }
.wb-email { font-size: 0.75rem; color: var(--mid); margin-bottom: 20px; }
.wb-card {
    width: 100%; max-width: 320px;
    background: var(--card); border: 1px solid var(--border);
    border-radius: 16px; padding: 16px; margin-bottom: 16px;
}
.wb-row {
    display: flex; justify-content: space-between; align-items: center;
    padding: 7px 0; border-bottom: 1px solid var(--border);
    font-size: 0.78rem; color: var(--mid);
}
.wb-row:last-child { border-bottom: none; }
.wb-row span:last-child { color: var(--pxt); font-weight: 600; font-size: 0.75rem; }

/* Streamlit input overrides */
.stTextInput > div > div > input {
    background: rgba(124,58,237,0.06) !important;
    border: 1px solid rgba(124,58,237,0.2) !important;
    border-radius: 11px !important;
    color: var(--text) !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 0.88rem !important;
    transition: all .2s !important;
}
.stTextInput > div > div > input:focus {
    border-color: rgba(124,58,237,0.55) !important;
    box-shadow: 0 0 0 3px rgba(124,58,237,0.1) !important;
}
.stTextInput > div > div > input::placeholder { color: var(--dim) !important; }
.stTextInput label {
    font-size: 0.72rem !important; font-weight: 600 !important;
    color: var(--mid) !important; font-family: 'Outfit',sans-serif !important;
}

.stButton > button {
    background: linear-gradient(135deg, #7c3aed, #a855f7) !important;
    border: none !important; border-radius: 11px !important;
    color: #fff !important; font-family: 'Outfit',sans-serif !important;
    font-size: 0.88rem !important; font-weight: 700 !important;
    width: 100% !important;
    box-shadow: 0 4px 18px rgba(124,58,237,0.4) !important;
    transition: all .2s !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 7px 24px rgba(124,58,237,0.5) !important;
}

div[data-testid="stCheckbox"] label {
    font-size: 0.78rem !important; color: var(--mid) !important;
    font-family: 'Outfit',sans-serif !important;
}
</style>
""", unsafe_allow_html=True)

# ── Session ──────────────────────────────────────────────────
for k,v in {
    "splash_done": False, "logged_in": False,
    "user_name": "", "user_email": "", "login_time": None
}.items():
    if k not in st.session_state: st.session_state[k] = v

def valid_email(e):
    return bool(re.match(r'^[^@]+@[^@]+\.[^@]+$', e))

def initials(name):
    p = name.strip().split()
    return (p[0][0]+p[-1][0]).upper() if len(p)>=2 else name[:2].upper()

# ── SPLASH ───────────────────────────────────────────────────
if not st.session_state.splash_done:
    st.markdown("""
    <div class="splash">
        <div class="s-logo">NEXO</div>
        <div class="s-tag">Smart Conversations · Smarter Results</div>
        <div class="s-bar-wrap"><div class="s-bar"></div></div>
    </div>
    """, unsafe_allow_html=True)
    time.sleep(2.0)
    st.session_state.splash_done = True
    st.rerun()

# ── WELCOME BACK ─────────────────────────────────────────────
elif st.session_state.logged_in:
    name  = st.session_state.user_name
    email = st.session_state.user_email
    ini   = initials(name)
    ltime = st.session_state.login_time or datetime.now().strftime("%Y-%m-%d %H:%M")
    exp   = (datetime.strptime(ltime, "%Y-%m-%d %H:%M") + timedelta(days=30)).strftime("%d %B %Y")

    st.markdown(f"""
    <div class="wb-page">
        <div class="wb-av">{ini}</div>
        <div class="wb-name">Welcome back, {name.split()[0]}! 👋</div>
        <div class="wb-email">{email}</div>
        <div class="wb-card">
            <div class="wb-row"><span>👤 Name</span><span>{name}</span></div>
            <div class="wb-row"><span>📧 Email</span><span>{email[:20]}{'…' if len(email)>20 else ''}</span></div>
            <div class="wb-row"><span>🔐 Status</span><span>Active ✓</span></div>
            <div class="wb-row"><span>📅 Expires</span><span>{exp}</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        if st.button("🚀 Open Nexo"):
            st.success("Launching Nexo AI ✨")
            time.sleep(1)
            st.info("Main app merge කළාට පස්සේ launch වෙනවා!")
    with c2:
        if st.button("🚪 Sign Out"):
            for k in ["logged_in","user_name","user_email","login_time","splash_done"]:
                st.session_state[k] = False if k in ["logged_in","splash_done"] else ""
            st.rerun()

# ── LOGIN ────────────────────────────────────────────────────
else:
    st.markdown("""
    <div style="text-align:center; padding: 30px 0 18px; position:relative; z-index:1;">
        <div class="l-logo">NEXO</div>
        <div class="l-sub">Your AI Companion</div>
    </div>
    """, unsafe_allow_html=True)

    name_in  = st.text_input("Your Name", placeholder="Hasith Heshan", key="n_in")
    email_in = st.text_input("Email Address", placeholder="you@example.com", key="e_in")
    remember = st.checkbox("Remember me for 30 days", value=True)

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

    if st.button("✦ Sign In to Nexo", key="signin"):
        if not name_in.strip():
            st.error("⚠️ Please enter your name")
        elif not email_in.strip():
            st.error("⚠️ Please enter your email")
        elif not valid_email(email_in.strip()):
            st.error("⚠️ Please enter a valid email")
        else:
            with st.spinner("Signing you in..."):
                time.sleep(1.0)
            st.session_state.logged_in  = True
            st.session_state.user_name  = name_in.strip().title()
            st.session_state.user_email = email_in.strip().lower()
            st.session_state.login_time = datetime.now().strftime("%Y-%m-%d %H:%M")
            st.success(f"Welcome, {name_in.strip().title()}! 🎉")
            time.sleep(0.6)
            st.rerun()

    st.markdown("""
    <div class="l-footer">
        No password required — just your name &amp; email · Nexo AI
    </div>
    """, unsafe_allow_html=True)
