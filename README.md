# assignment

To run the project smoothly, run the following command
```
pip install -r requirements.txt
```
Follow the following process:
```
1. In settings.py, set Database credentials.
2. RUN python manage.py makemigrations
3. RUN python manage.py migrate
4. RUN python manage.py runserver
```


Curl for POST method
```
curl --location --request POST 'http://127.0.0.1:8000/chatlogs/?user_id=abcd' \
--header 'Content-Type: application/json' \
--data-raw '{
    "message": "Second message",
    "isSent": false,
    "timestamp": 1652371784
}'
```

Curl for GET method
```
curl --location --request GET 'http://127.0.0.1:8000/chatlogs/?limit=10&user_id=abcd'
```

Curl for DELETE method
```
curl --location --request DELETE 'http://127.0.0.1:8000/chatlogs/?user_id=abcde&message_id=4'
```
