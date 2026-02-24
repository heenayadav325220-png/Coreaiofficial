import streamlit as st
import google.generativeai as genai

# 1. पेज की सजावट
st.set_page_config(page_title="CORE AI", page_icon="♾️", layout="centered")

# 2. 'Secrets' से चाबी (Key) उठाना
try:
    # यह लाइन सीधे तेरे Streamlit Secrets वाले डब्बे से चाबी खींचेगी
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    st.error("भाई, चाबी (Key) नहीं मिल रही!")
    st.info("Streamlit के Secrets में जाकर देखो कि क्या वहां GOOGLE_API_KEY लिखा है?")
    st.stop() # अगर चाबी नहीं मिली तो ऐप यहीं रुक जाएगा

# 3. AI की याददाश्त (Memory) सेट करना
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# 4. स्क्रीन पर दिखने वाला हिस्सा (UI)
st.title("♾️ CORE AI")
st.markdown(f"**Master:** Rohit Yadav | **Guardian:** Nick 🛡️")
st.divider()

# पुरानी बातें स्क्रीन पर दिखाना
for message in st.session_state.chat.history:
    role = "user" if message.role == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

# 5. सवाल पूछने का डब्बा
prompt = st.chat_input("रोहित भाई, यहाँ अपना सवाल लिखें...")

if prompt:
    # यूजर का मैसेज दिखाओ
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI का जवाब लाओ
    with st.chat_message("assistant"):
        try:
            response = st.session_state.chat.send_message(prompt)
            st.markdown(response.text)
        except Exception as e:
            st.error("AI से बात नहीं हो पा रही है भाई!")
            st.info("हो सकता है इंटरनेट धीमा हो या की (Key) में दिक्कत हो।")

# साइडबार में सेटिंग्स
with st.sidebar:
    st.title("🚀 कंट्रोल पैनल")
    st.write("Status: **Online** ✅")
    if st.button("चैट साफ़ करें"):
        st.session_state.chat = model.start_chat(history=[])
        st.rerun()
