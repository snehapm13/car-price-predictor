import streamlit as st


def apply_custom_css():

    st.markdown(
        """
        <style>

        /* Complete page */
        .stApp {
            background:
                linear-gradient(
                    135deg,
                    #f4f7fb,
                    #e8f0ff
                );
        }

        /* Main content */
        .block-container {
            max-width: 1100px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        /* Main heading card */
        .main-header {
            background:
                linear-gradient(
                    135deg,
                    #173b67,
                    #2563a9
                );
            color: white;
            padding: 28px;
            border-radius: 18px;
            text-align: center;
            margin-bottom: 25px;
            box-shadow:
                0 8px 20px
                rgba(0, 0, 0, 0.12);
        }

        .main-header h1 {
            color: white;
            margin: 0;
            font-size: 38px;
        }

        .main-header p {
            margin-top: 8px;
            margin-bottom: 0;
            font-size: 17px;
        }

        /* Section headings */
        h2, h3 {
            color: #173b67;
        }

        /* Buttons */
        div.stButton > button {
            background-color: #2563a9;
            color: white;
            border: none;
            border-radius: 10px;
            padding: 10px 24px;
            font-weight: 600;
        }

        div.stButton > button:hover {
            background-color: #173b67;
            color: white;
        }

        /* Input fields */
        div[data-baseweb="input"] {
            border-radius: 10px;
        }

        /* Metric card */
        div[data-testid="stMetric"] {
            background-color: white;
            border-left: 5px solid #2563a9;
            padding: 18px;
            border-radius: 12px;
            box-shadow:
                0 4px 14px
                rgba(0, 0, 0, 0.08);
        }

        /* Chat messages */
        div[data-testid="stChatMessage"] {
            background-color: white;
            border-radius: 12px;
            padding: 10px;
        }

        /* Footer */
        .footer {
            text-align: center;
            color: #5f6b7a;
            margin-top: 35px;
            padding: 15px;
            border-top: 1px solid #ccd6e3;
        }

        </style>
        """,
        unsafe_allow_html=True
    )