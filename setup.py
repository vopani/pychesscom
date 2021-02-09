import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read()

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pychesscom',
    version=version,
    author='Rohan Rao',
    author_email='rohanrao88@gmail.com',
    description='An asynchronous Python client for Chess.com\'s API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/vopani/pychesscom',
    project_urls={
        'Documentation': 'https://pychesscom.readthedocs.io/',
        'Source': 'https://github.com/vopani/pychesscom',
        'Tracker': 'https://github.com/vopani/pychesscom/issues'
    },
    python_requires='>=3.7',
    install_requires=[
        'aiohttp'
    ],
    license='Apache License, Version 2.0',
    platforms='any',
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    keywords=[
        'api',
        'async',
        'chess',
        'client'
    ]
)