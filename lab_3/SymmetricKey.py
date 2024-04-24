import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from WorkingWithFiles import (read_data, 
                              read_data_bytes, 
                              deserialization_symmetric_key, 
                              write_data_bytes,
                              write_data)


class SymmetricKey:
    """Working with Symmetric Key"""
    def generation_symm_key(self) -> bytes:
        """
        Generation a symmetric key
        
        Return:
            Symmetric key
        """
        return os.urandom(16)
    

    def encrypt_text(self, 
                     path_text : str, 
                     path_encr_text : str, 
                     path_key : str) -> bytes:

        """
        Encrypt the text using a symmetric key and save result in file
        --------
        Args:
            path_text: path to the text file
            path_encr_text: path to the enctypted text file
            path_key: path to the symmetric key file

        Return:
            encrypted text in bytes
        """
        text = bytes(read_data(path_text), 'UTF-8')
        key = deserialization_symmetric_key(path_key)

        padder = padding.PKCS7(128).padder()
        padded_text = padder.update(text)+padder.finalize()
        iv = os.urandom(16) 
        cipher = Cipher(algorithms.SEED(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        encryptor_text = encryptor.update(padded_text) + encryptor.finalize()

        write_data_bytes(encryptor_text, path_encr_text)
        return encryptor_text
    
    def decrypt_text(self, 
                     path_encr_text : str, 
                     path_decry_text : str,
                     path_key : str) -> str:
        """
        Decrypt the text using a symmetric key and save result in file
        --------
        Args:
            path_encr_text: path to the enctypted text file
            path_decry_tetx: path to the decrypted text file
            path_key: path to the symmetric key file

        Return:
            decrypted text
        """
        text = read_data_bytes(path_encr_text)
        key = deserialization_symmetric_key(path_key)
        iv = text[:16]
        text = text[16:]

        cipher = Cipher(algorithms.SEED(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        dc_text = decryptor.update(text) + decryptor.finalize()

        unpadder = padding.PKCS7(128).unpadder()
        unpadded_dc_text = unpadder.update(dc_text) + unpadder.finalize()
        result_text = unpadded_dc_text.decode('utf-8')
        write_data(result_text, path_decry_text)
        return result_text
