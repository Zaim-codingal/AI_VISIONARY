import base64
from io import BytesIO

import streamlit as st
from PIL import Image
from groq import groq
import config

st.set_page_config(page_title="AI VISIONARY", page_icon=":mag:", layout="wide")

STYLES = {

"Normal": (
"Look at this image carefully and write a clear, detailed report. "
"Describe the scene, objects, and what seems to be happening."
),

"Funny": (
"Look at this image carefully and write a funny image report. "
"Mention objects, details, and make the report playful and humorous, "
"but still describe the image correctly."
),

"Detective": (
"Look at this image like a detective. "
"Write an investigation-style report with clues, observations, and smart deductions."
),

"Dramatic": (
"Look at this image and describe it in a dramatic, cinematic way. "
"Make the report vivid, exciting, and expressive."
),

"Story Mode": (
"Look at this image and write a short story-like scene description. "
"Describe the setting, objects, and mood in a creative way."
),
}

def analyze_image(uploaded_file, style):
    encoded_image = base64.b64encode(uploaded_file.getvalue()).decode('utf-8')
    response = client.chat.completions.create(
        model = config.groq_vision_model,
        messages = [
            {
                "role":"user",
                "content":[
                    {"type":"text", "text": STYLES.get(style, STYLES["Normal"])},
                    {"type":"image_url",
                     "image_url": {"url": f"data:{uploaded_file.type};base64,{encoded}"}}
                ],
            },
        ],
            temperature=0.7,
            max_tokens=500,
    ),

    return response.choices[0].message.content

uploaded_file = st.file_uploader("Upload an image to analyze", type=["jpg", "jpeg", "png"])

report style = st.selectbox("Select a report style", list(STYLES))

if uploaded_file:
    st.image(
        Image.open(BytesIO(uploaded_file.getvalue())),
        caption="Uploaded Image",
        use_column_width=True,
    )

    if st.button("Analyze Image"):
        if not config.GROQ_API_KEY:
            st.error("Groq key is missing. Please set GROQ_API_KEY in your .env file.")
        elif not uploaded file:
            st.error("Please upload an image to analyze.")
        else:
            with st.spinner("Analyzing image..."):
                try:
                    st.success("Image analysis complete!")
                    st.subheader("Image Analysis Report")
                    st.write(analyze_image(uploaded_file, report_style))
                except Exception as e:
                    st.error(f"Something Went Wrong: {e}")