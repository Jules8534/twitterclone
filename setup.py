# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['twitterclone']

package_data = \
{'': ['*'], 'twitterclone': ['templates/*']}

install_requires = \
['django>=3.0.6,<4.0.0']

setup_kwargs = {
    'name': 'twitterclone',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Julita Marshall',
    'author_email': 'julitamcg5@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
