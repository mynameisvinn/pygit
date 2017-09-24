from hashlib import sha1
import Blob
from Tree import Tree
from Commit import Commit

class Git(object):
    def __init__(self):
        """create new dir
        """
        self.index_file = {'fname':[], 'fhash':[]}
        self.blobs = []
        pass

    def add(self, fname):
        """
        (1) creates blob; 
        (2) adds to index file
        """
        if self._is_new_file(fname):            
            b = self._create_blob(fname)  # new blob object
            self.blobs.append(b)  # store in blob dir
            self.index_file['fname'].append(fname)  # add file name to index
            self.index_file['fhash'].append(b.name)  # add hash to index
        else:
            print "no new files"
            pass
    
    def _is_new_file(self, fname):
        """before we add a file, need to check if it's new.
        
        returns True if new
        """
        # check by fname
        if fname not in self.index_file['fname']:
            return True
        elif self._generate_hash(fname) not in self.index_file['fhash']:
            return True
        else:
            return False


    def _create_blob(self, fname):
        """create new blob object from file contents.
        """
        fh = open(fname, "r").read()
        print "blob created"
        return Blob.Blob(fh)

    def commit(self, msg):
        """
        (1) create tree graph from index: represent the content of the version of the project being committed
        (2) create commit object
        (3) points branch to commit. points the current branch at the new commit object.
        """
        # create tree from index
        t = self._create_tree_obj()
        
        # create commit object, pointing to tree
        c = self._create_commit_obj(t.tree_hash, msg)
        
    
    def _create_commit_obj(self, t_hash, msg):
        print "creating commit"
        return Commit(t_hash, msg)
    
    def _create_tree_obj(self):
        print "creating tree"
        return Tree(self.index_file)
    
    def _generate_hash(self, fname):
        fh = open(fname, "r").read()
        return sha1(fh).hexdigest()