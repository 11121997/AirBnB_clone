# AirBnB Clone Project

## Description :label:
 
This project is an AirBnB clone, a simplified version of the popular online vacation rental platform. The implementation includes a command-line interpreter (console) for managing various aspects of the application, such as creating and managing instances of different classes (e.g., User, State, City, Amenity, Place, Review).

## Usage ���

The console works both in interactive mode and non-interactive mode, much like a Unix shell.
It prints a prompt **(hbnb)** and waits for the user for input.

Command | Example
------- | -------
Run the console | ```./console.py```
Show help for a command | ```(hbnb) help <command>```
Create an object | ```(hbnb) create <class>```
Show an object | ```(hbnb) show <class> <id>``` or ```(hbnb) <class>.show(<id>)```
Destroy an object | ```(hbnb) destroy <class> <id>``` or ```(hbnb) <class>.destroy(<id>)```
Show all objects, or all instances of a class | ```(hbnb) all``` or ```(hbnb) all <class>```
Update an attribute of an object | ```(hbnb) update <class> <id> <attribute name> "<attribute value>"``` or ```(hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")```
Exit the console | ```(hbnb) quit```

### Interactive mode (example)

```bash
$ ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  exit  help  quit  show  update

(hbnb)
(hbnb) quit
$
```

### Non-interactive mode (example)

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  exit  help  quit  show  update

(hbnb)
$
```

## Testing :straight_ruler:

Using unittests to test resaults in this project and defined in the [tests](./tests)
folder. To run the entire test, run the following command:

```
$ python3 unittest -m discover tests
```

You can specify a single test file to run at a time:

```
$ python3 unittest -m tests/test_console.py
```
