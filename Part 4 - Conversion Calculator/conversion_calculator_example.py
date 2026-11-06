# import libraries with necessary widgets
import sys
from PySide6.QtWidgets import QVBoxLayout, QWidget, QLineEdit, QLabel, QComboBox, QPushButton, QApplication, QMainWindow
from PySide6.QtGui import QDoubleValidator

# dictionary for distances (baseline set in meters)
units = {
    # metric
    "Meters (m)": 1.0,
    "Kilometers (km)": 1000.0,
    "Centimeters (cm)": 0.01,
    # imperial
    "Miles (mi)": 1609.344,
    "Feet (ft)": 0.3048,
    "Inches (in)": 0.0254,
    "Yards (yd)": 0.9144
}

class DistanceConverter(QWidget):
    def __init__(self):
        super().__init__()
        
        # create the window frame container
        self.setWindowTitle("Distance Converter") # this text will appear at the top of the window
        self.resize(300, 100)

        # create labels for text, we will add them in the correct order later
        input_label = QLabel("Input distance to convert here")
        output_label = QLabel("Output distance will be shown here")
        top_label = QLabel("Convert from...")
        bottom_label = QLabel("To...")

        # create box for input with QLineEdit
        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Type numbers here...")

        numerical_validator = QDoubleValidator() # create validator for only numerics so no non-numeric characters can be entered
        self.input_box.setValidator(numerical_validator) # add the numeric only validator to the input box

        # create output box
        self.output_box = QLineEdit()
        self.output_box.setReadOnly(True)  # Prevents the user from typing inside the output box
        self.output_box.setPlaceholderText("Results will show up here...")

        # create calculate button
        button = QPushButton("Convert")
        # Connect the button click event to our function
        button.clicked.connect(self.calculate_button_click)

        # Create dropdown boxes
        self.box_from = QComboBox()
        self.box_to = QComboBox()
        # populate drop down boxes with options from the dictionary
        for unit_name, meter_value in units.items():
            self.box_from.addItem(unit_name, meter_value)
            self.box_to.addItem(unit_name, meter_value)
        # set default for when app is launched
        self.box_from.setCurrentText("Kilometers (km)")
        self.box_to.setCurrentText("Miles (mi)")

        # add objects to the layout
        # create the QVBox layout object, this will allow us to easily position elements together vertically
        layout = QVBoxLayout()
        # since we are using QVBoxLayout (Vertical Box Layout), the order in which we add widgets matters.
        layout.addWidget(input_label) # Will be an element at the top
        layout.addWidget(self.input_box)
        layout.addWidget(top_label)
        layout.addWidget(self.box_from)
        layout.addWidget(bottom_label)
        layout.addWidget(self.box_to)
        layout.addWidget(output_label)
        layout.addWidget(self.output_box)
        layout.addWidget(button) # Will be an element at the bottom

        # add the QVBox layout to the window
        self.setLayout(layout)

    # button calculation function for when clicked
    def calculate_button_click(self):
        text = self.input_box.text()
        if not text: # in the case of no input
            return

        value = float(text)
        
        # obtain conversion factors
        from_factor = self.box_from.currentData()
        to_factor = self.box_to.currentData()
        
        # use meters as a baseline, then convert to actual requested units
        meters = value * from_factor
        converted_value = meters / to_factor
        
        # round to 4 decimal places
        self.output_box.setText(f"{round(converted_value, 4)}")

if __name__ == "__main__":
    # start the global application instance
    app = QApplication(sys.argv)

    # create the window frame container
    window = DistanceConverter()

    # show the window and run the app
    window.show()
    sys.exit(app.exec())