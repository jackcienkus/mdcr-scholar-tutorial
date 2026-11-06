import sys
from PySide6.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout

app = QApplication(sys.argv)

dialog = QDialog()
dialog.setWindowTitle("My Pop-Up")
dialog.resize(300, 150)

layout = QVBoxLayout(dialog)
label = QLabel("Hello! This is a custom pop-up with text.")
label.setWordWrap(True)
layout.addWidget(label)

dialog.exec()