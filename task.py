from datetime import date

class Task:

    def __init__(self, name, desc, checked):
        self._name = name
        self._desc = desc
        self._checked = checked
        self._date = date.today()

    @property
    def getName(self): #getter
        return self._name
    
    @getName.setter
    def setName(self, name):
        self._name = name

        
    
