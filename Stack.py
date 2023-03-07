class Stack:
    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next  = next
    
    def __init__(self):
        self.top = None

    def push(self, val):
        self.top = Stack.Node(val, self.top)
        
    def pop(self):
        assert self.top, 'Stack is empty'
        val = self.top.val
        self.top = self.top.next
        return val
    
    def peek(self):
        return self.top.val if self.top else None
    
    def empty(self):
        return self.top == None
    
    def __bool__(self):
        return not self.empty()
    
    def __repr__(self):
        if not self.top:
            return ''
        return '--> ' + ', '.join(str(x) for x in self)
    
    def __iter__(self):
        n = self.top
        while n:
            yield n.val
            n = n.next

 
            
#paired delimiter matching
delim_openers = '{([<'
delim_closers = '})]>'

def check_delimiters(expr):
    """Returns True if and only if `expr` contains only correctly matched delimiters, else returns False."""
   
    delim = Stack()
    for x in expr:
        try:
            i = delim_openers.index(x)
            delim.push(i)
            continue
        except ValueError:
            pass
        try:
            i = delim_closers.index(x)
            if not delim:
                return False
            j = delim.pop()
            if j != i:
                return False
            continue
        except ValueError:
            pass
    return delim.empty()


#infix - postfix conversion
# you may find the following precedence dictionary useful
prec = {'*': 2, '/': 2,
        '+': 1, '-': 1}

def infix_to_postfix(expr):
    """Returns the postfix form of the infix expression found in `expr`"""
    ops = Stack()
    postfix = []
    toks = expr.split()
     
    for t in toks:
        if t.isdigit():
            postfix.append(t)
        elif t == '(':
            ops.push(t)
        elif t == ')':
            op = ops.pop()
            while op != '(':
                postfix.append(op)
                op = ops.pop()
        else:
            while True:
                if ops.empty() or ops.peek() == '(':
                    ops.push(t)
                    break
                if prec[t] > prec[ops.peek()]:
                    ops.push(t)
                    break
                else:
                    postfix.append(ops.pop())
    while not ops.empty():
        postfix.append(ops.pop())
    return ' '.join(postfix)
