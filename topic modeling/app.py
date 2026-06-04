import base64
import streamlit as st
import streamlit.components.v1 as components

# Set page to wide mode
st.set_page_config(layout="wide")

# 1. Update this to your exact filename
html_file_path = "topic modeling/amazon_topics_visualization.html"

try:
    # 2. Read the file with safe UTF-8 encoding
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # 3. Convert the content into a Base64 data URI
    b64_html = base64.b64encode(html_content.encode("utf-8")).decode("utf-8")
    src_data = f"data:text/html;base64,{b64_html}"

    # 4. Display using a full-screen iframe
    st.title("Topic modeling")
    components.iframe(src=src_data, height=1000, scrolling=True)

except FileNotFoundError:
    st.error(
        f"❌ File not found! Make sure '{html_file_path}' is in the exact same folder as your Python script."
    )

