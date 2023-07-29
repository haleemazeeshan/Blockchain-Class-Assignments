from cryptography.hazmat.primitives.asymmetric import rsa, dsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
from cryptography.hazmat.primitives import padding

text="Hello Paksitan"
# public_exponent=65537
# key_size=2048
def generateRSAKeyPair():
    privateKey=rsa.generate_private_key(public_exponent=65537,key_size=2048) 
    public_key=privateKey.public_key()
    return public_key, privateKey

def RSAEncrypt(publicKey, text):
    cipher_text = publicKey.encrypt(text, padding=PKCS1v15())
    return cipher_text
    
def RSADecrypt(privatekey, cipher_text):
    plain_text = privatekey.decrypt(cipher_text,padding=PKCS1v15())
    return plain_text

def generateDSAKeyPair():
    privatekey=dsa.generate_private_key(key_size=1024)
    publickey=privatekey.public_key()
    return publickey, privatekey

# Generate a signature by calling the sign(message,
# hashing algorithm) method of privateKey. Use
# hashes.SHA256() as the hashing algorithm.
# 2. Return the resulting signature.

def DSASign(privateKey, message):
    signature = privateKey.sign(message, algorithm=hashes.SHA256())
    return signature

# Function DSAVerify(publicKey, message, signature):
# 1. Try to verify the signature by calling the verify(signature,
# message, hashing algorithm) method of publicKey. Use
# hashes.SHA256() as the hashing algorithm.
# 2. If the verification succeeds, return True.
# 3. If an exception occurs (doesn’t verify) during
# verification, return False

def DSAVerify(publickey, message, signature):
    try:
        publickey.verify(signature, message, hashes.SHA256())
        return True
    except:
        return False
    
# Function main():
# 1. Generate an RSA key pair by calling
# generateRSAKeyPair(). Store the returned keys as
# RSAprivateKey and RSApublicKey.
def main():
    RSAprivateKey, RSApublicKey = generateRSAKeyPair()
    plain_text = b"Pakistan Zindabad"
    plain_text = message.encode()
    cipher_text = RSAEncrypt(RSApublicKey, plain_text)

    #cipher_text = rsaEncrypt(public_Key, plain_text)
    decryptedText = RSADecrypt(RSAprivateKey, cipher_text)
    print("RSA Public Key:", RSApublicKey)
    print("RSA Private Key:", RSAprivateKey)
    print("Plaintext:", plain_text.decode())
    print("Ciphertext:", cipher_text)
    print("Decrypted Text:", decryptedText)

DSAPrivateKey, DSAPublicKey = generateDSAKeyPair()
message = b"Pakistan Zindabad"
signature = DSASign(DSAPrivateKey, message)
verified = DSAVerify(DSAPublicKey, message, signature)
print("DSA details:")
print("DSA Public Key:", DSAPublicKey)
print("DSA Private Key:", DSAPrivateKey)
print("Message:", message)
print("Signature:", signature)
print("Verification:", verified)

#if __name__ == "__main__":
main()
