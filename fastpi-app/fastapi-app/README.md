# FastAPI Application

This project is a FastAPI application that provides a simple API for managing human records. It includes functionality to add, update, delete, and list human entries in a SQLite database.

## Project Structure

```
fastapi-app
├── src
│   └── main.py          # Main entry point of the FastAPI application
├── requirements.txt     # Lists the dependencies required for the project
└── README.md            # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd fastapi-app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   Start the FastAPI application and call the `/setup_db` endpoint to create the database schema.

5. **Run the application:**
   ```
   uvicorn src.main:app --reload
   ```

## Usage

- **Add a human:**
  - Endpoint: `POST /humans`
  - Body: `{ "name": "John Doe", "age": 30, "gender": "male" }`

- **List all humans:**
  - Endpoint: `GET /humans`

- **Update a human:**
  - Endpoint: `PUT /humans`
  - Body: `{ "id": 1, "name": "Jane Doe", "age": 25, "gender": "female" }`

- **Delete a human:**
  - Endpoint: `DELETE /humans?human_id=1`

## License

This project is licensed under the MIT License.