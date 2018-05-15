

def list_to_tree(t, i):
    if i >= len(t) or t[i] is None:
        return None
    else:
        return ('Node', t[i], list_to_tree(t, 2 * i + 1), list_to_tree(t, 2 * i + 2) )


# Serialization
#
# We replace references with an index in a dictionary. The index is computed
# using the id function.

def serialize(t):

    db = {}
    db[id(None)] = None

    def serialize_aux(t):
        if t is None: 
            return id(None)
        else:
            _, v, l, r = t
            i = id(t) 
            m = v, serialize_aux(l), serialize_aux(r)
            db[i] = m
            return i
        
    serialize_aux(t)
    return db

# Merkelization
#
# Similar to the previous solution, but the index is the hash
# of the node, computed recursively. Of course, Python hash function
# isn't suitable for this (implementation dependent, not crypto-safe). 
# 
# We get some important properties, in addition to serialization.
#
# - content addressable -> integrity for free
# - certificate 

def merkelize(t):

    db = {}
    db[hash(None)] = None

    def merkelize_aux(t):
        if t is None: 
            return hash(None)
        else:
            _, v, l, r = t
            m = v, merkelize_aux(l), merkelize_aux(r)
            h = hash(m)
            db[h] = m
            return h
        
    merkelize_aux(t)
    return db

t = list_to_tree([1,2,3,4,5,6,7], 0)
print(merkelize(t))






