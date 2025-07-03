# Markdown to HTML Converter with Live Preview

A professional single-file Python application that converts Markdown files to HTML with real-time preview capabilities. Built using only Python standard library modules for maximum portability and offline functionality.

## Overview

The Markdown to HTML Converter is designed for technical writers, developers, and students who need a portable, offline-friendly Markdown editing experience. The application provides real-time conversion from Markdown syntax to clean HTML with instant browser preview capabilities.

## Features

### Core Functionality
- **Live Preview**: Instantly preview Markdown content as HTML in your default web browser
- **File Operations**: Open, create, save, and export Markdown and HTML files
- **Real-time Editing**: Edit Markdown content with immediate feedback
- **Clean HTML Output**: Generate well-structured HTML from Markdown syntax

### Markdown Support
- Headers (H1 through H6)
- Text formatting (bold, italic)
- Code blocks and inline code
- Ordered and unordered lists
- Links
- Blockquotes
- Paragraph formatting

### User Interface Features
- **Professional GUI**: Clean, intuitive interface built with tkinter
- **Menu System**: Comprehensive menu with keyboard shortcuts
- **Status Bar**: Real-time feedback on application state
- **Scrollable Editor**: Large text editing area with scroll support

### Advanced Features
- **Theme Toggle**: Switch between light and dark preview themes
- **Auto-save**: Optional automatic saving of changes
- **HTML Export**: Export converted content to standalone HTML files
- **Syntax Help**: Built-in Markdown syntax reference
- **Keyboard Shortcuts**: Quick access to common functions

## Requirements

### System Requirements
- Python 3.6 or higher
- Windows, macOS, or Linux operating system
- Default web browser for preview functionality

### Dependencies
The application uses only Python standard library modules:
- `tkinter` - GUI framework
- `os` - Operating system interface
- `re` - Regular expressions
- `webbrowser` - Browser control
- `html` - HTML utilities
- `tempfile` - Temporary file handling
- `datetime` - Date and time utilities

## Installation

### Method 1: Direct Download
1. Download the `markdown_converter.py` file
2. Ensure Python 3.6+ is installed on your system
3. Run the application directly

### Method 2: Clone Repository
```bash
git clone https://github.com/NemaAdarsh/Markdown-to-HTML-Converter-Live-Preview.git
cd "Markdown to HTML Converter (Live Preview)"
```

## Usage

### Starting the Application
```bash
python markdown_converter.py
```

### Basic Workflow
1. **Open or Create**: Use "File > Open" to load an existing Markdown file or "File > New" to start fresh
2. **Edit Content**: Type or paste Markdown content in the editor
3. **Live Preview**: Click "Live Preview" or press F5 to see HTML output in browser
4. **Save Work**: Use "File > Save" to save your Markdown file
5. **Export HTML**: Use "File > Export HTML" to create standalone HTML files

### Keyboard Shortcuts
- `Ctrl+N` - New file
- `Ctrl+O` - Open file
- `Ctrl+S` - Save file
- `Ctrl+Shift+S` - Save as
- `Ctrl+E` - Export HTML
- `F5` - Live preview
- `Ctrl+T` - Toggle theme
- `Ctrl+Q` - Quit application

### Menu Navigation
#### File Menu
- **New**: Create a new document
- **Open**: Load existing Markdown files
- **Save**: Save current document
- **Save As**: Save with new filename
- **Export HTML**: Generate standalone HTML file
- **Exit**: Close application

#### View Menu
- **Live Preview**: Open preview in browser
- **Toggle Theme**: Switch between light and dark themes

#### Help Menu
- **Markdown Syntax**: Display syntax reference
- **About**: Application information

## Markdown Syntax Support

### Headers
```markdown
# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6
```

### Text Formatting
```markdown
**Bold text** or __Bold text__
*Italic text* or _Italic text_
`Inline code`
```

### Code Blocks
```markdown
```python
def hello_world():
    print("Hello, World!")
```
```

### Lists
```markdown
Unordered List:
- Item 1
- Item 2
- Item 3

Ordered List:
1. First item
2. Second item
3. Third item
```

### Links
```markdown
[Link text](https://example.com)
```

### Blockquotes
```markdown
> This is a blockquote
> It can span multiple lines
```

## Configuration Options

### Theme Settings
- **Light Theme**: Clean, professional appearance with light background
- **Dark Theme**: Modern dark interface for reduced eye strain
- Theme changes apply to HTML preview output

### Auto-save Functionality
- Enable auto-save to automatically save changes as you type
- Requires an existing file to be opened
- Toggle via checkbox in status bar

## Technical Architecture

### Application Structure
The application follows a single-class design pattern with the `MarkdownConverter` class handling:
- GUI initialization and management
- File operations and error handling
- Markdown to HTML conversion logic
- Browser integration for live preview
- Theme management and styling

### Conversion Process
1. **Input Processing**: Raw Markdown text is captured from the editor
2. **HTML Escaping**: Special characters are properly escaped
3. **Pattern Matching**: Regular expressions identify and convert Markdown syntax
4. **HTML Generation**: Structured HTML output is created with proper styling
5. **Template Integration**: Complete HTML document with CSS styling is generated
6. **Output Delivery**: Final HTML is written to temporary file and opened in browser

### File Handling
- **Encoding**: UTF-8 encoding for international character support
- **Temporary Files**: Preview HTML files are created in system temp directory
- **Cleanup**: Automatic cleanup of temporary files on application exit
- **Error Handling**: Comprehensive error handling for file operations

## Error Handling

The application includes robust error handling for:
- File not found errors
- Encoding/decoding issues
- Permission errors
- Browser launch failures
- Invalid file formats

Error messages are displayed via user-friendly dialog boxes with specific information about the issue and suggested solutions.

## Troubleshooting

### Common Issues

#### Application Won't Start
- Verify Python 3.6+ is installed
- Check that tkinter is available (usually included with Python)
- Ensure you have proper permissions to run Python scripts

#### Preview Not Opening
- Verify default browser is properly configured
- Check system permissions for temporary file creation
- Ensure browser can access local files

#### File Save Issues
- Verify write permissions for target directory
- Check available disk space
- Ensure filename is valid for your operating system

#### Display Issues
- Update your system's display drivers
- Try running with different Python versions
- Check system compatibility with tkinter

### Performance Optimization
- For large files, consider breaking content into smaller sections
- Use auto-save judiciously with very large documents
- Close unused preview windows to free system resources

## Contributing

### Code Style Guidelines
- Follow PEP 8 Python style guidelines
- Use descriptive variable and function names
- Include comprehensive docstrings for all functions and classes
- Maintain consistent indentation and formatting

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make changes with proper documentation
4. Test thoroughly on multiple platforms
5. Submit pull request with detailed description

### Testing Checklist
- Test file operations (open, save, export)
- Verify Markdown conversion accuracy
- Check browser preview functionality
- Test theme switching
- Validate error handling
- Confirm keyboard shortcuts work

## Version History

### Version 1.0.0 (July 3, 2025)
- Initial release
- Complete Markdown to HTML conversion
- Live preview functionality
- Theme support (light/dark)
- Auto-save capability
- Comprehensive GUI with menus and shortcuts
- Built-in help system
- Export functionality

## Support and Documentation

### Getting Help
- Use the built-in help system (Help > Markdown Syntax)
- Refer to this README for comprehensive documentation
- Check the About dialog for version information

### System Requirements Verification
To verify your system meets the requirements:
```python
import sys
print(f"Python version: {sys.version}")
import tkinter
print("tkinter is available")
```

### File Format Support
- **Input**: .md, .markdown, .mdown, .mkd, .txt files
- **Output**: .html, .htm files
- **Encoding**: UTF-8 (recommended for international characters)

This application provides a complete, professional solution for Markdown editing and HTML conversion without requiring external dependencies or internet connectivity.
