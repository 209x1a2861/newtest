n=[1,2,34,543,6456,7,5,57,34,34,23,345,235,4]
a=len(n)
def insertion(a,n):
    for i in range(a):
        for j in range(i+1,a):
            if n[i]>n[j]:
                n[i],n[j]=n[j],n[i]
    return n
x=insertion(a,n)
print(x)