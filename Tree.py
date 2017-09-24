import json
from hashlib import sha1

class Tree(object):
    def __init__(self, index):
        self.contents = index         
        contents = json.dumps(index)  # convert dict to str, for hashing purposes
        self.tree_hash = sha1(contents).hexdigest()
        
class Commit(object):
    def __init__(self, tree_hash, msg):
        self.tree_hash = tree_hash
        self.msg = msg