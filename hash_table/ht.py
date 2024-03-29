from typing import Optional
class HashTable:

    def __init__(self,size=7):
        self.data_map=[None]*size

    def __hash(self,key):
        my_hash=0
        for letter in key:
            my_hash=(my_hash+ord(letter)*23)%len(self.data_map) # number can be any prime number
        return my_hash

    def set_item(self,key,value):
        index=self.__hash(key)
        if self.data_map[index]==None:
            self.data_map[index]=list()
        self.data_map[index].append([key,value])

    def get_item(self,key:str):
        index=self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0]==key:
                    return self.data_map[index][i][1]
        return None

    def print_table(self):
        for i,val in enumerate(self.data_map):
            print(i,":",val)

my_hash_table=HashTable()

my_hash_table.set_item("bolts",400)
my_hash_table.set_item("washers",50)
my_hash_table.set_item("lumber",70)
print(my_hash_table.get_item("bolts"))
print(my_hash_table.get_item("rods"))
# my_hash_table.print_table()