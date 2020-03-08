from setuptools import setup, find_packages
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
VERSION_FILE = os.path.join(BASE_DIR, "steelflask", "version.py")

setup(
    name='steelflask',
    packages=find_packages(
        exclude=('tests', 'tests.*')
    ),
    include_package_data=True,
    zip_safe=False,
    use_scm_version=True,
    entry_points={
        'console_scripts': [
            'steelflask=steelflask.cli:steelflask'
        ],
    },
    setup_requires=['setuptools_scm'],
    install_requires=[
        'Click>=7.0',
        'Mako>=1.1.2'
    ],
)
