## How to Run Locally

### 1. Clone the repo and enter the folder

```bash
git clone https://github.com/hazzyadil/zepto-ai-recipe-assistant.git
cd zepto-ai-recipe-assistant
```

### 2. Create a virtual environment

macOS/Linux:

```bash
python3 -m venv .venv
```

Windows:

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

Your terminal prompt should now start with `(.venv)`.

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Add your API key

Create a file named `.env` in the project folder containing:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Replace the placeholder with your real key. Never commit this file.

### 6. Run the app

```bash
streamlit run app.py
```

The app opens in your browser at http://localhost:8501.

## Troubleshooting

- **`python: command not found`:** use `python3` (macOS/Linux).
- **`streamlit: command not found`:** activate the venv (step 3) and retry.
- **API key error:** check that `.env` is in the project root and the key has no quotes or spaces.

