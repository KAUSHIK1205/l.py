def pal(tuple):
    s=0
    e= len(tuple) -1
    while (s<e):
        if tuple[s]!=tuple[e]:
            return False
        s=s+1
        e=e-1
    return True

t=(0,1,2,2,1,0)
t1=('k','e','a','a','e','k')
print(t1)

if pal(t1):
    print("it is a palindrome")
else:
    print("no it is not a palindrome")

