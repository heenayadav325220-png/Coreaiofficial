import streamlit as st
import google.generativeai as genai
import time

# --- SETUP ---
st.set_page_config(page_title="CORE AI PRO", page_icon="⚡", layout="wide")

# --- CSS FOR WORLD CLASS LOOK ---
st.markdown("""
    <style>
    .stApp { background: #050505; color: white; }
    .stButton>button { width: 100%; border-radius: 10px; background: linear-gradient(45deg, #00f2ff, #0066ff); color: white; border: none; }
    .chat-bubble { padding: 15px; border-radius: 15px; margin: 10px 0; border: 1px solid #333; }
    </style>
    """, unsafe_allow_html=True)

# --- AI ENGINE ---
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    # हम यहाँ प्रो मॉडल यूज़ कर रहे हैं
    model = genai.GenerativeModel("gemini-1.5-flash")
except:
    st.error("Engine Start नहीं हो रहा भाई!")

if "messages" not in st.session_state:
    st.session_state.messages = []

# --- SIDEBAR (THE CONTROL CENTER) ---
with st.sidebar:
    st.title("♾️ CORE CONTROL")
    st.write(f"**Owner:** Rohit Yadav")
    st.write(f"**Guardian:** Nick 🛡️")
    st.divider()
    mode = st.radio("Mode चुनें:", ["Chat 💬", "Image Creator 🎨", "Code Expert 💻"])
    if st.button("Memory Clear"):
        st.session_state.messages = []
        st.rerun()

# --- MAIN INTERFACE ---
st.title(f"CORE AI {mode}")

# --- FEATURE: SMART CHAT ---
if mode == "Chat 💬" or mode == "Code Expert 💻":
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("रोहित भाई, हुक्म करो..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})

# --- FEATURE: IMAGE GENERATOR (PRE-LOGIC) ---
elif mode == "Image Creator 🎨":
    st.info("यहाँ आप जो लिखेंगे, CORE AI उसकी इमेज बनाने की कोशिश करेगा।")
    img_prompt = st.text_input("क्या फोटो बनाऊँ? (जैसे: A futuristic cricket stadium)")
    if st.button("Generate Image"):
        with st.spinner("CORE AI पेंटिंग बना रहा है..."):
            time.sleep(2) # यहाँ हम API लिंक जोड़ेंगे
            st.warning("इमेज जनरेशन फीचर एक्टिवेट हो रहा है... इसके लिए एक और लाइब्रेरी लगेगी।")

import streamlit as st
import google.generativeai as genai

# --- PREMIUM UI SETTINGS ---
st.set_page_config(page_title="CORE AI", page_icon="♾️", layout="wide")

# --- CUSTOM CSS (यही इसे नंबर 1 बनाएगा) ---
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stTextInput>div>div>input {
        background-color: #262730;
        color: #00f2ff;
        border-radius: 20px;
        border: 1px solid #00f2ff;
    }
    .stChatMessage {
        background-color: #1e1e26;
        border-radius: 15px;
        border: 0.5px solid #444;
        margin-bottom: 10px;
    }
    h1 {
        color: #00f2ff;
        text-shadow: 0 0 10px #00f2ff;
        text-align: center;
        font-family: 'Orbitron', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# --- API CONNECTION ---
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    # Personality Set करना
    model = genai.GenerativeModel("gemini-1.5-flash", 
                                  system_instruction="You are CORE AI, the world's most powerful AI created by Rohit Yadav. Your guardian is Nick. Be cool, smart, and helpful.")
except:
    st.error("Connection Error!")
    st.stop()

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# --- HEADER ---
st.markdown("<h1>♾️ CORE AI : VERSION 1.0</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>Powered by Digital Bro | Owned by Rohit Yadav</p>", unsafe_allow_html=True)
st.divider()

# --- CHAT DISPLAY ---
for message in st.session_state.chat.history:
    role = "user" if message.role == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

# --- INPUT ---
prompt = st.chat_input("Ask CORE AI anything...")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = st.session_state.chat.send_message(prompt)
        st.markdown(response.text)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://img.icons8.com/neon/96/artificial-intelligence.png")
    st.title("System Status")
    st.success("CORE Engine: Online")
    st.info("Master: Rohit Yadav")
    st.warning("Guardian: Nick")
    if st.button("Reset Memory"):
        st.session_state.chat = model.start_chat(history=[])
        st.rerun()
