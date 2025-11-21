from collections import deque
class MyStack:

    def __init__(self):
        self.a=deque()
        self.b=deque()

    def push(self, v: int) -> None:
        self.a.append(v)

    def pop(self) -> int:
        while len(self.a)>1:
            self.b.append(self.a.popleft())
        r=self.a.popleft()
        self.a,self.b=self.b,self.a
        return r

    def top(self) -> int:
        while len(self.a)>1:
            self.b.append(self.a.popleft())
        r=self.a.popleft()
        self.b.append(r)
        self.a,self.b=self.b,self.a
        return r

    def empty(self) -> bool:
        return not self.a
