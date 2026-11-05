# VisionTalk – AI Visual Assistant

🚀 **Live Demo:** https://visiontalk-3xyt967yagzwpkzb3zxxdh.streamlit.app/

VisionTalk is an AI-powered visual assistant that:
- Captures images using a camera.
- Understands images using Google Gemini AI.
- Accepts voice and text questions.
- Responds with text and speech.

## Technologies Used
- Python
- Streamlit
- Google Gemini API
- gTTS

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
