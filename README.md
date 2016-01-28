## django-facemash

### A Facemash-like app as seen in the movie The Social Network, except with more features.


**Please note that this doesn't include `tests`.**

## Description

The site basically lets users register, login and create their own facemash game, which they can share and have people vote on. Games are public (whoever has the link), but ratings and ability to add players to the game are private (to whoever who created the game).

1. **Programming language -** Python
2. **Web framework -** Django
3. **Algorithm -** Glicko-2
4. **Learn more -** [Glicko-2 website](http://glicko.net/glicko.html) | [Glico-2 Wikipedia](http://en.wikipedia.org/wiki/Glicko_rating_system)

## How to install

Install it like any other Django app.

1. Extract `facemash` folder from `django-facemash` directory and keep it inside your project's directory.
2. In your project's `settings.py` file, add `facemash` to `INSTALLED_APPS`.
3. Run `python manage.py syncdb`.
4. In your project's `urls.py` file, copy the urls.py added in the root folder.
5. Visit `127.0.0.1:8000/facemash/` and see it in action.

## Tested with

Tested with `django 1.5` and `django 1.6`.

## Issues

I havent' run into any issues so far whatsoever. You may, perhaps, run into some minor issues with `{% url %}` tag if you try to install this app on `django < 1.5` because of the change in syntax since `v 1.5`. I'm certain you can fix it by changing the `{% url %}` tag in the templates.

**For example:**

The tag `{% url 'facemash' %}` should be changed to `{% url facemash %}` for `django < 1.5`. Change all the `{% url %}` tags likewise. 


