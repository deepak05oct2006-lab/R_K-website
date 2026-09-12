# ShreeSai Paint & Polish Works — Django Website

Ready-to-run Django site for a paint contractor / wood polishing business.

## Setup

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit http://127.0.0.1:8000/ for the site, and http://127.0.0.1:8000/admin/ to manage:
- **Services** — what you offer
- **Gallery Images** — upload photos of finished work (category: Painting / Wood Polishing)
- **Testimonials** — client reviews
- **Contact Messages** — leads submitted from the contact form

## Structure
- `config/` — Django project settings/urls
- `core/` — app with models, views, templates, static (CSS/JS)
- Plain HTML + CSS + vanilla JS, no build step needed.

## Customize
- Edit business name/phone/email in `core/templates/core/base.html` (header & footer).
- Colors: edit CSS variables at the top of `core/static/core/css/style.css`.
- Add real content via the Django admin instead of editing templates.

## Deploy
Set `DEBUG = False` and a real `SECRET_KEY` + `ALLOWED_HOSTS` in `config/settings.py` before production use. Run `python manage.py collectstatic`.
