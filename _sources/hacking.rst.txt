Hacking
#######

Users who want to override specific theme stylings can do so by injecting a
custom stylesheet into the generated output. For example, a user can create a
stylesheet ``_static/theme_overrides.css`` with the following options added into
``conf.py``:

.. code-block:: python

    html_context = {
        'css_files': ['_static/theme_overrides.css'],
    }
    html_static_path = ['_static']

Example styling of a user overriding the header color is as follows:

.. code-block:: css

    h1 {
        color: #ff0000 !important;
    }
