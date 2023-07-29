import hashlib

def concatenate_and_hash(hash1, hash2):
    concatenated = hash1 + hash2
    hashed = hashlib.sha256(concatenated.encode()).hexdigest()
    return hashed

# Four hash values
Part1 = "1d0ada7a906e529d19fb2aca66911eaaee84ff4c7c6b685f019cd79c2deec5ff"
Part2 = "40791afdc85ba029dc28348174e5bd5070dd664a421234f7a935a62d43f7852f"
Part3 = "1e1b9dbeb353e6728457945cc47dac1a0121a3089bacf01650059bab0bfe92b6"
Part4 = "c4d635156f40988570f84cb5bac38b412c1649b5261c524dcd199293e50331b0"

# Step 1
hash12 = concatenate_and_hash(Part1, Part2)
hash34 = concatenate_and_hash(Part3, Part4)

# Step 2
root = concatenate_and_hash(hash12, hash34)
print("Hash 1", Part1)
print("Hash 2", Part2)
print("Hash 3", Part3)
print("Hash 4", Part4)
print("Concatenated Hash 1 + Hash 2", hash12)
print("Concatenated Hash 3 + Hash 4", hash34)
print("Merkle tree root value:", root)
