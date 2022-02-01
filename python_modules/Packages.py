# What are Packages ?

'''
- Packages are just folders(directories) that contains modules. 

- They contain a special python file named __init__.py

- The __init__.py file can be empty. The files tells python that the directory of
folder contains a python package which can be imported like module.

- Packages are a Convenient way to orgnize modules. 

- A package can also contain sub-packages.
 
 Creating a Package.

Step 1: create a directory for saving the packages

Step 2: Create __init__py file inside your directory 

step 3: Add another python files create some modules

Accessing Module in Package
'''

# way 1
from healthy import foo
# way2
import healthy.foo


# way 1
healthy.foo.fruits("Apple")
# way 2
foo.fruits("Orange")
