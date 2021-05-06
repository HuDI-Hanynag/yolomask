import random as r

def checking(lotto):
    i=0
    while(i!=lotto):
        i=i+1
    return i

lotto=r.randint(1,10)

print(checking(lotto))
