# simpledraw
A very simple console-based drawing program exercise in Python.

## Prerequisites
Any reasonably standard Python 2.6+ should do, including the version that comes pre-installed with Mac OSX and most Linux distrbutions. There are no dependencies on any external packages.

The program has been tested successfully on Mac OSX 10.12 and Ubuntu Linux 16.04.1 LTS. It *should* also work correctly on Microsoft Windows.

## Installation
The source is available from GitHub using one of the following methods:

1. Checking out the code using git:
  `$ git checkout https://github.com/grahamdaley/simpledraw.git`

2. Downloading a [zip file](https://github.com/grahamdaley/simpledraw/archive/master.zip "simpledraw-master.zip") containing the code and extracting it into a new folder

## Running
1. Open a terminal window (or command prompt)

2. Change to the folder containing the program source, e.g.:
  `$ cd ~/simpledraw`

3. Starting the program from the command line:
  `$ ./simpledraw.py`

## Tests

Unit tests are in the `tests` folder. To run all of the tests in one go, type the following command from within the main source folder:
`$ python -m unittest discover tests "*.py"`