## Setup
- Setup virtualenv ```virtualenv venv```, and activate it ```source venv/bin/activate```
- Install dependencies in Linux ```pip install -r requirements.txt```, not sure windows has the same dependencies or not.

## Usage
- For using a 0.1min of mouse movement execute the following ```python mouse_bot.py --time=.1```

## Documentation
- Documentation is built with Sphinx, module indexing is done with autodoc

### Steps For Regenerating Docs
- Goto ```doc/sphinx``` directory.  
- Clean previous documentation with ```make clean```.  
- Generate the api-docs for the new module(s) with ```sphinx-apidoc -o . ../../```.  
- We need all the .rst files except for the ```modules.rst```, move all of them to the ```doc/sphinx/source``` directory except for the ```modules.rst```, move it to the trash for now.
- Rebuild the documentation with ```make clean```

## Learning History
- Virtualenv
- Pip requirements
- Mouse manoeuvering
- Argparse
- Makefile:
    - [Intro to Make](http://www.linuxdevcenter.com/pub/a/linux/2002/01/31/make_intro.html?page=2)
    - [The purpose of Phony](http://stackoverflow.com/questions/2145590/what-is-the-purpose-of-phony-in-a-makefile)
- Python code structure:
    - [The Hitchhiker's guide to Python](http://docs.python-guide.org/en/latest/writing/structure/)

