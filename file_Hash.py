import hashlib
import sys
import numpy
# 获取 HASH 值
def check_hash(file_path):
    res = {}
    source = open(file_path, 'rb').read()
    res['md5'] = hashlib.md5(source).hexdigest()
    res['sha1'] = hashlib.sha1(source).hexdigest()
    res['sha256'] = hashlib.sha256(source).hexdigest()
    res['sha512'] = hashlib.sha512(source).hexdigest()
    return res

# 打印 hash 值
if __name__ == '__main__':
    for key, value in check_hash(sys.argv[0]).items():#sys.argv命令行参数List，第一个元素是程序本身路径
        print(key + ": " + value)