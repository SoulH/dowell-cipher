from _pytest.python_api import raises

from cipher.salted import b64_encode, b64_decode


def test_raise_exception():
    payload, salt_key, salt_index = 'abc', 'xxx', 1
    encoded = b64_encode(payload, salt_key, salt_index)
    with raises(Exception):
        b64_decode(encoded, salt_key, 0)