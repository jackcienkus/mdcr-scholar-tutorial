# Imports
import sys
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

# Class to create the widget and buttons
class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Create a layout for the window
        layout = QVBoxLayout(self)
        
        # Classic button, interacts with a click
        st_button = QPushButton(text="click here", parent=self)
        # Set the size of the button
        st_button.setFixedSize(120, 60)
        layout.addWidget(st_button)
        
        # Checker button, switches states when clicked
        self.ch_button = QPushButton(text="Checked", parent=self)
        # Set the initial state of the checkable button
        self.ch_button.setCheckable(True)
        self.ch_button.setChecked(True)
        self.ch_button.setFixedSize(120, 60)
        
        # Connect the button's clicked signal to the handler method
        self.ch_button.clicked.connect(self.buttoncheck)
        
        layout.addWidget(self.ch_button)
        self.setLayout(layout)

    # Handler function for the check button
    def buttoncheck(self):
        # If-else to switch between the two states once the button is clicked on
        if self.ch_button.isChecked():
            self.ch_button.setText("Checked")
        else:
            self.ch_button.setText("Unchecked")


if __name__ == "__main__":
    # create and show the window
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())