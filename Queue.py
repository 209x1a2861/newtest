'''similar to Stack'''
from queue import Queue
q=Queue(maxsize=5)
for i in range(q.maxsize):
    q.put(i)
print(q.get())
'''also implement using deque popleft() best append and pop() oprations'''
'''also list operations'''
from queue import LifoQueue
stack=LifoQueue(maxsize=10)
for i in range(stack.maxsize):
    stack.put(i)
print(stack.get())
'''above stack'''