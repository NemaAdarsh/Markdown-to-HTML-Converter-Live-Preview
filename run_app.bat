@echo off
title Markdown to HTML Converter Launcher

echo Markdown to HTML Converter with Live Preview
echo =============================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.6 or higher from https://python.org
    echo.
    pause
    exit /b 1
)

echo Python found. Checking application files...

REM Check if main application file exists
if not exist "markdown_converter.py" (
    echo Error: markdown_converter.py not found
    echo Please ensure the application file is in the same directory
    echo.
    pause
    exit /b 1
)

echo Application file found. Starting Markdown to HTML Converter...
echo.

REM Run the application
python markdown_converter.py

REM If we get here, the application has closed
echo.
echo Application closed.
pause
