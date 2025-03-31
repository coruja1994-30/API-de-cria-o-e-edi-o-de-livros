# Flask MySQL API

This project is a Flask API connected to a MySQL database. It provides a structured way to manage and interact with data using SQLAlchemy and Flask-Migrate for database migrations.

## Project Structure

```
flask-mysql-api
├── app
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── config.py
├── migrations
├── requirements.txt
├── .env
├── run.py
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd flask-mysql-api
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up the environment variables:**
   Create a `.env` file in the root directory and add your database credentials:
   ```
   DATABASE_URL=mysql://<username>:<password>@localhost/<database_name>
   SECRET_KEY=<your_secret_key>
   ```

5. **Initialize the database:**
   ```
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

## Usage

To run the application, execute the following command:
```
python run.py
```

The API will be available at `http://localhost:5000`.

## Endpoints

- **GET /api/resource**: Retrieve a list of resources.
- **GET /api/resource/<id>**: Retrieve a specific resource by ID.
- **POST /api/resource**: Create a new resource.
- **PUT /api/resource/<id>**: Update an existing resource by ID.
- **DELETE /api/resource/<id>**: Delete a resource by ID.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes. 

## License

This project is licensed under the MIT License.