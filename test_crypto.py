import unittest
from client.crypto_utils import generate_keys, encrypt_message, decrypt_message

class TestCryptoUtils(unittest.TestCase):
    def setUp(self):
        self.private_key, self.public_key = generate_keys()
        self.message = "Test secure message"

    def test_encrypt_decrypt(self):
        encrypted = encrypt_message(self.message, self.public_key)
        decrypted = decrypt_message(encrypted, self.private_key)
        self.assertEqual(decrypted, self.message)

    def test_encrypt_output_differs(self):
        encrypted1 = encrypt_message(self.message, self.public_key)
        encrypted2 = encrypt_message(self.message, self.public_key)
        self.assertNotEqual(encrypted1, encrypted2)
