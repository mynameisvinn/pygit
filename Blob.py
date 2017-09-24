from hashlib import sha1

class Blob(object):
    def __init__(self, new_file):
        self.name = sha1(new_file).hexdigest()
        self.content = sha1(new_file).hexdigest()