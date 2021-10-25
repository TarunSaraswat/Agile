class diffadd:
    a=0
    b=0
    def add(self):
        return (self.a+self.b)
    
    def diff(self):
        return (self.a-self.b)

var=diffadd()

def test_sum():
    assert var.add()==6, "Should be 6"

def test_sub():
    assert  var.diff()==2, "Should be 2"
    
    

if __name__ == "__main__":
    
    var.a=int(input())
    var.b=int(input())
    test_sum()
    test_sub()
    print("Everything passed")