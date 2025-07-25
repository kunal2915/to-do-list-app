def task():
    tasks=[]#empty list
    print("--------welcome to the task managment app----------")

    total_task=int(input("enter number of tasks you want to add:"))#7
    for i in range (1,total_task+1):
        task_name=input(f"enter task {i}:")
        tasks.append(task_name)
        
    print(f"tasks are:\n{tasks}")

    while True:
        operation=int(input("enter 1-add\n2-update\n3-delete\n4-view\n5-exit"))
        if operation==1:
            add=input("enter the task you want to add")
            tasks.append(add)
            print(f"updated task is {add} has been successfully added") 

        elif operation==2:
            updated_val=input("enter the task you want to update:")
            if updated_val in tasks:
                up=input("enter new task")
                ind=tasks.index(updated_val)# in integer 
                tasks[ind]=up
                print(f"updated task:{up}")

        elif operation==3:
            deleted_val=input("enter the task you wwant to delete:")
            if deleted_val in tasks:
              ind=tasks.index(deleted_val)
              del tasks[ind]
              print(f"{deleted_val} task has been deleted succesfully")
        
        elif operation==4:
            print(f"tasks are\n{tasks}")
        
        elif operation==5:
            print("closing the program......")
            break
task()