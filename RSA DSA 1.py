from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, dsa
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
from cryptography.hazmat.backends import default_backend

def generateRSAKeyPair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
       
    )
    public_key = private_key.public_key()
    return private_key, public_key

def RSAEncrypt(public_key, plain_text):
    cipher_text = public_key.encrypt(
        plain_text.encode(),
        padding=PKCS1v15()
    )
    return cipher_text

def RSADecrypt(private_key, cipher_text):
    plain_text = private_key.decrypt(
        cipher_text,
        padding=PKCS1v15()
    )
    return plain_text.decode()

def generateDSAKeyPair():
    private_key = dsa.generate_private_key(
        key_size=1024,
        
    )
    public_key = private_key.public_key()
    return private_key, public_key

def DSASign(private_key, message):
    signature = private_key.sign(
        message.encode(),
        algorithm=hashes.SHA256()
    )
    return signature

def DSAVerify(public_key, message, signature):
    try:
        public_key.verify(
            signature,
            message.encode(),
            algorithm=hashes.SHA256()
        )
        return True
    except:
        return False

def main():
    RSAprivateKey, RSApublicKey = generateRSAKeyPair()
    plainText = "Message for RSA algorithm"
    cipherText = RSAEncrypt(RSApublicKey, plainText)
    decryptedText = RSADecrypt(RSAprivateKey, cipherText)
    print("RSA Public Key:", RSApublicKey)
    print("RSA Private Key:", RSAprivateKey)
    print("Plaintext:", plainText)
    print("Ciphertext:", cipherText)
    print("Decrypted Text:", decryptedText)

    DSAPrivateKey, DSAPublicKey = generateDSAKeyPair()
    message = "Message for DSA algorithm"
    signature = DSASign(DSAPrivateKey, message)
    verified = DSAVerify(DSAPublicKey, message, signature)
    print("DSA details:")
    print("DSA Public Key:", DSAPublicKey)
    print("DSA Private Key:", DSAPrivateKey)
    print("Message:", message)
    print("Signature:", signature)
    print("Verification:", verified)

main()
