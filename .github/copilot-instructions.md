# Copilot Instructions for `langchain-course`

## Project Overview
- This is a minimal Python project for experimenting with LangChain and environment variable management.
- Main entry point: `main.py`.
- Uses `langchain`, `python-dotenv`, and expects an `OPENAI_API_KEY` in the environment.

## Architecture & Data Flow
- All logic currently resides in `main.py`.
- The app loads environment variables from a `.env` file using `python-dotenv`.
- Prints a greeting and the value of `OPENAI_API_KEY` (if set).
- No complex service boundaries or multi-file architecture yet.

## Developer Workflows
- **Run the app:**
  ```sh
  python main.py
  ```
- **Install dependencies:**
  ```sh
  pip install -r requirements.txt
  # or use pyproject.toml with a tool like 'uv' or 'pip'
  ```
- **Format code:**
  ```sh
  black .
  isort .
  ```
- **Environment setup:**
  - Place your API keys in a `.env` file at the project root.
  - Example:
    ```env
    OPENAI_API_KEY=sk-...
    ```

## Conventions & Patterns
- All environment variables are loaded at startup via `load_dotenv()`.
- Dependencies are managed in `pyproject.toml` (not requirements.txt).
- Formatting tools (`black`, `isort`) are included as dev dependencies.
- No custom test, build, or CI workflows are present yet.

## External Integrations
- Relies on `langchain` for LLM workflows (expand as project grows).
- Uses `python-dotenv` for environment management.
- No other integrations or cross-component communication yet.

## Key Files
- `main.py`: All logic and entry point.
- `pyproject.toml`: Dependency and project metadata.
- `.env`: Not checked in; used for secrets.

---

**If you add new files, services, or workflows, update this document to help future AI agents stay productive.**
