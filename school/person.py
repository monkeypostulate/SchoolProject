from abc import ABCMeta, abstractmethod

class Person(metaclass = ABCMeta):
    def __init__(self,
                 first_name='test',
            family_name=None):
        self.first_name = first_name
        self.family_name = family_name
    @abstractmethod
    def create(self):
        pass
    
    @abstractmethod    
    def update_info(self):
        pass
    
    @abstractmethod
    def delete(self):
        pass
