import streamlit as st
import google.generativeai as genai
import uuid

# --- BASIC CONFIG ---
st.set_page_config(page_title="CORE AI")

# --- API CONNECTION ---
# यहाँ मैंने सीधे तेरी चाबी जोड़ दी है ताकि कोई झंझट न रहे
API_KEY = "AIzaSyD_rfyCd96Jq_SJOOgFWSjf1cAwIptc5U0"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# --- MEMORY ---
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# --- UI ---
st.title("♾️ CORE AI")

# डिस्प्ले पुरानी चैट
for message in st.session_state.chat.history:
    with st.chat_message("user" if message.role == "user" else "assistant"):
        st.markdown(message.parts[0].text)

# इनपुट बॉक्स
prompt = st.chat_input("यहाँ लिखें...")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = st.session_state.chat.send_message(prompt)
            st.markdown(response.text)
        except Exception as e:
            st.error("AI Connect नहीं हो पा रहा है।")

# --- SIDEBAR (सिर्फ काम की चीज) ---
with st.sidebar:
    st.write("### CORE AI CONTROL")
    st.write("Master: Rohit Yadav")
