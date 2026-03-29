# Patient Management App

## Overview

This repository contains a full-stack patient management application:
- `patient-project/patient-backend`: Django REST API
- `patient-project/patient-frontend`: React client

## Quick Start

### 1. Backend setup

```powershell
cd "C:\New folder\patient-project\patient-backend"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

- API should be available at `http://127.0.0.1:8000/`

### 2. Frontend setup

```powershell
cd "C:\New folder\patient-project\patient-frontend"
npm install
npm start
```

- Frontend should run at `http://localhost:3000/`

### 3. Testing

- Backend: `python manage.py test`
- Frontend: `npm test`

## Project structure

- `patient-backend/`: Django project and app(s)
- `patient-frontend/`: React app

## Notes for reviewers

- Remove generated `__pycache__`, `db.sqlite3` and frontend build artifacts from commit unless intentionally shared.
- Confirm `requirements.txt` and `package.json` match the intended dependency versions.

## GitHub push

```powershell
cd "C:\New folder"
git add .
git commit -m "chore: initial sync + add README for teammate setup"
git push origin main
```

