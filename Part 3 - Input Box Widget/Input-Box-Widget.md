# Part 3 - Input Box Widget

To create an input box with PySide6, we'll use the `QLineEdit()` object. 
The code in `input-box-widget.py` creates a simple, one-line text editing box
in which you can write a simple ten-character message. 

There are three main inputs you provide to the widget: The text
you type, whether you highlight any text in the box or not, and whether
you hit enter/return or not.

The text you type is dynamically saved as an attribute in the `MainWindow` class,
and a message in the terminal saying "Text edited..." confirms when text is 
added or changed. When you hit enter/return in the box, it'll recognize the input,
print a message in the terminal saying "Return pressed!", and change the text in
the widget to say "BOOM!".

To run this widget, assuming you're in the root directory of the repo, paste the
following into your terminal:

macOs:
```
cd "Part 3 - Input Box Widget"
python3 input-box-widget.py
```

Windows:
```
cd "Part 3 - Input Box Widget"
py input-box-widget.py
```