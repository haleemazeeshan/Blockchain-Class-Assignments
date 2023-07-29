import hashlib

def calculate_hash(file_path, hash_algorithm):
    with open(file_path, "rb") as file:
        content = file.read()
        hash_object = hashlib.new(hash_algorithm)
        hash_object.update(content)
        return hash_object.hexdigest()

file1_path = "C:\\Users\\Zeeshan Khan\\Downloads\\message1.bin"
file2_path = "C:\\Users\\Zeeshan Khan\\Downloads\\message2.bin"

md5_hash_file1 = calculate_hash(file1_path, "md5")
sha1_hash_file1 = calculate_hash(file1_path, "sha1")

md5_hash_file2 = calculate_hash(file2_path, "md5")
sha1_hash_file2 = calculate_hash(file2_path, "sha1")

print("File: ", file1_path)
print("MD5: ", md5_hash_file1)
print("SHA-1: ", sha1_hash_file1)
print()

print("File: ", file2_path)
print("MD5: ", md5_hash_file2)
print("SHA-1: ", sha1_hash_file2)
