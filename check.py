tasks=[]

##The method to add a task
def addtask():
    tasktoadd = input("please enter a task ")
    tasks.append(tasktoadd)
    print(f"task '{tasktoadd}' added to the list")


def deletetask():
    listTasks()
    tasktodelete = int(input("Enter the number of the task you want to delete"))
    if(tasktodelete < 0 | tasktodelete > len(tasks)):
        print(f"Task I was not found") 
    else:   
        tasks.pop(tasktodelete)
        print(f"Task '{tasktodelete}' was deleted")


def listTasks():
    if not tasks:
        print("No tasks was found in the list")
    else:
        for index, tsks in enumerate(tasks):
            print(f"Tasks : '{index}'.  {tsks}")

if __name__ =="__main__":
    ### create a loop to rub the app 
    print ("welcome to the to do list app:)")
while True:
    print("\n")
    print("please select one of the following options ")
    print("-------------------------------------------")
    print("1. Add a new task ")
    print("2. Delete a task ")
    print("3. List tasks")
    print("4. Quit")

    choice=input ("enter your choice: ")
    
    if (choice == "1"):
        addtask()
    elif(choice == "2"):
      deletetask()
    elif (choice == "3"):
       listTasks()
    elif(choice == "4"):
         break 
    else:
        print("invalid input.please try again ")

        print("Goodbye(:(: )")

    



