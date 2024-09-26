# Symlink

A one stop solution for your privacy issues.

## Tech stack

- [Python]()
- [Postgresql](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)

## Getting Started

- Clone the repo and execute command `npm install`
- Activate the venv using the following command `source venv/bin/activate`
- Install all dependencies using the following command `pip3 install -r requirements.txt`
- Create a file named .env
- Install postgres
- Provide postgres, user details in .env file as mentioned below

| Database configuration(Required) |                                                                |
| -------------------------------- | -------------------------------------------------------------- |
| DATABASE_URL                     | postgresql+psycopg2://postgres:postgres@localhost:5432/symlink |

- To run migrations, use `flask db upgrade`
- Run the server using `python3 app.py`
- Service should be up and running in http://localhost:5000.
