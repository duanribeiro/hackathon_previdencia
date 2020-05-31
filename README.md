# Database API
[![Python](https://img.shields.io/badge/python-3.6-blue.svg)]()

The main objective of this API is create a communication layer between services and the database. Built in
[Flask RESTPlus](https://flask-restplus.readthedocs.io/en/stable/index.html) which encourages best practices with 
minimal setup.

# Getting Started

## Installing

```
git clone https://github.com/duanribeiro/hackathon_previdencia.git && cd hackathon_previdencia
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

After the application goes up, open your browser on `localhost:5000/docs`  to see the self-documented interactive API.
Live Example: [https://jwtrc70u17.execute-api.us-east-1.amazonaws.com/dev/docs](https://jwtrc70u17.execute-api.us-east-1.amazonaws.com/dev/docs)