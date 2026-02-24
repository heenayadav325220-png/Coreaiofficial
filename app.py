import streamlit as st
import google.generativeai as genai
import os
import time
import uuid

# ---------------- 1. CONFIG & STYLE ----------------
st.set_page_config(page_title="CORE AI", page_icon="♾️", layout="centered")

# Custom CSS for better look
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stChatMessage { border-radius: 15px; }
    </style>
    """, unsafe_allow_index=True)

# ---------------- 2. UNIQUE SESSION ID ----------------
if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())[:8]

# ---------------- 3. API KEY & MODEL SETUP ----------------
# Safe loading of API Key
if "GEMINI_API_KEY" in st.secrets:
    API_KEY = st.secrets["GEMINI_API_KEY"]
else:
    API_KEY = "AIzaSyD_rfyCd96Jq_SJOOgFWSjf1cAwIptc5U0" 

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# ---------------- 4. CHAT MEMORY ----------------
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

if "usage" not in st.session_state:
    st.session_state.usage = 0

# ---------------- 5. MAIN INTERFACE ----------------
st.title("♾️ CORE AI")
st.caption("Emotionally Intelligent Assistant | Created by Rohit Yadav")

# Display History
for message in st.session_state.chat.history:
    with st.chat_message("user" if message.role == "user" else "assistant"):
        st.markdown(message.parts[0].text)

# User Input
prompt = st.chat_input("अपनी बात यहाँ लिखें...")

if prompt:
    # Rate Limiting Feature
    if "last_time" not in st.session_state:
        st.session_state.last_time = 0

    if time.time() - st.session_state.last_time < 2:
        st.warning("⏳ थोड़ा धीरे भाई, CORE AI सोच रहा है...")
        st.stop()

    st.session_state.last_time = time.time()

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("CORE AI is thinking..."):
            try:
                response = st.session_state.chat.send_message(prompt)
                st.markdown(response.text)
                st.session_state.usage += 1
            except Exception as e:
                st.error("⚠️ AI busy. Try later.")

# ---------------- 6. SIDEBAR (All Features Restored) ----------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712035.png", width=100)
    st.markdown("## 🚀 CORE AI CONTROL")
    st.write(f"**Master:** Rohit Yadav")
    st.write(f"**User ID:** `{st.session_state.user_id}`")
    st.write(f"**Messages:** {st.session_state.usage}")
    
    st.markdown("---")
    
    # Share section
    st.markdown("### 📢 Share CORE AI")
    # यहाँ तेरा असली ऐप लिंक आएगा
    share_link = "https://core-ai-official.streamlit.app" 
    st.code(share_link)
    st.caption("Copy and share with friends 🔥")

    st.markdown("---")

    # Coming Soon section (Original feature)
    st.markdown("### 🏆 Roadmap")
    st.write("• 🎤 Voice Mode")
    st.write("• 🧠 Memory Save")
    st.write("• 🎁 Referral Rewards")
    
    st.markdown("---")
    st.success("Protected by Nick 🛡️")
