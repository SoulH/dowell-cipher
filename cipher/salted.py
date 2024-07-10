from base64 import b64encode, b64decode
from types import NoneType


_sep, _mov = 'e', 4


def b64_encode(payload: str, salt_key: str, salt_index: int | None = None):
    if not salt_key or not salt_key.strip():
        raise Exception("salt key hasn't defined")
    if salt_index and salt_index < 0:
        raise Exception('salt index must to be a natural number or zero')
    if not salt_index or len(payload) <= salt_index:
        text = payload + _sep + salt_key
    else:
        head, tail = payload[:salt_index], payload[salt_index:]
        text = head + _sep + salt_key + _sep + tail
    # extra security layer => only to avoid get the original data easily with a base64 decode
    # could be replaced with a more suitable cipher method
    text = ''.join([chr(ord(x) + _mov) for x in text])
    return b64encode(text.encode()).decode()


def b64_decode(payload, salt_key: str, salt_index: int | None = None):
    text = b64decode(payload).decode()
    # undo second cipher
    text = ''.join([chr(ord(x) - _mov) for x in text])
    if isinstance(salt_index, NoneType) and text.endswith(_sep + salt_key):
        return text.replace(_sep + salt_key, '')
    if (isinstance(salt_index, int) and text[:salt_index+1][-1] == _sep
            and text[salt_index+1:].startswith(salt_key + _sep)):
        return text.replace(_sep + salt_key + _sep, '')
    raise Exception('invalid salt key or index')
