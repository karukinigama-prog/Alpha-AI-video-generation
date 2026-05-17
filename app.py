import streamlit as st
import time
import json
import hashlib
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Nexo AI — Login",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ─── CSS ───────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
    --bg:        #070712;
    --card:      #0f0f26;
    --border:    rgba(255,255,255,0.06);
    --border-p:  rgba(139,92,246,0.4);
    --purple:    #7c3aed;
    --purple-lt: #a855f7;
    --purple-xt: #c084fc;
    --cyan:      #06b6d4;
    --text:      #f0f0ff;
    --text-dim:  #4a5070;
    --text-mid:  #8890b0;
    --green:     #22c55e;
    --red:       #ef4444;
}

html, body, .stApp {
    font-family: 'Outfit', sans-serif !important;
    background: var(--bg) !important;
    color: var(--text) !important;
}

#MainMenu, header, footer,
[data-testid="stToolbar"],
[data-testid="collapsedControl"],
[data-testid="stSidebarCollapsedControl"],
[data-testid="stDecoration"],
section[data-testid="stSidebar"],
.stDeployButton { display: none !important; visibility: hidden !important; }

.block-container { padding: 0 !important; max-width: 100% !important; }

/* Ambient glow */
.stApp::before {
    content: '';
    position: fixed; inset: 0;
    background:
        radial-gradient(ellipse 70% 50% at 50% 0%, rgba(124,58,237,0.18) 0%, transparent 60%),
        radial-gradient(ellipse 50% 40% at 20% 100%, rgba(6,182,212,0.08) 0%, transparent 60%),
        radial-gradient(ellipse 40% 30% at 80% 60%, rgba(168,85,247,0.06) 0%, transparent 70%);
    pointer-events: none; z-index: 0;
}

/* ── SPLASH SCREEN ── */
.splash {
    position: fixed; inset: 0; z-index: 999;
    background: var(--bg);
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    gap: 20px;
}
.splash-logo {
    font-size: 5rem; font-weight: 900; letter-spacing: -3px;
    background: linear-gradient(135deg, #c084fc 0%, #7c3aed 45%, #06b6d4 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text; line-height: 1;
    animation: logoIn 0.8s cubic-bezier(.16,1,.3,1) both;
    filter: drop-shadow(0 0 40px rgba(124,58,237,0.5));
}
@keyframes logoIn {
    from { opacity:0; transform: scale(0.7) translateY(20px); }
    to   { opacity:1; transform: scale(1) translateY(0); }
}
.splash-bar-wrap {
    width: 200px; height: 3px;
    background: rgba(255,255,255,0.05);
    border-radius: 10px; overflow: hidden;
    margin-top: 10px;
}
.splash-bar {
    height: 100%; width: 0%;
    background: linear-gradient(90deg, #7c3aed, #06b6d4);
    border-radius: 10px;
    animation: loadBar 1.8s ease forwards;
}
@keyframes loadBar { 0%{width:0%} 100%{width:100%} }
.splash-tag {
    font-size: 0.65rem; letter-spacing: 4px;
    text-transform: uppercase; color: var(--text-dim);
    animation: fadeIn 0.6s 0.4s both;
}
@keyframes fadeIn { from{opacity:0} to{opacity:1} }

/* ── LOGIN PAGE ── */
.login-page {
    min-height: 100vh;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    padding: 30px 20px;
    position: relative; z-index: 1;
    animation: fadeIn 0.5s ease both;
}
.login-header { text-align: center; margin-bottom: 32px; }
.login-logo {
    font-size: 3rem; font-weight: 900; letter-spacing: -2px;
    background: linear-gradient(135deg, #c084fc 0%, #7c3aed 45%, #06b6d4 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text; line-height: 1;
    filter: drop-shadow(0 0 24px rgba(124,58,237,0.4));
}
.login-sub {
    font-size: 0.68rem; letter-spacing: 3px; text-transform: uppercase;
    color: var(--text-dim); margin-top: 5px;
}
.login-card {
    width: 100%; max-width: 380px;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 24px;
    padding: 28px 24px;
    box-shadow: 0 8px 40px rgba(0,0,0,0.4), 0 0 0 1px rgba(124,58,237,0.08);
    animation: cardIn 0.6s cubic-bezier(.16,1,.3,1) both;
}
@keyframes cardIn {
    from { opacity:0; transform: translateY(24px); }
    to   { opacity:1; transform: translateY(0); }
}
.login-title {
    font-size: 1.2rem; font-weight: 700; color: var(--text);
    margin-bottom: 4px;
}
.login-desc {
    font-size: 0.78rem; color: var(--text-mid); margin-bottom: 24px;
}
.field-label {
    font-size: 0.75rem; font-weight: 600;
    color: var(--text-mid); letter-spacing: 0.5px;
    margin-bottom: 6px; display: block;
}
.divider {
    display: flex; align-items: center; gap: 10px;
    margin: 20px 0; color: var(--text-dim); font-size: 0.72rem;
}
.divider::before, .divider::after {
    content: ''; flex: 1; height: 1px; background: var(--border);
}
.footer-note {
    text-align: center; margin-top: 20px;
    font-size: 0.68rem; color: var(--text-dim);
}

/* ── WELCOME BACK SCREEN ── */
.welcome-back {
    min-height: 100vh;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    padding: 30px 20px;
    position: relative; z-index: 1;
    text-align: center;
    animation: fadeIn 0.5s ease both;
}
.wb-avatar {
    width: 72px; height: 72px; border-radius: 50%;
    background: linear-gradient(135deg, #7c3aed, #06b6d4);
    display: flex; align-items: center; justify-content: center;
    font-size: 2rem; margin: 0 auto 16px;
    box-shadow: 0 0 0 4px rgba(124,58,237,0.2), 0 8px 32px rgba(124,58,237,0.3);
    animation: avatarIn 0.6s cubic-bezier(.16,1,.3,1) both;
}
@keyframes avatarIn {
    from { opacity:0; transform: scale(0.5); }
    to   { opacity:1; transform: scale(1); }
}
.wb-name {
    font-size: 1.6rem; font-weight: 800; color: var(--text);
    margin-bottom: 4px;
}
.wb-email { font-size: 0.8rem; color: var(--text-dim); margin-bottom: 24px; }
.wb-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 20px; padding: 20px;
    max-width: 320px; width: 100%;
    margin-bottom: 20px;
}
.wb-stat {
    display: flex; justify-content: space-between; align-items: center;
    padding: 8px 0; border-bottom: 1px solid var(--border);
    font-size: 0.8rem; color: var(--text-mid);
}
.wb-stat:last-child { border-bottom: none; }
.wb-stat span:last-child { color: var(--purple-xt); font-weight: 600; }

/* Streamlit overrides */
.stTextInput input {
    background: rgba(124,58,237,0.06) !important;
    border: 1px solid rgba(124,58,237,0.2) !important;
    border-radius: 12px !important;
    color: var(--text) !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 0.9rem !important;
    padding: 10px 14px !important;
    transition: all 0.2s !important;
}
.stTextInput input:focus {
    border-color: rgba(124,58,237,0.6) !important;
    box-shadow: 0 0 0 3px rgba(124,58,237,0.1) !important;
    outline: none !important;
}
.stTextInput input::placeholder { color: var(--text-dim) !important; }
.stTextInput label {
    font-size: 0.75rem !important; font-weight: 600 !important;
    color: var(--text-mid) !important; letter-spacing: 0.5px !important;
    font-family: 'Outfit', sans-serif !important;
}

.stButton > button {
    background: linear-gradient(135deg, #7c3aed, #a855f7) !important;
    border: none !important; border-radius: 12px !important;
    color: white !important; font-family: 'Outfit', sans-serif !important;
    font-size: 0.92rem !important; font-weight: 700 !important;
    padding: 12px 24px !important; width: 100% !important;
    letter-spacing: 0.3px !important;
    box-shadow: 0 4px 20px rgba(124,58,237,0.4) !important;
    transition: all 0.2s !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 28px rgba(124,58,237,0.55) !important;
}
.stButton > button:active { transform: translateY(0) !important; }

div[data-testid="stCheckbox"] label {
    font-size: 0.8rem !important; color: var(--text-mid) !important;
    font-family: 'Outfit', sans-serif !important;
}

.stSuccess {
    background: rgba(34,197,94,0.1) !important;
    border: 1px solid rgba(34,197,94,0.3) !important;
    border-radius: 10px !important; color: var(--green) !important;
}
.stError {
    background: rgba(239,68,68,0.1) !important;
    border: 1px solid rgba(239,68,68,0.3) !important;
    border-radius: 10px !important; color: var(--red) !important;
}
.stSpinner { color: var(--purple-lt) !important; }
</style>
""", unsafe_allow_html=True)

# ─── Session State ──────────────────────────────────────────────
if "splash_done"   not in st.session_state: st.session_state.splash_done   = False
if "logged_in"     not in st.session_state: st.session_state.logged_in     = False
if "user_name"     not in st.session_state: st.session_state.user_name     = ""
if "user_email"    not in st.session_state: st.session_state.user_email    = ""
if "login_time"    not in st.session_state: st.session_state.login_time    = None
if "show_welcome"  not in st.session_state: st.session_state.show_welcome  = False

# ─── Cookie helpers via query params trick ──────────────────────
# Streamlit doesn't have real cookies, but we persist via st.session_state
# For 30-day persistence we use st.secrets-free local JSON via st.cache_data workaround
# In Streamlit Cloud: data persists for the session; for real 30-day, Firebase needed
# We simulate "remember me" by auto-filling if session still alive

def validate_email(email):
    import re
    return bool(re.match(r'^[^@]+@[^@]+\.[^@]+$', email))

def get_initials(name):
    parts = name.strip().split()
    if len(parts) >= 2:
        return (parts[0][0] + parts[-1][0]).upper()
    return name[:2].upper() if name else "N"

# ─── SPLASH SCREEN ─────────────────────────────────────────────
if not st.session_state.splash_done:
    st.markdown("""
    <div class="splash">
        <div class="splash-logo">NEXO</div>
        <div class="splash-tag">Smart Conversations · Smarter Results</div>
        <div class="splash-bar-wrap">
            <div class="splash-bar"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    time.sleep(2.2)
    st.session_state.splash_done = True
    st.rerun()

# ─── LOGGED IN — WELCOME BACK ───────────────────────────────────
elif st.session_state.logged_in:
    name     = st.session_state.user_name
    email    = st.session_state.user_email
    initials = get_initials(name)
    login_dt = st.session_state.login_time or datetime.now().strftime("%Y-%m-%d %H:%M")
    expires  = (datetime.strptime(login_dt, "%Y-%m-%d %H:%M") + timedelta(days=30)).strftime("%Y %B %d")

    st.markdown(f"""
    <div class="welcome-back">
        <div class="wb-avatar">{initials}</div>
        <div class="wb-name">Welcome back,<br>{name.split()[0]}! 👋</div>
        <div class="wb-email">{email}</div>
        <div class="wb-card">
            <div class="wb-stat">
                <span>👤 Account</span>
                <span>{name}</span>
            </div>
            <div class="wb-stat">
                <span>📧 Email</span>
                <span>{email[:18]}{'...' if len(email)>18 else ''}</span>
            </div>
            <div class="wb-stat">
                <span>🔐 Session</span>
                <span>Active</span>
            </div>
            <div class="wb-stat">
                <span>📅 Expires</span>
                <span>{expires}</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🚀 Open Nexo AI"):
            st.success("Launching Nexo AI... ✨")
            time.sleep(1)
            # Redirect to main app or show main content
            st.info("Merge කළාට පස්සේ main app launch වෙනවා!")
    with col2:
        if st.button("🚪 Sign Out"):
            st.session_state.logged_in    = False
            st.session_state.user_name    = ""
            st.session_state.user_email   = ""
            st.session_state.login_time   = None
            st.session_state.splash_done  = False
            st.rerun()

# ─── LOGIN SCREEN ───────────────────────────────────────────────
else:
    st.markdown("""
    <div class="login-page">
        <div class="login-header">
            <div class="login-logo">NEXO</div>
            <div class="login-sub">Your AI Companion</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Center the card
    col_l, col_c, col_r = st.columns([1, 10, 1])
    with col_c:
        st.markdown('<div class="login-card">', unsafe_allow_html=True)
        st.markdown('<div class="login-title">Sign In ✦</div>', unsafe_allow_html=True)
        st.markdown('<div class="login-desc">Enter your details to access Nexo AI</div>', unsafe_allow_html=True)

        name_input  = st.text_input("Your Name", placeholder="Hasith Heshan", key="name_in")
        email_input = st.text_input("Email Address", placeholder="you@example.com", key="email_in")
        remember_me = st.checkbox("Remember me for 30 days", value=True)

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("✦ Sign In to Nexo", key="signin_btn"):
            if not name_input.strip():
                st.error("⚠️ Please enter your name")
            elif not email_input.strip():
                st.error("⚠️ Please enter your email")
            elif not validate_email(email_input.strip()):
                st.error("⚠️ Please enter a valid email address")
            else:
                with st.spinner("Signing you in..."):
                    time.sleep(1.2)
                st.session_state.logged_in   = True
                st.session_state.user_name   = name_input.strip().title()
                st.session_state.user_email  = email_input.strip().lower()
                st.session_state.login_time  = datetime.now().strftime("%Y-%m-%d %H:%M")
                st.success(f"Welcome, {name_input.strip().title()}! 🎉")
                time.sleep(0.8)
                st.rerun()

        st.markdown("""
        <div class="divider">or</div>
        <div class="footer-note">
            By signing in, you agree to use Nexo AI responsibly.<br>
            <span style="color:#7c3aed">No password required</span> — just your name & email.
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
