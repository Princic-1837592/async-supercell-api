Welcome to async-supercell-api documentation!
========================================

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

    from async_supercell_api.clash_royale import ClashRoyaleAPI

.. toctree::
    :hidden:
    :caption: Available games

    api/index
    api/BS/index
    api/CoC/index
    api/CR/index
