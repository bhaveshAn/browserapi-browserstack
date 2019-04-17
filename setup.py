# -*- coding: utf-8 -*-
from os.path import dirname, join

from setuptools import setup, find_packages

import mybrowser

description = 'BrowserStack API wrapper'


setup(
    name="mybrowser",
    version="0.0.1",
    description=description,
    author='Bhavesh Anand',
    author_email='bhaveshanand96@gmail.com',
    packages=find_packages(),
    package_dir={'mybrowser': 'mybrowser'},
    include_package_data=True,
    install_requires=[
          'certifi==2019.3.9',
          'chardet==3.0.4',
          'idna==2.8',
          'requests==2.21.0',
          'urllib3==1.24.1'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python',
        'Programming Language :: Python',
    ],
    zip_safe=False,
    keywords="wrapper browserstack",
)