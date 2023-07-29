import hashlib

def calculate_hash(file_path):
    with open(file_path, "rb") as file:
        content = file.read()
        return hashlib.sha256(content).hexdigest()

file_path = r"C:\Users\Zeeshan Khan\Desktop\webdesign.pptx"
file_hash = calculate_hash(file_path)

print("SHA-256 Hash:", file_hash)
