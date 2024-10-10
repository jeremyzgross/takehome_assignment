# Meme Generator API

## Overview

The Meme Generator API is a RESTful service built using Django and PostgreSQL. It allows users to create, retrieve, and rate memes. The application is containerized using Docker for easy deployment and testing.

## Requirements

- Python 3.12
- Docker
- Docker Compose

## Installation

1. Clone the repository:

   ```bash
   git clone
   cd meme_generator
   ```

2. Create a `.env` file in the project root with the following content:

   ```env
   DATABASE_ENGINE=django.db.backends.postgresql
   DATABASE_NAME=meme_generator
   DATABASE_USER=user
   DATABASE_PASSWORD=password
   DATABASE_HOST=db
   DATABASE_PORT=5432
   ```

3. Build and run the application:
   ```bash
   docker-compose up --build
   ```
4. Unless a superuser exists, one will be created with the username 'admin' and email 'admin@test.com' and the password 'admin123'.
## API Endpoints

### 1. List all meme templates

- **URL:** `/api/templates/`
- **Method:** `GET`
- **Response:** List of all meme templates.

### 2. List all memes

- **URL:** `/api/memes/`
- **Method:** `GET`
- **Response:** List of all memes with pagination.

### 3. Create a new meme

- **URL:** `/api/memes/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "template": 1,
    "top_text": "Top text",
    "bottom_text": "Bottom text"
  }
  ```
- **Response:** Details of the created meme.

### 4. Retrieve a specific meme

- **URL:** `/api/memes/<id>/`
- **Method:** `GET`
- **Response:** Details of the specified meme.

### 5. Rate a meme

- **URL:** `/api/memes/<id>/rate/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "score": 5
  }
  ```
- **Response:** Details of the updated rating.

### 6. Get a random meme

- **URL:** `/api/memes/random/`
- **Method:** `GET`
- **Response:** A random meme.

### 7. Get top 10 rated memes

- **URL:** `/api/memes/top/`
- **Method:** `GET`
- **Response:** List of top 10 rated memes.

## Authentication

The API uses token authentication. You can obtain a token by creating a superuser and logging in.

## Running Tests

To run tests, you can use the following command:

```bash
docker-compose exec web python manage.py test
```

Example:

# Start the containers

docker-compose up -d

# Run the tests

docker-compose exec web python manage.py test

# Stop the containers (optional)

docker-compose down
