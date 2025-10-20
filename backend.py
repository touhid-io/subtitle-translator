from flask import Flask, request, jsonify, Response, stream_with_context
from flask_cors import CORS
import google.generativeai as genai
import json
import os

app = Flask(__name__)
CORS(app)

@app.route('/translate', methods=['POST'])
def translate():
    # Get data OUTSIDE the generator
    data = request.get_json()
    api_key = data.get('apiKey')
    subtitles = data.get('subtitles')
    custom_prompt = data.get('customPrompt', 'Translate to natural Bengali.')
    
    if not api_key:
        return jsonify({'error': 'API key required'}), 400
    
    if not subtitles:
        return jsonify({'error': 'Subtitles required'}), 400
    
    @stream_with_context
    def generate():
        try:
            # Configure Gemini
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-2.0-flash-exp')
            
            # Process in batches
            batch_size = 20
            translated_subtitles = []
            total_batches = (len(subtitles) + batch_size - 1) // batch_size
            
            for batch_idx, i in enumerate(range(0, len(subtitles), batch_size), 1):
                batch = subtitles[i:i + batch_size]
                texts_to_translate = [sub['text'] for sub in batch]
                
                # Send progress update
                progress = int((batch_idx / total_batches) * 100)
                yield f"data: {json.dumps({'progress': progress, 'message': f'Translating batch {batch_idx}/{total_batches}...'})}\n\n"
                
                prompt = f"""{custom_prompt}

Translate the following English subtitles to Bengali. Return ONLY a JSON array with the translations in the same order. Each element should be the Bengali translation as a string.

English subtitles:
{json.dumps(texts_to_translate, ensure_ascii=False, indent=2)}

IMPORTANT: Return ONLY a valid JSON array like ["translation1", "translation2", ...]. Do not include any explanation or markdown formatting."""
                
                # Call Gemini API
                try:
                    response = model.generate_content(prompt)
                    response_text = response.text.strip()
                except Exception as e:
                    yield f"data: {json.dumps({'error': f'Gemini API error: {str(e)}'})}\n\n"
                    return
                
                # Extract JSON from response
                try:
                    # Remove markdown code blocks if present
                    if response_text.startswith('```'):
                        response_text = response_text.split('```')[1]
                        if response_text.startswith('json'):
                            response_text = response_text[4:]
                        response_text = response_text.strip()
                    
                    translations = json.loads(response_text)
                    
                    # Validate it's a list
                    if not isinstance(translations, list):
                        raise ValueError("Response is not a list")
                    
                except Exception as e:
                    yield f"data: {json.dumps({'error': f'Failed to parse translation: {str(e)}'})}\n\n"
                    return
                
                # Combine with original subtitle data
                for idx, subtitle in enumerate(batch):
                    translated_subtitles.append({
                        'index': subtitle['index'],
                        'timestamp': subtitle['timestamp'],
                        'text': translations[idx] if idx < len(translations) else subtitle['text']
                    })
            
            # Send final result
            yield f"data: {json.dumps({'progress': 100, 'message': 'Complete!', 'translatedSubtitles': translated_subtitles})}\n\n"
        
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"
    
    return Response(generate(), mimetype='text/event-stream')

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'running'})

if __name__ == '__main__':
    print("=" * 50)
    print("🎬 Subtitle Translator Backend Server")
    print("=" * 50)
    print("✅ Server running on: http://localhost:5000")
    print("📂 Open frontend.html in your browser")
    print("🔑 Get Gemini API key: https://aistudio.google.com/app/apikey")
    print("=" * 50)
    app.run(debug=True, port=5000)
