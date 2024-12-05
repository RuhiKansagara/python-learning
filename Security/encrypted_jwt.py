from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import jwt

# Generate RSA keys
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# Payload
payload = {"data": "This is sensitive"}

# Encrypt the payload and the use of Optimal Asymmetric Encryption Padding (OAEP)
encrypted_payload = public_key.encrypt(
    jwt.encode(payload, "key", algorithm="HS256").encode(),
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("Encrypted JWT:", encrypted_payload)

# Decrypt the payload
decrypted_payload = private_key.decrypt(
    encrypted_payload,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("Decrypted Payload:", jwt.decode(decrypted_payload.decode(), "key", algorithms=["HS256"]))