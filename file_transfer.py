import hashlib
import os

def compute_checksum(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def verify_file_integrity(file_path, expected_checksum):
    return compute_checksum(file_path) == expected_checksum

def split_file(file_path, chunk_size=4096):
    with open(file_path, "rb") as f:
        return [f.read(chunk_size) for _ in range((os.path.getsize(file_path) + chunk_size - 1) // chunk_size)]

def reassemble_file(chunks, output_path):
    with open(output_path, "wb") as f:
        for chunk in chunks:
            f.write(chunk)
