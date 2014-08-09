from setuptools import setup

setup(
    name="lexical-uuid",
    version="0.1.0",
    url='http://github.com/samuraisam/lexical_uuid',
    author='Samuel Sutch',
    author_email='sam@sutch.net',
    description='A sensible class for dealing with Lexical UUIDs',
    long_description=
"""
lexical_uuid is a lightweight Python library for sensibly dealing with Lexical UUIDs. Handy when you want a roughly-ordered primary key for your database that any node in your system can generate.
""",
    packages=['lexical_uuid'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ]
)
