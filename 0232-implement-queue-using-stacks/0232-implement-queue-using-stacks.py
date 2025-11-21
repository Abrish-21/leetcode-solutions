class MyQueue:

    def __init__(self):
        self.a=[]
        self.b=[]

    def push(self, v: int) -> None:
        self.a.append(v)

    def pop(self) -> int:
        if not self.b:
            while self.a:
                self.b.append(self.a.pop())
        return self.b.pop()

    def peek(self) -> int:
        if not self.b:
            while self.a:
                self.b.append(self.a.pop())
        return self.b[-1]

    def empty(self) -> bool:
        return not self.a and not self.b
