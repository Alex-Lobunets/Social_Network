- create virtual environment `python3 -m venv venv`
- build project from docker-compose `make build`
- migrate db: `make migrate`
- run server: `make server`



- User signup: 

`curl --location --request POST 'http://127.0.0.1:8006/api/v1/users/register/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "<your username>",
    "password": "<your password>"
}'`

- Get access token: 

`curl --location --request POST 'http://127.0.0.1:8006/api/token/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "<your username>",
    "password": "<your password>"
}'`

- Get all users:

`curl --location --request GET 'http://127.0.0.1:8006/api/v1/users' \
--header 'Authorization: Bearer <access token>'`


- Get all posts:


`curl --location --request GET 'http://127.0.0.1:8006/api/v1/posts/' \
--header 'Authorization: Bearer <access token>'`

- Create post:

`curl --location --request POST 'http://127.0.0.1:8006/api/v1/posts/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <access token>' \
--data-raw '{
    "title": "<title of post>",
    "body": "<body of post>"
}'`

- Like post:

`curl --location --request POST 'http://127.0.0.1:8006/api/v1/posts/<post_id>/post-like/' \
--header 'Authorization: Bearer <access token>'`

- Unlike post:

`curl --location --request DELETE 'http://127.0.0.1:8006/api/v1/posts/<post_id>/post-unlike/' \
--header 'Authorization: Bearer <access token>'`

- Example of data analytics url:
date format YYYY-MM-DD

`curl --location --request GET 'http://127.0.0.1:8006/api/v1/analytics/?date_from=<date from>=&date_to=<date to>' \
--header 'Authorization: Bearer <access token>'`


- Get user's activity:

`curl --location --request GET 'http://127.0.0.1:8006/api/v1/users/<user_id>/user-activity/' \
--header 'Authorization: Bearer <access token>'`

Bot usage:
- have local server running
- input integers into rules.cfg
- run command `python3 bot.py`
  - for another use of bot clean database by `make flush`