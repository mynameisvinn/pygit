import json
from hashlib import sha1

class Tree(object):
    """
    a tree is created every time "git commit" is invoked. it is a hash of the current 
    index, a dict where k = fnames (for files being tracked) and v = corresponding 
    blob ids.

    trees serve as "snapshots" of the index. this is important because the index changes
    over time (eg, because there is a new file to be tracked or a tracked file has been 
    edited). 

    Unlike Commit objects, Trees do not know about their parents.

    parameters
    ----------
    index : dict
        representing files being tracked. k is file name, v is corresponding blob id.

    attributes
    ----------
    ref_type : str
        obj description. could be either Commit, Tree, or Blob.
    index : str
        index as of the latest commit in str (not dict) representationt.
    id : str:
        unique 20 char for Tree object.
    """
    def __init__(self, index):
        self.ref_type = "Tree"
        self.index = json.dumps(index)  # convert dict to str before hashing
        self.id = sha1(self.index).hexdigest()