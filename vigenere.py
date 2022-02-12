## Nick MacDonald
## Vigenere Cipher
## Professor Seasholtz
## 02/11/2022

## Function to remove spaces from string
def remove(string):
    return string.replace(" ", "")

## Function to create key
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return (key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return ("".join(key))

## Encryption function
def encryption(string, key):
    string = remove(string)
    string = string.upper()
    key = key.upper()
    encrypt_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        encrypt_text.append(chr(x))
    return ("".join(encrypt_text))

## Decryption function
def decryption(string, key):
    string = remove(string)
    encrypt_text = string.upper()
    key = key.upper()
    orig_text = []
    for i in range(len(encrypt_text)):
        x = (ord(encrypt_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return ("".join(orig_text))

## Main Function
if __name__ == "__main__":
    ## Is this Encryption or Decryption?
    type = input("Do you want to [E]ncrypt or [D]ecrypt the message? (Choose E or D): ")

## If statement to decide whether to encrypt or decrypt
    if type == "E" or type == "e": ## Encryption
        print("")
        string = input("Enter the message to be Encrypted/Decrypted: ")
        print("")
        keyword = input("Enter the keyword: ")
        print("")
        key = generateKey(string, keyword)
        encrypt_text = encryption(string, key)
        print("Encrypted message: ", encrypt_text)
        print("Decrypted message: ", decryption(encrypt_text, key))
    elif type == "D" or type == "d": ## Decryption
        print("")
        string = input("Enter the message to be Encrypted/Decrypted: ")
        print("")
        keyword = input("Enter the keyword: ")
        print("")
        key = generateKey(string, keyword)
        encrypt_text = encryption(string, key)
        print("Encrypted message: ", string)
        print("Decrypted message: ", decryption(string, key))
    else:
        print("Invalid Option...Choose either 'E' or 'D'")
        exit(0)
