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
