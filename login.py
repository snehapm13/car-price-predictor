import streamlit as st

# Login details
USER_ID = "admin"
PASSWORD = "admin"


def login():

    # Create login status
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    # Return True if already logged in
    if st.session_state.logged_in:
        return True

    # Login heading
    st.title("CarPrice AI")

    st.subheader("Login")

    # Login form
    with st.form("login_form"):

        user_id = st.text_input(
            "User ID"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        login_button = st.form_submit_button(
            "Login"
        )

    # Check login details
    if login_button:

        if (
            user_id == USER_ID
            and password == PASSWORD
        ):
            st.session_state.logged_in = True

            st.success("Login successful.")

            st.rerun()

        else:
            st.error(
                "Incorrect User ID or Password."
            )

    return False


def logout():

    if st.button("Logout"):

        st.session_state.logged_in = False

        st.rerun()