Options
#######

The Alice theme supports a series of theme-specific options specified through
the |html_theme_options|_ configuration. A full option set is as follows:

.. code-block:: python

    html_theme_options = {
        #'canonical_url': 'https://www.example.com',
        #'includehidden': False,
        #'navigation_depth': 4,
        #'prev_next_buttons_location': 'both',
        #'titles_only': False,
    }

For standard HTML configuration and theme options, also consult:

    | Sphinx -- Configuration -- Options for HTML output
    | http://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

The following outlines the specific theme options provided by this extension:

.. contents::
    :local:

canonical_url
-------------

Specifies the value which should be added (if any) into the
`canonical link HTML element`_ in every page header. By default, no canonical
element is added.

.. code-block:: python

    html_theme_options = {
        'canonical_url': 'https://www.example.com',
    }

includehidden
-------------

Specifies whether or not the navigation will includes hidden marked table(s) of
contents. By default, table(s) of contents which are marked with the
``:hidden:`` option remain hidden with a value of ``False``.

.. code-block:: python

    html_theme_options = {
        'includehidden': True,
    }

navigation_depth
----------------

Specifies the maximum depth of children which will be visible in a table of
contents tree. By default, a maximum of depth of ``4`` is applied. Set this to
``-1`` to not restrict the depth of any tree.

.. code-block:: python

    html_theme_options = {
        'navigation_depth': 4,
    }

prev_next_buttons_location
--------------------------

Configures how "Next" and "Previous" links (if any) should be rendered in the
final documentation set. Permitted values include ``both``, ``top``, ``bottom``
or ``None``. By default, these links are included in ``both`` the top and the
bottom of each page.

.. code-block:: python

    html_theme_options = {
        'prev_next_buttons_location': 'both',
    }

titles_only
-----------

Specifies whether or not only titles (not subheadings) of a document are
included in table(s) of contents. By default, subheadings are permitted with a
value of ``False``.

.. code-block:: python

    html_theme_options = {
        'titles_only': True,
    }

.. |html_theme_options| replace:: ``html_theme_options``
.. _canonical link HTML element: https://wikipedia.org/wiki/Canonical_link_element
.. _html_theme_options: http://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_theme_options
