import pytest
from generate_password import hash_password

def test_hash_password_sha256():
    assert hash_password('hello', 'sha256') == '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'

def test_hash_password_md5():
    assert hash_password('hello', 'md5') == '5d41402abc4b2a76b9719d911017c592'

def test_hash_password_sha512():
    assert hash_password('hello', 'sha512') == '9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043'
