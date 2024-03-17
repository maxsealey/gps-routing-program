class HashTable:
    def __init__(self, capacity=20):
        # initialize hashmap with empty values
        self.table = []
        for i in range(capacity):
            self.table.append([])

    # insert a new item into hash table
    def insert(self, key, i):
        # get hash and append new item in hashed location
        container = hash(key) % len(self.table)
        container_list = self.table[container]
        container_list.append(i)

    # looks for value with matching key and returns if found
    def look_up(self, key):
        # get list where matching key is located
        container = hash(key) % len(self.table)
        container_list = self.table[container]

        # search for key in list, returns None (if not found), or the item itself
        if key in container_list:
            i = container_list.index(key)
            return container_list[i]
        else:
            return None

    # removes item with matching key
    def remove(self, key):
        # get list where matching key is located
        container = hash(key) % len(self.table)
        container_list = self.table[container]
        if key in container_list:
            container_list.remove(key)

