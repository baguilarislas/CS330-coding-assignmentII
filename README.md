# CS330-coding-assignmentII
Coding assgnment relating to graphs made to remmediate the incomplete grade 

# Part A
This part generates a graph and can guaarantee that it is connected. the arguments are as follows 

```python3 partA.py --vertices x --connected```

where x is the number of vertices and the second argument will guarantee that the graph is connected

# Part B

This part generates the shortest part of a graph, arguments are as follows

```python3 partB.py x y```

where x and y are star and end vertices respectively and then you are prompted to input a graph description in the form

```
a c 12
c b 3
c e 1
e b 5
```

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

# To generate an executable from a Python file on Ubuntu 22.04:

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
pyinstaller partA.py or partB.py
```
This will create a dist directory with the executable and other necessary files.

You can now run the executable by navigating to the dist directory and running the executable:

```
bash
cd dist
./partA.py or ./partB.py
```

Note: You may need to install additional libraries or packages if your Python file requires them for the executable to work properly.






