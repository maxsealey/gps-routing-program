class HashTable:
    def __init__(self, capacity=20):
        self.table = [] # initialize hashmap with empty values
        for i in range(capacity):
            self.table.append([])

    # insert a new item into hash table
    def insert(self, i):

        # get hash and append new item in hashed location
        container_list = self.get_hash_value(self, i)
        container_list.append(i)

    # looks for value with matching key and returns if found
    def look_up(self, key):

        # get list where matching key is located
        container_list = self.get_hash_value(self, key)

        # search for key in list, returns None (if not found), or the item itself
        if key in container_list:
            i = container_list.index(key)
            return container_list[i]
        else:
            return None

    # removes item with matching key
    def remove(self, key):

        # get list where matching key is located
        container_list = self.get_hash_value(self, key)
        if key in container_list:
            container_list.remove(key)

    # code block used to get hash value and return list of items in container
    def get_hash_value(self, i):
        container = hash(i) % len(self.table)
        container_list = self.table[container]

        # returns list where item is to be appended
        return container_list

