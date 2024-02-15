# LAB - Class 28

## Project: Django CRUD and Forms

## Author: Bradley Hower

## Overviewgit ini

A futher built out Django app, with CRUD functionality added.

## Getting Started

To initialize, simultaneously run the following in two seperate terminals:

`npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch`

`python3 manage.py runserver`

Follow the url given in the prompt to view the web page.

## Tests

To run tests, `python3 manage.py test`

One test, "test_snack_update_view_redirect" is failing. However, it appears this is erroneous, as Django immediately runs a 200 after the 302.
