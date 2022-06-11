import os
import platform
import sys
import sysconfig
import socket
import psutil


def main():
    #f = open('test.txt', 'a')
    #f.write('owned')
    #f.close()

    #print(os.name)
    #print(platform.system())
    #print(platform.release())
    #print(platform.version())
    #print(platform.uname())
    #print(platform.architecture())
    #print(platform.processor())
    #print(platform.machine())
    #print(sys.version)
    #print(psutil.virtual_memory())
    #print(socket.gethostname())

    test = 1337
    print(id(test))


if __name__ == '__main__':
    main()

