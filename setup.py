import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'async-supercell-api',
    version = '0.0.1',
    author = 'Andrea Princic',
    author_email = 'princic.1837592@studenti.uniroma1.it',
    description = 'Async wrapper for Supercell API',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://async-supercell-api.readthedocs.io/en/latest/',
    packages = ['async_supercell_api'],
    python_requires = '>=3.7',
    install_requires = [
        'aiohttp',
    ]
)