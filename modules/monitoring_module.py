from abc import ABC, abstractmethod, abstractproperty


class MonitoringModule(ABC):

    @abstractmethod
    def tick(self):
        pass

    @abstractproperty
    def as_string(self):
        pass
