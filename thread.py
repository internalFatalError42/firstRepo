import threading
import time


class MyFred(threading.Thread):
    lock_me = threading.Lock()

    def __init__(self, id: int, name: str) -> None:
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self) -> None:
        self.lock_me.acquire()
        print(f"Starte {self.id}")
        time.sleep(self.id * 3)
        self.lock_me.release()
        print(f"Beende {self.id}")


def main():
    #lock_me = threading.Lock()
    t1 = MyFred(1, "t1")
    t2 = MyFred(2, "t2")

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("Beende Main Fred")


if __name__ == "__main__":
    main()
