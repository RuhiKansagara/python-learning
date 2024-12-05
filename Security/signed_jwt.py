import jwt
import time

# Secret key for signing
secret_key = "mysecret"

# Header and payload
payload = {
    "sub": "1234567890",
    "name": "John Doe",
    "iat": int(time.time()),  # Current time in seconds (issued at)
    "exp": int(time.time() + 3600),  # Expire in 1 hour (3600 seconds)a(hours=1) (expiry time)
}

# Create the token
token = jwt.encode(payload, secret_key, algorithm="HS256")
print("Signed JWT:", token)

# Verify the token
decoded = jwt.decode(token, secret_key, algorithms=["HS256"])
print("Decoded Payload:", decoded)
