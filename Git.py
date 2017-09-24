from hashlib import sha1

import Blob
from Tree import Tree
from Commit import Commit
from Reference import Reference

class Git(object):
    """
    attributes
    ----------
    dir_blobs : list
        list of Blobs
    dir_trees : list
        list of Trees
    dir_commits : list
        list of Commits
    Master : Reference
        represents Master ref
    Head : Reference
        initially points at Master ref but could point at Commits
    """
    def __init__(self):
        self.index_file = {}
        self.dir_blobs = []
        self.dir_trees = []
        self.dir_commits = []
        self.master = Reference("master")
        self.head = Reference("head", ref=self.master)
        

    def add(self, fname):
        """
        creates blob object, and then adds fname/hash to index.
        
        parameters
        ----------
        fname : str
            fname of file to be tracked.
        """
        b = self._create_blob(fname)
        self.dir_blobs.append(b)  # TODO: write to disk
        self.index_file[fname] = b.blob_id

    def _create_blob(self, fname):
        """create new blob object.
        """
        fh = open(fname, "r").read()
        return Blob.Blob(fh)

    def commit(self, msg):
        """
        (1) create tree graph from index: represent the content of the version of the project being committed
        (2) create commit object
        (3) points branch to commit. points the current branch at the new commit object.
        """
        # step 1: create Tree, which is just an official snapshot of index
        t = Tree(self.index_file)
        self.dir_trees.append(t)
        
        # step 2: create Commit
        
        # if this is the 1st commit, then commit's parent is the tree
        if self.master.reference == None:
            parent = t
        else:
            parent = self.master.reference
        
        new_commit_obj = Commit(t.tree_hash, msg, parent)
        self.dir_commits.append(new_commit_obj)
        
        # step 3: master branch points to latest commit object
        self.master.reference = new_commit_obj