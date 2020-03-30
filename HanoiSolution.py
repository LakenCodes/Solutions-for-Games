

def move(f,t):
    print("Move disc from {} to {}:".format(f,t))



def move_via(f,v,t):
    move(f,v)
    move(v,t)

# move_via("A","B","C")
#

print("How many discs are being used? ")
disc_amt = int(input())
def foo(x):
    foo(x)

def hanoi(n,f,h,t):
    if n == 0:
        pass
    else:
        hanoi(n-1,f,t,h)
        move(f,t)
        hanoi(n-1,h,f,t)

hanoi(disc_amt,"A","B","C")