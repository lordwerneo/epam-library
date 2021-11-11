from setuptools import setup, find_packages


setup(
	name='project-library',
	version='0.1.0',
	description='this package contains samples of project-library code',
	author='Roman Leontovych',
	author_email='lordwerneo@gmail.com',
	url='https://github.com/lordwerneo/project-library/',
	install_requires=[],
	packages=find_packages(exclude=('tests*', 'testing*')),
	entry_points={
		'console_scripts': [
			'test_folder-cli = test_folder.test:main',
		]
	}
)
