from setuptools import setup


setup(
    name='helper_functions',
    version='0.1.0',    
    description='Collection of useful helper functions',
    url='https://github.com/matteobonotto/helper_functions.git',
    author='Matteo Bonotto',
    author_email='matteob.90@hotmail.it',
    # license='BSD 2-clause',
    packages=['helper_functions'],
    install_requires=[
        'numpy',
        'matplotlib',
        ],
    # classifiers=[
    #     'Development Status :: 1 - Planning',
    #     'Intended Audience :: Science/Research',
    #     'License :: OSI Approved :: BSD License',  
    #     'Operating System :: POSIX :: Linux',        
    #     'Programming Language :: Python :: 2',
    #     'Programming Language :: Python :: 2.7',
    #     'Programming Language :: Python :: 3',
    #     'Programming Language :: Python :: 3.4',
    #     'Programming Language :: Python :: 3.5',
    # ],
)