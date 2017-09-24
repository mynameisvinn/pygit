from hashlib import sha1

class Blob(object):
    """
    a blob is a compressed representation of the file being tracked.

    parameters
    ----------
    new_file : str

    attributes
    ----------
    ref_type : str
        object description. could be either Commit, Tree, or Blob.
    id : str:
        unique 20 char for Blob object.
    """
    def __init__(self, new_file):
        self.ref_type = "Blob"
        self.id = sha1(new_file).hexdigest()
        self.compressed = sha1(new_file).hexdigest()  # should be written to disk