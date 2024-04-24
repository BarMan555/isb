from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from WorkingWithFiles import (deserialization_symmetric_key,
                              serialization_symmetric_key, 
                              deserialization_public_key, 
                              deserialization_private_key,
                              write_data_bytes)

class AsymmetricalKey:
    """Working with Asymmetric Key"""
    def generation_asym_keys(self) -> tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey]:
        """
        Generation pair of asymmetric keys

        Return:
            tuple: public key and private key
        """
        keys = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        private_key = keys
        public_key = keys.public_key()
        return (public_key, private_key)
    

    def encrypt_symm_key(self, 
                         path_symmetric : str,
                         path_public : str, 
                         path_encr_symmetric : str) -> None:
        """
        Encrypt the symmetric key using a public key and save to bytes file

        Args:
            path_symmetric: path to the file with symmetric key
            path_public: path to the file with public key
            path_encr_symmetric: path to the file where will be save a encrypted symmetric key
        """
        public_key = deserialization_public_key(path_public)
        symmetric_key = deserialization_symmetric_key(path_symmetric)

        encr_key = public_key.encrypt(symmetric_key, 
                                      padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                   algorithm=hashes.SHA256(),
                                                   label=None))
        write_data_bytes(encr_key, path_encr_symmetric)


    def decrypt_symm_key(self,
                         path_encr_symmetric : str,
                         path_private : str,
                         path_decr_symmetric : str) -> bytes:
        """
        Decrypt symmetric key using a private key
        
        Args:
            path_encr_symmetric: path to the file with encrypted symmetric key
            path_private: path to the file with private key
            path_decr_symmetric: path to the file where will be save a encrypted symmetric key
        Return:
            bytes: symmetric key
        """
        encr_symmetric = deserialization_symmetric_key(path_encr_symmetric)
        private_key = deserialization_private_key(path_private)

        symmetric_key = private_key.decrypt(encr_symmetric,
                                      padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                   algorithm=hashes.SHA256(),
                                                   label=None))
        serialization_symmetric_key(symmetric_key, path_decr_symmetric)
        return symmetric_key