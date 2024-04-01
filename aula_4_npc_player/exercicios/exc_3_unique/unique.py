# -*- coding: utf-8 -*-
import argparse
import hashlib

def parse_arguments():
    parser = argparse.ArgumentParser(description='Hashing given password')
    parser.add_argument('password', help='Input password you want to hash')
    parser.add_argument('-t', '--type', default='sha256', choices=['sha256', 'sha512', 'md5'])
    args = parser.parse_args()
    return args

def hash_password(password, hash_type):
    m = getattr(hashlib, hash_type)()
    m.update(password.encode())
    return m.hexdigest()

if __name__ == "__main__":
    args = parse_arguments()
    hashed_password = hash_password(args.password, args.type)
    print("< hash-type : " + args.type + " >")
    print(hashed_password)