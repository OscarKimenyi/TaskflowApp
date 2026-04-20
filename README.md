# TaskFlow

A full-stack to-do list web application built with Python and Flask. TaskFlow lets users register, log in, and manage personal task lists with priorities, categories, due dates, and completion tracking — all through a polished dark-themed web interface.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Running the Application](#running-the-application)
- [Using the Application](#using-the-application)
- [Configuration Reference](#configuration-reference)
- [Database Models](#database-models)
- [Routes Reference](#routes-reference)
- [Troubleshooting](#troubleshooting)
- [Extending the Project](#extending-the-project)
- [Deployment Guide](#deployment-guide)

---

## Project Overview

TaskFlow is a full-stack web application designed as a practical, production-quality learning project that covers all the essential pillars of modern Python web development: routing, authentication, database modeling, form validation, CSRF protection, and responsive UI design.

The codebase is clean, well-structured, and intentionally kept simple so every part is easy to understand and extend. It uses Flask as the web framework, SQLAlchemy as the ORM, SQLite as the database, and Jinja2 for server-side HTML rendering — no JavaScript frameworks required.

---

## Features

### User Authentication
- Register a new account with username, email, and password
- Secure login with email and password
- Passwords hashed with Werkzeug (PBKDF2/SHA-256)
- Session management with Flask-Login
- CSRF protection on all forms via Flask-WTF
- Per-user task isolation — users only ever see their own tasks

### Task Management
- Create tasks with a title and optional description
- Set priority level: High, Medium, or Low
- Assign tasks to a custom category (e.g. Work, Personal, Shopping)
- Set a due date per task
- Toggle tasks complete/incomplete with an instant AJAX update (no page reload)
- Edit any task detail at any time
- Delete tasks with a confirmation prompt

### Dashboard & Filtering
- Stats bar showing total, pending, completed, and overdue task counts
- Progress bar showing overall completion percentage
- Live search by task title
- Filter by status: All / Active / Completed
- Filter by priority: All / High / Medium / Low
- Filter by category (populated dynamically from your own tasks)
- Sort by: Newest first, Due date, Priority, or A–Z

### Visual Design
- Dark theme with a refined indigo/slate color palette
- Overdue tasks highlighted with a red left border
- Priority badges color-coded: red (High), amber (Medium), green (Low)
- Flash messages that auto-dismiss after 4 seconds
- Fully responsive — works on mobile and desktop

### Feature Status

| Feature | Status |
|---|---|
| User Registration & Login | ✅ |
| Password Hashing (Werkzeug) | ✅ |
| CSRF Protection on all forms | ✅ |
| Task CRUD (Create, Read, Update, Delete) | ✅ |
| Priority Levels (High / Medium / Low) | ✅ |
| Categories / Tags | ✅ |
| Due Dates + Overdue Detection | ✅ |
| Toggle Complete via AJAX | ✅ |
| Search by Task Title | ✅ |
| Filter by Status, Priority, Category | ✅ |
| Sort by Date, Priority, Title, Due Date | ✅ |
| Progress Bar (% complete) | ✅ |
| Stats Bar (Total / Pending / Done / Overdue) | ✅ |
| Responsive Design (mobile-ready) | ✅ |
| Dark Theme | ✅ |

---

## Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| Backend | Flask 3.0 | Web framework and routing |
| ORM | Flask-SQLAlchemy 3.1 | Database models and queries |
| Database | SQLite | Lightweight file-based database |
| Migrations | Flask-Migrate | Database schema versioning |
| Auth | Flask-Login | Session-based user authentication |
| Forms | Flask-WTF + WTForms | Form rendering, validation, CSRF |
| Security | Werkzeug | Password hashing |
| Templating | Jinja2 | Server-side HTML rendering |
| Styling | Vanilla CSS | Custom design system |
| JavaScript | Vanilla JS | AJAX toggle, flash auto-dismiss |
| Config | python-dotenv | Environment variable management |
| Fonts | Google Fonts (Syne + DM Sans) | Typography |

---

## Project Structure

```
taskflow/
├── run.py                        ← Entry point
├── requirements.txt              ← Python dependencies
├── .env                          ← Environment variables (never commit this)
├── .env.example                  ← Template for .env
├── .gitignore
└── app/
    ├── __init__.py               ← App factory: Flask, DB, Auth, CSRF
    ├── models.py                 ← User & Task database models
    ├── forms.py                  ← WTForms: Register, Login, Task
    ├── routes/
    │   ├── __init__.py           ← Makes routes a Python package
    │   ├── auth.py               ← /auth/register, /auth/login, /auth/logout
    │   └── tasks.py              ← /, /dashboard, /tasks/...
    ├── static/
    │   ├── css/
    │   │   └── main.css          ← Full design system
    │   └── js/
    │       └── main.js           ← Flash auto-dismiss
    └── templates/
        ├── base.html             ← Navbar, flash messages, layout
        ├── index.html            ← Landing page
        ├── auth/
        │   ├── login.html
        │   └── register.html
        └── tasks/
            ├── dashboard.html    ← Task list, filters, search, stats
            └── task_form.html    ← Create / Edit form
```

---

## Prerequisites

Before setting up the project, make sure you have the following installed:

- **Python 3.10 or higher** — the core runtime
- **pip** — Python package manager (comes bundled with Python)
- **Git** — for version control (optional but recommended)
- **A code editor** — VS Code is recommended

Verify your Python version:

```bash
python3 --version
# Expected: Python 3.10.x or higher
```

> **Windows note:** You may need to use `python` instead of `python3`. Try both and use whichever works in your terminal.

---

## Installation & Setup

### Step 1 — Get the project files

Create a folder called `taskflow` on your machine and place all the project files inside it, maintaining the directory structure shown above.

### Step 2 — Open a terminal inside the project folder

```bash
# macOS / Linux
cd ~/Desktop/taskflow

# Windows (PowerShell)
cd C:\Users\YourName\Desktop\taskflow
```

### Step 3 — Create a virtual environment

A virtual environment isolates your project's Python packages from the rest of your system, preventing version conflicts between projects.

```bash
python3 -m venv venv
```

This creates a `venv/` folder inside your project. Never commit this folder to Git (it's already in `.gitignore`).

### Step 4 — Activate the virtual environment

You must activate it every time you open a new terminal to work on this project.

```bash
# macOS / Linux
source venv/bin/activate

# Windows (PowerShell)
venv\Scripts\activate

# Windows (Command Prompt)
venv\Scripts\activate.bat
```

Once activated, your prompt will show `(venv)` at the start. This confirms all pip commands now install into your virtual environment, not globally.

### Step 5 — Install all dependencies

```bash
pip install -r requirements.txt
```

This installs:

| Package | Version | Purpose |
|---|---|---|
| Flask | 3.0.3 | Web framework |
| Flask-SQLAlchemy | 3.1.1 | Database ORM |
| Flask-Login | 0.6.3 | User session management |
| Flask-WTF | 1.2.1 | Forms and CSRF protection |
| Flask-Migrate | 4.0.7 | Database migrations |
| WTForms | 3.1.2 | Form field definitions and validators |
| Werkzeug | 3.0.3 | Password hashing |
| python-dotenv | 1.0.1 | Loads .env config file |
| email-validator | 2.2.0 | Validates email fields in forms |

### Step 6 — Create your `.env` file

```bash
# macOS / Linux
cp .env.example .env

# Windows
copy .env.example .env
```

Open `.env` in your editor and set a strong `SECRET_KEY`. You can generate one with:

```bash
python3 -c "import secrets; print(secrets.token_hex(32))"
```

Your `.env` file should look like this:

```env
SECRET_KEY=3f2a1b9c8d7e6f5a4b3c2d1e0f9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1
DATABASE_URL=sqlite:///taskflow.db
FLASK_ENV=development
FLASK_DEBUG=1
```

> **Security:** Never commit your `.env` file to Git. It contains your secret key which signs session cookies. The `.gitignore` already excludes it. In production, use a long random key and set `FLASK_DEBUG=0`.

---

## Running the Application

With your virtual environment active, start the Flask development server:

```bash
python run.py
```

You should see output like this:

```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
```

Open your browser and go to **http://127.0.0.1:5000**

The SQLite database file (`taskflow.db`) is created automatically the first time you run the app — no extra database setup needed.

To stop the server, press `Ctrl + C` in your terminal.

> **Auto-reload:** Because `FLASK_DEBUG=1` is set, the server automatically reloads whenever you save changes to any Python file. Template and CSS changes take effect on the next browser refresh.

---

## Using the Application

### Register an account
1. Navigate to `http://127.0.0.1:5000`
2. Click **"Get started — it's free"** on the landing page
3. Fill in your username, email, and password (minimum 6 characters)
4. Click **"Create Account"** — you'll be redirected to the login page

### Sign in
1. Enter your email and password
2. Optionally check **"Keep me logged in"** for a persistent session
3. Click **"Sign In"** — you'll land on your dashboard

### Create a task
1. Click **"+ New Task"** in the top navigation bar
2. Enter a task title (required)
3. Optionally add a description, priority, category, and due date
4. Click **"Save Task"**

### Manage tasks
- **Complete a task:** Click the circle on the left of any task card to toggle it complete/incomplete
- **Edit a task:** Click the ✏️ pencil icon on the right of the task card
- **Delete a task:** Click the 🗑️ bin icon — a confirmation prompt appears before deletion

### Search, filter, and sort
- **Search:** Type in the search box to filter tasks by title
- **Status filter:** Click "All", "Active", or "Done"
- **Priority filter:** Use the priority dropdown
- **Category filter:** Use the category dropdown (populated from your own task categories)
- **Sort:** Use the sort dropdown to order by Newest, Due Date, Priority, or A–Z

---

## Configuration Reference

All configuration is managed via the `.env` file:

| Variable | Default | Description |
|---|---|---|
| `SECRET_KEY` | *(required)* | Signs session cookies and CSRF tokens. Must be long and random in production. |
| `DATABASE_URL` | `sqlite:///taskflow.db` | SQLAlchemy database URI. Change to a PostgreSQL URL for production. |
| `FLASK_ENV` | `development` | Set to `production` when deploying. |
| `FLASK_DEBUG` | `1` | Set to `0` in production to disable the debugger. |

---

## Database Models

### User (`users` table)

| Column | Type | Notes |
|---|---|---|
| `id` | INTEGER | Primary key |
| `username` | VARCHAR(80) | Unique |
| `email` | VARCHAR(120) | Unique |
| `password_hash` | VARCHAR(256) | Hashed by Werkzeug |
| `created_at` | DATETIME | Auto-set on creation |

**Methods:**
- `set_password(password)` — hashes and stores the password
- `check_password(password)` — verifies a plain-text password against the stored hash

### Task (`tasks` table)

| Column | Type | Notes |
|---|---|---|
| `id` | INTEGER | Primary key |
| `title` | VARCHAR(200) | Required |
| `description` | TEXT | Optional |
| `completed` | BOOLEAN | Default: `False` |
| `priority` | VARCHAR(10) | `'low'` / `'medium'` / `'high'` |
| `category` | VARCHAR(50) | Optional |
| `due_date` | DATE | Optional |
| `created_at` | DATETIME | Auto-set on creation |
| `updated_at` | DATETIME | Auto-updated on save |
| `user_id` | INTEGER | Foreign key → `users.id` |

**Methods:**
- `is_overdue()` — returns `True` if `due_date` is in the past and the task is not completed
- `to_dict()` — serializes the task to a dictionary (useful for building a JSON API later)

---

## Routes Reference

| Method | Route | Handler | Description |
|---|---|---|---|
| GET | `/` | `tasks.index` | Landing page (redirects to dashboard if logged in) |
| GET | `/dashboard` | `tasks.dashboard` | Main task list with filters, search, and stats |
| GET, POST | `/tasks/new` | `tasks.new_task` | Create new task form |
| GET, POST | `/tasks/<id>/edit` | `tasks.edit_task` | Edit existing task form |
| POST | `/tasks/<id>/toggle` | `tasks.toggle_task` | Toggle complete/incomplete (AJAX, CSRF-exempt) |
| POST | `/tasks/<id>/delete` | `tasks.delete_task` | Delete a task |
| GET, POST | `/auth/register` | `auth.register` | User registration form |
| GET, POST | `/auth/login` | `auth.login` | User login form |
| GET | `/auth/logout` | `auth.logout` | Log out and redirect to login |

---

## Troubleshooting

**`ModuleNotFoundError: No module named 'app.routes'`**

The `routes/` folder is missing its `__init__.py` file. Create it:

```bash
# Windows
echo. > app\routes\__init__.py

# macOS / Linux
touch app/routes/__init__.py
```

---

**`ModuleNotFoundError: No module named 'flask'`**

Your virtual environment is not activated. Run:

```bash
source venv/bin/activate     # macOS / Linux
venv\Scripts\activate        # Windows
```

---

**`csrf_token is undefined` (500 error)**

`CSRFProtect` is not initialized. Check that `app/__init__.py` contains:

```python
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect()
# and inside create_app():
csrf.init_app(app)
```

---

**`Address already in use`**

Port 5000 is occupied by another process. Run Flask on a different port:

```bash
flask run --port 5001
```

---

**Database file not created**

The `db.create_all()` call inside `create_app()` handles this automatically. If it still doesn't appear, check that `DATABASE_URL` is set correctly in your `.env` and that your working directory is the project root when you run `python run.py`.

---

## Extending the Project

TaskFlow is intentionally kept simple so it is easy to build on. Here are some suggested next steps:

**Beginner**
- Add a task count badge in the navbar
- Add a "Clear all completed tasks" bulk-delete button
- Add a character counter to the description textarea

**Intermediate**
- Add subtasks — a one-to-many relationship from `Task` to a `SubTask` model
- Export tasks to CSV using Python's built-in `csv` module
- Add pagination to the dashboard for users with many tasks
- Add a profile page where users can update their username or email
- Send due-date reminder emails using Flask-Mail and APScheduler

**Advanced**
- Swap SQLite for PostgreSQL by changing `DATABASE_URL` in `.env`
- Add real-time updates with Flask-SocketIO so changes sync across browser tabs
- Build a REST JSON API for each endpoint and connect a React frontend
- Add Google OAuth login using Flask-Dance
- Add shared task lists — allow users to invite collaborators
- Write a test suite using `pytest` and Flask's built-in test client

---

## Deployment Guide

The following steps describe how to deploy TaskFlow to a production Linux server (e.g. a DigitalOcean Droplet or AWS EC2 instance running Ubuntu).

### 1 — Prepare for production

Update your `.env`:

```env
SECRET_KEY=<long-random-key>
DATABASE_URL=postgresql://user:password@localhost/taskflow
FLASK_ENV=production
FLASK_DEBUG=0
```

### 2 — Install server dependencies

```bash
sudo apt update && sudo apt install python3 python3-pip python3-venv nginx -y
git clone https://github.com/yourname/taskflow.git
cd taskflow
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn
```

### 3 — Run with Gunicorn

```bash
gunicorn -w 4 -b 0.0.0.0:8000 "run:app"
```

### 4 — Configure Nginx as a reverse proxy

Create `/etc/nginx/sites-available/taskflow`:

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Enable it and restart Nginx:

```bash
sudo ln -s /etc/nginx/sites-available/taskflow /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl restart nginx
```

### 5 — Enable HTTPS with Let's Encrypt

```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d your-domain.com
```

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

*Built with ❤️ using Python & Flask*
