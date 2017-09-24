from time import time

class Commit(object):

	"""
	The commit object is just another text file in .git/objects/
	"""
    def __init__(self, tree_hash, msg):
        self.tree_hash = tree_hash
        self.msg = msg
        self.time = time()