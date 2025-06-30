tasks = []

def add_task():
    description = input("Tozih vazife ro vared kon: ").strip()
    due_date = input("Tarikh mo'od (YYYY-MM-DD) ya khali bezar: ").strip()
    priority = input("Olaviat ro vared kon (bala, motavaset, payin): ").strip().lower()

    if priority not in ["bala", "motavaset", "payin"]:
        print("❌ Lotfan faghat 'bala', 'motavaset' ya 'payin' ro vared kon.")
        return

    if due_date == "":
        due_date = "nadarad"

    task = {
        "description": description,
        "due_date": due_date,
        "priority": priority
    }

    tasks.append(task)
    print("✅ Vazife ba movafaghiat ezafe shod.")

def view_tasks():
    if not tasks:
        print("📭 Hich vazifei sabt nashode.")
    else:
        print("\n📋 List-e vazayef:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task['description']} - Mo'od: {task['due_date']} - Olaviat: {task['priority']}")
        print("")

def delete_task():
    view_tasks()

    if not tasks:
        return

    number = input("Shomare vazife baraye hazf ro vared kon: ").strip()

    if number.isdigit():
        index = int(number) - 1
        if 0 <= index < len(tasks):
            confirm = input(f"Motmaeni ke '{tasks[index]['description']}' hazf beshe? (yes/no): ").strip().lower()
            if confirm == "yes":
                tasks.pop(index)
                print("✅ Vazife hazf shod.")
            else:
                print("❎ Hazf laghv shod.")
        else:
            print("❌ Shomare vared shode dorost nist.")
    else:
        print("❌ Lotfan faghat adad sahih vared kon.")

def show_menu():
    while True:
        print("\n📌 Menu:")
        print("1. Ezafe kardan vazife")
        print("2. Namayesh vazayef")
        print("3. Hazf vazife")
        print("4. Khoroj")

        choice = input("Yeki az gozinehaye (1-4) ro entekhab kon: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("👋 Khodahafez!")
            break
        else:
            print("❌ Lotfan adad 1 ta 4 ro vared kon.")

show_menu()
