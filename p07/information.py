
people_info = {}

people_tasks = {}

while True:
    command = input("Enter command (new, report, ordered report, end): ")

    if command == "new":

        name = input("Enter name: ")
        age = int(input("Enter age: "))
        height = int(input("Enter height (cm): "))
        people_info[name] = (age, height)
        people_tasks[name] = set()
        
        tasks = input("Enter tasks (separated by spaces): ").lower().split()
        people_tasks[name].update(tasks)
        print(f"updated.")
    
    elif command == "report":
        for name, (age, height) in people_info.items():
            tasks = ", ".join(people_tasks[name])
            print(f"Name: {name}, Age: {age}, Height: {height} cm, Tasks: {tasks}")
    
    elif command == "ordered report":
        sorted_people = sorted(people_info.items(), key=lambda x: x[1][1])
        for name, (age, height) in sorted_people:
            tasks = ", ".join(people_tasks[name])
            print(f"Name: {name}, Age: {age}, Height: {height} cm, Tasks: {tasks}")
    
    elif command == "end":
        print("Exiting program.")
        break
    
    # else:
    #     if command in people_info:
    #         tasks = input("Enter tasks (separated by spaces): ").lower().split()
    #         people_tasks[command].update(tasks)
    #         print(f"Tasks for {command} updated.")
    #     else:
    #         print("Invalid command or name.")
            
