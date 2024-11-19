#!python3
import binascii
import urllib3  

# Cette librairie n'est pas fournie avec Python, il faut installer les pré-requis
import requests

# Suppress only the single warning from urllib3.
urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)

def scramble(byt):
    mask = b'inf805'
    lmask = len(mask)
    return bytes(c ^ mask[i % lmask] for i, c in enumerate(byt))

def main():
    # Un humain ne peut pas lire cet url, il ne devrait pas y avoir de danger...
    obfuscated_url = '011a1248430f46411248021b1d0b154c1f41195c495b5f510c3100545152'

    print(requests.post(scramble(binascii.unhexlify(obfuscated_url)).decode(), data={ 'auth':'0a01025d6f53050f01' }, verify=False).text)


if __name__ == "__main__":
   main()
