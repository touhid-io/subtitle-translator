<h1 align="center">🎬 Subtitle Translator – English → Bengali</h1> <p align="center"><strong>AI-Powered Language Bridge Built on Google Gemini 2.5</strong></p> <p align="center">A next-gen translation system that converts English SRT subtitle files into natural, context-aware Bengali using <strong>Gemini Flash</strong>.</p> 

---

## 🌟 Overview

**Subtitle Translator** is a sophisticated localization tool designed for Bengali-speaking movie enthusiasts and content creators. It leverages Google's cutting-edge Gemini 2.5 Flash AI to deliver context-aware, culturally nuanced translations that preserve the essence of cinematic dialogue.

Unlike basic word-for-word translators, this system understands:
- Emotional context and tone
- Cultural references and idioms  
- Conversational flow and timing
- Character voice consistency

### Why This Matters

Bengali is one of the world's most spoken languages, yet quality localized content remains scarce. This tool democratizes access to global cinema by making professional-grade translation available to everyone.

---

## ✨ Key Features

### 🧠 Intelligent Translation
- **Gemini 2.5 Flash Integration** – Leverages state-of-the-art language models for human-quality output
- **Context Preservation** – Maintains narrative flow across subtitle sequences
- **Dialect Customization** – Choose between formal literary Bengali or colloquial conversational style
- **Tone Adaptation** – Adjusts translation based on genre (drama, comedy, thriller)

### ⚡ Performance & Workflow
- **Batch Processing** – Handles large SRT files with hundreds of entries
- **Real-Time Progress** – Live streaming updates via Server-Sent Events (SSE)
- **Instant Download** – One-click export of translated `.srt` files
- **Error Recovery** – Graceful handling of API limits and network issues

### 🎨 User Experience
- **Glassmorphism Design** – Modern frosted-glass aesthetic with animated gradients
- **Drag & Drop Upload** – Intuitive file handling
- **Mobile Responsive** – Works seamlessly across devices
- **Zero Configuration** – Just add your API key and start translating

---

## 🖼️ Interface Preview 

### 📸 Screenshot 

![Screenshot](https://res.cloudinary.com/drphgjcmk/image/upload/v1760973255/Screenshot_2025-10-20_205816_xazlko.png) 

### 🌐 Preview Link 
**[➡️ Click Here to View Live Project](https://subtitle-translator-kappa.vercel.app/)** 

---

## 🏗️ Architecture

```
┌─────────────────┐      ┌──────────────────┐      ┌─────────────────┐
│   Frontend      │─────▶│  Flask Backend   │─────▶│  Gemini API     │
│  (Vanilla JS)   │◀─────│  (Python/SSE)    │◀─────│  (Translation)  │
└─────────────────┘      └──────────────────┘      └─────────────────┘
     │                            │
     │                            ▼
     │                   ┌──────────────────┐
     └──────────────────▶│  SRT Parser      │
                         │  (Subtitle Logic)│
                         └──────────────────┘
```

**Tech Stack:**
- **Backend:** Flask (Python), Google Generative AI SDK
- **Frontend:** HTML5, CSS3 (Custom Animations), Vanilla JavaScript
- **Communication:** SSE (Server-Sent Events) for real-time updates
- **Deployment:** Vercel (Frontend), Python-compatible hosting (Backend)

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.9+** installed on your system
- **Gemini API Key** from [Google AI Studio](https://aistudio.google.com/app/apikey) (free tier available)
- Modern web browser (Chrome, Firefox, Edge, Brave)

### Installation

#### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/subtitle-translator-gemini.git
cd subtitle-translator-gemini
```

#### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

**Required packages:**
```
flask
flask-cors
google-generativeai
python-dotenv
```

#### 3️⃣ Configure Environment
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_api_key_here
FLASK_ENV=development
```

#### 4️⃣ Run the Backend
```bash
python backend.py
```
The server will start at `http://localhost:5000`

#### 5️⃣ Launch the Frontend
Open `index.html` in your browser, or use a local server:
```bash
# Using Python's built-in server
python -m http.server 8000
# Then visit http://localhost:8000
```

---

## 📖 Usage Guide

### Basic Workflow

1. **Upload SRT File**  
   Drag and drop your English subtitle file or click to browse

2. **Enter API Key**  
   Paste your Gemini API key (stored locally, never sent to external servers)

3. **Customize Translation** (Optional)  
   - Select tone: Formal, Casual, or Neutral
   - Choose dialect: Literary Bengali or Conversational

4. **Translate**  
   Click "Start Translation" and watch real-time progress

5. **Download**  
   Once complete, download your translated `.srt` file

### Advanced Options

**Custom Prompts:**  
Modify the translation prompt in `backend.py` to fine-tune output:
```python
prompt = f"""
Translate this English subtitle to Bengali.
Style: {custom_style}
Context: {genre}
Preserve timing codes and formatting.
"""
```

**Batch Processing:**  
For multiple files, modify the upload endpoint to accept arrays:
```python
@app.route('/batch-translate', methods=['POST'])
def batch_translate():
    files = request.files.getlist('files[]')
    # Process each file
```

---

## 🎯 Use Cases

- **Movie Fans:** Enjoy international films in native Bengali
- **Content Creators:** Localize YouTube videos and web series
- **Educators:** Translate educational content for Bengali-speaking students
- **Streaming Platforms:** Build localization pipelines for regional markets
- **Subtitle Communities:** Accelerate fansubbing projects

---

<p align="center">
  <strong>Made for the Bengali-speaking community</strong><br/>
  <em>Bridging languages, connecting cultures</em>
</p>

<p align="center">
  <sub>Star this repo if you find it useful! ⭐</sub>
</p>
