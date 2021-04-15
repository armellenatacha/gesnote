release: python manage.py migrate
web: gunicorn gestionNoteProject.wsgi  --timeout 120 --log-file -