n=[1,2,24,4,5,34,4334,32,2,45,54,56,54,6,45]
am=list(n)
am.sort()
l=len(n)-1
def partition(n,start,end):
    pivot=n[end]
    i=start-1
    for j in range(start,end):
        if n[j]<=pivot:
            i=i+1
            n[i],n[j]=n[j],n[i]
    n[i+1],n[end]=n[end],n[i+1]
    return i+1
def quick(n,start,end):
    if start<end:
        j=partition(n,start,end)
        quick(n,start,j-1)
        quick(n,j+1,end)
    return n
x=quick(n,0,l)
print(x)
print(am)
