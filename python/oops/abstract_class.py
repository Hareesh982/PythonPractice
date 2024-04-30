from abc import ABC,abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class car(vehicle):
    def start(self):
        print("car started")
    def stop(self):
        print("car stopped")

class bike(vehicle):
    def start(self):
        print("bike started")
    def stop(self):
        print("bike stopped")

obj = car()
obj_1 = bike()
obj.start()
obj.stop()
obj_1.start()
obj_1.stop()