import streamlit as st

# Set up the page configuration
st.set_page_config(
    page_title="Themed App",
    page_icon="🌟",
    layout="wide"
)

# Apply custom CSS to achieve the desired theme
st.markdown(
    """
    <style>
    /* Apply primary color to the sidebar */
    .main st-emotion-cache-bm2z3a ea3mdgi8 {
        background-color: #5D3FD3 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Your app content
st.title("Welcome to the Themed App")
st.write("This is a simple Streamlit app with a custom theme applied via CSS.")
