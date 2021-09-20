# Review Flask 

Working MTV:
- Model
- Template
- Views

```bash
(venv) ➜ flask_project (main) ✗ tree
.
├── app
│   ├── __init__.py
│   ├── models
│   │   └── __init__.py
│   ├── templates
│   │   └── __init__.py
│   └── views
│       ├── cliente_view.py
│       ├── __init__.py
├── README.md
├── run.py
└── venv

```


# Migrations

Flask-Migrate is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic. The database operations are made available through the Flask command-line interface.

- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)

```bash
pip install Flask-Migrate

flask db init

flask db migrate

flask db upgrade
```
