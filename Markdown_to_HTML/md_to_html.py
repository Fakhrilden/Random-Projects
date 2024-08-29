import markdown
import argparse
import os

def markdown_to_html(input_file, output_file, extensions=None, css_file=None):

    # Read the Markdown content from the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        markdown_text = f.read()

    # Convert Markdown to HTML with specified extensions
    html = markdown.markdown(markdown_text, extensions=extensions)

    # Read the CSS content if provided
    if css_file:
        with open(css_file, 'r', encoding='utf-8') as f:
            css = f.read()
        # Insert the CSS into a <style> tag in the <head> section
        html = f"<html><head><style>{css}</style></head><body>{html}</body></html>"
    else:
        # Basic HTML structure without CSS
        html = f"<html><head></head><body>{html}</body></html>"

    # Write the HTML content to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Conversion complete. HTML output saved to {output_file}")

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Convert Markdown to HTML with optional CSS styling.")
    parser.add_argument('input', type=str, help='Path to the input Markdown file')
    parser.add_argument('output', type=str, help='Path to the output HTML file')
    parser.add_argument('--extensions', type=str, nargs='*', default=['extra', 'codehilite', 'tables', 'footnotes'], help='Markdown extensions to enable')
    parser.add_argument('--css', type=str, help='Path to a CSS file for styling the HTML output')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Check if input file exists
    if not os.path.exists(args.input):
        print(f"Error: The file {args.input} does not exist.")
        return

    # Convert Markdown to HTML with the specified options
    markdown_to_html(args.input, args.output, extensions=args.extensions, css_file=args.css)

if __name__ == "__main__":
    main()
