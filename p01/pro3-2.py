tasks = []
deleted_tasks = []

def add_task():
    description = input("Tozih vazife ro vared kon: ").strip()
    due_date = input("Tarikh mo'od (YYYY-MM-DD) ya khali bezar: ").strip()
    priority = input("Olaviat ro vared kon (bala, motavaset, payin): ").strip().lower()

    if priority not in ["bala", "motavaset", "payin"]:
        print("❌ Lotfan az kalamat bala, motavaset ya payin estefade kon.")
        return

    if due_date == "":
        due_date = "nadarad"

    task = {
        "description": description,
        "due_date": due_date,
        "priority": priority
    }

    tasks.append(task)
    print("✅ Vazife ezafe shod!")

def view_tasks():
    if not tasks:
        print("📭 Hich vazifei sabt nashode.")
    else:
        print("\n📋 List-e vazayef:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task['description']} - Mo'od: {task['due_date']} - Olaviat: {task['priority']}")
        print("")

def delete_tasks():
    view_tasks()
    if not tasks:
        return

    numbers = input("Shomare vazayefi ke mikhay hazf beshan ro ba , joda kon (mesal: 1,3): ").strip()

    ids = numbers.split(",")
    indexes = []

    for n in ids:
        n = n.strip()
        if n.isdigit():
            i = int(n) - 1
            if 0 <= i < len(tasks):
                indexes.append(i)
            else:
                print(f"❌ Shomare {n} vojood nadare.")
        else:
            print(f"❌ '{n}' adad nist.")

    indexes.sort(reverse=True)

    for i in indexes:
        print(f"❓ Hazf '{tasks[i]['description']}'...")
        confirm = input("Motmaeni? (yes/no): ").strip().lower()
        if confirm == "yes":
            deleted_tasks.append(tasks[i])  
            tasks.pop(i)
            print("✅ Hazf shod.")
        else:
            print("❎ Hazf laghv shod.")

def undo_delete():
    if deleted_tasks:
        last = deleted_tasks.pop()
        tasks.append(last)
        print("↩️ Akharin vazife bazgasht dade shod.")
    else:
        print("❌ Hich vazifeyi baraye bazgasht vojood nadarad.")

def show_menu():
    while True:
        print("\n📌 Menu:")
        print("1. Ezafe kardan vazife")
        print("2. Namayesh vazayef")
        print("3. Hazf chand vazife")
        print("4. Bazgasht akharin hazf (Undo)")
        print("5. Khoroj")

        choice = input("Yeki az gozinehaye (1-5) ro entekhab kon: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_tasks()
        elif choice == "4":
            undo_delete()
        elif choice == "5":
            print("👋 Khodahafez!")
            break
        else:
            print("❌ Lotfan adad 1 ta 5 ro vared kon.")


show_menu()
