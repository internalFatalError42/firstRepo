from functools import cache
import pyzipper
from tqdm import tqdm
from queue import Queue
#TODO: multithreading
# x4ivygA51F


class Crack:
    def __init__(self, password_list: str) -> None:
        self.password_list: str = password_list

    @cache
    def crack_zip(self) -> None:
        wordlist = open(self.password_list, "rb")
        n_words = len(list(open(self.password_list, "rb")))
        print(n_words)
        with pyzipper.AESZipFile('test.zip', 'r', compression=pyzipper.ZIP_DEFLATED,
                                 encryption=pyzipper.WZ_AES) as extracted_zip:
            for word in tqdm(wordlist, total=n_words, unit='word'):
                try:
                    extracted_zip.extractall(pwd=word.strip())
                except:
                    continue
                else:
                    print(word.decode())
                    return
        print("Password not found")

    # Prüft ob das passwort in der .txt vorhanden ist
    @cache
    def check_list_for_password(self, password: str) -> None:
        count: int = 0
        wordlist: str = self.password_list
        with open(wordlist, "rb") as wordlist:
            for word in wordlist:
                try:
                    if word.decode().strip() == password:
                        count += 1
                        print(f"{password} exists")
                        return
                    else:
                        count += 1
                except Exception as e:
                    print(e)


# beschneidet die Liste
def cp_list() -> None:
    wordlist: str = "rockyou.txt"

    with open(wordlist, "r+", errors="ignore") as fp:
        lines = fp.readlines()
        fp.seek(0)
        fp.truncate()

        for number, line in enumerate(lines):
            if number < 1000000:
                fp.write(line)


def main():
    l1: str = 'rockyou.txt'
    l2: str = 'passwordlist.txt'

    t1: object = Crack(l2)
    #t1.crack_zip()

    t1.check_list_for_password('x4ivygA51F')


if __name__ == "__main__":
    main()
