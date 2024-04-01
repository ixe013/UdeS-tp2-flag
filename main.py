#!python3
import binascii

# Cette librairie n'est pas fournie avec Python, il faut installer les pré-requis
import requests


def scramble(byt):
    mask = b'inf805'
    lmask = len(mask)
    return bytes(c ^ mask[i % lmask] for i, c in enumerate(byt))

# Un humain ne peut pas lire cet url, il ne devrait pas y avoir de danger...
obfuscated_url = '011a12480a1a461a160a1e410c1d121744455b410557545036080a5957'

print(requests.post(scramble(binascii.unhexlify(obfuscated_url)).decode(), data={ 'auth':'0a01025d6f53050f01' }).text)

