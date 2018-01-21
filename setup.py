# -*- coding: utf-8 -*-
from setuptools import setup


def readme():
		try:
				with open('README.rst') as f:
						return f.read()
		except:
				pass

setup(name='bshare',
			version='1.0.0',
			classifiers=[
				'Development Status :: 4 - Beta',
				'License :: OSI Approved :: MIT License',
				'Programming Language :: Python',
				'Programming Language :: Python :: 2',
				'Programming Language :: Python :: 2.6',
				'Programming Language :: Python :: 2.7',
				'Programming Language :: Python :: 3',
				'Programming Language :: Python :: 3.3',
				'Programming Language :: Python :: 3.4',
				'Programming Language :: Python :: 3.5',
				'Programming Language :: Python :: 3.6',
			],
			keywords='bluetooth file sharer',
			description='A command line bluetooth file sharing application for Linux.',
			long_description=readme(),
			url='https://github.com/nikhilkumarsingh/bshare',
			author='Nikhil Kumar Singh',
			author_email='nikhilksingh97@gmail.com',
			license='MIT',
			packages=['bshare', 'PyOBEX'],
			install_requires=['pyqt5', 'pybluez'],
			include_package_data=True,
			entry_points="""
			[console_scripts]
			bshare = bshare.bshare:main
			""",
			zip_safe=False)
