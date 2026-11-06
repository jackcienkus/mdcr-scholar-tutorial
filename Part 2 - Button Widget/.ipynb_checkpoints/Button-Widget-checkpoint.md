# Part 2 - Button Widget

**Author:** Yousif Elya

**Language:** Python

**Tags:** GUI, Interface, Widget

**Description:** Shows how to add a button, one clickable and one checkable to a widget created through PySide6

**Dependencies:** PySide6.QtCore, PySide6.QtGui, PySide6.QtWidgets


### Running the python file 

The python file creates a widget with two interactive objects: a standard button that will click, and a check button which will change states once clicked.

```
cd "Part 2 - Button Widget"
py button-widget.py
```

### file contents

Each chunk within the file is annotated step by step for clarity. In summary, the file creates a window class through 'QtWidgets' and sets up a basic layout. It then includes two button objects and a line to Connect the button's clicked signal to the handler method. The class is complete, and using 'window.show()' in main the widget will be created once the file is run.

### Easy adjustments

To better understand the code, here are changes you can make to easily change the widget output.

**Line 16:**  st_button = QPushButton(text="click here", parent=self)
Edit 'click here' to change what is on the button

**Line 18:** st_button.setFixedSize(120, 60)
Edit '120, 60' to change the sixe of the button and widget

**Line 19:** layout.addWidget(st_button)
Comment out this line to make this button not show up on the widget

**Line 25:** self.ch_button.setChecked(True)
Edit 'True' to false to change the initial state of the button 

Feel free to make changes and play with the class to see what works.