class PeekingIterator:
    def __init__(self, iterator):
        self.iter = iterator
        self.has_next = iterator.hasNext()
        self.cache = iterator.next() if self.has_next else None

    

    def peek(self):
        return self.cache
        

    def next(self):
        value = self.cache
        self.has_next = self.iter.hasNext()
        self.cache = self.iter.next() if self.has_next else None
        return value
        

    def hasNext(self):
        return self.has_next
  