# Hash Table Exercise #

## Setup ##

1. Clone a copy of this exercise. This command makes a new folder called `hash-table-exercise`, and then puts the exercise into this new folder. You do not need to fork the repository.

```bash
git clone ...
```

Use `ls` to confirm there's a new project folder

2. Move your location into this project folder

```bash
cd hash-table-exercise
```

3. Create a virtual environment named `venv` for this project:

```bash
python3 -m venv venv
```

4. Activate this environment:

```bash
source venv/bin/activate
```

Verify that you're in a python3 virtual environment by running:

- `$ python --version` should output a Python 3 version
- `$ pip --version` should output that it is working with Python 3

5. Install dependencies once at the beginning of this exercise with

```bash
# Must be in activated virtual environment
pip install -r requirements.txt
```

6. Exit and re-enter the virtual enviornment with the following command. This is needed to ensure the correct version of pytest is used in the terminal.

```bash
deactivate && source venv/bin/activate
```
