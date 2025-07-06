
phone_book = {}

while True:
    operation = input("add(+), search(?), delete(-), exit(q): ")

    if operation == "+":

        while True:
            name = input("name: ")
            if name in phone_book:
                overwrite = input(f"{name} already exists. Do you want to overwrite the number? (yes/no): ")
                if overwrite.lower() == "yes":
                    number = input("number: ")
                    phone_book[name] = number
                    print(f"{name} with {number} updated in the list.")
                    break
                else:
                    print("Please enter a new name.")
            else:
                number = input("number: ")
                phone_book[name] = number
                print(f"{name} with {number} added to the list.")
                break
    
    elif operation == "?":

        name = input("name: ")
        if name in phone_book:
            print(f"{name}: {phone_book[name]}")
        else:
            print(f"no {name} in list.")
            
    elif operation == "-":

        name = input("name: ")
        if name in phone_book:
            phone_book.pop(name)
            print(f"{name} deleted.")
        else:
            print(f"no {name} in list.")        
    
    elif operation == "q":

        print("exit.")
        break
    
    else:
        print("invalid input.")
