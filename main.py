import argparse

from cipher.salted import b64_encode, b64_decode


parser = argparse.ArgumentParser()
parser.add_argument('-a', '--action', choices=['encrypt', 'decrypt'], help='action', required=True)
parser.add_argument('-p','--payload', help='text to encrypt or decrypt', required=True)
parser.add_argument('-k','--salt-key', help='salt key', required=True)
parser.add_argument('-i','--salt-index', type=int, help='salt index', default=None)


if __name__ == "__main__":
    args = parser.parse_args()
    if args.action == 'encrypt':
        print(b64_encode(args.payload, args.salt_key, args.salt_index))
    if args.action == 'decrypt':
        print(b64_decode(args.payload, args.salt_key, args.salt_index))