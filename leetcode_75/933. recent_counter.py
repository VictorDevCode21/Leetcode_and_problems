from collections import deque


class RecentCounter:

    def __init__(self):
        self.q = deque()
        self.req = 0
        
        
    
    def ping(self, t: int) -> int:
        self.q.append(t)
        self.req +=1
        
        while self.q and self.q[0] < t-3000:
            self.q.popleft()
            self.req -=1
        
        
        
        return self.req

obj = RecentCounter()
print(obj.ping(1)   )
print(obj.ping(100) )
print(obj.ping(3001))
print(obj.ping(3002))

