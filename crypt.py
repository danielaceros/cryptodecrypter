from cryptography.fernet import Fernet
from os import remove
from time import sleep
from tqdm import tqdm


def maincrypt():
    def gen():
        f = Fernet.generate_key()
        with open("key.key", "wb") as filekey:
            filekey.write(f)
            filekey.close()

    def chrg():
        return open("key.key", "rb").read()

    def crypt():
        path = input("""Enter your FILE PATH:
 > """)
        fe = Fernet(chrg())
        with open(path, "rb") as fileread:
            rd = fileread.read()
            fileread.close()
        for i in tqdm(range(1000)):
            sleep(0.01)
        print("File CRYPTED")
        with open(path, "wb") as filewrite:
            crypt = fe.encrypt(rd)
            filewrite.write(crypt)
            filewrite.close()

    gen()
    chrg()
    crypt()
maincrypt()
