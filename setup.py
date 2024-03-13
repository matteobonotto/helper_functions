from setuptools import setup


setup(
    name='helper_functions',
    version='0.2.0',    
    description='Collection of useful helper functions',
    url='https://github.com/matteobonotto/helper_functions.git',
    author='Matteo Bonotto',
    author_email='matteob.90@hotmail.it',
    # license='BSD 2-clause',
    packages=['helper_functions'],
    install_requires=[
        'numpy',
        'matplotlib',
        'h5py'
        ],
)