from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Generate a random 16-byte key for AES encryption
key = get_random_bytes(16)

def encrypt_message(message):
    """
    Encrypts a message using AES encryption.
    """
    # Create a new AES cipher object
    cipher = AES.new(key, AES.MODE_CBC)
    
    # Pad the message to make it a multiple of 16 bytes
    padded_message = pad(message.encode(), AES.block_size)
    
    # Encrypt the message
    ciphertext = cipher.encrypt(padded_message)
    
    # Return the ciphertext and the initialization vector (IV)
    return ciphertext, cipher.iv

def decrypt_message(ciphertext, iv):
    """
    Decrypts a ciphertext using AES encryption.
    """
    # Create a new AES cipher object with the same key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Decrypt the message
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    
    # Return the original message
    return decrypted_message.decode()

# Example usage
if __name__ == "__main__":
    original_message = "Hello, This is an example for pycryptodome!"
    print(f"Original Message: {original_message}")
    
    # Encrypt the message
    encrypted_message, iv = encrypt_message(original_message)
    print(f"Encrypted Message: {encrypted_message}")
    
    # Decrypt the message
    decrypted_message = decrypt_message(encrypted_message, iv)
    print(f"Decrypted Message: {decrypted_message}")
