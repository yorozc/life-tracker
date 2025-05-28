from interface import userInterface

def main():
    user = userInterface()
    user.createTask()
    user.printTasks()

if __name__=="__main__":
    main()