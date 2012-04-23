
=====================
Development HTML Sign
=====================

A simple middleware to show predefined message bars on the top of the page. This helps clients and developers alike to identify, for instance, that they are working on the development server, instead of production.

.. image:: https://github.com/awarepixel/django-devsign/raw/master/docs/_images/screenshot.png


Usage
=====

Add a dictionary DEVSIGN_MESSAGES to your settings.py::

    DEVSIGN_MESSAGES = {
        [Host name]: {
            'message': [Message],
            'style': [CSS Styles]
        }
    }

Example::

    DEVSIGN_MESSAGES = {
        'dev.example.org': {
            'message': 'You are using the DEVELOPMENT site.',
            'style': 'background-color: purple; color: white; font-size: 16px; padding: 12px;'
        },
        'experimental.example.org': {
            'message': 'Experimental branch.',
            'style': 'background-color: black; color: white; font-size: 16px; padding: 12px;'
        }
    }


    