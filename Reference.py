class Reference(object):
    """
    references are labels. they point either Tree or Commit objects.

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