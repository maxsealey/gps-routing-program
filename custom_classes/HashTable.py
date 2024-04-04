"""
Chaining Hash Table - Self Adjusting Data Structure

Used to store all the packages to be delivered in a custom hash table.

Followed along with:
Tepe, Cemal (2020, Nov). Let's Go Hashing Webinar. Panopto.
Retrieved Mar 20th, 2024, from https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=f08d7871-d57a-496e-a6a1-ac7601308c71

"""


class HashTable:
    def __init__(self, init_capacity=15):
        # initialize hash table with empty values
        self.table = []
        for i in range(init_capacity):
            self.table.append([])

    # insert a new item into hash table
    def insert(self, key, i):
        # get hash and append new item in hashed location
        container = hash(key) % len(self.table)
        container_list = self.table[container]

        # if item already exists, overwrite/update new item
        for key_val in container_list:
            if key_val[0] == key:
                key_val[1] = i
                return True
        # add item to list in hashed container
        container_list.append([key, i])
        return True

    # looks for value with matching key and returns if found
    def look_up(self, key):
        # get list where matching key is located
        container = hash(key) % len(self.table)
        container_list = self.table[container]

        # search for key in list, returns None (if not found), or the item itself
        for key_val in container_list:
            if key_val[0] == key:
                return key_val[1]
        return None

    # removes item with matching key
    def remove(self, key):
        # get list where matching key is located
        container = hash(key) % len(self.table)
        container_list = self.table[container]

        # remove item if found
        for key_val in container_list:
            if key_val[0] == key:
                container_list.remove([key_val[0], key_val[1]])
