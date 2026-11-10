# GoalGrid

A simple to-do and goal tracker built with Django. Each user signs up, logs in, and manages their own private list of goals.

## Features

- Sign up, log in and log out (Django's built-in authentication)
- Add goals with a title, description, due date and priority (low, medium, high)
- Edit, complete (and undo) or delete a goal
- Goal counter and progress bar ("3 of 5 goals completed")
- Goals sorted by urgency: unfinished first, earliest due date first
- Overdue goals are flagged
- Privacy: users can only see and change their own goals

## Tech stack

- Python 3
- Django
- SQLite (Django's default database)

## Getting started

1. Clone the repository and open the project folder:

   ```
   git clone https://github.com/Olaoluwatoni/GoalGrid.git
   cd GoalGrid
   ```

2. (Recommended) Create and activate a virtual environment:

   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install Django:

   ```
   python -m pip install django
   ```

   On Windows, if you see a time zone error, also run `python -m pip install tzdata`.

4. Create the database tables:

   ```
   python manage.py migrate
   ```

5. (Optional) Create an admin account to inspect data at `/admin/`:

   ```
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```
   python manage.py runserver
   ```

7. Open http://127.0.0.1:8000/ in your browser.

## Project structure

```
GoalGrid/        Project settings and the main URL configuration
tracker/         The app: models, views, forms, URLs and templates
  models.py      The Goal model
  views.py       Signup, goal list, add, edit, toggle and delete views
  forms.py       The goal form
  urls.py        URL routes for the app
  templates/     HTML templates (base layout, goals, login, signup)
manage.py        Django's command-line utility
```

## Notes

- This project is for learning and runs in development mode (`DEBUG = True`). Before deploying, move `SECRET_KEY` into an environment variable and set `DEBUG = False`.
- `db.sqlite3` is not committed, so each person who clones the project creates their own database with `migrate`.

## Roadmap

- Automated tests
- Streak tracking
- Reminders