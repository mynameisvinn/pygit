class Reference(object):
    """
    References are labels pointing to either Tree or Commit objects.

    HEAD points to the current branch (which could be MASTER or some 
    other branch). Since it points to the current branch, it will change 
    the most often. 

    parameters
    ----------
    ref_type : str
        Reference object can be labeled as "head", "master", etc.
    ref : Tree, Commit or another Reference
        Reference objects should point to either Tree or Commit objects. 
    
    attributes
    ----------
    time : datetime
        placeholder
    """
    def __init__(self, ref_type, ref=None):
        self.ref_type = ref_type
        self.reference = ref
        self.time = None