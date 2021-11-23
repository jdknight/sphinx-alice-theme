Installation
############

The recommended method of installation is using pip_:

.. code-block:: shell

    pip install -U sphinx-alice-theme
        (or)
    python -m pip install -U sphinx-alice-theme

To verify the package has been installed, the following command can be used:

.. code-block:: shell

    sphinx_alice_theme --version
        (or)
    python -m sphinx_alice_theme --version

This theme can be uninstalled with the following command:

.. code-block:: shell

    pip uninstall sphinx-alice-theme
        (or)
    python -m pip uninstall sphinx-alice-theme

Quick-start
-----------

The following provides a series of steps to assist in preparing a new
environment to use this package. This quick-start will aim to use the most
recent version of Python.

Linux
~~~~~

While the use of Python_/pip_ is almost consistent between Linux distributions,
the following are a series of helpful steps to install this package under
specific distributions of Linux. From a terminal, invoke the following commands:

Arch
++++

.. code-block:: shell-session

    $ sudo pacman -Sy
    $ sudo pacman -S python-pip
    $ sudo pip install -U sphinx-alice-theme
    $ sphinx_alice_theme --version
    sphinx-alice-theme <version>

CentOS
++++++

.. code-block:: shell-session

    $ sudo yum install epel-release
    $ sudo yum install python-pip
    $ sudo pip install -U sphinx-alice-theme
    $ sphinx_alice_theme --version
    sphinx-alice-theme <version>

Fedora
++++++

.. code-block:: shell-session

    $ sudo dnf install python-pip
    $ sudo pip install -U sphinx-alice-theme
    $ sphinx_alice_theme --version
    sphinx-alice-theme <version>

openSUSE
++++++++

.. code-block:: shell-session

    $ pip install -U sphinx-alice-theme
    $ sphinx_alice_theme --version
    sphinx-alice-theme <version>

Ubuntu
++++++

.. code-block:: shell-session

    $ sudo apt-get update
    $ sudo apt-get install python-pip
    $ sudo pip install -U sphinx-alice-theme
    $ sphinx_alice_theme --version
    sphinx-alice-theme <version>

OS X
~~~~

From a terminal, invoke the following commands:

.. code-block:: shell-session

    $ sudo easy_install pip
    $ sudo pip install -U sphinx-alice-theme
    $ sphinx_alice_theme --version
    sphinx-alice-theme <version>

Windows
~~~~~~~

If not already installed, download the most recent version of Python_:

    | Python - Downloads
    | https://www.python.org/downloads/

When invoking the installer, it is recommended to select the option to "Add
Python to PATH"; however, users can explicitly invoked Python from an absolute
path (the remainder of these steps will assume Python is available in the path).

Open a Windows command prompt and invoke the following:

.. code-block:: doscon

    > python -m pip install sphinx-alice-theme
    > python -m sphinx_alice_theme --version
    sphinx-alice-theme ~version~

Development
-----------

To install the most recent development sources, the following pip_ command can
be used:

.. code-block:: shell

    pip install git+https://github.com/jdknight/sphinx-alice-theme.git

.. _Python: https://www.python.org/
.. _pip: https://pip.pypa.io/
