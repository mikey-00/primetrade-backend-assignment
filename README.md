# Primetrade Backend Developer Assignment

## Overview

This project is a scalable REST API built using FastAPI with JWT Authentication and Role-Based Access Control (RBAC). A simple frontend is included to demonstrate API functionality.

## Features

### Authentication

* User Registration
* User Login
* Password Hashing using Passlib
* JWT Authentication

### Authorization

* Role-Based Access Control (Admin/User)
* Protected Routes
* Admin Dashboard Endpoint

### Task Management

* Create Task
* View Tasks
* Update Task
* Delete Task

### Frontend

* User Registration UI
* User Login UI
* Task Dashboard
* Create and View Tasks
* Delete Tasks

## Tech Stack

### Backend

* FastAPI
* SQLAlchemy
* SQLite
* JWT (python-jose)
* Passlib

### Frontend

* HTML
* CSS
* JavaScript

## API Endpoints

### Authentication

* POST /api/v1/auth/register
* POST /api/v1/auth/login

### Tasks

* POST /api/v1/tasks/
* GET /api/v1/tasks/
* PUT /api/v1/tasks/{task_id}
* DELETE /api/v1/tasks/{task_id}

### Admin

* GET /api/v1/admin/dashboard

## Installation

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## API Documentation

Swagger UI:

```text
http://localhost:8000/docs
```
## Project Structure

```text
backend/
├── app/
│   ├── routes/
│   ├── auth.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── main.py

frontend/
├── index.html
├── dashboard.html
├── script.js
└── style.css
```

## Scalability

Please refer to SCALABILITY.md for future scaling considerations including PostgreSQL migration, Redis caching, Docker deployment, load balancing, and microservices architecture.



## Author

Manan Makhija