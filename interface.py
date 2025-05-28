from task import Task

class userInterface:
    
    def __init__(self): 
        self._tasks = []

    def createTask(self):
        name = input("Please input name of task: ")
        description = input("(Optional) Please input description: ")
        newTask = Task(name, description)
        self.addTasks(newTask)

    def addTasks(self, task):
        self._tasks.append(task)

    def printTasks(self):
        if len(self._tasks) == 0:
            print("No current tasks")
        else:
            for task in self._tasks:
                print(task.printTask())

    

    