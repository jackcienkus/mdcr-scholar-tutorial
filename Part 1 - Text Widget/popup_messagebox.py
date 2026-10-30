import sys
from PySide6.QtWidgets import QApplication, QMessageBox

app = QApplication(sys.argv)

QMessageBox.information(None, "My Pop-Up", "Hello! This is a pop-up with text.")