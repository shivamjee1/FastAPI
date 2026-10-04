# FastAPI Todo API

A backend Todo API built with **FastAPI**, **Pydantic**, **SQLAlchemy**, and **PostgreSQL**.

This project is being developed phase-by-phase to understand backend development concepts practically, including API design, validation, CRUD operations, database integration, configuration management, and environment variables.

---

## 🚀 Tech Stack

- **Python**
- **FastAPI**
- **Pydantic**
- **SQLAlchemy**
- **PostgreSQL**
- **python-dotenv**
- **Uvicorn**
- **Git & GitHub**

---

# 📌 Project Development Phases

Each Git commit represents one development phase.

---

## Phase 1 — Setup of FastAPI

**Commit:** `3837605`  
**Commit:** `Setup of FastAPI`

### What was done

- Created the initial FastAPI project structure.
- Installed and configured FastAPI.
- Created the FastAPI application instance.
- Configured the development server using Uvicorn.
- Created the first basic API endpoint.
- Verified that the FastAPI application runs successfully.

### Important Concepts

- FastAPI application object
- Uvicorn ASGI server
- API endpoint
- HTTP request/response
- Development server
- Project structure

### Key Learning

> FastAPI provides the framework for creating APIs, while Uvicorn runs the FastAPI application as an ASGI server.

---

# Phase 2 — FastAPI Project Startup, Environment & First API

**Commit:** `1a3b89e`  
**Commit:** `fastapi project startup setup environment and first api`

### What was done

- Established the project development environment.
- Configured the Python virtual environment.
- Added the initial API structure.
- Created the first functional API.
- Verified API execution through the FastAPI development server.
- Started organizing the project for further backend development.

### Important Concepts

- `.venv`
- Project environment
- FastAPI application startup
- Uvicorn
- API routes
- Development workflow

### Key Learning

> A properly isolated virtual environment keeps project dependencies separate and makes backend development reproducible.

---

# Phase 3 — Full CRUD Operations with Pydantic

**Commit:** `b22b4ed`  
**Commit:** `full crud operation with pydentic understanding`

### What was done

Implemented the complete CRUD workflow for Todo data.

### CRUD Operations

| Operation | HTTP Method | Purpose |
|---|---|---|
| Create | `POST` | Create a new Todo |
| Read | `GET` | Retrieve Todo data |
| Update | `PUT` / `PATCH` | Modify Todo data |
| Delete | `DELETE` | Remove Todo |

### Pydantic

Pydantic models were introduced for:

- Request validation
- Data structure definition
- Type checking
- API request/response schemas

### Important Concepts

- CRUD
- Pydantic models
- Request body
- Response data
- Type validation
- HTTP methods
- API schemas

### Key Learning

> Pydantic separates API data validation from the actual application logic and ensures that incoming data follows the expected structure.

---

# Phase 4 — ID Clarification

**Commit:** `b9cd607`  
**Commit:** `id clarification`

### What was done

- Clarified how Todo IDs are handled.
- Improved understanding of identifying individual resources.
- Worked with ID-based API operations.
- Made the CRUD workflow more logically structured around unique Todo records.

### Important Concepts

- Resource identification
- Unique IDs
- Path parameters
- ID-based retrieval
- ID-based update
- ID-based deletion

### Example

```http
GET /todos/1

# phase 5 databse integration

# phase 6 getting the .env content through pydantic settings


## 🟢 Phase 07 — Database Session Implementation

**Commit:** `feat: implement database session management`

### 🎯 Objective

Implement a reusable and controlled **SQLAlchemy database session** for FastAPI using dependency injection.

This phase connects the API request lifecycle with the database session lifecycle, creating a clean foundation for database-driven endpoints.



### 🔧 What Was Implemented

- Created a reusable SQLAlchemy database session.
- Implemented a `get_db()` dependency.
- Used FastAPI's dependency injection system.
- Provided a database session to API endpoints when required.
- Ensured the session is properly closed after the request.
- Separated database session management from API route logic.



### 🏗️ Database Session Flow

    text
                 HTTP Request
                      │
                      ▼
              FastAPI Endpoint
                      │
                      ▼
              Depends(get_db)
                      │
                      ▼
              Create DB Session
                      │
                      ▼
             Execute DB Operations
                      │
                      ▼
                API Response
                      │
                      ▼
               Close Session

#phase 8 table creation by fastapi in db 

used basic instruction to create table in the database 
Base.metadata.create_all(bind=engine)

# phase 9 full crud operation used db table 
