import unittest
import os
from client.file_transfer import compute_checksum, verify_file_integrity, split_file, reassemble_file

class TestFileTransfer(unittest.TestCase):
    def setUp(self):
        self.test_file = "testfile.txt"
        self.content = b"File content for test."
        with open(self.test_file, "wb") as f:
            f.write(self.content)

    def tearDown(self):
        os.remove(self.test_file)
        if os.path.exists("reconstructed.txt"):
            os.remove("reconstructed.txt")

    def test_checksum(self):
        checksum = compute_checksum(self.test_file)
        self.assertTrue(verify_file_integrity(self.test_file, checksum))

    def test_checksum_fails(self):
        checksum = compute_checksum(self.test_file)
        with open(self.test_file, "ab") as f:
            f.write(b"corruption")
        self.assertFalse(verify_file_integrity(self.test_file, checksum))

    def test_split_and_reassemble(self):
        chunks = split_file(self.test_file, chunk_size=8)
        reassemble_file(chunks, "reconstructed.txt")
        original_checksum = compute_checksum(self.test_file)
        new_checksum = compute_checksum("reconstructed.txt")
        self.assertEqual(original_checksum, new_checksum)
