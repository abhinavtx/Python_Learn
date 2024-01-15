# Python contains module abc (abstract class)
from abc import ABC, abstractmethod

class Computer(ABC):
    # Now we have made computer as an abstract class
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    pass

com1 = Laptop()
# We can't call Laptop because it just has its parent abstract class and nothing of its own
# We can't access abstract class directly
    

