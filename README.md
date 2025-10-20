# 🎬 Subtitle Translator - English to Bengali

Translate English SRT subtitle files to natural Bengali using **Google Gemini AI**.

## ✨ Features

- 🌐 **English to Bengali Translation** powered by Gemini 2.0 Flash
- 📝 **Custom Translation Prompts** - Control the style and tone
- ⚡ **Batch Processing** - Handles large subtitle files efficiently
- 📊 **Real-time Progress Tracking** - See translation status live
- 💾 **Download Translated SRT** - Get Bengali subtitles instantly
- 🎨 **Beautiful UI** - Modern gradient design with animations

## 🚀 Live Demo

- **Frontend:** [Deploy on Vercel](https://vercel.com)
- **Backend:** [Deploy on Render](https://render.com)

## 📋 Prerequisites

- Google Gemini API Key ([Get it free](https://aistudio.google.com/app/apikey))
- Python 3.9+ (for backend)
- Modern web browser (for frontend)

## 🛠️ Local Setup

### Backend Setup

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/subtitle-translator-gemini.git
cd subtitle-translator-gemini
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the backend server:
```bash
python backend.py
```

Backend will run on `http://localhost:5000`

### Frontend Setup

1. Open `index.html` in your browser, or use a local server:
```bash
python -m http.server 8000
```

2. Open `http://localhost:8000` in your browser

3. Enter your Gemini API key and upload an SRT file

## 🌐 Deployment

### Deploy Backend (Render.com)

1. Go to [Render.com](https://render.com)
2. Click **New** → **Web Service**
3. Connect your GitHub repository
4. **Build Command:** `pip install -r requirements.txt`
5. **Start Command:** `gunicorn --bind 0.0.0.0:$PORT backend:app`
6. Click **Deploy**
7. Copy your backend URL (e.g., `https://your-app.onrender.com`)

### Deploy Frontend (Vercel)

1. Go to [Vercel.com](https://vercel.com)
2. Click **Add New** → **Project**
3. Import your GitHub repository
4. Click **Deploy**
5. After deployment, update `index.html`:
```javascript
const BACKEND_URL = 'https://your-backend.onrender.com'; // Replace with your Render URL
```
6. Commit and push changes - Vercel will auto-redeploy

## 📖 Usage

1. Get your free Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Enter the API key in the app
3. (Optional) Customize translation style with a custom prompt
4. Upload your English `.srt` subtitle file
5. Click **Translate to Bengali**
6. Wait for translation to complete
7. Download the Bengali subtitle file

## 🔧 API Endpoints

### `POST /translate`
Translates subtitles with Server-Sent Events (SSE) for real-time progress.

**Request:**
```json
{
  "apiKey": "your-gemini-api-key",
  "subtitles": [
    {
      "index": "1",
      "timestamp": "00:00:01,000 --> 00:00:03,000",
      "text": "Hello world"
    }
  ],
  "customPrompt": "Translate to casual Bengali"
}
```

**Response (SSE):**
