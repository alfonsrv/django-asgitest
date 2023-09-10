# ASGI Database Creation?

```bash
pip install -r requirements.txt
mv sample-dotenv .env
vi .env
set -o allexport; source .env; set +o allexport
python manage.py test core.tests
```

Uses Chrome for Selenium & Postgres for database
