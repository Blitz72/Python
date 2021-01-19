import hashlib
from hmac import compare_digest

m = hashlib.sha256()
m.update(b'Davey smells,')
m.update(b' really bad, dude!')  # same as m.update(b'Davey smells, really bad, dude!')

print(m.digest())
print(m.hexdigest())
print(m.digest_size)
print(m.block_size)

print(m.name)
print(hashlib.algorithms_available)

# compare = hmac.compare_digest(m, 'c0ab6671a6fc347b5fe99e542452f8ea1653340cc2449225295dbbb12b3cffc2')
# print(compare)