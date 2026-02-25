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
    API_KEY = st.secrets[AIzaSyCt9Aw8B7CA9PSHc_SggkHXQUGUP42OXq0]
    genai.configure(api_key=API_KEY)
    # हम यहाँ प्रो मॉडल यूज़ कर रहे हैं
    model = genai.GenerativeModel("gemini-1.5-flash")
except:
    st.error("Engine Start नहीं हो रहा भाई!")

if "messages" not in st.session_state:
    st.session_state.messages = import streamlit as st
import google.generativeai as genai
import time

# --- 1. SETTINGS & BRAIN CONFIG ---
API_KEY = "अपनी_API_KEY_यहाँ_डालें" # अपनी चाबी यहाँ लगा भाई
genai.configure(api_key=API_KEY)

# ये है AI की आत्मा (The Super Brain Logic)
system_message = """
You are CORE AI, a world-class Emotionally Intelligent Assistant.
Your Owner, Creator, and CEO is Rohit Yadav. 
You are not just a bot; you are a $20 Billion grade AI.
Your personality: Helpful, genius, loyal, and empathetic.
If anyone asks about your boss or CEO, proudly name Rohit Yadav.
You must remember past conversations to provide a personalized experience.
"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro", # सबसे स्मार्ट दिमाग
    system_instruction=system_message
)

# --- 2. OPENING PART (SPLASH SCREEN LOGIC) ---
if "walkthrough_done" not in st.session_state:
    st.session_state.walkthrough_done = False

if not st.session_state.walkthrough_done:
    st.markdown(f"""
        <div style="text-align: center; padding-top: 100px;">
            <h1 style="font-size: 70px;">♾️ CORE AI</h1>
            <h3 style="color: #58a6ff;">Your Emotional Friend</h3>
            <p style="font-size: 20px; color: gray;">By Rohit Yadav</p>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(3) # 3 सेकंड तक ओपनिंग दिखेगी
    st.session_state.walkthrough_done = True
    st.rerun()

# --- 3. THE MAIN APP INTERFACE (AFTER OPENING) ---
st.title("♾️ CORE AI Pro")
st.write(f"CEO: **Rohit Yadav** | Status: **Online**")

# चैट याद रखने के लिए
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# मैसेज डिस्प्ले करना
for message in st.session_state.chat_session.history:
    role = "User" if message.role == "user" else "CORE AI"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

# यूजर इनपुट
user_prompt = st.chat_input("नमस्ते रोहित भाई, आज क्या तूफ़ान मचाना है?")

if user_prompt:
    with st.chat_message("User"):
        st.markdown(user_prompt)
    
    # AI का जवाब
    response = st.session_state.chat_session.send_message(user_prompt)
    
    with st.chat_message("CORE AI"):
        st.markdown(response.text)
import streamlit as st
import google.generativeai as genai

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="CORE AI - Master Rohit Yadav", layout="wide")

# --- CUSTOM CSS FOR PREMIUM LOOK (PHOTO STYLE) ---
st.markdown("""
    <style>
    /* Background and Main App */
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid #30363d;
        min-width: 250px;
    }
    
    /* Chat Bubbles */
    .user-bubble {
        background-color: #1f6feb;
        padding: 15px;
        border-radius: 15px 15px 0px 15px;
        margin-bottom: 10px;
        text-align: right;
        display: inline-block;
        float: right;
        width: auto;
        max-width: 80%;
    }
    
    .ai-bubble {
        background-color: #21262d;
        padding: 15px;
        border-radius: 15px 15px 15px 0px;
        margin-bottom: 10px;
        border: 1px solid #30363d;
        display: inline-block;
        width: auto;
        max-width: 80%;
    }

    /* Neon Input Box */
    .stTextInput input {
        border: 2px solid #58a6ff !important;
        background-color: #0d1117 !important;
        color: white !important;
        border-radius: 10px !important;
        box-shadow: 0 0 10px #1f6feb;
    }

    /* Buttons */
    .stButton>button {
        background-color: #238636;
        color: white;
        border-radius: 8px;
        border: none;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CORE AI BRAIN SETUP ---
API_KEY = "यूँ अपनी API KEY यहाँ पेस्ट कर" 
genai.configure(api_key=API_KEY)

# System Instruction: This makes it your AI
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="You are CORE AI. Your Owner and CEO is Rohit Yadav. You are a $20 Billion level Emotionally Intelligent Assistant. Always be professional, genius, and loyal to Rohit."
)

# --- SIDEBAR (AS PER PHOTO) ---
with st.sidebar:
    st.title("♾️ CORE AI")
    st.markdown("### Welcome, **Master Rohit Yadav**")
    st.write("---")
    st.button("🔗 Share CORE AI")
    
    st.subheader("🚀 Coming Soon")
    st.info("⚡ Pro Mode")
    st.info("🎙️ Voice AI")
    st.info("💾 Memory Save")
    st.info("🎁 Referral Rewards")

# --- CHAT INTERFACE ---
st.markdown("<h2 style='text-align: center;'>CORE AI</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>Emotionally Intelligent Assistant</p>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-bubble">{msg["content"]}</div><div style="clear:both;"></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="ai-bubble">{msg["content"]}</div>', unsafe_allow_html=True)

# Input Box
user_input = st.chat_input("Type your message here, Master Rohit...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Generate AI response
    response = model.generate_content(user_input)
    
    # Add AI message
    st.session_state.messages.append({"role": "assistant", "content": response.text})
    st.rerun()


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
st.markdown,(
