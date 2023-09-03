n=[1,2,34,543,6456,7,5,57,34,34,23,345,235,4]
a=len(n)
for i in range(1,a):
    key=n[i]
    j=i-1
    while j>=0 and key<n[j]:
        n[j+1]=n[j]
        j-=1
    n[j+1]=key
print(n)
