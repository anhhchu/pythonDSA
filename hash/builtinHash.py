'''
understand the python built-in hash function

'''

class Emp:
    def __init__(self, Id, name):
        self.Id = Id
        self.name = name

    def __hash__(self):
        h = hash("{}.{}".format(self.Id, self.name))
        return h

Emp1 = Emp(12345, "Ada")

print("Hash Value of object1 {}".format(hash(Emp1)))

Emp2 = Emp(12346, "Ritchie")

print("Hash Value of object2 {}".format(hash(Emp2)))


'''
Objects hashed using hash() are irreversible, leading to loss of information.
hash() returns hashed value only for immutable objects, hence can be used as an indicator to check for mutable/immutable objects.
https://www.geeksforgeeks.org/python-hash-method/
'''

# initializing objects 
# tuple are immutable 
tuple_val = (1, 2, 3, 4, 5) 
  
# list are mutable 
list_val = [1, 2, 3, 4, 5] 
  
# Printing the hash values. 
# Notice exception when trying 
# to convert mutable object 
print ("The tuple hash value is : " + str(hash(tuple_val))) 
print ("The list hash value is : " + str(hash(list_val))) 

 