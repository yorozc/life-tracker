from task import Task

class userInterface:
    
    def __init__(self): 
        self._tasks = []

    def mainInterface(self):
        while(True):
            print("=============================================================================")
            self.printTasks()
            choice = input("What operation would you like to do:\n" \
            "1. Add Task\n" \
            "2. Delete Task\n" \
            "3. Edit Task\n" \
            "4. Complete Task\n" \
            "5. Print Tasks\n" \
            "6. Quit app\n")
            self.choice(choice)
            print("=============================================================================")

    def choice(self, choice):
        match choice:
            case "1":
                self.createTask()
            case "2":
                self.deleteTasks()
            case "3":
                self.editTasks()
            case "4":
                self.completeTask()
            case "5":
                self.printTasks()
            case "6":
                exit()

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
        completedTask = input("Type name of task that is completed: ")
        completedTask = completedTask.lower()
        completedTask = completedTask.replace(" ", "")
        print(completedTask)

        for task in self._tasks:
            individualTask = task.getName.lower()
            individualTask = individualTask.replace(" ", "")
            if completedTask == individualTask:
                task.setPrintTask() #flips switch that marks task as completed

    def deleteTasks(self):
        pass

    def editTasks(self):
        pass    

    

    