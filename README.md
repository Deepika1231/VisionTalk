# VisionTalk 👁️

VisionTalk is a simple AI-powered visual assistant. It captures an image from the user's camera, accepts a spoken or typed question, analyses the image with Google Gemini, and reads the answer aloud.

## Features
- Camera capture in the browser
- Spoken question recording or typed questions
- Image understanding and question answering with Gemini
- Text-to-speech answers

## Tech stack
Python · Streamlit · Google Gemini API · gTTS

## Run locally
1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the app:

   ```bash
   streamlit run app.py
   ```

5. Open the local URL shown in the terminal (usually http://localhost:8501).
6. Add a Gemini API key in the sidebar. Create one at https://aistudio.google.com/app/apikey.
7. Allow camera and microphone access, take a picture, record a question, and click **Ask VisionTalk**.

## Notes
- An internet connection and Gemini API key are required for AI answers.
- Do not put API keys in source code or commit them to GitHub.
- This is a prototype; it is not a certified accessibility or emergency-response tool.
