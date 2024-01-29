from setuptools import setup, find_packages

setup(
    name='logger',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # Dependencies listed in requirements.txt can also go here
        "colorama",
        "termcolor"
    ],
    # Add other parameters as necessary
)