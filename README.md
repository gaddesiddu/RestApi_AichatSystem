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


