def solution(s):
    answer = True
    
    class Stack:
        def __init__(self):
            self.stack = []
        
        def push(self, v):
            self.stack.append(v)
        
        def pop(self):
            return self.stack.pop()
        
        def top(self):
            return self.stack[-1]
        
        def is_empty(self):
            if len(self.stack)==0:
                return True
            else:
                return False
    ss=Stack()
    
    for v in s:
        if ss.is_empty():
            if v==')':
                return False
            ss.push(v)
            continue
        if v==')':
            if ss.top()=='(':
                ss.pop()
            else:
                return False
        else:
            ss.push(v)
                
    
    if not ss.is_empty():
        answer=False

    return answer