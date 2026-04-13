<div align="center">

# Smart Task API

### Intelligent task management API powered by Python & FastAPI

A smart backend system that goes beyond CRUD, it analyzes tasks, estimates priority, and suggests focus time using simple intelligence rules.

---

<img src="https://img.shields.io/badge/FastAPI-0.110+-00C7B7?style=for-the-badge&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Type-Backend%20API-blue?style=for-the-badge"/>

</div>

---

# Overview

**Smart Task API** is an intelligent task management system built with **FastAPI**.  
Instead of just storing tasks, it **analyzes and enriches them** with smart metadata such as:

- Priority scoring
- Suggested focus time
- Task classification
- Productivity insights (rule-based logic)

This project simulates the backend of a **modern productivity SaaS platform**.

---

# Key Features

## Core Functionality
- Create tasks
- Read tasks
- Update tasks
- Delete tasks

## Smart Intelligence Layer
- Automatic priority classification
- Suggested execution time
- Task complexity estimation (rule-based)
- Productivity hints based on input

---

# Example Response

```json
{
  "task": "Study FastAPI for 2 hours",
  "priority": "high",
  "complexity": "medium",
  "suggested_focus_time": "2h deep work session",
  "reason": "learning task with medium complexity and long duration"
}
```

## Tech Stack
- Python 
- FastAPI
- Pydantic
- Uvicorn
- SQLite (or PostgreSQL optional)

---

### Project Structure

```bash:
smart-task-api/
├── app/
│   ├── main.py
│   ├── models/
│   ├── schemas/
│   ├── routes/
│   ├── services/
│   └── core/
├── tests/
├── requirements.txt
└── README.md
```

### Installation & Setup

```
1. Clone repository

git clone https://github.com/your-username/smart-task-api.git

cd smart-task-api

2. Create virtual environment

python -m venv venv

source venv/bin/activate  # Linux/Mac

venv\Scripts\activate     # Windows

3. Install dependencies

pip install -r requirements.txt

4. Run server

uvicorn app.main:app --reload
```

---

## API Endpoints

- Create Task
POST /tasks
- Get All Tasks
GET /tasks
- Update Task
PUT /tasks/{id}
- Delete Task
DELETE /tasks/{id}

---

## Smart Logic Concept
The intelligence layer uses simple rules such as:

- Long description → higher complexity
- Words like "study", "learn" → high priority
- Short urgent tasks → immediate focus suggestion

This simulates how real productivity AI systems structure tasks.

---

## Project Goals

This project was built to demonstrate:

- Clean API architecture
- Backend engineering skills
- Basic AI-like logic implementation
- Scalable project structure
- Production-style documentation

---

### Future Improvements
- Machine Learning-based priority prediction
- User authentication (JWT)
- PostgreSQL integration
- Task analytics dashboard
- Daily productivity scoring system

---

### Author

Developed by Giovanna

- If you like this project

Give it a ⭐ on GitHub and follow for more projects like this.
