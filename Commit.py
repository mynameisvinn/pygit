from time import time
from hashlib import sha1

class Commit(object):
    """
    The commit object is just another text file in .git/objects/. they track the
    root tree.

    parameters
    ----------
    tree_id : str
        hash of tree.
    msg : str
        represents commit message.

    attributes
    ----------
    ref_type : str
        object description. could be either Commit, Tree, or Blob.
    time : datetime
        unique time of commit.
    parent_obj : Object
        every Commit object knows its parent. its parent object is either the 
        previous Commit, or Tree if it is the first commit.
    id : str:
        unique 20 char for Commit object.
    """
    def __init__(self, tree_id, msg, parent):
        self.ref_type = "Commit"
        self.tree_id = tree_id
        self.msg = msg
        self.time = time()
        self.parent_obj = parent
        contents = self.msg + str(self.time)
        self.id = sha1(contents).hexdigest()