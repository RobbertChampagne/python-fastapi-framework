# Python-fastapi-framework

----

### Virtual Environments:

**Run the following command to create a virtual environment:**
```Bash
python -m venv python-fastapi-framework
```

**Activate the Virtual Environment:**
```Bash
python-fastapi-framework\Scripts\activate
```

**Install Packages:**
```Bash
pip install fastapi uvicorn sqlmodel
```

**Deactivate the Virtual Environment:**
```Bash
deactivate
```

**Export the installed packages to a requirements.txt file:**
```Bash
pip freeze > requirements.txt
```

**Install packages from requirements.txt:**
```Bash
pip install -r requirements.txt
```

**To list all virtual environments created using venv or other tools like virtualenv, you can use:**
```Bash
dir /s /b activate
```

---

### Virtual Environments in Anaconda:
Create a New Anaconda Environment:
```Bash
conda create --name python-fastapi-framework python=3.11
```
 To activate this environment, use:
```Bash
conda activate python-fastapi-framework
```
To deactivate an active environment, use
```Bash
conda deactivate
```
Example of the cmd:
```Bash
(python-fastapi-framework) C:\...\Desktop\github\...>
```

To effectively recreate the environment with the correct dependencies on another device, you would typically use an `environment.yml`.<br>
Here's how you can create an `environment.yml` file and use it to recreate the environment on another device:

1. **Export Your Environment:**
    - First, ensure your Conda environment (`python-fastapi-framework`) is activated.
    - Export your environment to an `environment.yml` file:

```Bash
conda env export > environment.yml
```
This file includes all the necessary information about the environment, including the name, channels from where packages are fetched, and the list of packages with their versions.

2. **Recreate the Environment on Another Device:**
    - Transfer the `environment.yml` file to the other device where you want to recreate the environment.
    - Use the following command to create an environment from the `environment.yml` file:

```Bash
conda env create -f environment.yml
```
This process ensures that you have an exact replica of your development environment on another device, including all dependencies with their correct versions.

---

```
python-fastapi-framework/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── module/
│   │   ├── __init__.py
│   │   ├── script1.py
│   │   └── level2/
│   │       ├── __init__.py
│   │       └── script2.py
│   │       └── level3/
│   │           ├── __init__.py
│   │           └── script3.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_script1.py
│   └── test_loggingSetup.py
├── .gitignore
├── pytest.ini
└── README.md
```

### The main script

`main.py`
```Python
import logging
from module.loggingSetup import setup_logging
from module.script1 import *

def mainFunction():
    """Main entry point"""
    setup_logging()
    logging.info("Start main")
    mul = multiplyOne(2, 3)
    main()
    logging.info(f"{mul}")
    
if __name__ == '__main__':
    try:
        mainFunction()
    finally:
        logging.info("End main")
```
**Output:**
```Bash
> python src/main.py
2024-10-17 06:15:07 - INFO - Start main
3
-1
2024-10-17 06:15:07 - INFO - In script2.py, the sum of 1 and 2 is 3
2024-10-17 06:15:07 - INFO - In script3.py, the difference of 1 and 2 is -1
2024-10-17 06:15:07 - INFO - 6
2024-10-17 06:15:07 - INFO - End main
```

---
