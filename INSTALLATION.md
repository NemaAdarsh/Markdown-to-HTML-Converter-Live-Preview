# Installation and Setup Guide

## Quick Start

### Windows
1. Ensure Python 3.6+ is installed
2. Download `markdown_converter.py`
3. Double-click the file or run from command prompt:
   ```cmd
   python markdown_converter.py
   ```

### macOS
1. Ensure Python 3.6+ is installed
2. Download `markdown_converter.py`
3. Open Terminal and navigate to the file location
4. Run the application:
   ```bash
   python3 markdown_converter.py
   ```

### Linux
1. Ensure Python 3.6+ is installed with tkinter support
2. Download `markdown_converter.py`
3. Open terminal and navigate to the file location
4. Run the application:
   ```bash
   python3 markdown_converter.py
   ```

## Detailed Installation Instructions

### Step 1: Python Installation

#### Windows
1. Visit [python.org](https://www.python.org/downloads/)
2. Download Python 3.6 or later
3. Run installer with "Add Python to PATH" checked
4. Verify installation:
   ```cmd
   python --version
   ```

#### macOS
1. Install using Homebrew (recommended):
   ```bash
   brew install python
   ```
2. Or download from [python.org](https://www.python.org/downloads/)
3. Verify installation:
   ```bash
   python3 --version
   ```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-tk
```

#### Linux (CentOS/RHEL)
```bash
sudo yum install python3 tkinter
```

### Step 2: Download Application
1. Download `markdown_converter.py` to your desired location
2. Optionally download `sample.md` for testing

### Step 3: Verify Requirements
Run the verification script from `requirements.txt` to ensure all dependencies are available.

### Step 4: First Run
1. Navigate to the application directory
2. Run the application using the appropriate Python command for your system
3. The GUI should appear with an empty editor

## Troubleshooting Installation

### Common Issues

#### "python is not recognized" (Windows)
- Python is not in system PATH
- Reinstall Python with "Add to PATH" option
- Or use full path: `C:\Python39\python.exe markdown_converter.py`

#### "tkinter not found" (Linux)
- Install tkinter package:
  ```bash
  sudo apt install python3-tk
  ```

#### Permission denied (macOS/Linux)
- Make file executable:
  ```bash
  chmod +x markdown_converter.py
  ```

#### Import errors
- Verify Python version is 3.6+
- Ensure standard library is complete
- Try different Python installation

### Performance Optimization

#### For better performance:
1. Use Python 3.8+ for improved performance
2. Ensure adequate RAM (512MB+ recommended)
3. Use SSD storage for faster file operations
4. Close other applications when working with large files

### Development Setup

#### For development or customization:
1. Use a code editor with Python support
2. Install development tools:
   ```bash
   pip install black flake8 mypy
   ```
3. Follow PEP 8 coding standards
4. Test on multiple platforms

## Configuration Options

### Default Settings
The application starts with these default settings:
- Light theme enabled
- Auto-save disabled
- Window size: 800x600 pixels
- Font: Consolas 11pt (editor)

### Customization
You can modify these settings by editing the source code:
- Change default window size in `__init__` method
- Modify default font in `setup_gui` method
- Adjust theme colors in `get_theme_styles` method

## File Structure

After installation, your directory should contain:
```
Markdown to HTML Converter (Live Preview)/
├── markdown_converter.py    # Main application file
├── README.md               # Comprehensive documentation
├── requirements.txt        # System requirements
├── INSTALLATION.md         # This installation guide
└── sample.md              # Sample Markdown file for testing
```

## Testing Installation

### Basic Functionality Test
1. Start the application
2. Open `sample.md` file
3. Click "Live Preview"
4. Verify HTML opens in browser
5. Try editing text and previewing again

### Feature Test Checklist
- [ ] Application starts without errors
- [ ] File menu functions work
- [ ] Text editor accepts input
- [ ] Live preview opens in browser
- [ ] Theme toggle works
- [ ] Export HTML function works
- [ ] Keyboard shortcuts respond
- [ ] Help dialogs display correctly

## Next Steps

After successful installation:
1. Read the main README.md for complete documentation
2. Try the sample.md file to understand features
3. Create your first Markdown document
4. Explore the help system within the application
5. Customize settings as needed

## Support

If you encounter issues during installation:
1. Check the troubleshooting section above
2. Verify system requirements
3. Ensure Python and tkinter are properly installed
4. Test with the provided sample file

The application is designed to work out-of-the-box with a standard Python installation, requiring no additional dependencies or complex setup procedures.
