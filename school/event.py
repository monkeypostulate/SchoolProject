from abc import ABCMeta, abstractmethod


class Event(metaclass = ABCMeta):
    def __init__(self,start_date = None,
                 end_date = None,
                 capacity = None):
        self.start_date = start_date
        self.end_date = end_date
        self.capacity = capacity
    @abstractmethod    
    def add(self):
        pass
    
    @abstractmethod 
    def update(self):
        pass
    
    @abstractmethod
    def add_participant(self):
        pass
    @abstractmethod
    def delete_participant(self):
        pass
        
        