from datetime import date

class Task:

    def __init__(self, name, desc=""):
        self._name = name
        self._desc = desc
        self._checked = False
        self._date = date.today()

    def __repr__(self):
        return f"Task name: {self._name}, Description: {self._desc}, Completion status: {self._checked}, added: {self._date}"    

    @property
    def getName(self): #getter
        return self._name
    
    @getName.setter
    def setName(self, name):
        self._name = name

    @property
    def getDesc(self): 
        return self._desc

    @getDesc.setter
    def setDesc(self, desc):
        self._desc = desc
    
    @property
    def getChecked(self):
        return self._checked

    @getChecked.setter
    def setCheched(self, checked):
        self._checked = checked

    @property
    def getDate(self):
        return self._date
    
    def printTask(self):
        return f"[] {self._name} {self._date}"
    
