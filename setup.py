from setuptools import setup, find_packages

setup(
    name="dictionary-cli",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'requests>=2.31.0',
        'click>=8.1.3',
    ],
    entry_points={
        'console_scripts': [
            'dict-cli=dictionary_cli.main:cli',
        ],
    },
    python_requires='>=3.6',
    author="Your Name",
    author_email="your.email@example.com",
    description="A CLI tool for querying Merriam-Webster dictionary",
    long_description="A command-line interface tool to query the Merriam-Webster dictionary.",
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

