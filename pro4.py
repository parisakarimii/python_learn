import json
import os
from colorama import Fore, Style, init
init(autoreset=True)
# این باعث میشه فقط همون خط رنگی بشه بعدیا نشن
tasks = []

def load_tasks():
    global tasks
    if os.path.exists('tasks.txt'):
        with open('tasks.txt', 'r') as file:
            tasks[:] = json.load(file)
    else:
        tasks[:] = []

def save_tasks():
    with open('tasks.txt', 'w', encoding='utf-8') as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)

def add_task():
    while True:
        title = input("📝 Tozih vazife ro vared kon: ").strip()
        if title:
            break
        print(Fore.RED + "⚠ Onvan nemitune khali bashe.")

    due_input = input("📅 Tarikh mo'od (YYYY-MM-DD) ya khali bezar: ").strip()
    if due_input == "":
        due_input = "nadarad"

    while True:
        priority = input("⭐ Olaviat (bala, motavaset, payin): ").strip().lower()
        if priority in ['bala', 'motavaset', 'payin']:
            break
        print(Fore.RED + "⚠ Olaviat dorost vared nashode.")

    task = {"title": title, "due": due_input, "priority": priority}
    tasks.append(task)
    print(Fore.GREEN + "✅ Vazife ezafe shod.")

def view_tasks():
    if not tasks:
        print(Fore.YELLOW + "📭 Hich vazife vojood nadare.")
    else:
        print(Fore.CYAN + "\n📋 List vazayef:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {Fore.YELLOW}{task['title']} {Style.RESET_ALL}| Mo'od: {task['due']} | Olaviat: {task['priority']}")

def get_valid_index(prompt):
    while True:
        num = input(prompt).strip()
        if num.lower() == 'b':
            return None
        if num.isdigit():
            index = int(num) - 1
            if 0 <= index < len(tasks):
                return index
            else:
                print(Fore.RED + "❌ Shomare mojood nist.")
        else:
            print(Fore.RED + "⚠ Lotfan adad sahih ya 'b' baraye bazgasht vared kon.")

def edit_task():
    if not tasks:
        print(Fore.YELLOW + "📭 Hich vazife vojood nadare.")
        return

    view_tasks()
    i = get_valid_index("✏ Shomare vazife baraye virayesh (ya 'b' baraye bazgasht): ")
    if i is None:
        return

    new_title = input("📝 Onvan jadid (khali = bigham): ").strip()
    new_due = input("📅 Tarikh jadid (khali = bigham): ").strip()
    new_priority = input("⭐ Olaviat jadid (bala, motavaset, payin): ").strip().lower()

    if new_title:
        tasks[i]['title'] = new_title
    if new_due:
        tasks[i]['due'] = new_due
    if new_priority in ['bala', 'motavaset', 'payin']:
        tasks[i]['priority'] = new_priority
    elif new_priority:
        print(Fore.RED + "⚠ Olaviat eshtebah bood va taghir dade nashod.")

    print(Fore.GREEN + "✅ Vazife virayesh shod.")

def delete_task():
    if not tasks:
        print(Fore.YELLOW + "📭 Hich vazife vojood nadare.")
        return

    view_tasks()
    i = get_valid_index("🗑 Shomare vazife baraye hazf (ya 'b' baraye bazgasht): ")
    if i is None:
        return

    del tasks[i]
    print(Fore.GREEN + "✅ Vazife hazf shod.")

def search_tasks():
    key = input("🔍 Kalameye klidi baraye jostojoo: ").strip().lower()
    # found = [t for t in tasks if key in t['title'].lower()]
    found = []
    for t in tasks:
        title_lower = t['title'].lower()
        if key in title_lower:
            found.append(t)

    if found:
        print(Fore.CYAN + f"\n🧾 Vazayefi ke '{key}' darand:")
        for t in found:
            print(f"📌 {t['title']} | Mo'od: {t['due']} | Olaviat: {t['priority']}")
    else:
        print(Fore.YELLOW + "❌ Hich vazifei peyda nashod.")

def menu():
    load_tasks()
    while True:
        print(Fore.MAGENTA + "\n📋 Menu:")
        print("1. ➕ Ezafe kardan vazife")
        print("2. 📄 Namayesh vazayef")
        print("3. ✏ Virayesh vazife")
        print("4. 🗑 Hazf vazife")
        print("5. 🔍 Jostojoo")
        print("6. 💾 Zakhire va khorooj")

        choice = input("➤ Entekhab kon (1-6): ").strip()
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            edit_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            search_tasks()
        elif choice == '6':
            save_tasks()
            print(Fore.GREEN + "✅ Vazayef zakhire shod. Khodahafez! 👋")
            break
        else:
            print(Fore.RED + "⚠ Lotfan adad 1 ta 6 ro vared kon.")

menu()
