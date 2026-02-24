import streamlit as st
import google.generativeai as genai
import os
import time
import uuid

# ---------------- CONFIG ----------------
st.set_page_config(page_title="CORE AI", page_icon="♾️")

# ---------------- UNIQUE SESSION ID ----------------
if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())[:8]

# ---------------- SECURE API ----------------
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    st.error("API Key missing. Add it in Secrets.")
    st.stop()

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

# ---------------- MEMORY ----------------
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

if "usage" not in st.session_state:
    st.session_state.usage = 0

# ---------------- MAIN UI ----------------
st.title("♾️ CORE AI")
st.caption("Emotionally Intelligent Assistant")

prompt = st.chat_input("अपनी बात लिखें...")

if prompt:

    if "last_time" not in st.session_state:
        st.session_state.last_time = 0

    if time.time() - st.session_state.last_time < 2:
        st.warning("⏳ थोड़ा धीरे...")
        st.stop()

    st.session_state.last_time = time.time()

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = st.session_state.chat.send_message(prompt)
                st.markdown(response.text)
                st.session_state.usage += 1
            except:
                st.error("⚠️ AI busy. Try later.")

# ---------------- SIDEBAR PROMOTION ----------------
with st.sidebar:
    st.markdown("## 🚀 Grow CORE AI")
    st.write(f"User ID: {st.session_state.user_id}")
    st.write(f"Messages this session: {st.session_state.usage}")

    st.markdown("---")

    # Share section
    st.markdown("### 📢 Share CORE AI")
    share_link = "https://your-streamlit-link.streamlit.app"
    st.code(share_link)
    st.caption("Copy and share with friends 🔥")

    st.markdown("---")

    st.markdown("### 🏆 Coming Soon")
    st.write("• Pro Mode")
    st.write("• Voice AI")
    st.write("• Memory Save")
    st.write("• Referral Rewards 🎁")
