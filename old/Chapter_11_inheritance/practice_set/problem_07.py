class vector:
    def __init__(self,l):
        self.l = l 
        
    def __len__(self):

        return len(self.l)   
    
a = vector([1,2,3,4,5])
print(len(a))    