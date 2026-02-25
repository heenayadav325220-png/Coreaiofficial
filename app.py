import streamlit as st
import google.generativeai as genai

# --- 1. CONFIG & BRAIN SETUP ---
# अपनी API Key यहाँ डालें
API_KEY = "यहाँ_अपनी_Key_डालें" 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="CORE AI", layout="wide")

# --- 3. PREMIUM CSS (Jarvas Look) ---
st.markdown("""
    <style>
    .stApp { background-color: #020617; color: white; }
    
    /* Jarvas Orb Animation */
    .orb-container { display: flex; justify-content: center; padding: 20px; }
    .orb {
        width: 100px; height: 100px;
        background: radial-gradient(circle, #00d4ff, #0077b6, transparent);
        border-radius: 50%;
        box-shadow: 0 0 50px rgba(0, 212, 255, 0.5);
        animation: pulse 4s infinite ease-in-out;
    }
    @keyframes pulse {
        0% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.1); opacity: 1; box-shadow: 0 0 70px #00d4ff; }
        100% { transform: scale(1); opacity: 0.8; }
    }

    /* Fixed Bottom Nav Styling */
    .stButton > button {
        width: 100%; border-radius: 10px; background: rgba(255,255,255,0.05);
        color: white; border: 1px solid rgba(255,255,255,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. SESSION STATE (Memory) ---
if "active_tab" not in st.session_state: st.session_state.active_tab = "Chat"
if "messages" not in st.session_state: st.session_state.messages = []

# --- 5. THE ORB (Top) ---
st.markdown('<div class="orb-container"><div class="orb"></div></div>', unsafe_allow_html=True)

# --- 6. NAVIGATION (Tere Purane Buttons) ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("💬 Chat"): st.session_state.active_tab = "Chat"
with col2:
    if st.button("🧠 Opus"): st.session_state.active_tab = "Opus"
with col3:
    if st.button("👁️ Vision"): st.session_state.active_tab = "Vision"
with col4:
    if st.button("🎥 Video"): st.session_state.active_tab = "Video"

st.markdown("---")

# --- 7. LOGIC ---
if st.session_state.active_tab == "Chat":
    st.subheader("CORE Chat (Gemini)")
    
    # Show history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # Input area
    if prompt := st.chat_input("Master Rohit, I am listening..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.write(prompt)

        with st.chat_message("assistant"):
            response = model.generate_content(prompt)
            st.write(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})

elif st.session_state.active_tab == "Opus":
    st.subheader("Opus 4.6 Reasoning")
    st.write("Deep Thinking mode will be activated here.")

elif st.session_state.active_tab == "Vision":
    st.subheader("Vision AI")
    st.file_uploader("Upload an image")

elif st.session_state.active_tab == "Video":
    st.subheader("Wan 2.1 Video")
    st.write("Video generation is coming soon.")
