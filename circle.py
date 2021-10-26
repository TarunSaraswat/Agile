
def circlearea(r):
    if r>0:
        return r*3.14
    else:
        raise ValueError("Negative Radius Provided")

if __name__ == "__main__":
    r=[1,2,46,-3,0]
    for i in r:
        print(circlearea(i))
        
#edited for automatic update
