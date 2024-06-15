# Simple Text Editor Application

This is a simple text editor application built using Python and Tkinter.

## Technologies Used

- **Python**: Programming language used for the application logic.
- **Tkinter**: Python's de-facto standard GUI (Graphical User Interface) package.
- **PyInstaller**: Used for packaging the Python application into standalone executables.
- **Git**: Version control system for managing and tracking changes to the project.
- **GitHub**: Platform for hosting the repository and collaborating with others.

## Features

- Create new files, open existing files, and save files.
- Undo and redo functionality for text editing.
- Cut, copy, and paste operations.
- Print functionality (not yet fully implemented in the provided code).

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/text-editor.git
   cd text-editor
    ```

2. **Install Dependencies**
Ensure you have Python installed. Install necessary dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application**

Execute the following command to run the text editor

    ```bash
    python app.py
    ```

4. **Package the Application (Optional)**
If you want to create standalone executables for distribution:

    ```bash
    pip install pyinstaller
    pyinstaller app.spec
    ```