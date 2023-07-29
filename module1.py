import hashlib

def calculate_sha256_hash(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode('utf-8'))
    return sha256.hexdigest()

def mine_hash_with_difficulty(difficulty, data):
    nonce = 0
    attempts = 0

    while True:
        attempts += 1
        hash_string = data + str(nonce)
        sha256_hash = calculate_sha256_hash(hash_string)

        if sha256_hash[:2] == difficulty:
            return nonce, sha256_hash, attempts

        nonce += 1

if __name__ == "__main__":
    sender_email = "haleema.zeeshan14@gmail.com"
    recipient_email = "noor@gmail.com"
    email_subject = "hello"
    message_body = "hello how are you doing?"

    # Concatenate all input parameters
    input_data = sender_email + recipient_email + email_subject + message_body

    # Set the desired difficulty level (first two hexadecimal digits)
    difficulty_level = "ffff"

    # Perform mining and find the nonce that meets the difficulty level
    nonce, sha256_hash, attempts = mine_hash_with_difficulty(difficulty_level, input_data)

    print(f"\nNonce found: {nonce}")
    print(f"SHA-256 Hash: {sha256_hash}")
    print(f"Number of attempts: {attempts}")
