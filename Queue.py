# For queue we use library called deque from collections
# Another way is to use list and then use pop(0) and append(0)
# The best way is to use queue from Queue

from collections import deque
nameQ = deque(["Eric", "John", "Michael"])
nameQ.append("Terry")           
nameQ.append("Graham") 
print(nameQ)         
nameQ.popleft()
nameQ.extend(deque(["Abhinav", "Aggarwal"]))
print(nameQ)


from queue import Queue

abc = Queue(["Eric", "John", "Michael"])
