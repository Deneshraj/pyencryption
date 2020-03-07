import os
import sys
import traceback
from optparse import OptionParser

from encryption.Encryption import Encryption

# Main Function
def main(file_name, directory_name, encrypt, decrypt, key_file, path, verbose, key_path):
    key_file_location = os.path.join(key_path, key_file + ".key")
    key_exist = os.path.isfile(key_file_location)

    if (not key_exist) and decrypt:
        print("The key file you Entered is Incorrect!")
        sys.exit(1)
    enc = Encryption(key_file_location, verbose)                                      # Instantiating the Encryption object

    try:
        os.chdir(path)
    except Exception:
        print("Invalid path! Exiting...")
        sys.exit(1)


    if encrypt == True:
        if file_name and os.path.isfile(file_name):
            enc.encrypt_file(file_name, os.getcwd())
        elif directory_name and os.path.isdir(directory_name):
            print(os.path.isdir(directory_name))
            enc.encrypt_directory(directory_name)
        else:
            print("The file you Entered is not here! please add -p option, specifying the location of the output file.")
            sys.exit(1)
        
        print("Encrypted Successfully!")

    elif decrypt == True:
        if file_name and os.path.isfile(file_name):
            enc.decrypt_file(file_name, os.getcwd())
        elif directory_name and os.path.isdir(directory_name):
            enc.decrypt_directory(directory_name)
        else:
            print("The file you Entered is not here! please add -p option, specifying the location of the output file.")
            sys.exit(1)

        print("Decrypted Successfully!")

    else:
        print("Invalid Option! Exiting...")
        sys.exit(1)

# Defining the Input Args
def handle_args(parser):
    parser.add_option("-f", "--file", help="File to Encrypt", dest="file")
    parser.add_option("-d", "--directory", help="Directory to Encrypt", dest="directory")
    parser.add_option("-k", "--key", help="Key file (without the extension of .key) to encrypt, defaults to key.key", dest="key_file", default="key")
    parser.add_option("-p", "--path", help="Path where the target file/directory is located (Eg., /home/Desktop if the file to encrypt is sample.txt in /home/Desktop/sample.txt)", dest="path", default=".")
    parser.add_option("-e", "--encrypt", help="Encrypt the file/directory", action="store_true", dest="encrypt", default=False)
    parser.add_option("-u", "--decrypt", help="decrypt the file/directory", action="store_true", dest="decrypt", default=False)
    parser.add_option("-v", "--verbose", help="Verbosity of the Actions", action="store_true", dest="verbose", default=False)
    parser.add_option("-l", "--key_path", help="Path where the key is located (Eg., /home/Desktop if the key is in /home/Desktop directory)", dest="key_path", default=".")

    return parser.parse_args()

# Validating the Argument
def validate(file_name, directory_name, encrypt, decrypt, key, path, key_path):  
    if file_name == None and directory_name == None and not encrypt and not decrypt:
        return False

    if((key == None or key == "") or (path == None or path == "")  or (key_path == None or key_path == "")):
        return False

    if encrypt == True and decrypt == True:
        return False
    
    file_len = 0 if file_name == None else len(file_name)
    dir_len = 0 if directory_name == None else len(directory_name)

    if (file_len > 3 or dir_len > 3) and (encrypt or decrypt):
        if file_len > 3 and directory_name == None or dir_len > 3 and file_name == None:
            return True
        
        return False


if __name__ == "__main__":
    parser = OptionParser("usage: encrypt.py [options] [options]")
    options, args = handle_args(parser)

    file_name = options.file
    directory_name = options.directory
    encrypt = options.encrypt
    decrypt = options.decrypt
    key = options.key_file
    path = options.path
    verbose = bool(options.verbose)
    key_path = options.key_path

    result = validate(file_name, directory_name, encrypt, decrypt, key, path, key_path)

    if not result:
        parser.error("Incorrect Number of Arguments!")
        sys.exit(1)    
    else:
        try:
            main(file_name, directory_name, encrypt, decrypt, key, path, verbose, key_path)
        except Exception as e:
            print("Error occured!")
            if verbose:
                exec_info = sys.exc_info()
                print(f"Cause of Error: {e}") 
                print("Traceback: ")
                print(traceback.format_exc(10))
                del exec_info