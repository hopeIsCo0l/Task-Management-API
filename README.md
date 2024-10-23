# Task Management API

This API enables effective task management through robust features that support creating, reading, updating, and deleting tasks, integrated with user authentication and authorization to ensure users only manage tasks they own.

## Features

- **CRUD Operations**: Manage tasks with full create, read, update, and delete capabilities.
- **User Authentication**: Secure registration and login processes.
- **Task Filtering and Sorting**: Advanced queries for task management.
- **Secure Access**: Utilizes JWT for secure API access.

## Technologies Used

- Django 5.1.2
- Django REST Framework 3.15.1
- Django Filter 21.1
- Django REST Framework SimpleJWT 5.3.1

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following installed:
- Python 3.12+
- pip 24.2+
- virtualenv (recommended)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/hopeIsCo0l/Task-Management-API.git
   cd Task-Management-API
Setup a virtual environment (recommended):

bash
Copy code
```python -m venv venv```
```source venv/bin/activate  # On Windows use `venv\Scripts\activate```
Install the required packages:

bash
Copy code
```pip install -r requirements.txt```
Run migrations to create the database schema:

bash
Copy code
```python manage.py migrate```
(Optional) Create a superuser for the Django admin interface:

bash
Copy code
```python manage.py createsuperuser```
Start the development server:

bash
Copy code
```python manage.py runserver```
Access the API at: http://127.0.0.1:8000/api/

Testing
Run the following command to execute tests:

bash
Copy code
```python manage.py test```

Deployment
Heroku
Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

Versioning

Authors
Abdellah Teshome - Initial work - hopeIsCo0l
License
This project is licensed under-

Acknowledgments
ALX
