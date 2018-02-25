class Queue(object):
    """A Queue is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def remove(self):
        """Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self"""
        try:
            return self.vals.pop(0)
            
        except:
            raise ValueError



##Edx answer

class Queue(object):

    def __init__(self):
        "Initializes 1 attribute: a list to keep track of the queue's elements"
        self.qlist = []

    def insert(self, element):
        "Adds an element to the attribute list using append"
        self.qlist.append(element)

    def remove(self):
        "Removes an element from the attribute list"
        # Check if the list is empty; if so then raise a ValueError
        if self.qlist == []:
            raise ValueError()
        else:
            # Otherwise we want to remove the first element from the list
            # and return that to the user.
            element = self.qlist[0]
            self.qlist.remove(element)
            return element
            # Could also do this in 1 line:
            # return self.qlist.pop(0)

    
