import hashlib
import bcrypt

# Step b: Taking name as input
name = "'decades after.'"

# Step c: Converting name string to bytes
name_bytes = name.encode()

# Step d: Generating hashes

# MD5 hash
md5_hash = hashlib.md5(name_bytes).hexdigest()

# SHA-1 hash
sha1_hash = hashlib.sha1(name_bytes).hexdigest()

# SHA-256 hash
sha256_hash = hashlib.sha256(name_bytes).hexdigest()

# SHA-512 hash
sha512_hash = hashlib.sha512(name_bytes).hexdigest()

# SHA-3 hash
sha3_hash = hashlib.sha3_256(name_bytes).hexdigest()

# BLAKE2 hash
blake2_hash = hashlib.blake2s(name_bytes).hexdigest()

# bcrypt hash
bcrypt_hash = bcrypt.hashpw(name_bytes, bcrypt.gensalt()).decode()

# RIPEMD-160 hash
ripemd160_hash = hashlib.new('ripemd160', name_bytes).hexdigest()

# Printing the hashes
print("MD5 hash:", md5_hash)
print("SHA-1 hash:", sha1_hash)
print("SHA-256 hash:", sha256_hash)
print("SHA-512 hash:", sha512_hash)
print("SHA-3 hash:", sha3_hash)
print("BLAKE2 hash:", blake2_hash)
print("bcrypt hash:", bcrypt_hash)
print("RIPEMD-160 hash:", ripemd160_hash)
