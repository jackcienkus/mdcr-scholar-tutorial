# Imports
import sys
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # classic button, interact with a click
        st_button = QPushButton(text="Standard Button",parent=self)
        st_button.setFixedSize(100, 60)
        
        # checker button, switched states once clicked
        ch_botton = QPushButton(text="Checked", parent=self)
        ch_botton.setCheckable(True)
        ch_button.setChecked(True)
        ch_botton.setFixedSize(100, 60)
        
        layout.addWidget(bottomBtn)
        self.setLayout(layout)

    def buttoncheck(self):
        if self.ch_button.isChecked():
            self.ch_button.setText("Checked")
        else:
            self.ch_button.setText("Unchecked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())