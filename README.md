# notif_ai_recruitment

    - my app is deployed on heroku https://notifyairecruitment.herokuapp.com/

## Local deployment

For ease of deployment use docker-compose

`docker-compose up`

App will start listening on localhost:8001
Postgres db will listen on localhost:55432

# API specs

https://notifyairecruitment.herokuapp.com/docs

## /register

/register endpoint accepts only PUT method needs username and password query params

Example:
`curl -X PUT 'localhost:8001/register?username=DaftAi&password=DaftAi' -D -`
https://notifyairecruitment.herokuapp.com/register?username=DaftAi&password=DaftAi
now this link will create new user if there isn't already one with the same username

### Response

HTTP/1.1 201 Created
date: Wed, 26 May 2021 01:32:13 GMT
server: uvicorn
content-length: 9
content-type: application/json

{"id":40}

## Registering with username already in db

### Response

HTTP/1.1 409 Conflict
date: Wed, 26 May 2021 01:33:42 GMT
server: uvicorn
content-length: 44
content-type: application/json

{"detail":"User already exists in Database"}

## /login

/login endpoint accepts only POST method and also needs username and password as query params
Example:
`curl -X POST 'localhost:8001/login?username=DaftAi&password=DaftAi' -D -`
https://notifyairecruitment.herokuapp.com/login?username=DaftAi&password=DaftAi
This will result in returing jwt as response as also setting access_token cookie

### Response

HTTP/1.1 200 OK
date: Wed, 26 May 2021 01:38:22 GMT
server: uvicorn
content-length: 302
content-type: application/json
set-cookie: access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZHVzZXIiOjM3LCJ1c2VybmFtZSI6IkRhZnRBaSIsImhhc2hlZHBhc3N3b3JkIjoiOTYwOTIzZGU5NWFiOWMzMDJhNTVmNmZkYjIyYWVjZWE5ZmUxNThhYmNhNTM0ZmVjNzgyOTdhM2QzNTE0NGI4YSIsInBhc3N3b3Jkc2FsdCI6IjNHRjREamVRNTV1UEtLbXYifQ.oWmBfGzKYmvok7vAoeoUhv7ygX0_YcykWJH\*-ZaejR4; Path=/; SameSite=lax

{"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZHVzZXIiOjM3LCJ1c2VybmFtZSI6IkRhZnRBaSIsImhhc2hlZHBhc3N3b3JkIjoiOTYwOTIzZGU5NWFiOWMzMDJhNTVmNmZkYjIyYWVjZWE5ZmUxNThhYmNhNTM0ZmVjNzgyOTdhM2QzNTE0NGI4YSIsInBhc3N3b3Jkc2FsdCI6IjNHRjREamVRNTV1UEtLbXYifQ.oWmBfGzKYmvok7vAoeoUhv7ygX0_YcykWJH\*-ZaejR4"}

##Wrong username or password
###Response
HTTP/1.1 406 Not Acceptable
date: Wed, 26 May 2021 01:41:00 GMT
server: uvicorn
content-length: 48
content-type: application/json

{"detail":"Supplied wrong username or password"}

## /logout

/logout endpoint accepts only POST method and will reset token if present
Example:
https://notifyairecruitment.herokuapp.com/logout
###Response with cookie present
HTTP/1.1 200 OK
date: Wed, 26 May 2021 01:47:45 GMT
server: uvicorn
content-length: 31
content-type: application/json
set-cookie: access_token=""; Path=/; SameSite=lax
set-cookie: access_token=""; expires=Wed, 26 May 2021 01:47:45 GMT; Max-Age=0; Path=/; SameSite=lax

{"detail":"Happily logged out"}%
###Response if cookie is not present
HTTP/1.1 204 No Content
date: Wed, 26 May 2021 01:45:17 GMT
server: uvicorn
content-length: 31
content-type: application/json

## /posts

/posts endpoint accepts only GET method and doesn't increase view counter
https://notifyairecruitment.herokuapp.com/posts

### Response

HTTP/1.1 200 OK
date: Wed, 26 May 2021 01:50:31 GMT
server: uvicorn
content-length: 518
content-type: application/json

[{"idpost":3,"viewscounter":11,"postcontent":"string","iduser":2},{"idpost":4,"viewscounter":1,"postcontent":"string","iduser":2},{"idpost":5,"viewscounter":0,"postcontent":"notifai","iduser":29},{"idpost":6,"viewscounter":0,"postcontent":"notifai","iduser":29},{"idpost":7,"viewscounter":1,"postcontent":"notifai","iduser":29},{"idpost":8,"viewscounter":0,"postcontent":"daft","iduser":29},{"idpost":9,"viewscounter":0,"postcontent":"daft","iduser":29},{"idpost":10,"viewscounter":0,"postcontent":"daft","iduser":29}]

## /post/{id} GET

/post endpoint accepts GET, PUT, PATCH and DELETE methods
https://notifyairecruitment.herokuapp.com/post/3

### Response if present

HTTP/1.1 200 OK
date: Wed, 26 May 2021 01:55:53 GMT
server: uvicorn
content-length: 42
content-type: application/json

{"postcontent":"string","viewscounter":12}

https://notifyairecruitment.herokuapp.com/post/4324321

### Response if missing

HTTP/1.1 404 Not Found
date: Wed, 26 May 2021 01:56:28 GMT
server: uvicorn
content-length: 30
content-type: application/json

{"detail":"No post was found"}

## /post PUT

These one inserts post into db and requires access\*token cookie and json message with postcontent key
accepts only values between 1 to 160 chars
https://notifyairecruitment.herokuapp.com/post

- curl -X PUT 'localhost:8001/post' -D - -H 'Cookie: access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZHVzZXIiOjM3LCJ1c2VybmFtZSI6IkRhZnRBaSIsImhhc2hlZHBhc3N3b3JkIjoiOTYwOTIzZGU5NWFiOWMzMDJhNTVmNmZkYjIyYWVjZWE5ZmUxNThhYmNhNTM0ZmVjNzgyOTdhM2QzNTE0NGI4YSIsInBhc3N3b3Jkc2FsdCI6IjNHRjREamVRNTV1UEtLbXYifQ.oWmBfGzKYmvok7vAoeoUhv7ygX0_YcykWJH\*-ZaejR4' -H 'Content-Type: application/json' -d '{"postcontent": "text"}'

### Valid request response

HTTP/1.1 201 Created
date: Wed, 26 May 2021 02:02:17 GMT
server: uvicorn
content-length: 13
content-type: application/json

{"idpost":20}

- curl -X PUT 'localhost:8001/post' -D - -H 'Cookie: access*token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZHVzZXIiOjM3LCJ1c2VybmFtZSI6IkRhZnRBaSIsImhhc2hlZHBhc3N3b3JkIjoiOTYwOTIzZGU5NWFiOWMzMDJhNTVmNmZkYjIyYWVjZWE5ZmUxNThhYmNhNTM0ZmVjNzgyOTdhM2QzNTE0NGI4YSIsInBhc3N3b3Jkc2FsdCI6IjNHRjREamVRNTV1UEtLbXYifQ.oWmBfGzKYmvok7vAoeoUhv7ygX0_YcykWJH*-ZaejR4' -H 'Content-Type: application/json' -d '{"postcontent": ""}'

### When request values isn't desired length

HTTP/1.1 400 Bad Request
date: Wed, 26 May 2021 02:06:20 GMT
server: uvicorn
content-length: 57
content-type: application/json

{"detail":"Post need to be between 1 and 160 chars long"}

- curl -X PUT 'localhost:8001/post' -D - -H 'Cookie: access*token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZHVzZXIiOjM3LCJ1c2VybmFtZSI6IkRhZnRBaSIsImhhc2hlZHBhc3N3b3JkIjoiOTYwOTIzZGU5NWFiOWMzMDJhNTVmNmZkYjIyYWVjZWE5ZmUxNThhYmNhNTM0ZmVjNzgyOTdhM2QzNTE0NGI4YSIsInBhc3N3b3Jkc2FsdCI6IjNHRjREamVRNTV1UEtLbXYifQ.oWmBfGzKYmvok7vAoeoUhv7ygX0_YcykWJH*-Zae4' -H 'Content-Type: application/json' -d '{"postcontent": "fdas"}'

### When unable to authorize

HTTP/1.1 401 Unauthorized
date: Wed, 26 May 2021 02:07:13 GMT
server: uvicorn
content-length: 51
content-type: application/json

{"detail":"You're not authorized or session ended"}

## /post/{id} PATCH

These one updates record in db but except cookie and json content it also needs id for the specified post

https://notifyairecruitment.herokuapp.com/post

- curl -X PATCH 'localhost:8001/post/20' -D - -H 'Cookie: access*token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZHVzZXIiOjM3LCJ1c2VybmFtZSI6IkRhZnRBaSIsImhhc2hlZHBhc3N3b3JkIjoiOTYwOTIzZGU5NWFiOWMzMDJhNTVmNmZkYjIyYWVjZWE5ZmUxNThhYmNhNTM0ZmVjNzgyOTdhM2QzNTE0NGI4YSIsInBhc3N3b3Jkc2FsdCI6IjNHRjREamVRNTV1UEtLbXYifQ.oWmBfGzKYmvok7vAoeoUhv7ygX0_YcykWJH*-ZaejR4' -H 'Content-Type: application/json' -d '{"postcontent": "t"}'

### Response when request is valid

HTTP/1.1 200 OK
date: Wed, 26 May 2021 02:20:37 GMT
server: uvicorn
content-length: 36
content-type: application/json

{"postcontent":"t","viewscounter":0}

- curl -X PATCH 'localhost:8001/post/3' -D - -H 'Cookie: access*token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZHVzZXIiOjM3LCJ1c2VybmFtZSI6IkRhZnRBaSIsImhhc2hlZHBhc3N3b3JkIjoiOTYwOTIzZGU5NWFiOWMzMDJhNTVmNmZkYjIyYWVjZWE5ZmUxNThhYmNhNTM0ZmVjNzgyOTdhM2QzNTE0NGI4YSIsInBhc3N3b3Jkc2FsdCI6IjNHRjREamVRNTV1UEtLbXYifQ.oWmBfGzKYmvok7vAoeoUhv7ygX0_YcykWJH*-ZaejR4' -H 'Content-Type: application/json' -d '{"postcontent": "t"}'

### Response when id of creator doesn't match with the id from access_token

HTTP/1.1 401 Unauthorized
date: Wed, 26 May 2021 02:21:37 GMT
server: uvicorn
content-length: 36
content-type: application/json

{"detail":"Cannot modify this post"}

- curl -X PATCH 'localhost:8001/post/9321' -D - -H 'Cookie: access*token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZHVzZXIiOjM3LCJ1c2VybmFtZSI6IkRhZnRBaSIsImhhc2hlZHBhc3N3b3JkIjoiOTYwOTIzZGU5NWFiOWMzMDJhNTVmNmZkYjIyYWVjZWE5ZmUxNThhYmNhNTM0ZmVjNzgyOTdhM2QzNTE0NGI4YSIsInBhc3N3b3Jkc2FsdCI6IjNHRjREamVRNTV1UEtLbXYifQ.oWmBfGzKYmvok7vAoeoUhv7ygX0_YcykWJH*-ZaejR4' -H 'Content-Type: application/json' -d '{"postcontent": "t"}'

### Response when there's no post with matching id

HTTP/1.1 404 Not Found
date: Wed, 26 May 2021 02:24:06 GMT
server: uvicorn
content-length: 36
content-type: application/json

{"detail":"This post doesn't exist"}

##/post{id} DELETE
this needs access_token and id of a post
When request is invalid the same responses as with PATCH method
https://notifyairecruitment.herokuapp.com/post

- curl -X DELETE 'localhost:8001/post/20' -D - -H 'Cookie: access*token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZHVzZXIiOjM3LCJ1c2VybmFtZSI6IkRhZnRBaSIsImhhc2hlZHBhc3N3b3JkIjoiOTYwOTIzZGU5NWFiOWMzMDJhNTVmNmZkYjIyYWVjZWE5ZmUxNThhYmNhNTM0ZmVjNzgyOTdhM2QzNTE0NGI4YSIsInBhc3N3b3Jkc2FsdCI6IjNHRjREamVRNTV1UEtLbXYifQ.oWmBfGzKYmvok7vAoeoUhv7ygX0_YcykWJH*-ZaejR4'

### Valid request response

HTTP/1.1 200 OK
date: Wed, 26 May 2021 02:27:09 GMT
server: uvicorn
content-length: 26
content-type: application/json

{"message":"post deleted"}
