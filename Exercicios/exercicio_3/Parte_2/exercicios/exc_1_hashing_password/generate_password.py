# -*- coding: utf-8 -*-
import argparse
import hashlib

def hash_password(password, hashtype='sha256'):
    m = getattr(hashlib, hashtype)()
    m.update(password.encode())
    return m.hexdigest()

def main():
    parser = argparse.ArgumentParser(description='Hashing given password')
    parser.add_argument('password', help='Input password you want to hash')
    parser.add_argument('-t', '--type', default='sha256', choices=['sha256', 'sha512', 'md5'])
    args = parser.parse_args()

    hashed_password = hash_password(args.password, args.type)

    
    print("< hash-type : " + args.type + " >")
    print(hashed_password)

if __name__ == "__main__":
    main()