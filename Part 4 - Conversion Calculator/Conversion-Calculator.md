# PySide6 Tutorial Part 4: Distance Conversion Calculator
**Author:** Anthony Kosinski <br>
**Language:** Python<br>
**Tags:** Gooey, Interface, Software Application, Qt<br>
**Description:** How to build a distance converter application with PySide6<br>
**Dependencies:** PySide6

In this last tutorial, we will be putting together the widgets we've learned about to create a simple conversion calculator for different measurement types.

### 1. Setting up imports and data
For our conversion calculator, we will need:
 * An Application Window
 * Text Labels
 * Input Text
 * Double Input Validator
 * Button
 * Drop-down Selection Box
 * Layout Formatter

For these, we will start by importing:<br>
```
import sys
from PySide6.QtWidgets import QVBoxLayout, QWidget, QLineEdit, QLabel, QComboBox, QPushButton, QApplication, QMainWindow
from PySide6.QtGui import QDoubleValidator
```

Since we are creating a conversion calculator for distances, we also need a dictionary which contains measurements for each distance. We will do these measurements relative to meters to give us an easy baseline to use. We will also use this dictionary to populate a drop-down box for our application.

```
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
```

Now that we have the imports and the data we need set up, we just need to make the application.

### 2. Basic Application
We are going to set up a class to contain our application by writing the following:<br>
```
class DistanceConverter(QWidget):
    def __init__(self):
        super().__init__()
```
<br>We need to super() this class so we can inherit the QWidget class for our application. We will be doing most of our application building in this init function for simplicity, but you can also split each component into separate functions if preferred.

Within the __init__ function, let's set up our window. We'll keep the window fairly small and set a relevant title for our application.
```
        self.setWindowTitle("Distance Converter") # this text will appear at the top of the window
        self.resize(300, 100)
```

Now our application will open a basic window named "Distance Converter", but we still need to populate the window with labels, input boxes, drop down boxes, and an output. We will do this next.

### 3 Creating the DistanceConvertor Class<br>
#### 3.1 Setting up the Class<br>
For our application, we'll make a class by inheriting from the QWidget class. We'll call our class DistanceConverter.

```
class DistanceConverter(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Distance Converter") # this text will appear at the top of the window
        self.resize(300, 100)
```

This will open our basic window, so let's also have a main function (not in the class) which will run it properly when the script is called.

```
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = DistanceConverter()

    window.show()
    sys.exit(app.exec())
```

Now we have a window, but nothing inside of it! So next we'll create the objects needed to populate the window.

#### 3.2 Creating application objects<br>
Inside of our initialization function is where we'll initalize our application objects. If preferred, you could also split each into its own function for neater code. For our purposes though, this is simpler.

In our program, we'll need these things for it to function:
 * Labels guiding the user as to which input box is for what
 * Input box for a number input (and a way to ensure only numbers can be entered)
 * Output box that will give the conversion result based on the input.
 * A button to run the conversion
 * Two dropdown boxes, one for input one for output, which specify the distances being converted from/to

**Labels**<br>
Starting with the labels, we'll create four with QLabel. Note that currently we are just initalizing the labels, not placing them yet, so the initialization order won't matter. These objects won't actually appear in the window until we add them to a layout which we will do in 3.3.

We can use a string to add text that we want shown with our QLabel:<br>
```
input_label = QLabel("Input distance to convert here")
output_label = QLabel("Output distance will be shown here")
top_label = QLabel("Convert from...")
bottom_label = QLabel("To...")
```

Note I didn't make these labels "self" objects, since they aren't used in any outside functions. Other objects that are needed to 

**Input Box**<br>
Next we'll use QLineEdit to create an input box. We can also give it placeholder text for when there is no input, which will help guide the user as to where to type.
```
self.input_box = QLineEdit()
self.input_box.setPlaceholderText("Type numbers here...")
```
Having just an input box alone though means someone could type anything in there which can cause problems, we can remedy this by ensuring only numbers can be entered with a QDoubleValidator object which we attach to the input box.
```
numerical_validator = QDoubleValidator() # create validator for only numerics so no non-numeric characters can be entered
self.input_box.setValidator(numerical_validator)
```

**Output Box**<br>
Now our output box will also be a QLineEdit box, but we'll ensure it can't be edited by setting it to read only. We can also add more placeholder text for further user clarification
```
self.output_box = QTextEdit()
self.output_box.setReadOnly(True)  # Prevents the user from typing inside the output box
self.output_box.setPlaceholderText("Results will show up here...")
```

**Dropdown Selection Boxes**<br>
Next we'll need our selection boxes for both our input and output. It'll be easier to create them together, as we'll need to populate both with the same options. So let's create two QComboBox objects, and using our dictionary from the beginning, we'll pull the key names and corresponding values to put into both QComboBox objects.
```
self.box_from = QComboBox()
self.box_to = QComboBox()

# populate both QComboBox objects.
for unit_name, meter_value in units.items():
    self.box_from.addItem(unit_name, meter_value)
    self.box_to.addItem(unit_name, meter_value)
```

We can also set a default option for both that the program will default to when opened, which just makes our program a bit nicer to use. Just need to make sure the text matches the key's text exactly!
```
self.box_from.setCurrentText("Kilometers (km)")
self.box_to.setCurrentText("Miles (mi)")
```

**Conversion Button**<br>
All that is left is our conversion button, which we left for last since it will require all of our previous objects to work.<br>
Adding a QPushButton is quite straightforward, and we can specify what text appears on the button with a string.
```
button = QPushButton("Convert")
```
However to make the button actually do something, we'll need to write a function for it. Let's create a new function in our DistanceConverter class and we'll name it "calculate_button_click", quite creative I know.

For our function, we'll need to do these things when our button is clicked:
1. Pull the numbers from the input text box.
2. Obtain factors based on the selection of both QComboBox objects.
3. Calculate the conversion between the two distances
4. Write the result to be displayed on the output text box.

The function ends up looking like this:
```
def calculate_button_click(self):
    text = self.input_box.text()
    if not text: # in the case of no input
        return

    value = float(text)
    
    # obtain conversion factors
    from_factor = self.box_from.currentData()
    to_factor = self.box_to.currentData()

    # conversion
    meters = value * from_factor
    converted_value = meters / to_factor

    # write to output
    self.output_box.setText(f"{round(converted_value, 4)}")
```

On top of what was mentioned, we also ensure that the text is not blank at the beginning. Since the text is pulled from an input box, it is actually pulled as a string which requires a conversion to float as well. We also round the result to the fourth decimal place, but of course this can be changed.

So now we have our function, we can go back to where we first initialized our button and connect it to our function.
```
button.clicked.connect(self.calculate_button_click)
```
Now when the button is clicked, it will call the calculation function.

### 3.4 Adding Objects to the Window
Great! We have all of these objects, but none of them actually show up? That's where we'll need a layout object. PySide6 offers a lot of different layout objects, some are very straightforward but offer minimal control, whereas others are more complicated but allow for more complicated layouts as well.

For our purposes, a simple layout will do just fine. We'll be using QVBoxLayout, which is a vertical layout that has all objects stacked on one another. The order in which we add objects to the box layout does matter, so we'll need to keep note of that.

Initalizing the layout is just like any other object.
```
layout = QVBoxLayout()
```

Then, we can add to the layout in the order we want elements to appear on the window from top to bottom.

```
layout.addWidget(input_label) # Will be an element at the top
layout.addWidget(self.input_box)
layout.addWidget(top_label)
layout.addWidget(self.box_from)
layout.addWidget(bottom_label)
layout.addWidget(self.box_to)
layout.addWidget(output_label)
layout.addWidget(self.output_box)
layout.addWidget(button) # Will be an element at the bottom
```

Then since our class is a QWidget object, we just set the layout to be our new layout object.
```
self.setLayout(layout)
```

### End
With that you should have a working conversion calculator program! Just run your script and the window should pop-up.

For an extra challenge, try to figure out how to make this calculator work without needing a conversion button (doing real-time conversion instead).