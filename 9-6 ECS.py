from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, dsa
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec


def generateECDSAKeyPair():
    privateKey= ec.generate_private_key(ec.SECP256K1())
    publicKey = privateKey.public_key()
    return privateKey, publicKey

def ECDSASign(privateKey, message):
    signature = privateKey.sign(message, ec.ECDSA(hashes.SHA256())) 
    return signature

def ECDSAVerify(publicKey, message, signature):
    try:
        publicKey.verify(signature, message, ec.ECDSA(hashes.SHA256()))
        return True
    except:
        return False
    
def main():
    ECDSAPrivateKey, ECDSAPublicKey = generateECDSAKeyPair()
    message = b"Message for ECDSA algorithm"
    signature = ECDSASign(ECDSAPrivateKey, message) 
    verified = ECDSAVerify(ECDSAPublicKey, message, signature) 
    print("ECDSA Public Key:", ECDSAPublicKey)
    print("ECDSA Private Key::", ECDSAPrivateKey)
    print("Message:", message)
    print("Signature:", signature)
    print("Verification:", verified)
    
main()




