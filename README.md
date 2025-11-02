Django ToDo Practice App

A simple CRUD-based To-Do web app built using Django, designed to help understand how Django handles views, models, templates, and forms.

🚀 Features

✏️ Add new tasks

🔁 Edit existing tasks

🗑️ Delete tasks

✅ Mark tasks as done (if added)

📋 Display all todos in a clean UI

⚙️ Tech Stack

Backend: Django (Python)

Frontend: HTML, CSS, Bootstrap

Database: SQLite (default Django DB)

🧠 Concepts Learned

Django Models, Views, Templates (MVT)

CRUD operations in Django

Handling forms and POST requests

Template rendering and URL mapping

⚡ Setup Instructions

Clone this repository

git clone https://github.com/Jatin-2075/Django-ToDo-practice-App.git
cd Django-ToDo-practice-App


Create virtual environment & activate

python -m venv venv
# activate it:
# on Windows
venv\Scripts\activate
# on Mac/Linux
source venv/bin/activate


Install dependencies

pip install -r requirements.txt


Run migrations

python manage.py migrate


Start the development server

python manage.py runserver


Visit 👉 http://127.0.0.1:8000/