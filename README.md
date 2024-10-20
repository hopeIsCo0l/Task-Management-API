# Task-Management-API
Task Management API built with Django REST Framework, supporting CRUD operations, user authentication via JWT, and advanced features like task filtering and sorting. Perfect for developers looking to streamline task handling in any project.

# Task Management API

This Task Management API is designed to help developers integrate task tracking functionalities into their applications efficiently. Built with Django REST Framework, it supports complete CRUD operations, user authentication, and advanced filtering and sorting mechanisms.

## Features

- **CRUD Operations:** Create, Read, Update, and Delete tasks.
- **Authentication:** Secure token-based authentication using JWT (JSON Web Tokens).
- **Task Filters and Sorting:** Enhanced searchability through filters and sorting by due date, priority, or status.
- **User Management:** Manage user accounts with unique username, email, and password.
- **Secure Access:** Users can only access and manage their tasks.

## Getting Started

### Prerequisites

- Python 3.8+
- Django 3.1+
- Django REST Framework

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/hopeIsCo0l/Task-Management-API.git
Navigate to the project directory:
bash
Copy code
cd task-manager-api
Install the requirements:
bash
Copy code
pip install -r requirements.txt
Run migrations:
bash
Copy code
python manage.py migrate
Start the server:
bash
Copy code
python manage.py runserver
Usage
After running the server, access the API at http://127.0.0.1:8000/api/.

Endpoints
User Registration: POST /api/users/
User Login: POST /api/token/
Create Task: POST /api/tasks/
List Tasks: GET /api/tasks/
Update Task: PUT /api/tasks/{task_id}/
Delete Task: DELETE /api/tasks/{task_id}/
Contributing
Contributions are welcome! Please fork the repository and submit pull requests with your enhancements.

# License



# Contact
Abdellah Teshome - abdellah.teshome@aait.edu.et

Acknowledgments
    AAiT
    ALX