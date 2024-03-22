import os
import json

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def key_for_symmetric_algorithm() -> bytes:
    key = os.urandom(32)
    return key


def keys_for_asymmetric_algorithm() -> tuple:
    keys = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    private_key = keys
    public_key = keys.public_key()
    return (public_key, private_key)


def serialization_public_key(path : str, key) -> None:
    with open(path, 'wb') as public_out:
            public_out.write(key.public_bytes(encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo))
            

def serialization_private_key(path : str, key) -> None:
    with open(path, 'wb') as private_out:
            private_out.write(key.private_bytes(encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()))