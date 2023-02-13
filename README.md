# CS330-coding-assignmentII
Coding assgnment relating to graphs made to remmediate the incomplete grade

# Instructions 

# Pre Requisites: 
### The instructions below are for a Linux environment (Ubuntu 22.04).
1. Python
2. Git

# Installation :
1. To install `python`:
```
$ sudo apt update
$ sudo apt install python3
```

2. To install the `coverage` module :
```
$ pip install coverage
```

3. To install `git`:
```
$ sudo apt-get update
$ sudo apt-get install git-all
```

# Configuration: 
1. Clone the repository
```
  $ git clone https://github.com/baguilarislas/CS330-codingAssignmentII.git
  $ cd CS330-codingAssignmentII
```

To generate an executable from a Python file on Ubuntu 22.04, you can follow these steps:

Install PyInstaller by running the following command in the terminal:

```
pip install pyinstaller
```
Navigate to the directory where your Python file is located:

```
bash
cd/path/to/your/python/file
```
Use PyInstaller to create an executable by running the following command:

```
pyinstaller your_script.py
```
This will create a dist directory with the executable and other necessary files.

You can now run the executable by navigating to the dist directory and running the executable:

```
bash
cd dist
./your_script
```

Note: You may need to install additional libraries or packages if your Python file requires them for the executable to work properly.






