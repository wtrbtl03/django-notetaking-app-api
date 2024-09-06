# A Django API for Managing Notes


## Setup

### Clone the rpository
```bash
git clone https://github.com/wtrbtl03/django-notetaking-app-api
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Apply migrations
```bash
python3 manage.py migrate
```

### Run the development server
```bash
python3 manage.py runserver
```

## API Docs

This is a simple REST API built using Django for managing notes. The API allows one to create, fetch, query, and update notes.

## Base URL

```
/api/
```

## Endpoints

### 1. Create a Note
- **URL:** `/note/`
- **Method:** `POST`
- **Description**: Creates a new note with a `title` and `body`.
- **Body:**
  ```json
  {
    "title": "Note Title",
    "body": "Note Body"
  }
  ```
- **Success Response:**
  - **Code:** `201 Created`
  - **Content:** 
    ```json
    {
      "id": 1,
      "title": "Note Title",
      "body": "Note Body",
      "created_at": "2024-09-06T12:00:00Z",
      "updated_at": "2024-09-06T12:00:00Z"
    }
    ```
- **Error Response:**
  - **Code:** `400 Bad Request`
  - **Content:**
    ```json
    {
      "error": "Both 'title' and 'body' are required fields"
    }
    ```

### 2. Fetch All Notes
- **URL:** `/note/all/`
- **Method:** `GET`
- **Description**: Retrieves all notes stored in the database.
- **Success Response:**
  - **Code:** `200 OK`
  - **Content:** 
    ```json
    [
      {
        "id": 1,
        "title": "Note Title",
        "body": "Note Body",
        "created_at": "2024-09-06T12:00:00Z",
        "updated_at": "2024-09-06T12:00:00Z"
      },
      {
        "id": 2,
        "title": "Another Note Title",
        "body": "Another Note Body",
        "created_at": "2024-09-06T12:10:00Z",
        "updated_at": "2024-09-06T12:10:00Z"
      }
    ]
    ```
- **Error Response:**
  - **Code:** `404 Not Found`
  - **Content:**
    ```json
    {
      "error": "No notes found"
    }
    ```

### 3. Fetch Note by ID
- **URL:** `/note/<int:note_id>/`
- **Method:** `GET`
- **Description**: Retrieves a specific note by its ID.
- **Success Response:**
  - **Code:** `200 OK`
  - **Content:** 
    ```json
    {
      "id": 1,
      "title": "Note Title",
      "body": "Note Body",
      "created_at": "2024-09-06T12:00:00Z",
      "updated_at": "2024-09-06T12:00:00Z"
    }
    ```
- **Error Response:**
  - **Code:** `404 Not Found`
  - **Content:**
    ```json
    {
      "error": "Note not found"
    }
    ```

### 4. Query Notes by Title
- **URL:** `/note/search/?title=<search_term>`
- **Method:** `GET`
- **Description**: Searches for notes with titles containing the given search term.
- **Success Response:**
  - **Code:** `200 OK`
  - **Content:** 
    ```json
    [
      {
        "id": 1,
        "title": "Note Title",
        "body": "Note Body"
      },
      ...
    ]
    ```
- **Error Response:**
  - **Code:** `400 Bad Request`
  - **Content:**
    ```json
    {
      "error": "Query parameter 'title' is required"
    }
    ```
  - **Code:** `404 Not Found`
  - **Content:**
    ```json
    {
      "error": "No notes found"
    }
    ```

### 5. Update Note
- **URL:** `/note/<int:note_id>/update/`
- **Method:** `PUT`
- **Description**: Updates an existing note by its ID. Either `title` or `body` or both can be updated.
- **Body:**
  ```json
  {
    "title": "Updated Title",
    "body": "Updated Body"
  }
  ```
- **Success Response:**
  - **Code:** `200 OK`
  - **Content:** 
    ```json
    {
      "id": 1,
      "title": "Updated Title",
      "body": "Updated Body",
      "created_at": "2024-09-06T12:00:00Z",
      "updated_at": "2024-09-06T13:00:00Z"
    }
    ```
- **Error Response:**
  - **Code:** `400 Bad Request`
  - **Content:**
    ```json
    {
      "error": "At least one of 'title' or 'body' must be provided for update"
    }
    ```
  - **Code:** `404 Not Found`
  - **Content:**
    ```json
    {
      "error": "Note not found"
    }
    ```

## License
The code for this project is available for use under the [MIT License](LICENSE).