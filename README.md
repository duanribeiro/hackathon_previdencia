# Database API
[![Python](https://img.shields.io/badge/python-3.6-blue.svg)]()

The main objective of this API is create a communication layer between services and the database. Built in
[Flask RESTPlus](https://flask-restplus.readthedocs.io/en/stable/index.html) which encourages best practices with 
minimal setup.

# Getting Started

## Installing

```
git clone https://github.com/OctaplusFinancialAnalytics/database_api.git && cd database_api
pip install -r requirements.txt
```

## Docker
### Build

```
docker build -t backend .
```

### Start a New Container

```
docker run --name backend backend
```

## Swagger
After the application goes up, open your browser on `localhost:5000/docs` to see the self-documented interactive API:

![](docs/screenshot_swagger.png)

## Project Structure

The project structure is based on the official 
[scaling your project](https://flask-restplus.readthedocs.io/en/stable/scaling.html#multiple-apis-with-reusable-namespaces).


```
.
├── api
│   ├── blueprints
│   │   ├── client_spreads
│   │   │   ├── __init__.py
│   │   │   ├── json_models.py
│   │   │   ├── models.py
│   │   │   ├── routes.py
│   │   │   └── serializers.py
│   │   └── ....
│   │       ├── __init__.py
│   │       ├── json_models.py
│   │       ├── routes.py
│   │       └── serializers.py
│   ├── helpers
│   └── __init__.py
├── app.py
├── config.py
├── docs
├── json_files
├── README.md
└── requirements.txt
```

### Folders

* `api` - All the RESTful API implementation is here.
* `api/helpers` - Useful function/class helpers for all modules.
* `api/blueprints` - Resource agroupment for all `v1` [Namespaces](https://flask-restplus.readthedocs.io/en/stable/scaling.html#multiple-namespaces).

### Files
* `api/__init__.py` - The Flask Application factory (`create_app()`) and it's configuration are done here.
* `api/blueprints/__init__.py` - Your [Blueprints](https://flask-restplus.readthedocs.io/en/stable/scaling.html#use-with-blueprints) are registered here.
* `config.py` - Config file for envs, global config vars and so on.
* `requirements.txt` - All project dependencies.
* `app.py` - The Application entrypoint.

