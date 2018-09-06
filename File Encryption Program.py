import pyAesCrypt

print (" ")
print ("Welcome to AnyPass file encryptor !          ~ Anonymous")
print ("--------------------------------------------------------")
print (" ")
print ("Please place the file (which is to be encrypted) in the root directory of this program.")
print (" ")

def encryptor():

    try:

        buffer_size = 64 * 1024
        origin_file = input("Enter name of file with its original file format : ")
        encrypted_file = input("Enter name of file with its original and new file format : ")
        password = input("Enter password with which you want to encrypt the file : ")

        def encryption():
            pyAesCrypt.encryptFile(origin_file, encrypted_file, password, buffer_size)

        encryption()

        print (" ")
        print ("Your file has been successfully encrypted !")
        print (" ")

    except:

        pass
        print(" ")
        print("Oops! An error occured... Please try again...")
        print(" ")
        encryptor()

while True:
    encryptor()