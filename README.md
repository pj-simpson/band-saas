## Band Saas 
An opinionated portfolio site for bands/musical artists with added webshop. **Currently a work in progress.**

## Motivation
For the few years I've been learning web development, its become obvious to me that building something which will actually be of use, is by far the best way to learn. 
I play in bands, my friends play in bands and broadly speaking every website for a musical project follows a similar structure. Rather than have to wrestle with a more generic CMS to fit these
requirements, I am attempting to build a tool which will be an natural fit for the requirements a musical artist might have for their site. 

## Code style
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Tech used

<b>Built with</b>
- [Django](https://www.djangoproject.com/)
- [Celery](https://docs.celeryproject.org/en/stable/getting-started/introduction.html) for asynchronous tasks like sending emails.
- [Django CKEditor](https://github.com/django-ckeditor/django-ckeditor) to give the users flexibility of how to edit and display their content.
- [Braintree](https://pypi.org/project/braintree/) for the payment gateway.
- [Django Storages](https://django-storages.readthedocs.io/en/latest/) as we expect the users to upload a lot of media.


## Credits
After having read [Test-Driven Development with Python](http://www.obeythetestinggoat.com/) by Harry Percival, I have attempted to strictly follow 'Outside-In' TDD for this project.
[The Definitive Guide to Django and Celery](https://testdriven.io/courses/django-celery/) by Michael Yin has been helpful, as was [Django3 By Example](https://www.packtpub.com/product/django-3-by-example-third-edition/9781838981952)
by Antonio Mele for ideas about how to design the webshop. 
