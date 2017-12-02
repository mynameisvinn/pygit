from hashlib import sha1

class Blob(object):
    """
    a blob is a compressed representation of a tracked file. you can always
    recover the original file from its blob.

    parameters
    ----------
    new_file : str
    	eg source code.

    attributes
    ----------
    ref_type : str
        obj description. could be either Commit, Tree, or Blob.
    id : str:
        unique 20 char hash for Blob object.
    """
    def __init__(self, new_file):
        self.ref_type = "Blob"
        self.id = sha1(new_file).hexdigest()
        self.compressed = sha1(new_file).hexdigest()  # TODO: should be written to disk