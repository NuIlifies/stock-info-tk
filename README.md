# tkinterUI
![Python Version](https://img.shields.io/static/v1?label=Python&message=3.9.1&color=informational) 

Nothing fancy here. Just a simple tkinter mock-CLI that I'm migrating to this independent repository for future use.

# Usage

The dictionary cmdList defined on line three should be used to actually define your commands. The key (**foo**:bar) should be used to define the name of the command, and the value ("foo":"**bar**") should be used to define the function which it will invoke. If the method defines parameters, arguments can be passed through by the "self.args" variable like so:
    - ("foo":"bar(**self.args**))

Please note that since the exec() method is being run within the scope of the class 'gui' you could either:
    - Create the method within the class gui and call it using the **self** keyword
    -Use the provided class **commands** and invoke the class + your corresponding method

## Requirements to Run

- Python 3
- tkinter

