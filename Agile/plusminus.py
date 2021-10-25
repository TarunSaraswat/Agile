class Diffadd:
    a=0
    b=0
    def __init__(self, f, s):
        self.a=f
        self.b=s
        
    def add(self):
        return (self.a+self.b)
    
    def diff(self):
        return (self.a-self.b)



if __name__ == "__main__":
    a=13
    b=10
    var=Diffadd(a,b)
    print(var.add())  
    print(var.diff())
