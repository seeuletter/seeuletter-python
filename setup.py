try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

setup(
    name='seeuletter',
    version='1.0.0',
    author='Seeuletter',
    author_email='hello@seeuletter.com',
    packages=['seeuletter'],
    description='Seeuletter Python Bindings',
    url='https://www.seeuletter.com',
    license='MIT',
    install_requires=[
        'requests'
        ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy"
    ]
)
