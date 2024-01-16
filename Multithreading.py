from threading import *
import time
# By usage of threading it helps in running of processes on different threads

class hello(Thread):
    def run(self):
        for i in range(1000):
            print("Hello")
            
class hi(Thread):
    def run(self):
        for i in range(1000):
            print("Hi")
t1 = hello()
t2 = hi()

t1.start()
t2.start()
print("Bye")