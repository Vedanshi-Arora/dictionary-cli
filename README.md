# Dictionary CLI Tool

A command-line interface tool that queries the Merriam-Webster dictionary API to provide word definitions and pronunciations.

![Build Status](https://github.com/Vedanshi-Arora/dictionary-cli/workflows/Dictionary%20CLI%20CI/badge.svg)

## Features

- Look up word definitions from Merriam-Webster dictionary
- Display phonetic pronunciations
- Show multiple definitions when available

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
- Merriam-Webster API key (get it from [Merriam-Webster API](https://dictionaryapi.com/))

## Installation

### From Source

1. Clone the repository:
\```bash
git clone https://github.com/Vedanshi-Arora/dictionary-cli.git
cd dictionary-cli
\```

2. Install dependencies and the package:
\```bash
make install
\```

### Using pip (if published)

\```bash
pip install dictionary-cli
\```

## Configuration

1. Get your API key from [Merriam-Webster API](https://dictionaryapi.com/)

2. Replace the API key in \`src/dictionary_cli/main.py\`:
\```python
API_KEY = 'your-api-key-here'
\```

## Usage

Basic word lookup:
\```bash
dict-cli <word>
\```

Example:
\```bash
dict-cli elephant
\```

Output example :

Pronunciation: ˈe-lə-fənt

Definitions:
1. a thickset, usually extremely large, nearly hairless, herbivorous mammal (family Elephantidae, the elephant family) that has a snout elongated into a muscular trunk and two incisors in the upper jaw developed especially in the male into long ivory tusks:
2. a tall, large-eared mammal (Loxodonta africana) of tropical Africa that is sometimes considered to comprise two separate species (L. africana of sub-Saharan savannas and L. cyclotis of central and western rainforests) —called also African elephant
3. a relatively small-eared mammal (Elephas maximus) of forests of southeastern Asia —called also Asian elephant, Indian elephant

\```

## Development

### Setting Up Development Environment

1. Create a virtual environment:
\```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
\```

2. Install development dependencies:
\```bash
make install
\```

### Build Pipeline

The project uses a three-step build pipeline:

1. Build/Compile:
\```bash
make build
\```

2. Run Tests:
\```bash
make test
\```

3. Create Artifacts:
\```bash
make artifact
\```

Run all steps:
\```bash
make all
\```

### Project Structure

\```
dictionary-cli/
├── src/
│   └── dictionary_cli/
│       ├── __init__.py
│       └── main.py
├── tests/
│   └── test_dictionary.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── Makefile
├── setup.py
├── requirements.txt
└── README.md
\```

### Testing

Run the test suite:
\```bash
make test
\```

The tests will show coverage information and any failing tests.

## Continuous Integration

The project uses GitHub Actions for CI/CD. The pipeline:
- Builds the project
- Runs the test suite
- Produces distributable artifacts

You can view the CI status in the "Actions" tab of the GitHub repository.

## Building

To build the distribution packages:
\```bash
make artifact
\```

This creates:
- Wheel file (.whl)
- Source distribution (.tar.gz)

## Contributing

1. Fork the repository
2. Create your feature branch:
\```bash
git checkout -b feature/new-feature
\```
3. Commit your changes:
\```bash
git commit -am 'Add new feature'
\```
4. Push to the branch:
\```bash
git push origin feature/new-feature
\```
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Merriam-Webster](https://www.merriam-webster.com/) for providing the dictionary API
- Click library for CLI interface
- Pytest for testing framework

## Troubleshooting

### Common Issues

1. API Key Issues:
   - Ensure you\'ve replaced the default API key
   - Verify your API key is active

2. Installation Issues:
   - Make sure you\'re using Python 3.6+
   - Try upgrading pip: \`pip install --upgrade pip\`

3. Build Issues:
   - Clear build artifacts: \`make clean\`
   - Ensure all dependencies are installed: \`make install\`

### Getting Help

If you encounter any issues:
1. Check the [Issues](https://github.com/Vedanshi-Arora/dictionary-cli/issues) page
2. Create a new issue with:
   - Description of the problem
   - Steps to reproduce
   - Expected vs actual behavior

## Version History

- 0.1.0
  - Initial release
  - Basic word lookup functionality
  - Test suite implementation
  - CI pipeline setup


