# Data Entry System

A dynamic web application built with Django and MySQL that allows users to create, view, edit, and delete personal and professional information entries.

## Features

- User-friendly interface with Bootstrap styling
- CRUD operations for personal information entries
- Form validation
- Responsive design

## Requirements

- Python 3.8+
- Django 5.0+
- MySQL 8.0+
- mysqlclient

## Installation and Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/data-entry-system.git
   cd data-entry-system
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure your MySQL database:
   - Create a MySQL database named `data_entry_db`
   - Update the database credentials in `data_entry_project/settings.py` if needed

4. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser (admin):
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Access the application:
   - Main application: http://127.0.0.1:8000/
   - Admin interface: http://127.0.0.1:8000/admin/

## Project Structure

- `data_entry_project/` - Main project directory
- `entry_app/` - Application directory
  - `models.py` - Data models
  - `forms.py` - Form definitions
  - `views.py` - View functions and classes
  - `urls.py` - URL routing
  - `templates/` - HTML templates
  - `admin.py` - Admin site configuration

## Data Model

The main model `PersonalInfo` stores the following information:
- Name
- Profession
- Area
- City
- State
- Creation and update timestamps 