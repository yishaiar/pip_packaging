# Name this repo!

# My Package

[Description goes here]

This is a simple Python package that includes a function to greet someone and a class representing a person.

pip install directory-tree
from directory_tree import display_tree
# Display the tree structure of the current directory
display_tree()

https://packaging.python.org/en/latest/tutorials/packaging-projects/#id1

1. build: creates the dist folder

1a. navigate to pyproject.toml directory

1b. run from cli:

python3 -m pip install --upgrade pip

python3 -m pip install --upgrade build

python3 -m build


rm -rf src/*.egg-info build dist && python3 -m pip install --upgrade pip &&  python3 -m pip install --upgrade build && python3 -m build && pip install --force-reinstall ./dist/*.whl

python3 -m pip install --upgrade pip &&  python3 -m pip install --upgrade build ./ && python3 -m build && pip install --force-reinstall ./dist/*.whl && rm -rf src/*.egg-info build dist

python setup.py sdist bdist_wheel && pip install --force-reinstall ./dist/*.whl && rm -rf src/*.egg-info build dist


python -m cibuildwheel --platform linux --platform macos --platform windows

## Installation

2a. run from cli:

pip install ./dist/example_package_YOUR_USERNAME_HERE-0.0.1.tar.gz

or

pip install ./dist/*.whl



pip install git+https://github.com/yourusername/my_package.git

locally:
pip install .



## Usage


```python
from example_package_YOUR_USERNAME_HERE import my_functions
my_functions.add_one(2)

from example_package_YOUR_USERNAME_HERE import my_functions, my_classes

# Use the function
print(my_functions.greet("Alice"))

# Use the class
p = my_classes.Person("Bob")
print(p.say_hello())




project run from main.py / main.ipynb



## 💻 Usage
1. Clone this repository to your local machine.
2. Install the required dependencies using the following command:
    ```shell
    pip install -r requirements.txt
    ```

## 📋 TODOs
- [ ] TODO 1
- [ ] TODO 2
- [ ] TODO 3