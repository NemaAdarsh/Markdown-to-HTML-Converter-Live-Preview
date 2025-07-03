"""
System Verification and Application Launcher

This script verifies system requirements and launches the Markdown to HTML Converter.
Run this script to ensure your system is properly configured.
"""

import sys
import os

def check_python_version():
    """Check if Python version meets requirements."""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 6:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro} (meets requirement 3.6+)")
        return True
    else:
        print(f"✗ Python {version.major}.{version.minor}.{version.micro} (requires 3.6+)")
        return False

def check_required_modules():
    """Check if all required modules are available."""
    required_modules = {
        'tkinter': 'GUI framework',
        'os': 'Operating system interface',
        're': 'Regular expressions',
        'webbrowser': 'Browser control',
        'html': 'HTML utilities',
        'tempfile': 'Temporary file handling',
        'datetime': 'Date and time utilities'
    }
    
    missing_modules = []
    
    print("\nChecking required modules:")
    for module, description in required_modules.items():
        try:
            __import__(module)
            print(f"✓ {module} - {description}")
        except ImportError:
            print(f"✗ {module} - {description} (MISSING)")
            missing_modules.append(module)
    
    return len(missing_modules) == 0, missing_modules

def check_application_file():
    """Check if the main application file exists."""
    app_file = "markdown_converter.py"
    if os.path.exists(app_file):
        print(f"\n✓ Application file '{app_file}' found")
        return True
    else:
        print(f"\n✗ Application file '{app_file}' not found")
        return False

def launch_application():
    """Launch the Markdown to HTML Converter application."""
    try:
        print("\nLaunching Markdown to HTML Converter...")
        import markdown_converter
        markdown_converter.main()
    except Exception as e:
        print(f"\n✗ Error launching application: {e}")
        return False
    return True

def main():
    """Main verification and launch function."""
    print("Markdown to HTML Converter - System Verification")
    print("=" * 50)
    
    # Check Python version
    python_ok = check_python_version()
    
    # Check required modules
    modules_ok, missing = check_required_modules()
    
    # Check application file
    app_file_ok = check_application_file()
    
    print("\n" + "=" * 50)
    
    if python_ok and modules_ok and app_file_ok:
        print("✓ All system requirements satisfied!")
        
        response = input("\nWould you like to launch the application now? (y/n): ")
        if response.lower() in ['y', 'yes']:
            launch_application()
        else:
            print("\nTo launch manually, run: python markdown_converter.py")
    else:
        print("✗ System requirements not met. Please address the following:")
        
        if not python_ok:
            print("  - Install Python 3.6 or higher")
        
        if not modules_ok:
            print(f"  - Install missing modules: {', '.join(missing)}")
            if 'tkinter' in missing:
                print("    Note: tkinter is usually included with Python")
                print("    On Linux, you may need: sudo apt install python3-tk")
        
        if not app_file_ok:
            print("  - Ensure 'markdown_converter.py' is in the current directory")

if __name__ == "__main__":
    main()
