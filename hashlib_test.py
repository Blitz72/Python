import hashlib

m = hashlib.sha256()
m.update(b'Davey smells, really bad, dude!')

print(m.hexdigest())
print(m.digest_size)
print(m.block_size)

print(m.name)