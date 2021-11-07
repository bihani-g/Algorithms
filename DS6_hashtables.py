# hashtable implementation

class HashTable:

    def __init__(self):
        # based on
        self.capacity = 10
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity

    # determines hash index value based on key
    def hash_function(self, key):
        hash_sum = 0

        for letter in key:
            hash_sum += ord(letter)

        return hash_sum % self.capacity

    def insert(self, key, data):

        # first find a valid location for the data
        index = self.hash_function(key)

        # but there may be collisions which means that the index will be occupied
        # while we do not find an empty array slot
        while self.keys[index] is not None:
            # sometimes we need to update the value if the key is already present
            if self.keys[index] == key:  # given key is already present and we need to update
                self.values[index] = data

            # otherwise do linear probing to find the next empty slot
            # update index such that it remains in the list (use %)
            index = (index + 1) % self.capacity

        # we have found the valid slot of the item, now insert item
        self.keys[index] = key
        self.values[index] = data

    def get(self, key):
        # find a valid index for the data
        index = self.hash_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]

            index = (index + 1) % self.capacity

        return None


if __name__ == '__main__':
    table = HashTable()
    table.insert('ADAM', 34)
    table.insert('mac', 45)
    table.insert('mac', 35)
    table.insert('BLAH', 89)

    print(table.get('mac'))
