import pytest
from hashing_password import generate_pass

def test_generate_pass(len, password):
    assert generate_pass(len, password)