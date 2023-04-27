
# Start-Project 
## Commands: 
1. -> git clone https://github.com/pyth0nd3v/ads-system.git
2. open the project and create "Virtual Environment": -> python3 -m venv ads-env
3. start the virtual environment: -> source ads-env/bin/activate
4. -> python3 manage.py runserver
5. -> python3 manage.py makemigrations
6. -> python3 manage.py migrate
7. -> python3 manage.py createsuperuser
### Open new terminal (Terminal Number 2) and Now RUN the Redis server
8. -> redis-server --port 6379
### Open new terminal (Terminal Number 3) and Now RUN the CELERY
9. -> python -m celery -A core worker

In this moment your project running total 3 terminals (Django Project + Redis server + Celery )

### - I used Celery distributed task queue, which help this program to work smoothly in the background without stucking on one task.
### - POSTMAN File is also attached in this project FILE_NAME: "Ads-Postman"
