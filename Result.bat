cd /d C:/Users/hp/Desktop/Result_Project
call .venv\Scripts\activate
cd Result
start cmd /k "python manage.py runserver"
timeout /t 10 /nobreak >nul
start "" "http://127.0.0.1:8000"


