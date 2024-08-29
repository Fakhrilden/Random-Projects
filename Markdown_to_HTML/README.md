# Markdown to HTML Converter

This is an advanced Python script that converts Markdown files to HTML. The script supports various Markdown extensions like tables, code highlighting, and footnotes, making it a powerful tool for generating HTML documents from Markdown content.

## Features

- **Convert Markdown to HTML**: Easily convert Markdown files to HTML format.
- **Support for Extensions**: Includes support for popular Markdown extensions such as tables, syntax highlighting, and footnotes.
- **Command-Line Interface**: Specify input and output files directly from the command line.
- **Flexible and Customizable**: Choose which Markdown extensions to enable.

## Requirements

- Python 3.x
- `markdown` library
- `pygments` library (for syntax highlighting)

## Installation

1. Clone the repository or download the script file.
2. Install the required Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the script, use the following command format:

```bash
python md_to_html.py <input_markdown_file> <output_html_file> --css <input_styles_file>
