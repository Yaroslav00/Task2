from python:3
workdir /app

copy . .
run pip install --no-cache-dir -r requirements.txt

cmd uwsgi --ini worker2.ini
