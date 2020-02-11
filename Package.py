import Destination

class Package:
    def __init__(self, id_number, destination, package_weight, deadline, special_note, delivery_status = "en route"):
        self.id_number = id_number
        self.destination = destination
        self.package_weight = package_weight
        self.deadline = deadline
        self.special_note = special_note
        self.delivery_status = delivery_status


class PackageHashTable:
    def __init__(self, capacity = 12):
        self.table = []
        for i in range(capacity):
            self.table.append([])
    #This inserts package into the hash table by package id number. Time complexity O(1)
    def insert_into_table(self, package):
        bucket = hash(package.id_number) % len(self.table)
        bucket_list = self.table[bucket]
        bucket_list.append(package)
    #This run a search in the hash table for package by id number. Time complexity O(n)
    def search_table(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for i in range(len(bucket_list)):
           if key == bucket_list[i].id_number:
               return bucket_list[i] 
        else: 
          return None
    #This runs a seach in the hash table for a package matching the id number. If a match is found, it is deleted. Time complexity O(n)
    def remove_from_table(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for i in range(len(bucket_list)):
            if key == bucket_list[i].id_number:
               bucket_list.remove[i]