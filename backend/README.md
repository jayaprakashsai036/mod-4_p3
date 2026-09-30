# Agentic SDC Project 3 - Python Backend

## 1. Create virtual environment

Windows PowerShell:

```powershell
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1
```

## 2. Install packages

```powershell
pip install -r requirements.txt
```

## 3. Start server

```powershell
python main.py
```

The API runs on:

`http://127.0.0.1:8000`

Swagger documentation:

`http://127.0.0.1:8000/docs`

## API

### GET /health

Checks whether the server is running.

### POST /chat

Example:

```json
{
  "session_id": "session_123",
  "message": "Hello"
}
```

The Android Emulator uses `10.0.2.2` to reach the host computer, so the Android app is configured for:

`http://10.0.2.2:8000/`
