import hashlib


# Eight hash values
Part1 = "if you happy"
hash_value1 = hashlib.sha256(Part1.encode()).hexdigest()
Part2 = "and you know it"
hash_value2 = hashlib.sha256(Part2.encode()).hexdigest()
Part3 = "and you really want to show it"
hash_value3 = hashlib.sha256(Part3.encode()).hexdigest()
Part4 = "clap your hands"
hash_value4 = hashlib.sha256(Part4.encode()).hexdigest()
Part5 = "stomp your feet"
hash_value5 = hashlib.sha256(Part5.encode()).hexdigest()
Part6 = "turn around"
hash_value6 = hashlib.sha256(Part6.encode()).hexdigest()
Part7 = "say hurry"
hash_value7 = hashlib.sha256(Part7.encode()).hexdigest()
Part8 = "say happy"
hash_value8 = hashlib.sha256(Part8.encode()).hexdigest()

print("Hash value 1:", hash_value1)
print("Hash value 2:", hash_value2)
print("Hash value 3:", hash_value3)
print("Hash value 4:", hash_value4)
print("Hash value 5:", hash_value5)
print("Hash value 6:", hash_value6)
print("Hash value 7:", hash_value7)
print("Hash value 8:", hash_value8)
# Step 1
hash12 = hash_value1+ hash_value2
hashed = hashlib.sha256(hash12.encode()).hexdigest()
print("Hash 1+ hash 2 =",hashed)
hash13 = hash_value3+ hash_value4
hashed1 = hashlib.sha256(hash13.encode()).hexdigest()
print("Hash 3+ hash 4 =",hashed1)
hash14 = hash_value5+ hash_value6
hashed2 = hashlib.sha256(hash14.encode()).hexdigest()
print("Hash 5+ hash 6 =",hashed2)
hash15 = hash_value7+ hash_value8
hashed3 = hashlib.sha256(hash15.encode()).hexdigest()
print("Hash 7+ hash 8 =",hashed3)


# Step 2
seclast= hashed+hashed1
hashe = hashlib.sha256(seclast.encode()).hexdigest()
print("Concatenated 1", hashe)
seclast2= hashed2+hashed3
hashe1 = hashlib.sha256(seclast2.encode()).hexdigest()
print("Concatenated 2", hashe1)


#Step 3
root=hashe+hashe1
has = hashlib.sha256(root.encode()).hexdigest()
print("Merkle tree root value:", has)
