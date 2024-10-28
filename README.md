# RestApi_AichatSystem

# Building REST APIs for an AI Chat System
Develop REST APIs using Django for an AI chat system. The system allows users to register, login, and interact with an AI-powered chatbot. The chatbot provides responses to user queries and deducts tokens from the user's account for each question asked.

## Requirements
- Django (version 4.2.7)
- Python (version 3.10)

## Project Setup


- python -m django startproject project_name
- python manage.py startapp app_name

## Documentation

- After setting up the project, make sure to include the app_name, rest_framework in the INSTALLED_APPS list in the project's settings.py file.
- Then, connect the project's main URLs to the URLs of the app by including the app's URLs in the project's main URLs configuration.

## Database setup
In app.models create the models User, Chat with given required fields and make sure to register these models in corresponding admin.py file.

Then run migrations in terminal

- Python manage.py makemigrations
- python manage.py migrate
  
This migrations will make ensure that models have been updated at admin site.

## Run Server

Run server -  python manage.py runserver

## How to register 
- Use POST method
- POST    : http://127.0.0.1:8000/register/
Example : In body 
{
    "username":"user",
    "password":"pass123"
}
Now try to Post the data then user receive registration successfull with status code 201 Created.
![Screenshot 2024-10-28 214210](https://github.com/user-attachments/assets/3d8cbb9d-8aad-46b5-a7e7-171cecf35b15)


## Login
- Use POST method
- POST    : http://127.0.0.1:8000/login/
Example : In body 
{
    "username":"user",
    "password":"pass123"
}
Now try to Post the data then user receive token of length 32 with status 200
![Screenshot 2024-10-28 214622](https://github.com/user-attachments/assets/1d06edbb-1811-497e-91d8-00e3257e2641)

## Login
- Use POST method
- POST    : http://127.0.0.1:8000/chat/
Example : In body 
{
    "message":"code hello world in python"
}
Now provide the authentication token in headers and give message in body section and in response Chat Ai respond with relevant information. And user is deducted with 100 tokens.
![Screenshot 2024-10-28 214836](https://github.com/user-attachments/assets/ac1f4077-a063-4489-9f9b-ed3b351122e4)
![Screenshot 2024-10-28 214911](https://github.com/user-attachments/assets/92d6dbea-be77-4a91-b5c2-fb6b06a30b8b)

## Balance of token
- Use POST method
- POST    : http://127.0.0.1:8000/balance/
User receive token balance with status code 200, for each response from chatAi get deducted with 100 tokens. If balance of token is less than 100 then user get response from server with out of tokens.
![Screenshot 2024-10-28 215519](https://github.com/user-attachments/assets/2f3efbfc-7d6d-4e87-9c54-03b31fa2caeb)

## Run Server

Run server -  python manage.py runserver

## Tech Stack

**Python, Django Rest Framework, Sqlite**














