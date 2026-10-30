import sys
from PySide6.QtWidgets import QApplication, QDialog, QTextEdit, QVBoxLayout #load the pyside6 classes needed

app = QApplication(sys.argv) #Creates the application. Every PySide6 program needs one before showing any window

# Create an empty pop-up window
dialog = QDialog()
dialog.setWindowTitle("My Pop-Up") #Sets the text in the title bar
dialog.resize(300, 150) #Sets the size in pixels (width, height)

layout = QVBoxLayout(dialog) #Creates a layout that stacks widgets vertically inside the dialog

text_box = QTextEdit() #Creates a multi-line text area
text_box.setReadOnly(True) #User can read and scroll, but not edit
text_box.setPlainText("This is an example of longer text\nWhere multiple lines are used\nLine 3\nLine 4\nLine 5\nLine 6\nLine 7\nLine 8\nLine 9\nLine 10") #The text to show
layout.addWidget(text_box) #Places the text box inside the dialog

dialog.exec() #Shows the dialog and waits until it is closed