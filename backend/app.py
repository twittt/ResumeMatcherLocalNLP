from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
import docx2txt
import PyPDF2
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

nltk.download('punkt_tab')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'resume' not in request.files or 'job_description' not in request.form:
        return jsonify({'error': 'No file part or job description'}), 400

    resume = request.files['resume']
    job_description = request.form['job_description']

    if resume.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if resume and allowed_file(resume.filename):
        filename = secure_filename(resume.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        resume.save(filepath)

        resume_text = extract_text_from_file(filepath)
        match_score, suggestions = analyze_resume(resume_text, job_description)

        return jsonify({'match_score': match_score, 'suggestions': suggestions})
    else:
        return jsonify({'error': 'File type not allowed'}), 400

def extract_text_from_file(filepath):
    text = ''
    if filepath.endswith('.pdf'):
        with open(filepath, 'rb') as file:
            reader = PyPDF2.PdfFileReader(file)
            for page_num in range(reader.numPages):
                text += reader.getPage(page_num).extract_text()
    elif filepath.endswith('.docx'):
        text = docx2txt.process(filepath)
    elif filepath.endswith('.doc'):
        text = docx2txt.process(filepath)
    return text

def analyze_resume(resume_text, job_description):
    vectorizer = TfidfVectorizer().fit_transform([resume_text, job_description])
    vectors = vectorizer.toarray()
    cosine_sim = cosine_similarity(vectors)
    match_score = cosine_sim[0][1]

    # Tokenize and provide suggestions for improvement
    resume_words = set(nltk.word_tokenize(resume_text.lower()))
    job_words = set(nltk.word_tokenize(job_description.lower()))
    missing_words = job_words - resume_words
    suggestions = list(missing_words)

    return match_score, suggestions

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)