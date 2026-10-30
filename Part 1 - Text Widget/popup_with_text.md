# Section 2: How To Get a Pop-up Widget With Text

## Objective
By the end of this section you will be able to make a small window pop up on the screen that displays text

___________

## What is a Pop-up Widget?
A pop-up widget is a small window that appears on top of the main window to show information to the user. Programs use them for messages, warnings, confirmations, and notes.

There are two ways to make them using PySide6:

| Method | Best For|
|--------|-------- |
|QMessageBox| Short Messages; Qt builds it for you|
|QDialog|Custom Pop-ups where the user controls the layout and text|

_____________

## Where to Run the Codes
Run these examples as .py files from a terminal or an editor like VS Code, not in a Jupyter notebook. Pop-up windows need their own event loop, which can freeze or crash a notebook kernel
_____

## Method 1: QMessageBox

#### Code
Create a file named popup_message.py inside the project folder and paste in the following code:

```python
import sys
from PySide6.QtWidgets import QApplication, QMessageBox # Load the PySide6 classes needed

app = QApplication(sys.argv) # Creates the application. Every PySide6 program needs one before showing any window


# Show the pop-up. The three values are: parent window, title, message text.
# None means there is no parent window
QMessageBox.information(None, "My Pop-Up", "Hello! This is a pop-up with text.") # Shows the pop-up and waits until the user clicks OK. The program ends afterward
```

#### Running the Code
In terminal, run: python popup_message.py

A pop-up will appear with your text and an "OK" button. Click "OK" to close it and end the program

*Note: if the pop-up does not appear, check the Dock or press Cmd+Tab (macOS) or Alt+Tab (Windows), since it can open behind your editor.*

#### Pop-up Example
![Screenshot 2026-10-29 at 6.29.29 PM.png](8e8476d1-6daa-4a0e-8e66-555fc6445f1f.png)

#### 3 Main Types using QMessageBox
- QMessageBox.information(None, "Info", "This is information.")
- QMessageBox.warning(None, "Warning", "Be careful!")
- QMessageBox.critical(None, "Error", "Something went wrong.")

#### The 3 Input Values
QMessageBox.information(parent, title, text)
- Parent: the window the pop-up belongs to. We use None because there is no other window yet.
- Title: the text in the pop-up's title bar.
- Text: the message shown inside the pop-up.

*Note: The icon and title can look different depending on operating system. For example, on MacOS the title is hidden and a generic icon may be shown. On Windows, a blue "i" icon and title appear*
______

## Method 2: QDialog
### QDialog with Label

#### Code
Create a file named popup_dialog.py inside the project folder and paste in the following code:

```python
import sys
from PySide6.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout #load the pyside6 classes needed

app = QApplication(sys.argv) #Creates the application. Every PySide6 program needs one before showing any window

# Create an empty pop-up window
dialog = QDialog()
dialog.setWindowTitle("My Pop-Up") # Set the text in the title bar
dialog.resize(300, 150) # Set the size of the window in pixels (width, height)

layout = QVBoxLayout(dialog) #Creates a layout that stacks widgets vertically inside the dialog
label = QLabel("Hello! This is a custom pop-up with text.") #Creates a widget that displays text
label.setWordWrap(True) #Wraps long text onto the next line
layout.addWidget(label) #Places the label inside the dialog

dialog.exec() #Shows the dialog and waits until it is closed
```

#### Running the Code
In terminal, run: python popup_dialog.py

A pop-up window opens showing your text. Close it with the window's close button.

#### Pop-up Example
![Screenshot 2026-10-29 at 6.33.03 PM.png](e1caab6d-9c71-47b5-8339-5203cd6ff479.png)

____
### QDialog with TextEdit

#### Code
Create a file named popup_textedit.py inside the project folder and paste in the following code:

```python
import sys
from PySide6.QtWidgets import QApplication, QDialog, QTextEdit, QVBoxLayout #load the pyside6 classes needed

app = QApplication(sys.argv) #Creates the application. Every PySide6 program needs one before showing any window

# Create an empty pop-up window
dialog = QDialog()
dialog.setWindowTitle("My Pop-Up") #Sets the text in the title bar
dialog.resize(300, 150) #Sets the size in pixels (width, height)

layout = QVBoxLayout(dialog) #Creates a layout that stacks widgets vertically inside the dialog

text_box = QTextEdit() #Creates a multi-line text area
text_box.setReadOnly(True) #User can read and scroll, but not edit (Remove this and users can edit)
text_box.setPlainText("This is an example of longer text\nWhere multiple lines are used\nLine 3\nLine 4\nLine 5\nLine 6\nLine 7\nLine 8\nLine 9\nLine 10") #The text to show
layout.addWidget(text_box) #Places the text box inside the dialog

dialog.exec() #Shows the dialog and waits until it is closed
```

#### Running the Code
In terminal, run: python popup_textedit.py

A pop-up window opens showing your text. Close it with the window's close button.

#### Pop-up Example
![Screenshot 2026-10-29 at 6.41.36 PM.png](76ed1239-7724-4d18-bce6-b2a47c8d36d5.png)
