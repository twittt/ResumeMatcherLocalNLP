# Resume Matcher with Local NLP

This project is a full-stack application that allows users to upload a resume and a job description, and receive a match score along with suggestions for improvement. The frontend is built with React, while the backend is implemented using Flask. The application performs cosine similarity analysis, tokenization, and custom NLP to provide the match score and suggestions.

## Project Structure

```
ResumeMatcherLocalNLP/
├── backend/
│   ├── app.py
│   ├── requirements.txt
└── frontend/
    ├── public/
    │   └── index.html
    ├── src/
    │   ├── App.css
    │   ├── App.js
    │   ├── index.js
    └── package.json
```

## Prerequisites

- Python 3.x
- Node.js
- npm (Node Package Manager)

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/twittt/ResumeMatcherLocalNLP.git
cd ResumeMatcherLocalNLP
```

### 2. Setup the Backend

#### a. Navigate to the Backend Directory

```sh
cd backend
```

#### b. Create a Virtual Environment

```sh
python -m venv venv
```

#### c. Activate the Virtual Environment

- Windows:
  ```sh
  venv\Scripts\activate
  ```
- macOS/Linux:
  ```sh
  source venv/bin/activate
  ```

#### d. Install the Requirements

```sh
pip install -r requirements.txt
```

#### e. Run the Flask App

```sh
python app.py
```

The Flask app will be running on `http://localhost:5000`.

### 3. Setup the Frontend

#### a. Navigate to the Frontend Directory

```sh
cd ../frontend
```

#### b. Install the Dependencies

```sh
npm install
```

#### c. Start the React App

```sh
npm start
```

The React app will be running on `http://localhost:3000`.

## Usage

1. Open your browser and navigate to `http://localhost:3000`.
2. Upload a resume file (`.pdf`, `.doc`, or `.docx`).
3. Paste the job description text.
4. Click on the "Match" button to get the match score and suggestions for improvement.
5. Use the "Reset" button to clear all uploads and text areas.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Make your changes and commit them: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature-branch`
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```` ▋