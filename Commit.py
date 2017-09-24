class Commit(object):
    def __init__(self, tree_hash, msg):
        self.tree_hash = tree_hash
        self.msg = msg