from task import Task
from queries import CREATE_TASK_TABLE, INSERT_TASK, GET_ALL_TASKS
import sqlite3

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
            "6. Quit app\n" \
            "Input choice here: ")
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
            #self.addTasks(newTask) #replace with sql query
            conn = sqlite3.connect("src/tasks.db")
            cursor = conn.cursor()
            cursor.execute(CREATE_TASK_TABLE)
            cursor.execute(INSERT_TASK, (newTask.name, newTask.desc, newTask.getChecked, newTask.getDate))
            conn.commit()
            conn.close()
            
        except ValueError as e:
            print("ERROR:", e)

    def addTasks(self, task):
        self._tasks.append(task)

    def printTasks(self):
    
        print("*******************Tasks***********************")
        #for task in self._tasks:
        #    print(task.printTask())
        conn = sqlite3.connect("src/tasks.db")
        cursor = conn.cursor()
        cursor.execute(GET_ALL_TASKS)
        tasks = cursor.fetchall()
        print(tasks)
        conn.close()
        print("***********************************************")

    def emptyTasks(self):
        if len(self._tasks) == 0:
            raise ValueError("No tasks found.")

    def findTask(self, taskToFind: str):
        taskToFind = taskToFind.lower().replace(" ", "")
        for task in self._tasks:
            newTask = task.name.lower().replace(" ", "")
            if taskToFind == newTask:
                return True, task
            else:
                raise ValueError("Task not found.")
            

    def completeTask(self):
        try:
            self.emptyTasks()
            
            completedTask = input("Type name of task that is completed: ")
            res, task = self.findTask(completedTask)
            if res:
                task.setPrintTask()
    
        except ValueError as e:
            print("ERROR:", e)

    def deleteTasks(self):
        try:
            self.emptyTasks()

            deleteTask = input("What task do you want to delete?: ")

            res, task = self.findTask(deleteTask)
            if res:
                check = input(f"Are you sure you want to delete {task.name}? y/n: ").lower()
                if(check == "y" or check == "yes"):
                    self._tasks.remove(task)
                    print(f"Task {task.name} is deleted!")

                elif(check == "n" or check == "no"):
                    print(f"Task {task.name} is not deleted. Canceling operation!")

                else:
                    #print("Not a valid input. Try again.")
                    raise ValueError("Invalid input. Try again.")
                
        except ValueError as e:
            print("ERROR:", e)

    def editTasks(self):
        try:
            self.emptyTasks()
            
            editTask = input("Which task would you like to edit?: ")

            res, task = self.findTask(editTask)

            editOption = input("What would you like to edit?\n"
                        "1. Name of task\n" \
                        "2. Description of task\n" \
                        "3. Status of completion for task\n" \
                        "Input choice here: ")
            if not editOption:
                raise ValueError("Option cannot be empty")
            
            match editOption:
                case "1": #changing name of task
                    if res:
                        newName = input("Insert new task name: ")
                        if not newName:
                            raise ValueError("Input cannot be empty.")
                        else:
                            task.name = newName

                case "2": #changing description of task
                    if res:
                        newDesc = input("Insert new description: ")
                        if not newDesc:
                            raise ValueError("Input cannot be empty.")
                        else:
                            task.desc = newDesc

                case "3": #changing status of completion for task
                    if res:
                        task.setPrintTask()
                
                case _:
                    raise ValueError("Not a valid option. Try again.")

        except ValueError as e:
            print("ERROR:", e)


    

    