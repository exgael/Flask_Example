# Book Management API Documentation

## Overview
This Flask-based API provides a simple interface for managing a collection of books. Utilizing a SQLite database, it allows users to create, read, update, and delete book records. This document serves as a guide to using the API.

## Getting Started
- **Base URL**: The base URL for the API is `http://localhost:8000/`.
- **Required Software**: Ensure you have Python and Flask installed on your system.

## API Endpoints

### 1. Add a New Book
- **URL**: `/books`
- **Method**: `POST`
- **JSON Body**:
  ```json
  {
    "title": "Book Title",
    "author": "Author Name",
    "published_year": 2020
  }
  ```
- **Response**:
  - **Code**: 201 (Created)
  - **Content Example**:
    ```json
    {
      "id": 1,
      "title": "Book Title",
      "author": "Author Name",
      "published_year": 2020
    }
    ```

### 2. Get All Books
- **URL**: `/books`
- **Method**: `GET`
- **Response**:
  - **Code**: 200 (OK)
  - **Content Example**:
    ```json
    [
      {
        "id": 1,
        "title": "Book Title",
        "author": "Author Name",
        "published_year": 2020
      }
    ]
    ```

### 3. Get a Single Book
- **URL**: `/books/<id>`
- **Method**: `GET`
- **Response**:
  - **Code**: 200 (OK)
  - **Content Example**:
    ```json
    {
      "id": 1,
      "title": "Book Title",
      "author": "Author Name",
      "published_year": 2020
    }
    ```

### 4. Update a Book
- **URL**: `/books/<id>`
- **Method**: `PUT`
- **JSON Body**:
  ```json
  {
    "title": "Updated Title",
    "author": "Updated Author",
    "published_year": 2021
  }
  ```
- **Response**:
  - **Code**: 200 (OK)
  - **Content Example**:
    ```json
    {
      "id": 1,
      "title": "Updated Title",
      "author": "Updated Author",
      "published_year": 2021
    }
    ```

### 5. Delete a Book
- **URL**: `/books/<id>`
- **Method**: `DELETE`
- **Response**:
  - **Code**: 204 (No Content)

## Error Handling
Errors are returned as JSON objects in the following format:
```json
{
  "error": 404,
  "message": "Resource not found"
}
```
The API will return three error types when requests fail:
- 400: Bad Request
- 404: Resource Not Found
- 405: Method Not Allowed