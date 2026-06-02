# Django Blog App

A full-featured blog application built with Django MVT architecture. Users can register, log in, write blog posts, manage categories, and interact via comments — all managed through a built-in dashboard.

🌐 **Live Demo:** [https://preshit17705.pythonanywhere.com](https://preshit17705.pythonanywhere.com)

---

## Features

- 📝 **Blog Posts** — Create, edit, and delete blog posts
- 🔐 **User Authentication** — Register and log in securely
- 💬 **Comments** — Add and delete comments on posts
- 🗂️ **Categories** — Organize posts by category
- 📊 **Dashboard** — Manage posts, categories, and users from one place

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 5.2 |
| Frontend | Bootstrap 5 |
| Database | SQLite |
| Hosting | PythonAnywhere |

---

## Project Structure

```
Blogapp/
├── manage.py
├── db.sqlite3
├── requirements.txt
│
├── blog_main/              # Project settings, root URLs, and static files
├── blogs/                  # Blog posts, categories, comments, and context processors
├── dashboard/              # Admin dashboard for managing posts, categories, and users
├── AutheticationApp/       # User registration and login
│
├── templates/              # All HTML templates
│   └── dashboard/          # Dashboard-specific templates
│
└── media/                  # User-uploaded files (blog images)
```

---

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/dev-preshit/Blog-app.git
   cd Blog-app
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. Open [http://localhost:8000](http://localhost:8000) in your browser.
