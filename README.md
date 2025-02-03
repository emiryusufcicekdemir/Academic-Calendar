# Academic-Calendar
Academic Calendar Web Application

This is a web application built with Django that allows users to view an academic calendar. The application includes an admin panel where CRUD (Create, Read, Update, Delete) operations can be performed on calendar events.

Features

View academic calendar events

Admin panel for managing events

CRUD operations on events (Create, Read, Update, Delete)

User-friendly interface

Technologies Used

Python

Django

SQLite

HTML/CSS

Installation

Clone the repository

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Apply migrations:

python manage.py migrate

Run the development server:

python manage.py runserver

Access the application:

Academic Calendar: http://127.0.0.1:8000/

Admin Panel: http://127.0.0.1:8000/admin/
