import json
from hashlib import sha1

class Tree(object):
    def __init__(self, index):
        self.contents = index         
        
        # convert dict to str before hashing
        contents = json.dumps(index)  
        self.tree_hash = sha1(contents).hexdigest()