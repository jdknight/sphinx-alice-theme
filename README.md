# Alice Theme for Sphinx

[![pip Version](https://img.shields.io/pypi/v/sphinx-alice-theme.svg)][PyPi]
[![Build](https://github.com/jdknight/sphinx-alice-theme/actions/workflows/build.yml/badge.svg)][Build]
[![Documentation](https://github.com/jdknight/sphinx-alice-theme/actions/workflows/docs.yml/badge.svg)][Documentation]

Provides the Alice theme for [Sphinx][Sphinx] projects.

<div align="center">
    <img src="https://sphinx-alice-theme.jdknight.me/overview-01.png" width="30%"></img>
    <img src="https://sphinx-alice-theme.jdknight.me/overview-02.png" width="30%"></img>
    <img src="https://sphinx-alice-theme.jdknight.me/overview-03.png" width="30%"></img>
    <img src="https://sphinx-alice-theme.jdknight.me/overview-04.png" width="30%"></img>
    <img src="https://sphinx-alice-theme.jdknight.me/overview-05.png" width="30%"></img>
    <img src="https://sphinx-alice-theme.jdknight.me/overview-06.png" width="30%"></img>
    <img src="https://sphinx-alice-theme.jdknight.me/overview-07.png" width="30%"></img>
    <img src="https://sphinx-alice-theme.jdknight.me/overview-08.png" width="30%"></img>
    <img src="https://sphinx-alice-theme.jdknight.me/overview-09.png" width="30%"></img>
</div>

## Installation

This theme can be installed using [pip][pip]:

```shell
pip install -U sphinx-alice-theme
    (or)
python -m pip install -U sphinx-alice-theme
```

## Usage

For an existing Sphinx documentation set, the Alice theme can be applied by
configuring the [`html_theme`][html_theme] value to `sphinx_alice_theme`.
For example:

```python
html_theme = 'sphinx_alice_theme'
```

The following theme options are available:

```python
html_theme_options = {
    #'canonical_url': 'https://www.example.com',
    #'includehidden': False,
    #'navigation_depth': 4,
    #'prev_next_buttons_location': 'both', # top, bottom, none
    #'titles_only': False,
}
```

## Dependencies

- [Gumshoe][Gumshoe]


[Build]: https://github.com/jdknight/sphinx-alice-theme/actions/workflows/build.yml
[Documentation]: https://sphinx-alice-theme.jdknight.me/
[Gumshoe]: https://github.com/cferdinandi/gumshoe
[PyPi]: https://pypi.python.org/pypi/sphinx-alice-theme
[Sphinx]: https://www.sphinx-doc.org/
[html_theme]: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_theme
[pip]: https://pip.pypa.io/
