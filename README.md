# Welcome to PyEncryption this is a encryption.

## This is used to encrypt all the files and directories using AES256

## Python Libraries Needed:
    optparse
    Crypto
    hashlib
    base64

## It is used to encrypt files and folders

## Usage: 
    python3 pyencrypt.py [options]

    Options:
        -h, --help                              show this help message and exit
        -f FILE, --file=FILE                    File to Encrypt
        -d DIRECTORY, --directory=DIRECTORY     Directory to Encrypt
        -k KEY_FILE, --key=KEY_FILE             Key file (without the extension of .key) to encrypt, defaults to key.key
        -p PATH, --path=PATH  path where the target file/directory is located (Eg., /home/Desktop if the file to encrypt is sample.txt in /home/Desktop/sample.txt)
        -e, --encrypt                           Encrypt the file/directory
        -u, --decrypt                           decrypt the file/directory
        -v, --verbose                           Verbosity of the Actions
        -l KEY_PATH, --key_path=KEY_PATH        Path where the key is located (Eg., /home/Desktop if the key is in /home/Desktop directory)

## Example: 
### Encryption
#### To Encrypt sample.txt file in current directory as the encrypt.py python file
    1. python3 encrypt.py -e -f sample.txt 

by default this generates the key "key.key" in current directory of the encrypt.py.

#### To Encrypt all files of sampledir directory in current directory as the encrypt.py python file
    2. python3 encrypt.py -e -f sampledir

by default this generates the key "key.key" in current directory of the encrypt.py.

#### To Encrypt /home/user/sample.txt file in /home/user directory
    3. python3 encrypt.py -e -f sample.txt -p /home/user

by default this generates the key "key.key" in current directory of the encrypt.py.

#### To Encrypt /home/user/sampledir directory in /home/user directory
    4. python3 encrypt.py -u -f sampledir -p /home/user

by default this uses the key "key.key" in current directory of the encrypt.py.

### Decryption
#### To Decrypt sample.txt file in current directory as the encrypt.py python file
    5. python3 encrypt.py -u -f sample.txt 

by default this uses the key "key.key" in current directory of the encrypt.py.

#### To Decrypt all files of sampledir directory in current directory as the encrypt.py python file
    6. python3 encrypt.py -u -f sampledir

by default this uses the key "key.key" in current directory of the encrypt.py.

#### To Decrypt /home/user/sample.txt file in /home/user directory
    7. python3 encrypt.py -u -f sample.txt -p /home/user

by default this uses the key "key.key" in current directory of the encrypt.py.

#### To Decrypt /home/user/sampledir directory in /home/user directory
    8. python3 encrypt.py -u -f sampledir -p /home/user

by default this uses the key "key.key" in current directory of the encrypt.py.

### To use separate key, use the -k argument.
Example:
#### To Decrypt /home/user/sampledir directory in /home/user directory using key key2.key
    9. python3 encrypt.py -u -f sampledir -p /home/user -k key2
    
by default this uses the key "key2.key" in current directory of the encrypt.py.
Notice that the ".key" extension is not specified here. Only specify the prefix.

## If you want to use the key file from some other location, then use
    10. python3 encrypt.py -u -f sampledir -p /home/user -k key2 -l /home/user

This execution will use /home/user/key2.key to encrypt the files in /home/user/sampledir

#### To Encrypt /home/user/sample.txt directory in /home/user directory using key key2.key
    11. python3 encrypt.py -e -f sample.txt -p /home/user -k key2
    
by default this uses the key "key2.key" in current directory of the encrypt.py.
Notice that the ".key" extension is not specified here. Only specify the prefix.

## If you want to see the Descriptions, use -v argument
    12. python3 encrypt.py -u -f sample.txt -p /home/user -k key2 -l /home/user -v

This execution will use /home/user/key2.key to encrypt the file in /home/user/sample.txt
This will print verbose output

# Normal Usage
    13. python3 encrypt.py -[u/e] -[f/d] [file/dir] [[-p /home/user] / blank] [[-k key2] / blank] [[-l /home/user] / blank]

    Here the blank denotes that this argument is not needed if the files are in the current directory
## Please store the key file somewhere safely. If lost, then it is nearly Impossible to recover the encrypted data.

# UPDATE
Now inorder to avoid forgetting the key files, I've Included the functionality, that encrypts with the password and decrypts with password.