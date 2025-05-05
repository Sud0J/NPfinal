from client.crypto_utils import generate_keys, encrypt_message, decrypt_message
from client.session import SessionManager
from client.ui import display_message, get_user_input

def main():
    session = SessionManager()
    display_message("Welcome to SecureChat")
    username = get_user_input("Username: ")
    token = "fake_token_123"  # Simulate token
    session.login(username, token)

    if session.is_authenticated():
        display_message(f"Logged in as {username}")

    priv, pub = generate_keys()
    text = get_user_input("Enter message to encrypt: ")
    encrypted = encrypt_message(text, pub)
    decrypted = decrypt_message(encrypted, priv)
    display_message(f"Decrypted message: {decrypted}")

if __name__ == "__main__":
    main()
