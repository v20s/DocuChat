import streamlit as st

def inject_css():
    st.markdown(r"""
    <style>
        /* Hide default Streamlit UI elements */
        #MainMenu, footer { visibility: hidden; }

        /* Page background & font */
        body, .reportview-container, .main {
            background-color: #1f1f1f;
            color: #f0f0f0;
            font-family: 'Segoe UI', sans-serif;
        }
        /* Sidebar background */
        .sidebar .css-1d391kg {
            background-color: #2a2a2a !important;
            padding-top: 1rem;
        }
        /* File uploader dropzone shadow */
        div[data-baseweb="file-uploader"] {
            border-radius: 8px !important;
            box-shadow: 0 2px 8px rgba(0,0,0,0.6) !important;
        }
        /* Input box */
        .stTextInput>div>div>input {
            background-color: #2a2a2a;
            border: 1px solid #444;
            border-radius: 6px;
            padding: 12px;
            color: #f0f0f0;
        }
        .stTextInput>div>div>input::placeholder {
            color: #888;
        }
        /* Send button */
        .stButton>button {
            background-color: #ff6b81;
            color: #fff;
            border: none;
            border-radius: 20px;
            padding: 10px 24px;
            font-weight: bold;
            box-shadow: 0 2px 4px rgba(0,0,0,0.6);
        }
        .stButton>button:hover {
            background-color: #ff8fa3;
        }
        /* Chat bubbles */
        .user-bubble, .bot-bubble {
            max-width: 75%;
            padding: 14px 16px;
            margin: 8px 0;
            border-radius: 12px;
            line-height: 1.5;
        }
        .user-bubble {
            background-color: #333333;
            color: #ffffff;
            margin-left: auto;
            box-shadow: 0 1px 4px rgba(0,0,0,0.5);
        }
        .bot-bubble {
            background-color: #414141;
            color: #e0e0e0;
            margin-right: auto;
            box-shadow: 0 1px 4px rgba(0,0,0,0.5);
        }
        /* Separator line */
        .css-1d5rx9s hr {
            border-color: #444;
        }
    </style>
    """, unsafe_allow_html=True)
