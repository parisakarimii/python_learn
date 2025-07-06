
phone_book = {}

while True:
    operation = input("add(+),search(?), delete(-), exit(q): ")

    if operation == "+":

        name = input("name: ")
        number = input("number: ")
        phone_book[name] = number
        print(f"{name} with {number} add to list")
    
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
            print(f"{name} delete.")
        else:
            print(f"no {name} in list")        
    
    
    elif operation == "q":

        print("exit.")
        break
    
    else:
        print("invalid input.")





