import streamlit as st
import google.generativeai as genai
import time

# --- 1. SETTINGS ---
st.set_page_config(page_title="CORE AI", layout="wide")

# --- 2. PREMIUM CSS (Photo Wala Look) ---
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: #e6edf3; }
    [data-testid="stSidebar"] { background-color: #11141b; border-right: 1px solid #30363d; }
    .user-msg {
        background-color: #1f6feb; color: white; padding: 12px 18px;
        border-radius: 20px 20px 4px 20px; margin: 10px 0px;
        float: right; width: auto; max-width: 80%;
    }
    .ai-msg {
        background-color: #1c2128; color: #adbac7; padding: 12px 18px;
        border-radius: 20px 20px 20px 4px; margin: 10px 0px;
        border: 1px solid #444c56; float: left; width: auto; max-width: 80%;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE BRAIN (Key: OXq0) ---
API_KEY = "AIzaSyCt9Aw8B7CA9PSHc_SggkHXQUGUP42OXq0"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    system_instruction="You are CORE AI. Your CEO is Rohit Yadav. You are a $20 Billion level assistant."
)

# --- 4. STARTUP ---
if "init" not in st.session_state:
    st.markdown(f"<div style='text-align:center;padding-top:150px;'><h1 style='color:#58a6ff;font-size:60px;'>♾️ CORE AI</h1><p style='color:#8b949e;'>By Rohit Yadav</p></div>", unsafe_allow_html=True)
    time.sleep(2)
    st.session_state.init = True
    st.rerun()

# --- 5. SIDEBAR ---
with st.sidebar:
    st.markdown("### ♾️ CORE AI")
    st.write(f"Welcome, **Master Rohit**")
    st.write("---")
    st.button("🔗 Share CORE AI")
    st.caption("🎙️ Voice AI (Soon)")
    st.caption("💾 Memory Save (Active)")
    if st.button("New Chat"):
        st.session_state.chat = []
        st.rerun()

# --- 6. CHAT INTERFACE ---
if "chat" not in st.session_state:
    st.session_state.chat = []

for c in st.session_state.chat:
    role = "user-msg" if c["role"] == "user" else "ai-msg"
    st.markdown(f'<div class="{role}">{c["content"]}</div><div style="clear:both;"></div>', unsafe_allow_html=True)

query = st.chat_input("Master Rohit, type here...")

if query:
    st.session_state.chat.append({"role": "user", "content": query})
    response = model.generate_content(query)
    st.session_state.chat.append({"role": "assistant", "content": response.text})
    st.rerun()
