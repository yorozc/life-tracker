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
            print("ERROR:", e)

    def addTasks(self, task):
        self._tasks.append(task)

    def printTasks(self):
        if len(self._tasks) == 0:
            print("No current tasks")
        else:
            print("*******************Tasks***********************")
            for task in self._tasks:
                print(task.printTask())
            print("***********************************************")

    def findTask(self, taskToFind):
        taskToReturn = None
        for task in self._tasks:
            newTask = task.getName.lower().replace(" ", "")
            if taskToFind == newTask:
                taskToReturn = task
                return True, taskToReturn

    def completeTask(self):
        completedTask = input("Type name of task that is completed: ").lower().replace(" ", "")

        res, task = self.findTask(completedTask)
        if res:
            task.setPrintTask()

    def deleteTasks(self):
        try:
            deleteTask = input("What task do you want to delete?: ").lower()
            deleteTask = deleteTask.replace(" ", "")

            for task in self._tasks:
                if task in self._tasks:
                    individualTask = task.getName.lower()
                    individualTask = individualTask.replace(" ", "")

                    if deleteTask == individualTask:
                        check = input(f"Are you sure you want to delete {task.getName}? y/n: ").lower()
                        if(check == "y" or check == "yes"):
                            self._tasks.remove(task)
                            print(f"Task {task.getName} is deleted!")

                        elif(check == "n" or check == "no"):
                            print(f"Task {task.getName} is not deleted. Canceling operation!")

                        else:
                            print("Not a valid input. Try again.")
                            break

                else:
                    raise ValueError("Task not found.")
                
        except ValueError as e:
            print("ERROR:", e)



    def editTasks(self):

        editTask = input("Which task would you like to edit?: ").lower().replace(" ", "")

        editOption = input("What would you like to edit?\n"
                     "1. Name of task\n" \
                     "2. Description of task\n" \
                     "3. Status of completion for task\n" \
                     "Input choice here: ")

        match editOption:
            case "1": #changing name of task
                for task in self._tasks:
                    editedTask = task.getName.lower().replace(" ", "")
                    if editTask == task.getName:
                        pass
                newName = input("Insert new task name: ")

            case "2": #changing description of task
                pass
            case "3": #changing status of completion for task
                pass


    

    