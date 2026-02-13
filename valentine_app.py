import streamlit as st
import requests
import os
import base64

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL", "") 

st.set_page_config(
    page_title="Важный вопрос 💕",
    page_icon="💝",
    layout="centered"
)

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffeef8 0%, #ffe6f0 100%);
    }
    
    .big-text {
        font-size: 2.5rem;
        font-weight: bold;
        color: #d63384;
        text-align: center;
        margin-top: 100px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .question-text {
        font-size: 3rem;
        font-weight: bold;
        color: #c41e3a;
        text-align: center;
        margin-top: 80px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .success-text {
        font-size: 10rem;
        font-weight: bold;
        color: #ff1493;
        text-align: center;
        margin-top: 100px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        animation: pulse 1.5s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    .stButton > button {
        background-color: #ff69b4;
        color: white;
        font-size: 1.2rem;
        font-weight: bold;
        border-radius: 25px;
        border: none;
        padding: 15px 40px;
        transition: all 0.3s ease;
        text-align: center;
    }
    
    .stButton > button:hover {
        background-color: #ff1493;
        transform: scale(1.05);
    }
    
    div[data-testid="column"] {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'intro'
if 'no_clicks' not in st.session_state:
    st.session_state.no_clicks = 0
if 'notification_sent' not in st.session_state:
    st.session_state.notification_sent = False

def send_discord_notification(message):
    if not DISCORD_WEBHOOK_URL:
        st.warning("Discord webhook is not configured. Please set DISCORD_WEBHOOK_URL environment variable.")
        return False
    try:
        data = {
            "content": message
        }
        response = requests.post(DISCORD_WEBHOOK_URL, json=data)
        return response.status_code == 204
    except Exception as e:
        st.error(f"Failed to send Discord notification: {e}")
        return False

if st.session_state.page == 'intro':
    st.markdown('<p class="big-text">Хочу тебя спросить о чём-то важном😄</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        file_ = open("akuma-cat.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
            f'<div style="display: flex; justify-content: center;"><img src="data:image/gif;base64,{data_url}" alt="cat gif intro" style="max-width: 100%; height: auto;"></div>',
            unsafe_allow_html=True,
        )

        if st.button("О чём? 😊", key="what_button", use_container_width=True):
            st.session_state.page = 'question'
            st.rerun()

elif st.session_state.page == 'question':
    st.markdown('<p class="question-text">Будешь ли ты моей валентинкой? 💝</p>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        file_ = open("romantice-cat.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
            f'<div style="display: flex; justify-content: center;"><img src="data:image/gif;base64,{data_url}" alt="cat gif" style="max-width: 100%; height: auto;"></div>',
            unsafe_allow_html=True,
        )
    
    button_size = max(0.1, 1 - (st.session_state.no_clicks * 0.15))
    
    st.markdown(f"""
        <style>
        button[data-testid="stBaseButton-secondary"] {{
            transform: scale({button_size}) !important;
            transition: transform 0.3s ease !important;
        }}
        </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <style>
        button[data-testid="stBaseButton-primary"] {{
            max-width: 100%;
            transform: scale({1+(1-button_size)}) !important;
            transform-origin: center;
            transition: transform 0.3s ease !important;
        }}
        </style>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns([2, 2, 0.5, 2, 2])
    
    with col2:
        if st.button("Да 💕", key="yes_button", type="primary", use_container_width=True):
            st.session_state.page = 'success'
            st.rerun()
    
    with col3:
        st.write("")
    
    with col4:
        if st.session_state.no_clicks <= 5:
            if st.button("Нет 😔", key="no_button", type="secondary", use_container_width=True):
                st.session_state.no_clicks += 1
                st.rerun()
        else:
            st.session_state.no_clicks += 1

elif st.session_state.page == 'success':
    if not st.session_state.notification_sent:
        send_discord_notification("🎉 Она сказала ДА! 💕")
        st.session_state.notification_sent = True
    
    st.markdown('<p class="success-text">Урааааа! 🥰🎉💖</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        file_ = open("cutest-white-cat.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
            f'<div style="display: flex; justify-content: center;"><img src="data:image/gif;base64,{data_url}" alt="cat gif intro" style="max-width: 100%; height: auto;"></div>',
            unsafe_allow_html=True,
        )