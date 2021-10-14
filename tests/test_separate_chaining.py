import random

from hashtable.separate_chaining import SeparateChainingTable

def test_insert():
    table = SeparateChainingTable()

    key1 = random.randint(0, 150)
    val1 = random.randint(0, 150)

    table.insert(key1, val1)

    assert table.size == 1
    assert table.get(key1) == val1

    key2 = random.randint(151, 250)
    val2 = random.randint(151, 250)

    table.insert(key2, val2)

    assert table.size == 2
    assert table.get(key2) == val2

    assert table.get(random.randint(251, 350)) == None
    assert table.get(random.randint(251, 350), "missing") == "missing"
