import random

from hashtable.separate_chaining import SeparateChainingTable

def test_insert():
    nums = []
    # Get a unique random number.
    #
    # This is mostly me being paranoid about bad luck.
    def get_unique_num():
        num = random.randint(-10000, 10000)
        while num in nums:
            num = random.randint(-10000, 10000)
        nums.append(num)
        return num

    table = SeparateChainingTable()

    for size in range(1, 5):
        key = get_unique_num()
        val = get_unique_num()

        table.insert(key, val)

        assert table.size == size
        assert table.get(key) == val

    # Check for missing keys.
    assert table.get(get_unique_num()) == None
    assert table.get(get_unique_num(), "missing") == "missing"
