import multiprocessing
from multiprocessing import Process
import pyzipper
from tqdm import tqdm


def extract_file(passwords: str) -> None:
    with pyzipper.AESZipFile('test.zip', 'r', compression=pyzipper.ZIP_DEFLATED,
                             encryption=pyzipper.WZ_AES) as extracted_zip:
        for password in passwords:
            try:
                extracted_zip.extractall(pwd=password.strip())
                print(f"password found: {password.strip()}")
            except Exception as e:
                pass


def crack_zip(password_list: str) -> None:
    with open(password_list, 'rb') as pass_file:
        passwords = [i.strip() for i in pass_file]

    N_PROC = multiprocessing.cpu_count()
    for i in range(N_PROC):
        p = Process(target=extract_file, args=[passwords[i::N_PROC]])
        p.start()


def main():
    p1 = 'rockyou.txt'
    p2 = 'passwordlist.txt'
    crack_zip(p2)


if __name__ == '__main__':
    main()
