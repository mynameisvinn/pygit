from time import time
from hashlib import sha1

class Commit(object):
    """
    The Commit object contains the current Tree and its corresponding metadata (eg 
    commit message, committer, commit date, parent.)

    The Commit ID is generated from (a) current Tree id, (b) current metadata, and 
    (c) previous Commit id. (every Commit knows its parent's commit - this is how a
    Commit object can track history.)

    What does this mean? Committing with the same tree would result in a new Commit 
    ID, since the timestamp changes. Changing a Tree would result in a new Commit
    ID, since the Tree's ID changes. In short, having two identical Commit IDs 
    guarantees identical Trees and identical parents.
    
    (In the same way, a block in the blockchain is generated from its metadata and 
    its parent's hash.)

    Why layer another object on top of a Tree? Unlike Trees, Commit objects track
    sequences by remembering parent objects.

    reference
    ---------
    https://blog.thoughtram.io/git/2014/11/18/the-anatomy-of-a-git-commit.html#the-commit-object

    parameters
    ----------
    tree_id : str
        unique id of current tree.
    msg : str
        commit message.
    parent_obj : Object
        every Commit object knows its parent. its parent object is either the 
        previous Commit or Tree (if it is the first commit). the parent's unique ID
        is also used as an input for the current Commit hash.

    attributes
    ----------
    ref_type : str
        object description. could be either Commit, Tree, or Blob.
    time : datetime
        unique time of commit.
    id : str:
        unique 20 char hash for Commit object. this hash is created by concatenating
        (a) metadata (eg commit message, time stamp), (b) current tree id, and (c) 
        parent hash.
    """
    def __init__(self, tree_id, msg, parent_obj):
        self.ref_type = "Commit"
        self.tree_id = tree_id
        self.msg = msg
        self.time = time()
        self.parent_obj = parent_obj

        # generate input for hashing
        metadata = self.msg + str(self.time)
        contents = metadata + tree_id + parent.id
        self.id = sha1(contents).hexdigest()