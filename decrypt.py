from cryptography.fernet import Fernet
from os import remove
from time import sleep
from tqdm import tqdm

def maindecrypt():
    def chrg():
        return open("key.key", "rb").read()

    def decrypt():
        path = input("""Enter your FILE PATH:
 > """)
        fe = Fernet(chrg())
        with open(path, "rb") as fileread:
            rd = fileread.read()
            fileread.close()
        for i in tqdm(range(1000)):
            sleep(0.01)
        print("File DECRYPTED")
        with open(path, "wb") as filewrite:
            decrypt = fe.decrypt(rd)
            filewrite.write(decrypt)
            filewrite.close()

    chrg()
    decrypt()
maindecrypt()
