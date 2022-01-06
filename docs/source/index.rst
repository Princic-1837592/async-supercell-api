Welcome to async-supercell-api documentation!
=============================================

async-supercell-api is a Python library for `Supercell <https://supercell.com/en/>`_'s games' players (currently only Clash Royale)
that offers an async and simple-to-use implementation of the Supercell APIs based on `Asyncio <https://docs.python.org/3/library/asyncio.html>`_.

Installation
^^^^^^^^^^^^

You can install using pip:

.. code-block:: text

    $ pip3 install -U async-supercell-api

Or you can directly install from GitHub:

.. code-block:: text

    $ pip3 install -U git+https://github.com/Princic-1837592/async-supercell-api

After installing, verify the installation:

.. code-block:: python

    from async_supercell_api import ClashRoyaleAPI, ClashOfClansAPI

    cr_api = ClashRoyaleAPI('api_key')
    coc_api = ClashOfClansAPI('api_key')

.. toctree::
    :hidden:
    :caption: Games

    games/index