from setuptools import setup, find_packages

setup(
    name = "DiffieHellman",
    version = "0.1",
    packages = find_packages(exclude=['tests']),

    setup_requires = ['nose >= 1.0', 'coverage'],
)
