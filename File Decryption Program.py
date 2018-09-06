import pyAesCrypt

print (" ")
print ("Welcome to AnyPass file decryptor !          ~ Anonymous")
print ("--------------------------------------------------------")
print (" ")
print ("Please place the file (which is to be decrypted) in the root directory of this program.")
print (" ")

def decryptor():

    try:

        buffer_size = 64 * 1024
        encrypted_file = input("Enter name of file with its original and new file format : ")
        decrypted_file = input("Enter name of file with its original file format : ")
        password = input("Enter password to decrypt the file : ")

        def decryption():
            pyAesCrypt.decryptFile(encrypted_file, decrypted_file, password, buffer_size)

        decryption()

        print (" ")
        print ("Your file has been successfully decrypted !")
        print (" ")

    except:

        pass
        print(" ")
        print("Oops! An error occured... Please try again...")
        print(" ")
        decryptor()

while True:
    decryptor()