import hashlib

def calculate_hash(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode('utf-8'))
    return sha256.hexdigest()

def find_nonce(difficulty_level):
    sender_email = input("Sender's email address: ")
    recipient_email = input("Recipient's email address: ")
    email_subject = input("Email subject: ")
    message_body = input("Message body: ")
    nonce = 0
    attempts = 0

    while True:
        data = sender_email + recipient_email + email_subject + message_body + str(nonce)
        hash_result = calculate_hash(data)

        if hash_result[:difficulty_level] == 'f' * difficulty_level:
            return nonce, attempts

        nonce += 1
        attempts += 1

# Task 1
print("Task 1: Finding nonce with difficulty level of 2 bytes (first two hex digits as 'ff')")
nonce_1, attempts_1 = find_nonce(2)
print(f"Nonce found: {nonce_1}")
print(f"Attempts made: {attempts_1}")

# Task 2
print("Task 2: Finding nonce with difficulty level of 4 bytes (first four hex digits as 'ffff')")
nonce_2, attempts_2 = find_nonce(4)
print(f"Nonce found: {nonce_2}")
print(f"Attempts made: {attempts_2}")
