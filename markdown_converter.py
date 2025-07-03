"""
Markdown to HTML Converter with Live Preview

A professional single-file Python application that converts Markdown files to HTML
with real-time preview capabilities. Built using only Python standard library modules.

"""

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os
import re
import webbrowser
import html
import tempfile
from datetime import datetime


class MarkdownConverter:
    """
    Main application class for the Markdown to HTML Converter.
    
    This class handles the GUI interface, file operations, and conversion logic
    for transforming Markdown content into HTML with live preview functionality.
    """
    
    def __init__(self):
        """Initialize the application with GUI components and default settings."""
        self.root = tk.Tk()
        self.root.title("Markdown to HTML Converter with Live Preview")
        self.root.geometry("800x600")
        self.root.minsize(600, 400)
        
        self.current_file = None
        self.dark_theme = False
        self.auto_save_enabled = False
        self.temp_html_file = None
        
        self.setup_gui()
        self.setup_menu()
        
    def setup_gui(self):
        """Set up the main GUI components including text editor and buttons."""
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        title_label = tk.Label(
            main_frame, 
            text="Markdown to HTML Converter", 
            font=("Arial", 16, "bold")
        )
        title_label.pack(pady=(0, 10))
        
        button_frame = tk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Button(
            button_frame, 
            text="Open File", 
            command=self.open_file,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 10, "bold"),
            relief=tk.RAISED,
            bd=2
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        tk.Button(
            button_frame, 
            text="Live Preview", 
            command=self.live_preview,
            bg="#2196F3",
            fg="white",
            font=("Arial", 10, "bold"),
            relief=tk.RAISED,
            bd=2
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            button_frame, 
            text="Export HTML", 
            command=self.export_html,
            bg="#FF9800",
            fg="white",
            font=("Arial", 10, "bold"),
            relief=tk.RAISED,
            bd=2
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            button_frame, 
            text="Toggle Theme", 
            command=self.toggle_theme,
            bg="#9C27B0",
            fg="white",
            font=("Arial", 10, "bold"),
            relief=tk.RAISED,
            bd=2
        ).pack(side=tk.LEFT, padx=5)
        
        editor_label = tk.Label(main_frame, text="Markdown Editor:", font=("Arial", 12))
        editor_label.pack(anchor=tk.W, pady=(10, 5))
        
        self.text_editor = scrolledtext.ScrolledText(
            main_frame,
            wrap=tk.WORD,
            font=("Consolas", 11),
            bg="#f8f9fa",
            fg="#212529",
            insertbackground="#007bff",
            selectbackground="#007bff",
            selectforeground="white"
        )
        self.text_editor.pack(fill=tk.BOTH, expand=True)
        
        self.text_editor.bind('<KeyRelease>', self.on_text_change)
        
        status_frame = tk.Frame(main_frame)
        status_frame.pack(fill=tk.X, pady=(10, 0))
        
        self.status_label = tk.Label(
            status_frame, 
            text="Ready - Open a Markdown file to begin",
            font=("Arial", 9),
            fg="#6c757d"
        )
        self.status_label.pack(side=tk.LEFT)
        
        self.auto_save_var = tk.BooleanVar()
        auto_save_check = tk.Checkbutton(
            status_frame,
            text="Auto-save",
            variable=self.auto_save_var,
            command=self.toggle_auto_save,
            font=("Arial", 9)
        )
        auto_save_check.pack(side=tk.RIGHT)
        
    def setup_menu(self):
        """Set up the application menu bar with file and help options."""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As", command=self.save_as_file, accelerator="Ctrl+Shift+S")
        file_menu.add_separator()
        file_menu.add_command(label="Export HTML", command=self.export_html, accelerator="Ctrl+E")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit, accelerator="Ctrl+Q")
        
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="View", menu=view_menu)
        view_menu.add_command(label="Live Preview", command=self.live_preview, accelerator="F5")
        view_menu.add_command(label="Toggle Theme", command=self.toggle_theme, accelerator="Ctrl+T")
        
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="Markdown Syntax", command=self.show_syntax_help)
        help_menu.add_command(label="About", command=self.show_about)
        
        self.root.bind('<Control-n>', lambda e: self.new_file())
        self.root.bind('<Control-o>', lambda e: self.open_file())
        self.root.bind('<Control-s>', lambda e: self.save_file())
        self.root.bind('<Control-Shift-S>', lambda e: self.save_as_file())
        self.root.bind('<Control-e>', lambda e: self.export_html())
        self.root.bind('<Control-q>', lambda e: self.root.quit())
        self.root.bind('<F5>', lambda e: self.live_preview())
        self.root.bind('<Control-t>', lambda e: self.toggle_theme())
        
    def markdown_to_html(self, markdown_text):
        """
        Convert Markdown text to HTML using custom parsing rules.
        
        Args:
            markdown_text (str): The input Markdown text to convert
            
        Returns:
            str: The converted HTML content
        """
        if not markdown_text:
            return ""
            
        html_content = html.escape(markdown_text)
        
        html_content = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', html_content, flags=re.MULTILINE)
        html_content = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', html_content, flags=re.MULTILINE)
        html_content = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', html_content, flags=re.MULTILINE)
        html_content = re.sub(r'^#### (.*?)$', r'<h4>\1</h4>', html_content, flags=re.MULTILINE)
        html_content = re.sub(r'^##### (.*?)$', r'<h5>\1</h5>', html_content, flags=re.MULTILINE)
        html_content = re.sub(r'^###### (.*?)$', r'<h6>\1</h6>', html_content, flags=re.MULTILINE)
        
        html_content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html_content)
        html_content = re.sub(r'__(.*?)__', r'<strong>\1</strong>', html_content)
        
        html_content = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html_content)
        html_content = re.sub(r'_(.*?)_', r'<em>\1</em>', html_content)
        
        html_content = re.sub(r'`([^`]+)`', r'<code>\1</code>', html_content)
        
        html_content = re.sub(r'^```(\w*)\n(.*?)\n```$', 
                             lambda m: f'<pre><code class="language-{m.group(1)}">{m.group(2)}</code></pre>',
                             html_content, flags=re.MULTILINE | re.DOTALL)
        
        html_content = re.sub(r'^> (.*?)$', r'<blockquote>\1</blockquote>', 
                             html_content, flags=re.MULTILINE)
        
        html_content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', html_content)
        
        html_content = re.sub(r'^(\d+)\. (.*?)$', r'<ol><li>\2</li></ol>', 
                             html_content, flags=re.MULTILINE)
        
        html_content = re.sub(r'^[-*+] (.*?)$', r'<ul><li>\1</li></ul>', 
                             html_content, flags=re.MULTILINE)
        
        html_content = re.sub(r'</ol>\s*<ol>', '', html_content)
        html_content = re.sub(r'</ul>\s*<ul>', '', html_content)
        
        html_content = re.sub(r'\n\n', '</p><p>', html_content)
        html_content = f'<p>{html_content}</p>'
        
        html_content = re.sub(r'<p></p>', '', html_content)
        html_content = re.sub(r'<p>(<h[1-6]>.*?</h[1-6]>)</p>', r'\1', html_content)
        html_content = re.sub(r'<p>(<(?:ul|ol|blockquote|pre)>.*?</(?:ul|ol|blockquote|pre)>)</p>', 
                             r'\1', html_content, flags=re.DOTALL)
        
        return html_content
        
    def generate_full_html(self, body_content):
        """
        Generate a complete HTML document with styling and metadata.
        
        Args:
            body_content (str): The HTML body content
            
        Returns:
            str: Complete HTML document
        """
        theme_styles = self.get_theme_styles()
        
        html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Markdown Preview</title>
    <style>
        {theme_styles}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Markdown Preview</h1>
            <p class="timestamp">Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </header>
        <main class="content">
            {body_content}
        </main>
    </div>
</body>
</html>"""
        return html_template
        
    def get_theme_styles(self):
        """
        Get CSS styles based on the current theme setting.
        
        Returns:
            str: CSS styles for the current theme
        """
        if self.dark_theme:
            return """
                body {
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                    line-height: 1.6;
                    color: #e9ecef;
                    background-color: #212529;
                    margin: 0;
                    padding: 0;
                }
                .container {
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                }
                header {
                    border-bottom: 2px solid #495057;
                    padding-bottom: 20px;
                    margin-bottom: 30px;
                }
                header h1 {
                    color: #fff;
                    margin: 0;
                    font-size: 2.5em;
                }
                .timestamp {
                    color: #6c757d;
                    font-size: 0.9em;
                    margin: 10px 0 0 0;
                }
                .content h1, .content h2, .content h3, .content h4, .content h5, .content h6 {
                    color: #fff;
                    margin-top: 30px;
                    margin-bottom: 15px;
                }
                .content h1 { font-size: 2.2em; }
                .content h2 { font-size: 1.8em; }
                .content h3 { font-size: 1.5em; }
                code {
                    background-color: #495057;
                    color: #f8f9fa;
                    padding: 2px 6px;
                    border-radius: 4px;
                    font-family: 'Consolas', 'Monaco', monospace;
                }
                pre {
                    background-color: #343a40;
                    color: #f8f9fa;
                    padding: 15px;
                    border-radius: 8px;
                    overflow-x: auto;
                    border-left: 4px solid #007bff;
                }
                blockquote {
                    border-left: 4px solid #6c757d;
                    padding-left: 20px;
                    margin: 20px 0;
                    color: #adb5bd;
                    font-style: italic;
                }
                a {
                    color: #007bff;
                    text-decoration: none;
                }
                a:hover {
                    text-decoration: underline;
                }
                ul, ol {
                    padding-left: 25px;
                }
                li {
                    margin-bottom: 8px;
                }
                p {
                    margin-bottom: 16px;
                }
            """
        else:
            return """
                body {
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                    line-height: 1.6;
                    color: #212529;
                    background-color: #ffffff;
                    margin: 0;
                    padding: 0;
                }
                .container {
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                }
                header {
                    border-bottom: 2px solid #dee2e6;
                    padding-bottom: 20px;
                    margin-bottom: 30px;
                }
                header h1 {
                    color: #343a40;
                    margin: 0;
                    font-size: 2.5em;
                }
                .timestamp {
                    color: #6c757d;
                    font-size: 0.9em;
                    margin: 10px 0 0 0;
                }
                .content h1, .content h2, .content h3, .content h4, .content h5, .content h6 {
                    color: #343a40;
                    margin-top: 30px;
                    margin-bottom: 15px;
                }
                .content h1 { font-size: 2.2em; }
                .content h2 { font-size: 1.8em; }
                .content h3 { font-size: 1.5em; }
                code {
                    background-color: #f8f9fa;
                    color: #e83e8c;
                    padding: 2px 6px;
                    border-radius: 4px;
                    font-family: 'Consolas', 'Monaco', monospace;
                    border: 1px solid #dee2e6;
                }
                pre {
                    background-color: #f8f9fa;
                    color: #212529;
                    padding: 15px;
                    border-radius: 8px;
                    overflow-x: auto;
                    border-left: 4px solid #007bff;
                    border: 1px solid #dee2e6;
                }
                blockquote {
                    border-left: 4px solid #007bff;
                    padding-left: 20px;
                    margin: 20px 0;
                    color: #6c757d;
                    font-style: italic;
                    background-color: #f8f9fa;
                    padding: 15px 20px;
                    border-radius: 4px;
                }
                a {
                    color: #007bff;
                    text-decoration: none;
                }
                a:hover {
                    text-decoration: underline;
                }
                ul, ol {
                    padding-left: 25px;
                }
                li {
                    margin-bottom: 8px;
                }
                p {
                    margin-bottom: 16px;
                }
            """
    
    def open_file(self):
        """Open and load a Markdown file into the editor."""
        file_path = filedialog.askopenfilename(
            title="Open Markdown File",
            filetypes=[
                ("Markdown files", "*.md *.markdown *.mdown *.mkd"),
                ("Text files", "*.txt"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    
                self.text_editor.delete(1.0, tk.END)
                self.text_editor.insert(1.0, content)
                
                self.current_file = file_path
                filename = os.path.basename(file_path)
                self.root.title(f"Markdown Converter - {filename}")
                self.update_status(f"Opened: {filename}")
                
            except FileNotFoundError:
                messagebox.showerror("Error", "File not found.")
            except UnicodeDecodeError:
                messagebox.showerror("Error", "Unable to decode file. Please ensure it's a valid text file.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while opening the file: {str(e)}")
    
    def new_file(self):
        """Create a new empty document."""
        if self.text_editor.get(1.0, tk.END).strip():
            if messagebox.askyesno("New File", "Current content will be lost. Continue?"):
                self.text_editor.delete(1.0, tk.END)
                self.current_file = None
                self.root.title("Markdown Converter - New Document")
                self.update_status("New document created")
        else:
            self.text_editor.delete(1.0, tk.END)
            self.current_file = None
            self.root.title("Markdown Converter - New Document")
            self.update_status("New document created")
    
    def save_file(self):
        """Save the current document."""
        if self.current_file:
            try:
                content = self.text_editor.get(1.0, tk.END)
                with open(self.current_file, 'w', encoding='utf-8') as file:
                    file.write(content)
                self.update_status(f"Saved: {os.path.basename(self.current_file)}")
            except Exception as e:
                messagebox.showerror("Error", f"Unable to save file: {str(e)}")
        else:
            self.save_as_file()
    
    def save_as_file(self):
        """Save the current document with a new filename."""
        file_path = filedialog.asksaveasfilename(
            title="Save Markdown File",
            defaultextension=".md",
            filetypes=[
                ("Markdown files", "*.md"),
                ("Text files", "*.txt"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            try:
                content = self.text_editor.get(1.0, tk.END)
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content)
                
                self.current_file = file_path
                filename = os.path.basename(file_path)
                self.root.title(f"Markdown Converter - {filename}")
                self.update_status(f"Saved as: {filename}")
                
            except Exception as e:
                messagebox.showerror("Error", f"Unable to save file: {str(e)}")
    
    def live_preview(self):
        """Generate and display live preview of the Markdown content."""
        markdown_content = self.text_editor.get(1.0, tk.END)
        
        if not markdown_content.strip():
            messagebox.showwarning("Warning", "No content to preview.")
            return
            
        try:
            html_body = self.markdown_to_html(markdown_content)
            full_html = self.generate_full_html(html_body)
            
            if self.temp_html_file and os.path.exists(self.temp_html_file):
                os.remove(self.temp_html_file)
            
            temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.html', 
                                                  delete=False, encoding='utf-8')
            temp_file.write(full_html)
            temp_file.close()
            
            self.temp_html_file = temp_file.name
            
            webbrowser.open(f'file://{os.path.abspath(self.temp_html_file)}')
            self.update_status("Live preview opened in browser")
            
        except Exception as e:
            messagebox.showerror("Error", f"Unable to generate preview: {str(e)}")
    
    def export_html(self):
        """Export the converted HTML to a file."""
        markdown_content = self.text_editor.get(1.0, tk.END)
        
        if not markdown_content.strip():
            messagebox.showwarning("Warning", "No content to export.")
            return
            
        file_path = filedialog.asksaveasfilename(
            title="Export HTML File",
            defaultextension=".html",
            filetypes=[
                ("HTML files", "*.html *.htm"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            try:
                html_body = self.markdown_to_html(markdown_content)
                full_html = self.generate_full_html(html_body)
                
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(full_html)
                
                filename = os.path.basename(file_path)
                self.update_status(f"Exported: {filename}")
                messagebox.showinfo("Success", f"HTML exported successfully to {filename}")
                
            except Exception as e:
                messagebox.showerror("Error", f"Unable to export HTML: {str(e)}")
    
    def toggle_theme(self):
        """Toggle between light and dark preview themes."""
        self.dark_theme = not self.dark_theme
        theme_name = "Dark" if self.dark_theme else "Light"
        self.update_status(f"Preview theme: {theme_name}")
        messagebox.showinfo("Theme Changed", f"Preview theme changed to {theme_name}. Generate a new preview to see changes.")
    
    def toggle_auto_save(self):
        """Toggle the auto-save functionality."""
        self.auto_save_enabled = self.auto_save_var.get()
        status = "enabled" if self.auto_save_enabled else "disabled"
        self.update_status(f"Auto-save {status}")
    
    def on_text_change(self, event=None):
        """Handle text changes in the editor for auto-save functionality."""
        if self.auto_save_enabled and self.current_file:
            self.save_file()
    
    def update_status(self, message):
        """
        Update the status bar with a new message.
        
        Args:
            message (str): The status message to display
        """
        self.status_label.config(text=message)
        self.root.update_idletasks()
    
    def show_syntax_help(self):
        """Display a help window with Markdown syntax information."""
        help_window = tk.Toplevel(self.root)
        help_window.title("Markdown Syntax Help")
        help_window.geometry("600x500")
        help_window.resizable(True, True)
        
        help_text = scrolledtext.ScrolledText(help_window, wrap=tk.WORD, 
                                            font=("Consolas", 10))
        help_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        syntax_guide = """
MARKDOWN SYNTAX REFERENCE

HEADERS
# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6

TEXT FORMATTING
**Bold text** or __Bold text__
*Italic text* or _Italic text_
`Inline code`

CODE BLOCKS
```python
def hello_world():
    print("Hello, World!")
```

LISTS
Unordered:
- Item 1
- Item 2
  - Nested item

Ordered:
1. First item
2. Second item
3. Third item

LINKS
[Link text](https://example.com)

BLOCKQUOTES
> This is a blockquote
> It can span multiple lines

PARAGRAPHS
Separate paragraphs with blank lines.

This is a new paragraph.

SUPPORTED FEATURES
- Headers (H1-H6)
- Bold and italic text
- Inline and block code
- Ordered and unordered lists
- Links
- Blockquotes
- Paragraphs
        """
        
        help_text.insert(1.0, syntax_guide)
        help_text.config(state=tk.DISABLED)
    
    def show_about(self):
        """Display application information and credits."""
        about_text = """Markdown to HTML Converter with Live Preview
Version 1.0.0

A professional single-file Python application for converting 
Markdown files to HTML with real-time preview capabilities.

Features:
- Live HTML preview in browser
- Dark and light themes
- Export to HTML
- Auto-save functionality
- Comprehensive Markdown support
- Built with Python standard library only

Supported Markdown Elements:
- Headers (H1-H6)
- Bold and italic text
- Code blocks and inline code
- Lists (ordered and unordered)
- Links
- Blockquotes
- Paragraphs

Built with: Python 3.x, tkinter, and standard library modules
Date: July 3, 2025"""
        
        messagebox.showinfo("About", about_text)
    
    def cleanup(self):
        """Clean up temporary files before closing the application."""
        if self.temp_html_file and os.path.exists(self.temp_html_file):
            try:
                os.remove(self.temp_html_file)
            except:
                pass
    
    def run(self):
        """Start the application main loop."""
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
    
    def on_closing(self):
        """Handle application closing event."""
        self.cleanup()
        self.root.destroy()


def main():
    """
    Main entry point for the application.
    Creates and runs the Markdown converter application.
    """
    app = MarkdownConverter()
    app.run()


if __name__ == "__main__":
    main()
