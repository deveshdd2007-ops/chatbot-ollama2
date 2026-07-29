# Deva Chat Bot

A simple Streamlit-based chatbot app powered by an Ollama-backed LLM. Ask a question in the web interface and get a response from the configured model.

## Features

- Streamlit UI for chat input and response display
- Uses `langchain` prompt chaining with an Ollama model
- Lightweight and easy to run locally

## Prerequisites

- Python 3.10+ (recommended)
- `streamlit`
- `langchain_community`
- `langchain_core`
- Ollama runtime configured locally and accessible

## Installation

1. Clone the repository or open the project folder.
2. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install the required packages:

```powershell
pip install streamlit langchain_community langchain_core
```

4. Make sure Ollama is installed and running locally.

## Running the app

Start the Streamlit app from the project root:

```powershell
streamlit run chatbot.py
```

Then open the local URL shown in the terminal.

## Project structure

- `chatbot.py` - main Streamlit app entrypoint

## Notes

- The app uses `ChatPromptTemplate` to format a simple system prompt and user query.
- The default model is `llama2` via Ollama. Change this in `chatbot.py` if needed.
- If the UI does not load, verify your virtual environment and package installation.

## License

This project does not include a license file. Add one if you want to share or reuse the code publicly.
