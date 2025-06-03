from datetime import date
import uuid

class Task:

    def __init__(self, name, desc=""):
        self.id = uuid.uuid4()
        self._name = name
        self._desc = desc
        self._checked = False
        self._date = date.today()

    def __repr__(self):
        return f"Task name: {self._name}, Description: {self._desc}, Completion status: {self._checked}, added: {self._date}"    

    @property
    def name(self): #getter
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def desc(self): 
        return self._desc

    @desc.setter
    def desc(self, desc):
        self._desc = desc
    
    @property
    def getChecked(self):
        return self._checked

    @property
    def getDate(self):
        return self._date
    
    def printTask(self):
        if self._checked:
           return f"[x] {self._name} {self._date}" 
        else:
            return f"[] {self._name} {self._date}"
    
    def setPrintTask(self):
        if self._checked == False:
            self._checked = True
        else:
            self._checked = False
    
