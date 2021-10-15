class SeparateChainingTable:
    def __init__(self, table_size=4):
        self.size = 0
        self.table = []
        for i in range(table_size):
            self.table.append([])

    def insert(self, key, value):
        """
        Insert `(key, value)` based on the hashed value of `key`.
        """
        index = hash(key) % len(self.table)
        self.table[index].append((key, value))


        # TODO: Try to insert into self.table

        # If successful, increment.
        self.size += 1

    def get(self, key, default=None):
        """
        Return the value stored with `key` or `default` if it is not there.
        """
        index = hash(key) % len(self.table)

        # Look for the key within the chain.
        for chain_key, value in self.table[index]:
            if key == chain_key:
                return value

        # Return default if we don't find the key.
        return default
