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

## Activity ##

For this activity you will write the `insert` method for the two different hash tables (`SeparateChainingTable` and `LinearProbingTable`) within the `hashtables` directory.

All this needs to do is insert the key into the table in the correct location.  It does _not_ need to handle the case where the key already exists (that is optional).  **Assume that the user will never insert the same key twice.**

You should use the built in function `hash` as your hash function (though you will need to mod by the size of the table each time you insert).

The only other method needed to pass the tests is already there (`get`).

### Optional Challenges ###

If you have extra time or are just super pumped about hash tables and want to do more after class you can do the following:

* Stop assuming the user will never try to insert the same key twice.
* Grow the table (double its size) when it is more than 75% full (`self.size >= len(table) * 0.75`).
* Implement `delete` to remove an item from the table.
