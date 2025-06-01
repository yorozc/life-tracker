from task import Task

class userInterface:
    
    def __init__(self): 
        self._tasks = []

    def mainInterface(self):
        while(True):
            choice = input("What operation would you like to do:\n" \
            "1. Add Task\n" \
            "2. Delete Task\n" \
            "3. Edit Task\n" \
            "4. Complete Task\n")
            self.createTask()

    def createTask(self):
        try:
            name = input("Please input name of task: ")
            if not name:
                raise ValueError("Name cannot be empty")
            description = input("(Optional) Please input description: ")
            newTask = Task(name, description)
            self.addTasks(newTask)
            
        except ValueError as e:
            print("Error:", e)

    def addTasks(self, task):
        self._tasks.append(task)

    def printTasks(self):
        if len(self._tasks) == 0:
            print("No current tasks")
        else:
            for task in self._tasks:
                print(task.printTask())

    def completeTask(self):
        pass

    

    