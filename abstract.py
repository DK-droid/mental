from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def registerObserver(): pass

    @abstractmethod
    def removeObserver(): pass

    @abstractmethod
    def notifyObservers(): pass

    @abstractmethod
    def notifyObserver(): pass

class Observer(ABC):
    @abstractmethod #обновление данных для себя
    def update(): pass

    @abstractmethod #запрос на получение данных
    def request(): pass

    @abstractmethod #выгрузка данных объекту
    def upload(): pass

class DisplayElement(ABC):
    @abstractmethod
    def display(): pas
