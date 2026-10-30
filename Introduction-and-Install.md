# Introduction 

 PySide6 is the official Python library that provides language bindings for the Qt6 framework, allowing developers to create cross-platform GUIs. 



# Basic - Installation 
 
 ## 1. Check your Python version
The PySide6 package on PyPI currently specifies Python 3.10 or newer and below Python 3.16. Use a supported Python version, and run the commands below in your terminal—not inside the Python interactive prompt.

macOS:
`python3 --version`

Windows:
`py --version`

If the command is not recognized, install Python from the official Python website, then close and reopen the terminal.

## 2. Create a project and virtual environment (recommended)
A virtual environment keeps this project's packages separate from other Python projects.

macOS — Terminal:
```
mkdir PySide6Project
cd PySide6Project
python3 -m venv .venv
source .venv/bin/activate
```

Windows — PowerShell:
```
mkdir PySide6Project
cd PySide6Project
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```
If PowerShell blocks activation, you can use Command Prompt instead and run `.venv\Scripts\activate.bat`. You can also install packages by calling the virtual environment's Python directly, without activating it.


## 3. Install PySide6
With the virtual environment activated, run the command for your operating system:

macOS:
```
python3 -m pip install --upgrade pip
python3 -m pip install PySide6
```

Windows:
```
py -m pip install --upgrade pip
py -m pip install PySide6
```

If your virtual environment is active, you can generally use `python -m pip install PySide6` on either platform. Using `python -m pip` helps ensure pip belongs to the Python interpreter you are running. You do not need to download a wheel or source archive manually from PyPI.

## 4. Confirm that installation worked
Run this command in the same terminal/environment:
`python -c "import PySide6; print(PySide6.__version__)"`

If a version number prints without an error, Python can import PySide6 successfully. If you receive `ModuleNotFoundError`, you may be using a different Python interpreter or environment from the one where you installed the package.

## 5. Run a small test application
Create a file named `main.py` inside the project folder and paste in the following code:

```
import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
 
app = QApplication(sys.argv)
 
window = QWidget()
window.setWindowTitle("My First PySide6 App")
window.resize(360, 160)
 
layout = QVBoxLayout(window)
layout.addWidget(QLabel("PySide6 is installed and working!"))
 
window.show()
sys.exit(app.exec())
```

Run the program from the project folder:
`python main.py`

A small window should appear with the message “PySide6 is installed and working!” Close the window to end the program.

## 6. Using PySide6 in Visual Studio Code

1. Open the PySide6Project folder in Visual Studio Code.

2. If prompted, install or enable the Python extension.

3. Choose the interpreter from the project's .venv folder: use the Command Palette and select “Python: Select Interpreter.”

4. Open main.py and run it using that selected interpreter, or run `python main.py` in the VS Code terminal.

5. Troubleshooting:
- `pip` or Python is not recognized — Try `python3` on macOS or `py` on Windows. Confirm Python is installed, then reopen the terminal.
- `ModuleNotFoundError: No module named 'PySide6'` — Activate the intended virtual environment, install PySide6 in it, and confirm your editor is using that same interpreter.
- Permission or access error — Use a virtual environment rather than installing system-wide. Avoid using administrator privileges unless you understand why they are needed.
- Installation fails or no compatible version is found — Check `python --version` and make sure the interpreter is supported by the PySide6 release shown on PyPI. Upgrade pip and retry.
- The program starts but no window appears — Check for errors in the terminal, confirm `window.show()` is called, and make sure the application has not exited immediately.

