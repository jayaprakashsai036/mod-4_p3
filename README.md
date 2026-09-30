# Agentic SDC Project 3

Complete Android Studio + Python FastAPI project.

## Android structure

- `app/src/main/java/com/example/mod4_p3/`
- `app/src/main/res/layout/`
- `app/src/main/res/values/`
- `app/src/main/res/values-night/`
- `app/src/main/res/xml/`
- `app/src/main/AndroidManifest.xml`
- `app/proguard-rules.pro`

## Python structure

- `backend/app/api/`
- `backend/app/core/`
- `backend/app/models/`
- `backend/app/services/`
- `backend/data/`
- `backend/tests/`

## Run Python backend

```powershell
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

Then run the Android app in Android Studio.

For the Android Emulator, the backend URL is:
`http://10.0.2.2:8000/`
