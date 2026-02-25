import streamlit as st

# --- 1. DARK INDUSTRIAL THEME CSS ---
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,400,1,0" rel="stylesheet" />
    
    <style>
    /* Full Dark Mode with Boltshift Gradient */
    .stApp {
        background: radial-gradient(circle at top right, #07191e 0%, #000000 100%);
        color: #acb2b1;
    }

    /* Standard Grid Boxes (Inspired by Boltshift) */
    .feature-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        transition: 0.4s ease;
    }
    .feature-card:hover {
        border-color: #00f2ff;
        background: rgba(0, 242, 255, 0.05);
        box-shadow: 0 0 20px rgba(0, 242, 255, 0.1);
    }

    /* Standard Classic Icons (No Emoji) */
    .material-symbols-rounded {
        font-size: 32px !important;
        color: #00f2ff;
    }

    /* Jarvas Style Orb */
    .orb-box { display: flex; justify-content: center; margin: 30px 0; }
    .orb {
        width: 130px; height: 130px;
        background: radial-gradient(circle, #00f2ff, #005f73, transparent);
        border-radius: 50%;
        box-shadow: 0 0 50px rgba(0, 242, 255, 0.3);
        animation: breathe 6s infinite ease-in-out;
    }
    @keyframes breathe { 0%, 100% { transform: scale(1); opacity: 0.7; } 50% { transform: scale(1.05); opacity: 1; } }

    /* Custom Input Bar (Like the one with Mic in your photo) */
    .stChatInputContainer {
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 20px !important;
        background: rgba(10, 10, 10, 0.6) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE UI LAYOUT ---

# Top Orb (Jarvas Vibe)
st.markdown('<div class="orb-box"><div class="orb"></div></div>', unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; letter-spacing: 5px; font-weight: 200;'>CORE AI</h2>", unsafe_allow_html=True)

# The 4 Feature Boxes (Standard Icons)
st.write("##")
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="feature-card"><span class="material-symbols-rounded">psychology</span><p style="font-size:11px; margin-top:10px; color:#666;">NEURAL LINK</p></div>', unsafe_allow_html=True)
    if st.button("ACTIVATE OPUS", use_container_width=True): pass

    st.markdown('<div class="feature-card"><span class="material-symbols-rounded">visibility</span><p style="font-size:11px; margin-top:10px; color:#666;">VISUAL CORE</p></div>', unsafe_allow_html=True)
    if st.button("ACTIVATE VISION", use_container_width=True): pass

with col2:
    st.markdown('<div class="feature-card"><span class="material-symbols-rounded">videocam</span><p style="font-size:11px; margin-top:10px; color:#666;">CINEMA GEN</p></div>', unsafe_allow_html=True)
    if st.button("ACTIVATE VIDEO", use_container_width=True): pass

    st.markdown('<div class="feature-card"><span class="material-symbols-rounded">mic</span><p style="font-size:11px; margin-top:10px; color:#666;">VOICE LINK</p></div>', unsafe_allow_html=True)
    if st.button("ACTIVATE NICK", use_container_width=True): pass

# Input Section (The "Standard" way)
st.write("---")
st.chat_input("Ask CORE AI anything...")
