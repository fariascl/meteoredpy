import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'meteoredpy',
    packages = ['meteoredpy'],
    version = '0.0.1',
    description = 'Libreria para consumir y parsear a JSON API de meteored.cl',
    long_description__content_type='text/markdown',
    author = 'Alejandro Farías',
    author_email = 'farias@8loop.cl',
    url = 'https://github.com/fariascl/meteoredpy',
    packages=setuptools.find_packages(),
    install_requires=['requests==2.31.0','xmltodict===0.13.0'],
    download_url = 'https://github.com/fariascl/meteoredpy/tarball/0.0.1',
    keywords = ['clima', 'json', 'api', 'meteored', 'chile'],
    classifiers = [],
    python_requires='>=3.6',
)
