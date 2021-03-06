from setuptools import setup, find_packages

__version__ = '0.1.22'

setup(
    name='vmnet',
    version=__version__,
    description='A test-suite for distributed networks',
    packages=find_packages(exclude=['docs', 'examples']),
    install_requires=open('requirements.txt').readlines(),
    url='https://github.com/Lamden/vmnet',
    author='Lamden',
    email='team@lamden.io',
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
)
