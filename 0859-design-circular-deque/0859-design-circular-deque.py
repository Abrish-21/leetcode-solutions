class MyCircularDeque:

    def __init__(self, k: int):
        self.xa=[0]*k
        self.hu=k
        self.lo=0
        self.ro=0
        self.sz=0

    def insertFront(self, v: int) -> bool:
        if self.sz==self.hu: return False
        self.lo=(self.lo-1)%self.hu
        self.xa[self.lo]=v
        self.sz+=1
        return True

    def insertLast(self, v: int) -> bool:
        if self.sz==self.hu: return False
        self.xa[self.ro]=v
        self.ro=(self.ro+1)%self.hu
        self.sz+=1
        return True

    def deleteFront(self) -> bool:
        if self.sz==0: return False
        self.lo=(self.lo+1)%self.hu
        self.sz-=1
        return True

    def deleteLast(self) -> bool:
        if self.sz==0: return False
        self.ro=(self.ro-1)%self.hu
        self.sz-=1
        return True

    def getFront(self) -> int:
        if self.sz==0: return -1
        return self.xa[self.lo]

    def getRear(self) -> int:
        if self.sz==0: return -1
        return self.xa[(self.ro-1)%self.hu]

    def isEmpty(self) -> bool:
        return self.sz==0

    def isFull(self) -> bool:
        return self.sz==self.hu
