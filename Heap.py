import heapq
li=[1,4,5,5,4,3,5,566,3,2,34,2,344,4,54,3,2,35,7,5,75,3,23,5]
heapq.heapify(li)
print(heapq.nlargest(5,li))
(heapq.heappush(li,10))bhargava
print(heapq.nsmallest(5,li))