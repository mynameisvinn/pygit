import json
from hashlib import sha1

class Tree(object):
    """
    a tree is a snapshot of the index, and is created everytime "git add" is invoked.

    parameters
    ----------
    index : dict
        representing files being tracked. key is file name, value is file blob id.


    attributes
    ----------
    ref_type : str
        object description. could be either Commit, Tree, or Blob.
    id : str:
        unique 20 char for Tree object.
    """
    def __init__(self, index):
        self.ref_type = "Tree"
        self.index = json.dumps(index)  # convert dict to str before hashing
        self.id = sha1(self.index).hexdigest()