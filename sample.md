# Sample Markdown Document

This is a sample Markdown document to demonstrate the capabilities of the Markdown to HTML Converter application.

## Text Formatting Examples

Here are various text formatting options supported by the converter:

**Bold text using double asterisks**
__Bold text using double underscores__

*Italic text using single asterisks*
_Italic text using single underscores_

You can also combine formatting: **bold and *italic* text** together.

## Code Examples

### Inline Code
Use `print("Hello, World!")` to display a message in Python.

### Code Blocks

Here's a Python function example:

```python
def calculate_fibonacci(n):
    if n <= 1:
        return n
    else:
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

result = calculate_fibonacci(10)
print(f"The 10th Fibonacci number is: {result}")
```

JavaScript example:

```javascript
function greetUser(name) {
    return `Hello, ${name}! Welcome to our application.`;
}

const message = greetUser("Developer");
console.log(message);
```

## Lists

### Unordered Lists
- First item in the list
- Second item with some details
- Third item
  - Nested item A
  - Nested item B
- Fourth item

### Ordered Lists
1. Primary objective
2. Secondary goals
3. Implementation steps
4. Testing procedures
5. Documentation requirements

## Links and References

Visit the [Python Official Website](https://www.python.org) for more information about Python programming.

You can also check out [GitHub](https://github.com) for open source projects.

## Blockquotes

> "The best way to predict the future is to create it."
> - Peter Drucker

> This is a longer blockquote that demonstrates
> how multiple lines are handled in the conversion
> process. The formatting should be preserved
> across line breaks.

## Headers Hierarchy

# Main Title (H1)
## Section Title (H2)
### Subsection Title (H3)
#### Sub-subsection Title (H4)
##### Minor Heading (H5)
###### Smallest Heading (H6)

## Technical Documentation

This converter supports the most commonly used Markdown syntax elements:

- Headers from H1 to H6
- Bold and italic text formatting
- Inline code and code blocks with syntax highlighting
- Ordered and unordered lists
- Hyperlinks
- Blockquotes for citations and emphasis
- Proper paragraph separation

## Project Features

The Markdown to HTML Converter includes several advanced features:

1. **Live Preview**: Real-time HTML preview in your default browser
2. **Theme Support**: Toggle between light and dark themes
3. **Auto-save**: Automatic saving of your work
4. **Export Functionality**: Save converted HTML to files
5. **Professional Interface**: Clean, intuitive user interface
6. **Keyboard Shortcuts**: Quick access to common functions

## Usage Instructions

To use this application effectively:

1. Open the application by running `python markdown_converter.py`
2. Create a new document or open an existing Markdown file
3. Edit your content in the text editor
4. Click "Live Preview" to see the HTML output
5. Use "Export HTML" to save your converted document

## Sample Content Types

### Meeting Notes
**Date**: July 3, 2025
**Attendees**: Development Team

**Agenda Items**:
- Project status review
- Technical requirements discussion
- Timeline planning

**Action Items**:
1. Complete documentation updates
2. Implement remaining features
3. Conduct testing procedures

### Technical Specifications

The application is built using:
- **Language**: Python 3.6+
- **GUI Framework**: tkinter
- **Dependencies**: Standard library only
- **Supported Formats**: Markdown (.md), Text (.txt)
- **Output Formats**: HTML (.html)

### Code Documentation

When documenting code, you can include examples like this:

```python
class MarkdownConverter:
    def __init__(self):
        self.setup_gui()
        self.setup_menu()
    
    def markdown_to_html(self, markdown_text):
        # Conversion logic here
        return converted_html
```

This sample document demonstrates all the major Markdown features supported by the converter. You can use this as a template for creating your own documents or as a test file to verify the application's functionality.
