import hashlib
import math

def calculate_block_hashes(blocks):
    block_hashes = []
    for block in blocks:
        hash_value = hashlib.sha256(block.encode('utf-8', errors='replace')).hexdigest()
        block_hashes.append(hash_value)
    return block_hashes

def concatenate_and_hash(hash1, hash2):
    concatenated = hash1 + hash2
    hashed = hashlib.sha256(concatenated.encode('utf-8', errors='replace')).hexdigest()
    return hashed

def construct_merkle_tree(hashes):
    if len(hashes) == 1:
        return hashes[0]

    markel_level = []
    for i in range(0, len(hashes), 2):
        if i+1 < len(hashes):
            combined_hash = concatenate_and_hash(hashes[i], hashes[i+1])
            markel_level.append(combined_hash)
        else:
            markel_level.append(hashes[i])
    
    return construct_merkle_tree(markel_level)

# Step 1: Import a file
file_path = r"C:\Users\Zeeshan Khan\Downloads\Lab 6-6-2023.pdf"

with open(file_path, 'r', encoding='latin-1') as file:
    content = file.read()
    print("Content length:", len(content))
    
block_size = (len(content) // 1024)  # Calculate block size, rounding down
print("Calculated block size:", (block_size))
# with open(file_path, 'r', encoding='latin-1') as file:  # Specify a different encoding, such as 'latin-1'
#     content = file.read()
# block_size = (len(content)//1024) # Calculate block size, rounding up
# blocks = []
# start = 0

# while start < len(content):
#     block = content[start:start+block_size]
#     blocks.append(block)
#     start += block_size
print ("block size",block_size)
# Step c: Calculate the SHA-256 hashes of each data block
block_hashes = calculate_block_hashes(block_size)
print("block hashes", block_hashes)

# Step d: Concatenate hashes to generate a Merkle tree
merkle_root = construct_merkle_tree(block_hashes)
 
# Step e: Print the Merkle root of the tree
print("Merkle root:", merkle_root)
