import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="CORE AI | JARVAS", layout="wide")

# --- JARVAS PREMIUM CSS ---
st.markdown("""
    <style>
    /* Background setup */
    .stApp {
        background: radial-gradient(circle at center, #001d3d 0%, #000814 100%);
        color: white;
    }

    /* Floating Jarvas Orb */
    .orb-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 300px;
        margin-top: 50px;
    }
    .orb {
        width: 150px;
        height: 150px;
        background: radial-gradient(circle, #00b4d8, #0077b6, transparent);
        border-radius: 50%;
        box-shadow: 0 0 50px #00b4d8, 0 0 100px #0077b6;
        animation: pulse 3s infinite ease-in-out;
    }
    @keyframes pulse {
        0% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.1); opacity: 1; }
        100% { transform: scale(1); opacity: 0.8; }
    }

    /* Glassmorphic Input Box */
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 20px !important;
        color: white !important;
        padding: 15px !important;
    }

    /* Hide unnecessary streamlit elements */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- THE UI LAYOUT ---

# 1. The Glowing Orb (Visual focus)
st.markdown('<div class="orb-container"><div class="orb"></div></div>', unsafe_allow_html=True)

# 2. Greeting
st.markdown("<h2 style='text-align: center;'>Hello, I'm CORE AI.</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8;'>How may I assist you today, Master Rohit?</p>", unsafe_allow_html=True)

# 3. Features Grid (The small buttons you liked in the photo)
col1, col2, col3 = st.columns(3)
with col1:
    st.button("✨ Edit Photo", use_container_width=True)
    st.button("📅 Plan Day", use_container_width=True)
with col2:
    st.button("📖 Read Story", use_container_width=True)
    st.button("🎙️ Tell Joke", use_container_width=True)
with col3:
    st.button("🔍 Deep Think", use_container_width=True)
    st.button("🪄 Surprise Me", use_container_width=True)

# 4. Main Chat Input (At the bottom)
st.write("---")
user_input = st.text_input("", placeholder="Ask me anything...")

st
import google.generativeai as genai

# --- 1. PAGE CONFIG & MOBILE-FIRST CSS ---
st.set_page_config(page_title="CORE AI", layout="wide")

st.markdown("""
    <style>
    /* Background and Glass Effect */
    .stApp { background-color: #020617; color: white; }
    
    /* Permanent Bottom Navigation Bar */
    .bottom-nav {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background: rgba(15, 23, 42, 0.9);
        backdrop-filter: blur(15px);
        display: flex;
        justify-content: space-around;
        padding: 15px 0;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        z-index: 1000;
    }
    
    .nav-item {
        color: #94a3b8;
        text-decoration: none;
        font-size: 12px;
        text-align: center;
        flex: 1;
    }
    
    .nav-item i { font-size: 20px; display: block; margin-bottom: 5px; }
    .nav-active { color: #38bdf8; font-weight: bold; }

    /* Space for bottom nav so content doesn't hide */
    .main-content { margin-bottom: 80px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. STATE MANAGEMENT ---
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "Chat"

# --- 3. THE SMART BOTTOM NAV (HTML/CSS) ---
# Yahan hum buttons ko session state se connect karenge
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("💬 Chat"): st.session_state.active_tab = "Chat"
with col2:
    if st.button("🧠 Opus"): st.session_state.active_tab = "Opus"
with col3:
    if st.button("👁️ Vision"): st.session_state.active_tab = "Vision"
with col4:
    if st.button("🎥 Video"): st.session_state.active_tab = "Video"

st.markdown("---") # Ek line divider ke liye

# --- 4. APP LOGIC (Content Change based on Bottom Nav) ---
st.markdown('<div class="main-content">', unsafe_allow_html=True)

if st.session_state.active_tab == "Chat":
    st.subheader("CORE Chat (Gemini)")
    st.write("Master Rohit, I am ready for your command.")
    # Gemini wala chat code yahan aayega

elif st.session_state.active_tab == "Opus":
    st.subheader("Opus 4.6 Reasoning")
    st.info("Thinking Mode: On (Using nohurry/Opus-4.6)")
    # Opus API call yahan aayegi

elif st.session_state.active_tab == "Vision":
    st.subheader("Vision AI (Hugging Face)")
    # Image upload logic yahan aayega

elif st.session_state.active_tab == "Video":
    st.subheader("Wan 2.1 Video Gen")
    st.write("Create Cinematic AI Videos")
    # Wan 2.1 API call yahan aayegi

st.markdown('</div>', unsafe_allow_html=True)
