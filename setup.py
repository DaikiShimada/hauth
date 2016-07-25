# -*- coding: utf-8 -*-

from setuptools import setup

six_version = 'six>=1.9.0'
install_requires = [
    six_version,
]

setup(
    name = 'hauth',
    version = '0.0.3',
    packages = ['hauth'],
    description = '',
    author = 'Daiki Shimada',
    author_email = 'daiki.shimada.9g@stu.hosei.ac.jp',
    url = 'https://gist.github.com/49f459da8a0522e05812.git',
    install_requires = install_requires,
    license='http://www.apache.org/licenses/LICENSE-2.0'
    )
