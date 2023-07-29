from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
import hashlib
import random
from cryptography.hazmat.primitives import serialization

def generateTxid():
    random_integer = random.randint(0, 999999)
    integer_string = str(random_integer)
    sha256_hash = hashlib.sha256(integer_string.encode()).hexdigest()
    return sha256_hash

def generateInput():
    prevTxid = generateTxid()
    prevOutputIndex = random.randint(0,5)
    return prevTxid, prevOutputIndex

def generateOutput():
    random_integer = random.randint(1, 100)
    recipientAddress = 'recipient_address_' + str(random_integer)
    amount = round(random.uniform(0.001, 1.0), 8)
    return recipientAddress, amount

def generateTransactionFee():
    fee = round(random.uniform(0.00001, 0.001), 8)
    return fee

def generateRandomTransaction():
    txid = generateTxid()
    inputPrevTxid, inputPrevOutputIndex = generateInput()
    outputRecipientAddress, outputAmount = generateOutput()
    transactionFee = generateTransactionFee()
    return txid, inputPrevTxid, inputPrevOutputIndex,outputRecipientAddress, outputAmount,transactionFee

def concatenateString(txid, inputPrevTxid,inputPrevOutputIndex, outputRecipientAddress,outputAmount, transactionFee):
    transactionData = str(txid) + str(inputPrevTxid) + str(inputPrevOutputIndex) + str(outputRecipientAddress) + str(outputAmount)+ str(transactionFee)
    return transactionData

def generateECDSAKeyPair():
    ECDSAPrivateKey = ec.generate_private_key(ec.SECP256K1())
    ECDSAPublicKey =  ECDSAPrivateKey.public_key()
    return ECDSAPrivateKey, ECDSAPublicKey

def ECDSASign(privateKey, message):
    signature = privateKey.sign(message,ec.ECDSA(hashes.SHA256()))
    return signature

def ECDSAVerify(publicKey, message,signature):
    try:
        publicKey.verify(signature, message,ec.ECDSA(hashes.SHA256()))
        return    True
    except Exception:
        return False
    
# def main():
#     txid, inputPrevTxid, inputPrevOutputIndex, outputRecipientAddress, outputAmount, transactionFee = generateRandomTransaction()
#     transactionDataAsMessage = concatenateString(txid, inputPrevTxid, inputPrevOutputIndex, outputRecipientAddress, outputAmount, transactionFee).encode()
#     transactionDataAsMessageSHA256Hashed = hashlib.sha256(transactionDataAsMessage).digest()
#     ECDSAPrivateKey, ECDSAPublicKey = generateECDSAKeyPair()
#     signature = ECDSASign(ECDSAPrivateKey, transactionDataAsMessageSHA256Hashed)
#     verified = ECDSAVerify(ECDSAPublicKey, transactionDataAsMessageSHA256Hashed, signature)
#     print("ECDSA:")
#     print("ECDSA Public Key:", ECDSAPublicKey.public_bytes(encoding=serialization.Encoding.X962, format=serialization.PublicFormat.UncompressedPoint).hex())
#     #print("ECDSA Private Key:", ECDSAPrivateKey.private_bytes(encoding=serialization.Encoding.DER, format=serialization.PrivateFormat.PKCS8).hex())
#     print("ECDSA Private Key:", ECDSAPrivateKey.private_bytes(encoding=serialization.Encoding.DER, format=serialization.PrivateFormat.PKCS8, encryption_algorithm=serialization.NoEncryption()).hex())
#     print("transactionDataAsMessageSHA256Hashed:", transactionDataAsMessageSHA256Hashed.hex())
#     print("Signature:", signature.hex())
#     print("Verification:", verified)

# main()   
def main():
    txid, inputPrevTxid, inputPrevOutputIndex,outputRecipientAddress, outputAmount,transactionFee = generateRandomTransaction()
    transactionDataAsMessage =concatenateString(txid, inputPrevTxid,inputPrevOutputIndex, outputRecipientAddress,outputAmount, transactionFee).encode()
    transactionDataAsMessageSHA256Hashed = hashlib.sha256(transactionDataAsMessage).hexdigest()
    ECDSAPrivateKey, ECDSAPublicKey = generateECDSAKeyPair()
    signature = ECDSASign(ECDSAPrivateKey, transactionDataAsMessageSHA256Hashed)
    verified = ECDSAVerify(ECDSAPublicKey, transactionDataAsMessageSHA256Hashed, signature)
    print ("ECDSA:")
    print ("ECDSA Public Key:", ECDSAPublicKey.to_bytes().hex())
    print ("ECDSA Private Key:", ECDSAPrivateKey.to_bytes().hex())
    print ("transactionDataAsMessageSHA256Hashed:",transactionDataAsMessageSHA256Hashed.hex())
    print ("Signature:", signature.hex())
    print ("Verification:", verified)

main() 
