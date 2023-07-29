
import base58
import hashlib
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec

# generate ECDSA public and private keys
def generate_keys():
    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    public_key = private_key.public_key()
    return private_key, public_key

# Function to derive Bitcoin wallet address from public key
def get_wallet_address(public_key):
    publicKeyBytes = public_key.public_bytes(
        encoding=serialization.Encoding.X962,
        format=serialization.PublicFormat.UncompressedPoint
    )
    sha256_hash = hashlib.sha256(publicKeyBytes).digest()
    ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()
    
    # Add the version byte (0x00) in front of the RIPEMD-160 hash
    extended_ripemd160_hash = b'\x00' + ripemd160_hash
    
    # Perform double SHA-256 hash on the extended RIPEMD-160 hash
    checksum = hashlib.sha256(hashlib.sha256(extended_ripemd160_hash).digest()).digest()
    
    # Add the first 32 bits of the checksum to the extended RIPEMD-160 hash
    final_hash = extended_ripemd160_hash + checksum[:4]
    
    # Encode the final hash in base58 to get the Bitcoin wallet address
    wallet_address = base58.b58encode(final_hash)
    
    return wallet_address.decode('utf-8')


def main():
    private_key, public_key = generate_keys()
    wallet_address = get_wallet_address(public_key)
    print(f"Bitcoin Wallet Address: {wallet_address}")

if __name__ == "__main__":
    main()
