from setuptools import setup, find_packages


setup(
	name='library-app',
	version='1.0.0',
	description='this package contains samples of project-library code',
	author='Roman Leontovych',
	author_email='lordwerneo@gmail.com',
	url='https://github.com/lordwerneo/project-library/',
	install_requires=[
		'Flask>=2.02',
		'Flask-Migrate>=3.1.0',
		'Flask-RESTful>=0.3.9',
		'Flask-SQLAlchemy>=2.5.1',
		'Flask-WTF>=1.0.0'
	],
	packages=find_packages(exclude=('tests*', 'testing*')),
	entry_points={
		'console_scripts': [
			'test_folder-cli = test_folder.test:main',
		]
	},
	zip_sage=False,
)
