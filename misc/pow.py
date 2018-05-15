from hashlib import sha256
from itertools import product

for b in product(range(256), repeat = 4):
    b = bytes(list(b))
    h = sha256(b).hexdigest()
    if h.startswith('000000'):
        print(h)
        print('ok')

