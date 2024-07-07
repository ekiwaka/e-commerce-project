# E-Commerce Flask App

## Setup

1. Create a virtual environment and activate it:
    python -m venv venv
    venv/Scripts/activate

2. Install dependencies:
    pip install -r requirements.txt

3. Run the application:
    flask run

## Endpoints

### Auth
- `/auth/signup` - Sign up with username and password
- `/auth/login` - Log in and get JWT token

### Data
- `/data/upload` - Upload product data CSV file

### Report
- `/report/summary` - Generate and download summary report CSV file

### Postman Collection is in data folder