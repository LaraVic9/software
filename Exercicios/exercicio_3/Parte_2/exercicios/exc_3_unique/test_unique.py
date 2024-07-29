import pytest
from  unique import hash_password

@pytest.mark.parametrize("password, hash_type, expected_start", [
    ("password123", "sha256", "ef92b"),
    ("password123", "sha512", "b109f"),
    ("password123", "md5", "482c8"),
])
def test_hash_password(password, hash_type, expected_start):
    hashed = hash_password(password, hash_type)
    assert hashed.startswith(expected_start), f"Hashed password does not start with expected value for {hash_type}"
