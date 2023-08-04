'''staxk using queue module'''
from queue import LifoQueue
stack=LifoQueue(maxsize=10)
for i in range(stack.maxsize):
    stack.put(i)
print(stack.get())
'''stack using deque // less complexity on append and pop operations O(1)'''
from collections import deque
stack = deque()
stack.append(10)
stack.append(20)
print(stack)
print(stack.pop())
'''deque END'''
'''using list also created'''
