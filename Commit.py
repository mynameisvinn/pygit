from time import time

class Commit(object):

    """
    The commit object is just another text file in .git/objects/

    attributes
    ----------
    tree_hash : str
        hash of root tree
    msg : str
        represents commit message
    time : datetime
        unique time of commit
    parent : Object
        parent is either previous Commit, or Tree in the case of first commit.
    """
    def __init__(self, tree_hash, msg, parent):
        self.tree_hash = tree_hash
        self.msg = msg
        self.time = time()
        self.parent = parent