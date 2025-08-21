# Recipe API Project

This project is a simple **RESTful API** for managing and retrieving recipes.  
It uses **PostgreSQL** as the database and **FastAPI** as the web framework.

---

## Features

- Database schema for storing recipes with:
  - `cuisine` (VARCHAR)
  - `title` (VARCHAR)
  - `rating` (FLOAT)
  - `prep_time` (INT)
  - `cook_time` (INT)
  - `total_time` (INT)
  - `description` (TEXT)
  - `nutrients` (JSONB)
  - `serves` (VARCHAR)
- Handles **NaN / invalid values** by storing them as `NULL`.
- REST API with pagination and sorting:
  - **GET `/api/recipes`** → Fetch all recipes, sorted by rating (desc), with pagination.

---

## Project Structure

recipe-api/
│── app/
│ ├── init.py
│ ├── database.py # DB connection setup
│ ├── models.py # SQLAlchemy models
│ ├── crud.py # Database queries
│ ├── routes.py # API routes
│ └── main.py # FastAPI app entrypoint
│
├── data/
│ └── recipes.json # Example recipe data
│
├── requirements.txt # Python dependencies
└── README.md # Documentation

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/recipe-api.git
cd recipe-api
2. Create Virtual Environment & Install Dependencies
python3 -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows

pip install -r requirements.txt
3. Configure Database
Make sure PostgreSQL is installed and running.
Create a new database:
createdb recipes_db
Update the DB URL in app/database.py if needed:
DATABASE_URL = "postgresql://username:password@localhost:5432/recipes_db"
4. Run Database Migrations
python -m app.models
5. Load Data from JSON
python -m app.crud
6. Start FastAPI Server
uvicorn app.main:app --reload
API Endpoints
1. Get All Recipes
Request:
GET /api/recipes?page=1&limit=10
Response:
{
  "page": 1,
  "limit": 10,
  "total": 50,
  "data": [
    {
      "id": 1,
      "title": "Sweet Potato Pie",
      "cuisine": "Southern Recipes",
      "rating": 4.8,
      "prep_time": 15,
      "cook_time": 100,
      "total_time": 115,
      "description": "Shared from a Southern recipe, this homemade sweet potato pie...",
      "nutrients": {
        "calories": "389 kcal",
        "carbohydrateContent": "48 g",
        "cholesterolContent": "78 mg",
        "fiberContent": "3 g",
        "proteinContent": "5 g",
        "saturatedFatContent": "10 g",
        "sodiumContent": "254 mg",
        "sugarContent": "28 g",
        "fatContent": "21 g"
      },
      "serves": "8 servings"
    }
  ]
}
Tech Stack
Python 3.9+

FastAPI

PostgreSQL

SQLAlchemy

License
MIT License








Ask ChatGPT
