# AirBnB Clone - The Console

## Introduction
Welcome to the AirBnB clone project! This project involves building a command interpreter in Python to manage AirBnB objects. The command interpreter allows you to create, retrieve, update, and delete objects related to AirBnB.

## Project Overview
The project is structured into various tasks, including creating a parent class (BaseModel), implementing serialization/deserialization, creating classes for AirBnB objects, and developing a file storage engine. The primary goal is to build a foundation for subsequent projects, such as HTML/CSS templating, database storage, and front-end integration.

## Concepts and Learning Objectives
The project focuses on several key concepts and learning objectives, including:
- Python packages
- Command interpreter using the `cmd` module
- Unit testing in a large project
- Serialization and deserialization of a class
- Reading and writing JSON files
- Managing datetime and UUID
- Understanding *args and **kwargs in Python
- Handling named arguments in functions

## Requirements
### Python Scripts
- Supported editors: vi, vim, emacs
- Interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- All files end with a new line
- The first line of all files is `#!/usr/bin/python3`
- Mandatory README.md file at the root
- Code follows PEP 8 style (checked with pycodestyle)
- All modules, classes, and functions have documentation
- All files must be executable

### Python Unit Tests
- All test files inside a 'tests' folder
- Use the `unittest` module
- Test files and folders follow the project structure
- Documentation for modules, classes, and functions in test files

## Execution
Your shell should work both in interactive and non-interactive mode. Examples:

### Interactive Mode
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

### Non-Interactive Mode
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

## Running Tests
$ echo "python3 -m unittest discover tests" | bash


