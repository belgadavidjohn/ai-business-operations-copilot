import streamlit as st

st.set_page_config(
    page_title="AI Business Operations Copilot",
    page_icon="📊",
)

st.title("AI Business Operations Copilot")
st.write(
    "Upload operational data and generate business insights using AI."
)

uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"],
)

if uploaded_file is not None:
    st.success("File uploaded successfully.")