from abc import ABCMeta, abstractmethod

class News(metaclass=ABCMeta):
    
    @abstractmethod
    def get_news(self):
        pass

