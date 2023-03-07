class Queue:
    def __init__(self, limit=10):
        self.data = [None] * limit
        self.head = -1
        self.tail = -1

    def enqueue(self, val):
        if self.tail == -1:
            assert self.head == -1
            self.head = self.tail = 0
            self.data[0] = val
        else:
            tail = self.tail + 1
            tail %= len(self.data)
            if self.head == tail:
                raise RuntimeError
            else:
                self.data[tail] = val
                self.tail = tail
        
    def dequeue(self):
        if self.empty():
            raise RuntimeError
        else:
            val = self.data[self.head]
            self.data[self.head] = None
            if self.head == self.tail:
                self.head = self.tail = -1
            else:
                self.head += 1
                self.head %= len(self.data)
        return val     
    
    def resize(self, newsize):
        assert(len(self.data) < newsize)
        newdata = [None] * newsize
        head = self.head
        current = self.data[head]
        count = 0
        while current != None:
            newdata[count] = current
            count += 1
            if count != 0 and head == self.tail:
                break
            if head != len(self.data) - 1:
                head = head + 1
                current = self.data[head]
            else:
                head = 0
                current = self.data[head]
        self.data = newdata
        self.head = 0
        self.tail = count - 1
        
        
    def empty(self):
        if self.tail == -1:
            assert self.head == -1
            return True
        else:
            return False
    
    def __bool__(self):
        return not self.empty()
    
    def __str__(self):
        if not(self):
            return ''
        return ', '.join(str(x) for x in self)
    
    def __repr__(self):
        return str(self)
    
    def __iter__(self):
        if self.empty():
            return
        i = self.head
        while i != self.tail:
            yield self.data[i]
            i += 1
            i %= len(self.data)
        yield self.data[self.tail]
