### Quiz API
* An API built with django rest framework 
- Comes with questions and answers
- It has 3 endpoints serving get all, random Quiz and Quiz Question based on a topic
- It comes with token authentication and permission classes
- Rate limiting for Anon and Auth users

- Endpoints
NAME                     | URI
:------------------------|:----------------------------------:|
-----------------------------------------------------------------------------
* All quiz category      | /quiz
* Random quiz category   | /random/category_name
* Category questions     | /q/category_name
