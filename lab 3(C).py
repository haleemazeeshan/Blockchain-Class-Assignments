import hashlib

def calculate_block_hashes(blocks):
    block_hashes = []
    for block in blocks:
        hash_value = hashlib.sha256(block.encode()).hexdigest()
        block_hashes.append(hash_value)
    return block_hashes

def concatenate_and_hash(hash1, hash2):
    concatenated = hash1 + hash2
    hashed = hashlib.sha256(concatenated.encode()).hexdigest()
    return hashed

def construct_merkle_tree(hashes):
    if len(hashes) == 1:
        return hashes[0]

    next_level = []
    for i in range(0, len(hashes), 2):
        if i+1 < len(hashes):
            combined_hash = concatenate_and_hash(hashes[i], hashes[i+1])
            next_level.append(combined_hash)
        else:
            next_level.append(hashes[i])

    return construct_merkle_tree(next_level)

# Step a: Import a file
file_path = r"C:\Users\Zeeshan Khan\Downloads\2.1 Building Blocks - Hash structures, signatures, and coins (1).pptx"

# Step b: Parse the file into eight blocks
with open(file_path, 'r', encoding='utf-8') as file:  # Specify the appropriate encoding
    content = file.read()
block_size = len(content) // 8
blocks = [content[i:i+block_size] for i in range(0, len(content), block_size)]

# Step c: Calculate the SHA-256 hashes of each data block
block_hashes = calculate_block_hashes(blocks)

# Step d: Concatenate hashes to generate a Merkle tree
merkle_root = construct_merkle_tree(block_hashes)

# Step e: Print the Merkle root of the tree
print("Merkle root:", merkle_root)
