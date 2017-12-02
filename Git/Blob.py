from hashlib import sha1

class Blob(object):
    """
    a Blob is the most basic data type in git. it is a compressed binary representation 
    of a tracked file. as result, there are always two duplicates of an added file: one
    existing in the user space (the working copy) and another in Git's objects. this 
    means you can always recover the original file from its corresponding Blob.

    if you check out a previous Commit, Git will replace the current copy in the user's
    working space with the decompressed, old Blob file.

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