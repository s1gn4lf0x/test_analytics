import base64

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet, MultiFernet

from django.conf import settings

class FernetHelper:
    """Helper class to decrypt fernet encrypted fields in the web DB"""
    def __init__(self):
        self.f = self.fernet(self.fernet_keys())

    def derive_fernet_key(self, input_key):
        """Derive a 32-bit b64-encoded Fernet key from arbitrary input key."""
        b = input_key if isinstance(input_key, bytes) else input_key.encode('utf-8')
        hkdf = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b'django-fernet-fields-hkdf-salt',
            info=b'django-fernet-fields',
            backend=default_backend(),
        )
        return base64.urlsafe_b64encode(hkdf.derive(b))

    def fernet_keys(self):
        keys = getattr(settings, 'FERNET_KEYS', None)
        if keys is None:
            keys = [settings.SECRET_KEY]
        if getattr(settings, 'FERNET_USE_HKDF', True):
            keys = [self.derive_fernet_key(k) for k in keys]
        return keys

    def fernet(self, keys):
        if len(keys) == 1:
            return Fernet(keys[0])
        else:
            return MultiFernet([Fernet[k] for k in keys])

    def decrypt_fernet_field(self, val):
        if val:
            return self.f.decrypt(bytes(val))
        return None
