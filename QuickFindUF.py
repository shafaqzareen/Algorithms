class QuickFindUF:
    
    def __init__(self, N:int):
        self.arr = []
        self.arr =  list(range(N))
             
    def connected(self, p,q):
        return self.arr[p] == self.arr[q]
  
    def union(self,p,q):
        pid = self.arr[p]
        qid = self.arr[q]
        
        for i in range(len(self.arr)):
            if self.arr[i] == pid: 
                self.arr[i] = qid
                
            
        
        