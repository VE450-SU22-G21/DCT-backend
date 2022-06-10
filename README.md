# DCT-backend

## Development

Install requirements:

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Start dev server:

```bash
python manage.py migrate
python manage.py runserver
```

## API Endpoints

1. GET `/report`: download all diagnosed keys
2. POST `/report`: post a `{key: xxx}` to report a diagnosed key
3. GET `/report/fake`: generate a random report
