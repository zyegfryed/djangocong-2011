This is an example project to demonstrate how to use PDFForm within Django `presented`_ at djangocong 2011.

.. _presented: http://www.scribd.com/doc/53196142/pdfform

Getting started
===============

First, you need to `install pdftk`_ on your system.

Then::

    $ git clone git://github.com/zyegfryed/djangocong-2011.git
    $ cd djangocong-2011
    $ virtualenv .
    $ source bin/activate
    $ pip install -r requirements.txt
    $ python manage.py runserver

Go to http://127.0.0.1:8000/ and click on the "Print your ticket" link to
download the generated PDF. Enjoy!

.. _install pdftk: http://www.pdflabs.com/docs/install-pdftk/

Plug'n'play
===========

Here's a `gist`_ to get you started right away into your project.

.. _gist: https://gist.github.com/918403

Compatibility
=============

Fully compatible with Django 1.3. I haven't tried any other versions, but
it should work unless a big refactoring in Django template engine.

