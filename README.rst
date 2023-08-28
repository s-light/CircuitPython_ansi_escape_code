Introduction
============


.. image:: https://readthedocs.org/projects/circuitpython-ansi-escape-code/badge/?version=latest
    :target: https://circuitpython-ansi-escape-code.readthedocs.io/
    :alt: Documentation Status


.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/s-light/CircuitPython_ansi_escape_code/workflows/Build%20CI/badge.svg
    :target: https://github.com/s-light/CircuitPython_ansi_escape_code/actions
    :alt: Build Status


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

simple helper library for common ANSI escape codes


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.

Installing from PyPI
=====================
On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/circuitpython-ansi-escape-code/>`_.
To install for current user:

.. code-block:: shell

    pip3 install circuitpython-ansi-escape-code

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install circuitpython-ansi-escape-code

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install circuitpython-ansi-escape-code



Installing to a Connected CircuitPython Device with Circup
==========================================================

Make sure that you have ``circup`` installed in your Python environment.
Install it with the following command if necessary:

.. code-block:: shell

    pipx install circup

With ``circup`` installed and your CircuitPython device connected use the
following command to install:

.. code-block:: shell

    circup install ansi_escape_code

Or the following command to update an existing version:

.. code-block:: shell

    circup update

Usage Example
=============

See scripts in the examples directory of this repository.

.. code-block:: python

    import ansi_escape_code as terminal
    print(
        terminal.ANSIColors.fg.lightblue
        + "Hello "
        + terminal.ANSIColors.fg.green
        + "World "
        + terminal.ANSIColors.fg.orange
        + ":-)"
        + terminal.ANSIColors.reset
    )


Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/s-light/CircuitPython_ansi_escape_code/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out
`this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
