n=[1,2,34,543,6456,7,5,57,34,34,23,345,235,4]
a=len(n)
def bubble(n,a):
    for i in range(len(n)):
        for j in range(len(n)):
            if (n[j]>=n[i]):
                n[i],n[j]=n[j],n[i]
    return n
x=bubble(n,a)
print(x)

