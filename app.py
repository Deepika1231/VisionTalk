import os
import streamlit as st
from google import genai
from google.genai import types
from gtts import gTTS
from io import BytesIO

st.set_page_config(page_title="VisionTalk", page_icon="👁️", layout="centered")

st.markdown("""
<style>
.main {max-width: 900px; padding-top: 2rem;}
.hero {padding: 1.5rem; border-radius: 18px; background: linear-gradient(120deg,#172554,#312e81); color: white;}
.small {color:#64748b;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero"><h1>👁️ VisionTalk</h1><p>See the world. Ask questions. Hear answers.</p></div>', unsafe_allow_html=True)
st.write("VisionTalk is a voice-enabled visual assistant. Show it something with your camera, ask a question, and hear an AI-generated answer.")

api_key = st.sidebar.text_input("Google Gemini API key", type="password",
                                value=os.getenv("GEMINI_API_KEY", ""))
st.sidebar.caption("Get a key from Google AI Studio. Your key is used only for this session.")

photo = st.camera_input("Take a picture of what you want VisionTalk to see")
audio = st.audio_input("🎙️ Ask your question")

question = st.text_input("Or type your question", placeholder="What objects can you see?")

if st.button("✨ Ask VisionTalk", type="primary", use_container_width=True):
    if not api_key:
        st.error("Please add your Gemini API key in the left sidebar.")
    elif photo is None:
        st.error("Please take a camera picture first.")
    elif audio is None and not question.strip():
        st.error("Please record or type a question.")
    else:
        try:
            client = genai.Client(api_key=api_key)
            prompt = question.strip() or "Listen to the user's audio question and answer it using the image."
            contents = [
                types.Part.from_bytes(data=photo.getvalue(), mime_type="image/jpeg"),
                types.Part.from_text(text=prompt)
            ]
            if audio is not None:
                contents.append(types.Part.from_bytes(
                    data=audio.getvalue(),
                    mime_type=audio.type or "audio/wav"
                ))
                contents.append(types.Part.from_text(
                    text="The audio contains the user's spoken question. Answer that question using the image."
                ))

            with st.spinner("VisionTalk is looking and listening..."):
                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=contents
                )
                answer = response.text or "Sorry, I could not create an answer. Please try again."
            st.subheader("💬 VisionTalk says")
            st.write(answer)
            speech = gTTS(text=answer, lang="en")
            audio_out = BytesIO()
            speech.write_to_fp(audio_out)
            st.audio(audio_out.getvalue(), format="audio/mp3")
        except Exception as e:
            st.error(f"Something went wrong: {e}")
            st.info("Check your internet connection, Gemini API key, and try again.")

st.divider()
st.caption("Built with Python, Streamlit, Google Gemini Vision and text-to-speech.")
