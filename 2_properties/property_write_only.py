import hashlib
import os


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    @property
    def password(self):
        raise AttributeError("Password is write-only")

    @password.setter
    def password(self, plaintext):
        self._hashed_password = hashlib.pbkdf2_hmac(
            "sha256", (self.name + plaintext).encode("utf-8"), os.urandom(32), 100_000
        )


user = User('Nicolay', '1234')

print(user._hashed_password)
# print(user.password)

user.password = '12345'
print(user._hashed_password)
