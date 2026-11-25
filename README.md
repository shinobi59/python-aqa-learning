# Python API Test Automation

![Python](https://img.shields.io/badge/Python-blue)
![Pytest](https://img.shields.io/badge/Pytest-green)
![REST API](https://img.shields.io/badge/REST-API-orange)

## About

A personal learning project focused on automated REST API testing using Python and Pytest.

The project demonstrates API testing techniques, reusable test architecture, CRUD operations, and API contract validation using the JSONPlaceholder public API.

## Tech Stack

- Python
- Pytest
- Requests
- JSON Schema
- Git

## Features

- 30 automated test cases
- Positive and negative API testing
- GET, POST, PUT, PATCH and DELETE requests
- Parameterized tests
- Reusable API client
- Pytest fixtures and session management
- JSON Schema validation
- Response status and data validation

## Project Structure

```text
python-aqa-learning/
├── api/
│   └── users_api.py
├── schemas/
│   └── users_schema.py
├── tests/
│   ├── test_users.py
│   ├── test_parametrized_users.py
│   ├── test_users_crud.py
│   └── test_users_schema.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Installation

```bash
git clone https://github.com/shinobi59/python-aqa-learning.git
cd python-aqa-learning
pip install -r requirements.txt
```

## Running Tests

Run all tests:

```bash
python -m pytest
```

Run CRUD tests:

```bash
python -m pytest tests/test_users_crud.py -v
```

Run API contract tests:

```bash
python -m pytest tests/test_users_schema.py -v
```

## Test API

https://jsonplaceholder.typicode.com

JSONPlaceholder simulates write operations. Created, updated and deleted resources are not permanently stored on the server.

## Roadmap

- [x] Python fundamentals
- [x] REST API testing
- [x] Pytest fixtures
- [x] Test parameterization
- [x] CRUD operations
- [x] JSON Schema validation
- [ ] Logging
- [ ] Exception handling
- [ ] Allure reporting
- [ ] CI/CD integration

## Project Status

In active development as part of my learning journey from Manual QA to Automation QA.