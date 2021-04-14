# tkinterUI

Nothing fancy here. Just a simple tkinter mock-CLI that I'm migrating to this independent repository for future use.

# USAGE

The dictionary cmdList defined on line three should be used to actually define your commands. The key (**foo**:bar) should be used to define the name of the command, and the value (foo:**bar**) should be used to define the function which it will invoke. Arguments are passed on automatically and no additional parameters need to be provided in the dictionary.

Please note that since the exec() method is being run within the scope of the class 'gui' you could either:
    1: Create the method within the class gui and call it using the **self** keyword
    2: Use the provided class **commands** and invoke the class + your corresponding method

## Requirements to Run

- Python 3
- tkinter

