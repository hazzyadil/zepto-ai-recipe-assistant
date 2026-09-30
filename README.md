# zepto-ai-recipe-assistant

## How to Run Locally

### 1. Enter the project folder

```bash
cd zepto-ai-recipe-assistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**macOS/Linux:**

```bash
source .venv/bin/activate
```

**Windows:**

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create and configure `.env`

Create a file named `.env` in the project folder and add:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Replace `your_groq_api_key_here` with your actual Groq API key.

### 6. Run the Streamlit app

```bash
streamlit run app.py
```

The app should open in your browser at the local Streamlit URL.
