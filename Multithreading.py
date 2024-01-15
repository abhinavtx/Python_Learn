from threading import *
import time
# By usage of threading it helps in running of processes on different threads

class hello(Thread):
    def run(self):
        for i in range(10):
            print("Hello")
            time.sleep(0.1)
            
class hi(Thread):
    def run(self):
        for i in range(10):
            print("Hi")
            time.sleep(0.1)
t1 = hello()
t2 = hi()

t1.start()
t2.start()
print("Bye")