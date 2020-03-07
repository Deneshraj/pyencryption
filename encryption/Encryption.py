import os
import sys
import base64
import hashlib
import random
import string
from Crypto.Cipher import AES
from Crypto import Random

class Encryption:
    """
        This class encrypts the Files and Directories
    """
    def __init__(self, key_file, verbose):
        self.key_file = key_file
        self.verbose = bool(verbose)
        self.key = ""
        self.generate_key()
    
    def get_file_content(self, joined_file, mode):
        text = ""
        with open(joined_file, mode) as f:
            text = f.read()
        return text

    def write_file_content(self, joined_file, text, mode):
        with open(joined_file, mode) as f:
            f.write(text)

    def encrypt_file(self, file_name, path):
        """
            Encrypts the File
        """
        joined_file = os.path.join(path, file_name)
        self.output("Encrypting " + joined_file)
        
        text = self.get_file_content(joined_file, "r")
        enc_text = self.aes_encrypt(text)
        self.write_file_content(joined_file, enc_text, "w")

    
    def decrypt_file(self, file_name, path):
        """
            Decrypts the Encrypted File
        """
        joined_file = os.path.join(path, file_name)
        self.output("Decrypting " + joined_file)

        text = self.get_file_content(joined_file, "r") 
        decrypted_text = self.aes_decrypt(text)
        self.write_file_content(joined_file, decrypted_text, "w")

    def encrypt_directory(self, directory):
        """
            Encrypts the Directory
        """
        os.chdir(directory)                                     # Change to the directory which should be encrypted
        sub_dirs = os.listdir()
        current_working_dir = os.getcwd()   
        dir_list = []                                           # Holds all the subdirectories.
        no_dirs = False                         
        
        while not no_dirs:                                      # Checks if there are no subdirectory
            for sub_dir in sub_dirs:
                if(os.path.isfile(sub_dir)):                    # Checking if it was a file and encrypt it
                    self.encrypt_file(sub_dir, os.getcwd())
                elif os.path.isdir(sub_dir):
                    cwd = os.getcwd()
                    result = os.path.join(cwd, sub_dir)
                    self.output("Encrypting " + result)
                    dir_list.append(os.path.join(cwd, sub_dir)) # Appends the subdir to iteratively go through each subdirs
                else:
                    print("Invalid File Type... Leaving it Unencrypted!")
            
            """
                Checking all the subdirs and if the subdirs exist, then iteratively encrypt files
                else break out of the loop.
            """
            if(len(dir_list) <= 0):
                no_dirs = True
            else:
                current_dir = dir_list[0]
                dir_list = dir_list[1:]
                os.chdir(current_dir)
                sub_dirs = os.listdir(".")

    def decrypt_directory(self, directory):
        os.chdir(directory)                                         # Change to the directory which should be encrypted
        sub_dirs = os.listdir()
        current_working_dir = os.getcwd()
        dir_list = []                                               # Holds all the subdirectories
        no_dirs = False
        
        while not no_dirs:                                          # Checks if there are no subdirectory
            for sub_dir in sub_dirs:
                if(os.path.isfile(sub_dir)):                        # Checking if it was a file and encrypt it
                    self.decrypt_file(sub_dir, os.getcwd())
                elif os.path.isdir(sub_dir):
                    cwd = os.getcwd()
                    result = os.path.join(cwd, sub_dir)
                    self.output("Decrypting " + result)
                    dir_list.append(result)     # Appends the subdir to iteratively go through each subdirs
                else:
                    print("Invalid File Type... Leaving it Encrypted!")
            
            """
                Checking all the subdirs and if the subdirs exist, then iteratively decrypt files
                else break out of the loop.
            """
            if(len(dir_list) <= 0):
                no_dirs = True
            else:
                current_dir = dir_list[0]
                dir_list = dir_list[1:]
                os.chdir(current_dir)
                sub_dirs = os.listdir(".")

    def aes_encrypt(self, text):
        """
            Encrypts a text in AES
        """
        key = hashlib.sha256(self.key).digest()
        text = self.pad(text)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        
        return base64.b64encode(iv + cipher.encrypt(text)).decode()

    def aes_decrypt(self, enc_text):
        """
            Decrypts a text in AES
        """
        key = hashlib.sha256(self.key).digest()
        enc_text = base64.b64decode(enc_text)
        iv = enc_text[:16]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        dec_text = cipher.decrypt(enc_text[16:])

        return self.unpad(dec_text.decode())

    def pad(self, s):
        block_size = 16
        length = len(s)
        block = block_size - length % block_size    # To compute remaining chars to string to make the string s as multiple of 16
        return s + (block) * chr(block)             # To multiply the string of block to block times so we could decrypt later easily.

    def unpad(self, s):
        length = len(s)
        return s[:-ord(s[-1])]                      # To remove the remaining text back to the original text.

    def generate_key(self):
        """
            Generates random key and stores that in the file given.
        """
        try:                                                            # Checks for the existance of file.
            file_text = ""
            file_text = self.get_file_content(self.key_file, "rb").decode("utf-8")
            # with open(self.key_file, "rb") as f:
            #     file_text = f.read().decode("utf-8")

            self.key = file_text.encode("utf-8")                        # If file exists store the key in key attribute
        except FileNotFoundError:
            print(f"The Key file {self.key_file} is not found! Creating the new file!")
            chars = string.ascii_letters + string.digits + string.punctuation
            max_length = random.randint(100, 200)
            key = ""
            chars_length = len(chars)

            for i in range(max_length):                                 # Generation of Random key
                random_char = random.randint(0, chars_length - 1)
                key += chars[random_char]

            self.key = key
            self.write_file_content(self.key_file, key.encode(), "wb")
            # with open(self.key_file, "wb") as f:
            #     f.write(key.encode())                                   # writing the output key to key_file as encoded

    def output(self, st):
        if self.verbose == True:
            print(st)
