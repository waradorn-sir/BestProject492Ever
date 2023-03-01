import hashlib

def hash(text:str):

    hash_obj = hashlib.md5(text.encode())

    md5_hash = hash_obj.hexdigest()

    return md5_hash