import hashlib
import sys

def md5():

    hash = hashlib.md5()
    hash.update(message.encode("utf-8"))
    print(hash.hexdigest())
    exit()

def sha1():

    hash = hashlib.sha1()
    hash.update(message.encode("utf-8"))
    print(hash.hexdigest())
    exit()

def sha2():

    hash = hashlib.sha256()
    hash.update(message.encode("utf-8"))
    print(hash.hexdigest())
    exit()


if "0" in sys.argv:
    message = str(sys.argv[sys.argv.index("0")+1])
    md5()
    
if "md5" in sys.argv:
    message = str(sys.argv[sys.argv.index("md5")+1])
    md5()

if "1" in sys.argv:
    message = str(sys.argv[sys.argv.index("1")+1])
    sha1()

if "sha1" in sys.argv:
    message = str(sys.argv[sys.argv.index("sha1")+1])
    sha1()

if "2" in sys.argv:
    message = str(sys.argv[sys.argv.index("2")+1])
    sha2()

if "sha2" in sys.argv:
    message = str(sys.argv[sys.argv.index("sha2")+1])
    sha2()

