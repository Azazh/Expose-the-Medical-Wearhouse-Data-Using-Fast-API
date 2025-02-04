# FastAPI Detection Results API

## Overview
This project is a FastAPI-based web application for managing detection results. It provides RESTful API endpoints to create, retrieve, and delete detection results stored in a PostgreSQL database.

## Features
- FastAPI framework for high-performance API development
- SQLAlchemy ORM for database interactions
- Pydantic for data validation and serialization
- PostgreSQL as the database backend
- Dependency injection for database sessions
- Exception handling for robustness

## Project Structure

my_project/
├── main.py         # Entry point for FastAPI application
├── database.py     # Database configuration and connection
├── models.py       # SQLAlchemy database models
├── schemas.py      # Pydantic schemas for request and response validation
├── crud.py         # CRUD operations for database interactions
├── requirements.txt # Project dependencies
└── README.md       # Project documentation


## Installation

### Prerequisites
- Python 3.9+
- PostgreSQL installed and running

### Step 1: Clone the Repository
sh
git clone https://github.com/yourusername/your-repository.git
cd your-repository


### Step 2: Create a Virtual Environment
sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate


### Step 3: Install Dependencies
sh
pip install -r requirements.txt


### Step 4: Configure Environment Variables
Create a `.env` file in the project root with the following content:
ini
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/medical_dw


### Step 5: Run Database Migrations (If Needed)
sh
python -c 'from database import Base, engine; Base.metadata.create_all(bind=engine)'


### Step 6: Start the FastAPI Application
sh
uvicorn main:app --reload


The API will be accessible at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## API Endpoints

### 1. Create a Detection Result
http
POST /detection_results/

**Request Body:**
json
{
  "image_path": "path/to/image.jpg",
  "class_label": "object",
  "confidence": 0.95,
  "x_min": 10,
  "y_min": 20,
  "x_max": 50,
  "y_max": 80
}


**Response:**
json
{
  "id": 1,
  "image_path": "path/to/image.jpg",
  "class_label": "object",
  "confidence": 0.95,
  "x_min": 10,
  "y_min": 20,
  "x_max": 50,
  "y_max": 80
}


### 2. Retrieve All Detection Results
http
GET /detection_results/


### 3. Retrieve a Detection Result by ID
http
GET /detection_results/{result_id}


### 4. Delete a Detection Result
http
DELETE /detection_results/{result_id}


## Testing the API
You can use tools like **Postman** or **cURL** to test API endpoints.

Example using cURL:
sh
curl -X GET http://127.0.0.1:8000/detection_results/


## License
This project is licensed under the MIT License.

## Author
[Your Name](https://github.com/yourusername)

