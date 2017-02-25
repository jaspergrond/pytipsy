#!/usr/bin/env python

from distutils.core import setup

setup(
		name="PyTipsy",
		version='1.3',
		author='Jasper Grond',
		author_email='grond.jasper@gmail.com',
		url='https://github.com/jaspergrond/pytipsy3',
		py_modules=['pytipsy'],
		license='LICENCE.txt',
		long_description=open('README.md').read(),
		install_requires=[
			"Numpy >= 1.5.1"
			],
)
