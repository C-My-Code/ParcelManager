class Destination:

    def __init__(self, destination_id, business_name, street_address, city, zip):
        self.destination_id = destination_id
        self.business_name = business_name
        self.street_address = street_address
        self.city = city
        self.zip = zip

class DestinationHashTable:
    def __init__(self, capacity = 12):
        self.table = []
        for i in range(capacity):
            self.table.append([])

    #This inserts a destination into the hash table by street addres. Time complexity O(1)
    def insert_into_table(self, destination):
        bucket = hash(destination.street_address) % len(self.table)
        bucket_list = self.table[bucket]
        bucket_list.append(destination)

     #This run a search in the hash table for a destination by street address. Time complexity O(n)
    def search_table(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for i in range(len(bucket_list)):
           if key == bucket_list[i].street_address:
               return bucket_list[i] 
        else: 
          return None
    #This runs a seach in the hash table for a destination matching the street address. If a match is found, it is deleted. Time complexity O(n)
    def remove_from_table(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        if key in bucket_list:
            bucket_list.remove(key)

    #This method simply calls the search method and returns a match if found. This was used for readability purposes elsewhere in the code.
    def existing_destination(self,streetaddress):
        x = self.search_table(streetaddress)
        return x;