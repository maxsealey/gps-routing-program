class HashTable:
    def __init__(self, init_capacity=15):
        # initialize hashmap with empty values
        self.table = []
        for i in range(init_capacity):
            self.table.append([])

    # insert a new item into hash table
    def insert(self, key, i):
        # get hash and append new item in hashed location
        container = hash(key) % len(self.table)
        container_list = self.table[container]
        
        for key_val in container_list:

            if key_val[0] == key:
                key_val[1] = i
                return True
        container_list.append([key, i])
        return True

    # looks for value with matching key and returns if found
    def look_up(self, key):
        # get list where matching key is located
        container = hash(key) % len(self.table)
        container_list = self.table[container]

        for key_val in container_list:
            if key_val[0] == key:
                return key_val[1]
        return None
        # search for key in list, returns None (if not found), or the item itself

    # removes item with matching key
    def remove(self, key):
        # get list where matching key is located
        container = hash(key) % len(self.table)
        container_list = self.table[container]

        for key_val in container_list:
            if key_val[0] == key:
                container_list.remove([key_val[0], key_val[1]])