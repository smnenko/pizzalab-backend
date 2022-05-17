# Pizzalab backend

### Stack of technologies
- Python 3.10
- SQLite 3

### Installation
1. Install python (skip if installed)
    1. Go to https://www.python.org/downloads/ and download the latest version (3.10.4)
    2. Install downloaded package
    

2. Configure virtual environment
    1. Run cmd (Win + R and pass "cmd")
    2. Pass ```python -m venv venv``` and press Enter
    3. Activate virtual environment
        - ```. .\venv\Scripts\activate``` for Windows
        - ```source venv/bin/activate``` for Linux
    4. !!! DO NOT CLOSE IT !!!
    

3. Install required packages
    1. Pass ```pip install -r requirements.txt``` and press Enter
    

4. Configure environment variables
    1. Run:
        - ```copy .env.template .env``` for Windows
        - ```cp .env.template .env``` for Linux
    
    2. Open ```.env``` file and fill all fields according to the next information
        ```
        SECRET_KEY - any secret phrase without spaces like verovberb345349be#$@vrnebo
      
        DEBUG - 0 or 1 (just set 1)
      
        ALLOWED_HOSTS - 127.0.0.1 localhost
      
        CORS_ALLOWED_ORIGINS - YOUR APPLICATION URL (http://localhost:3000 for React)
      
        DATABASE_NAME - fill just db.sqlite3
        ```
       
5. Apply database migrations ```python manage.py migrate```
6. Create superuser ```python manage.py createsuperuser```
       
### Running
1. Activate the virtual environment (if it's not activated) - see `Installation -> 2 -> iii`
2. Run application ```python manage.py runserver```

### Useful endpoints
- Admin Panel - http://localhost:8000/admin/
- Docs - http://localhost:8000/docs/