import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class SymmetricKey:
    """Working with Symmetric Key"""
    def generation_symm_key(self) -> bytes:
        """
        Generation a symmetric key
        
        Return:
            Symmetric key
        """
        return os.urandom(16)
    

    def encrypt_text(self, path_text : str, 
                     path_encr_text : str, 
                     key : bytes):

        """"
        Encrypt the text using a symmetric key and save result in file
        """

