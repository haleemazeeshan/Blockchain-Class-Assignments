from cryptography.hazmat.primitives.asymmetric import rsa, dsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
from cryptography.hazmat.primitives import padding

text = "Hello Pakistan"

def generateRSAKeyPair():
    privateKey = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    publicKey = privateKey.public_key()
    return publicKey, privateKey

def RSAEncrypt(publicKey, text):
    cipherText = publicKey.encrypt(text.encode(), padding=PKCS1v15())
    return cipherText

def RSADecrypt(privateKey, cipherText):
    plainText = privateKey.decrypt(cipherText, padding=PKCS1v15())
    return plainText.decode()

def generateDSAKeyPair():
    privateKey = dsa.generate_private_key(key_size=1024)
    publicKey = privateKey.public_key()
    return publicKey, privateKey

def DSASign(privateKey, message):
    signature = privateKey.sign(
        message.encode(), algorithm=hashes.SHA256()
    )
    return signature

def DSAVerify(publicKey, message, signature):
    try:
        publicKey.verify(
            signature, message.encode(), hashes.SHA256()
        )
        return True
    except:
        return False

def main():
    RSApublicKey, RSAprivateKey = generateRSAKeyPair()
    plainText = "Pakistan Zindabad"
    cipherText = RSAEncrypt(RSApublicKey, plainText)
    decryptedText = RSADecrypt(RSAprivateKey, cipherText)

    print("RSA Public Key:", RSApublicKey)
    print("RSA Private Key:", RSAprivateKey)
    print("Plaintext:", plainText)
    print("Ciphertext:", cipherText)
    print("Decrypted Text:", decryptedText)

    DSAPublicKey, DSAPrivateKey = generateDSAKeyPair()
    message = "Pakistan Zindabad"
    signature = DSASign(DSAPrivateKey, message)
    verified = DSAVerify(DSAPublicKey, message, signature)

    print("DSA details:")
    print("DSA Public Key:", DSAPublicKey)
    print("DSA Private Key:", DSAPrivateKey)
    print("Message:", message)
    print("Signature:", signature)
    print("Verification:", verified)

if __name__ == "__main__":
    main()
