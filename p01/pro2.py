tasks = []

def add_task():
    description = input("📝 Tozih vazife ro vared kon: ").strip()
    if not description:
        print("❌ Tozih nemitoone khali bashe.")
        return

    due_date = input("📅 Tarikh mo'od (YYYY-MM-DD) ya khali bezar: ").strip()
    if due_date == "":
        due_date = "nadarad"

    priority = input("⭐ Olaviat ro vared kon (bala, motavaset, payin): ").strip().lower()
    if priority not in ["bala", "motavaset", "payin"]:
        print("❌ Faghat 'bala', 'motavaset' ya 'payin' ghabool hast.")
        return

    task = {
        "description": description,
        "due_date": due_date,
        "priority": priority
    }

    tasks.append(task)
    print("✅ Vazife ba movafaghiat ezafe shod!\n")

def view_tasks():
    if not tasks:
        print("📭 Hich vazifei sabt nashode.\n")
        return

    print("\n📋 Liste vazayef:")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task['description']} | Mo'od: {task['due_date']} | Olaviat: {task['priority']}")
    print()

def delete_task():
    view_tasks()
    if not tasks:
        return

    user_input = input("❌ Shomare vazife baraye hazf ra vared kon: ").strip()
    if user_input.isdigit():
        task_num = int(user_input) - 1
        if 0 <= task_num < len(tasks):
            confirm = input(f"Motmaeni ke '{tasks[task_num]['description']}' hazf beshe? (yes/no): ").strip().lower()
            if confirm == "yes":
                tasks.pop(task_num)
                print("🗑️ Vazife hazf shod.\n")
            else:
                print("ℹ️ Hazf laghv shod.\n")
        else:
            print("❌ Shomare vared shode dorost nist.\n")
    else:
        print("❌ Lotfan adad sahih vared kon.\n")


add_task()
add_task()
delete_task()
view_tasks()
