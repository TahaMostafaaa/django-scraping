# django-scraping
Django Framework

# Steps to Run

- `docker-compose up -d`
- `docker-compose exec app python manage.py migrate`
- `docker-compose exec app python manage.py do_scrap`
- `docker-compose exec app python manage.py do_report`

go to `http://localhost:8000`
call any endpoint
