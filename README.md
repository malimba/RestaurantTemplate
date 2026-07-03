# Restaurant Template

A **Django-powered restaurant website** built around the **Fruitkha** HTML template — menu pages, shop layout, news section, and static assets wired into a runnable Django project.

![Django](https://img.shields.io/badge/Django-Python-092E20?style=flat-square&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/Template-Fruitkha-E34F26?style=flat-square&logo=html5&logoColor=white)

## Features

- Django project serving a polished **restaurant / organic food** landing page
- Bundled **Fruitkha 1.0.0** static template (shop, news, single-product pages)
- Ready-to-customize `index.html` via Django views
- Large asset pack (CSS, JS, fonts, images) under `mainsite/static/`

## Tech stack

| Layer | Choice |
|-------|--------|
| Framework | Django |
| Frontend | Fruitkha HTML/CSS/JS template |
| DB | SQLite (default) |

## Quick start

```bash
cd restaurant
pip install django
python manage.py migrate
python manage.py runserver
```

Open **http://127.0.0.1:8000**

## Project layout

```
restaurant/
  manage.py
  mainsite/
    templates/index.html
    static/templatezip/fruitkha-1.0.0/   # Full theme assets
  restaurant/                            # settings, urls
```

## Customization

Swap images, copy, and menu items in the Fruitkha HTML under `static/templatezip/`, or extend views to load dynamic menu data from the database.

---

Template integration by [malimba](https://github.com/malimba)
