import unittest
from client.session import SessionManager

class TestSessionManager(unittest.TestCase):
    def test_login_logout(self):
        session = SessionManager()
        self.assertFalse(session.is_authenticated())
        session.login("user1", "token123")
        self.assertTrue(session.is_authenticated())
        session.logout()
        self.assertFalse(session.is_authenticated())
