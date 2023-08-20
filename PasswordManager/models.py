import base64

from django.core.validators import URLValidator
from django.db import models
from cryptography.fernet import Fernet, InvalidToken


# Create your models here.
class Entry(models.Model):
    url = models.CharField(max_length=64, validators=[URLValidator()])
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    note = models.CharField(max_length=64)

    # key = models.TextField(max_length=300, null=True)

    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # deleted_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.url} {self.username} {self.password} {self.note}"

    # def serialize(self):
    #     return {
    #         "id": self.id,
    #         "url": self.url,
    #         "username": self.username,
    #         "password": self.password,
    #         "note": self.note
    #     }
    #
    # def unserialize(self, data):
    #     self.url = data["url"]
    #     self.username = data["username"]
    #     self.password = data["password"]
    #     self.note = data["note"]
    #     return self

    def encryptPassword(self):
        key = b'n_2ioxMtrX2YGzcAsHkX91WqiWMqczvdJsgu8I2Goss='
        f = Fernet(key)
        try:
            encrypted_password = f.encrypt(self.password.encode())
            self.password = base64.urlsafe_b64encode(encrypted_password).decode('utf-8')
            return self.password
        except InvalidToken:
            print("Invalid token or key. Encryption failed.")
            return None

    def decryptPassword(self):
        key = b'n_2ioxMtrX2YGzcAsHkX91WqiWMqczvdJsgu8I2Goss='
        f = Fernet(key)
        try:
            decrypted_password = f.decrypt(base64.urlsafe_b64decode(self.password)).decode('utf-8')
            return decrypted_password
        except InvalidToken:
            print("Invalid token or key. Decryption failed.")
            return None
