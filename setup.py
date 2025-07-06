from setuptools import setup, find_packages

setup(
    name="dictionary-cli",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'requests',
        'click',
    ],
    entry_points={
        'console_scripts': [
            'dict-cli=dictionary_cli.main:cli',
        ],
    },
)

