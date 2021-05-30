# QR Survey App

Web application where a user will be able to scan a QR code and be directed to a form where they can answer questions pertaining to a poster presentation. The questions are pre-determined with only admins being able to update. Answers are using a 1-5 rating system. 

## Tech Stack
- Django
- Postgres
- Docker

If using Docker plese run: `docker compose up` in project root directory

If building locally, please run `pip install -r requirements.txt` to install dependencies. 




## Testing
Uses default `unnittest` module, to run unit tests:

    python3 manage.py test qr_survey.tests




## Coverage
The `coverage` module provides viewable unit test coverage by:

    coverage run --source='.' manage.py test qr_survey.tests -v 2 && coverage report


HTML version of the report:

`coverage html`
