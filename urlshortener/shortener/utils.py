import hashlib
import uuid

def generate_short_code(long_url):
    unique_id = str(uuid.uuid4())  # Ensure the input to the hash function is unique
    hash_digest = hashlib.sha256(unique_id.encode() + long_url.encode()).hexdigest()
    short_code = hash_digest[:6]  # Take the first 6 characters for simplicity
    return short_code
