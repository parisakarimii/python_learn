tasks = []

def add_task():

    description = input("Tozihat-e vazife ra vared konid: ").strip()


    due_date = input("Tarikh-e mo'od ra vared konid [YYYY-MM-DD] ya khali bogzarid: ").strip()
    if due_date == "":
        due_date = "nadarad"
    elif len(due_date) != 10 or due_date[4] != "-" or due_date[7] != "-":
        print("❌ Tarikh eshtebah ast. Bayad be shekl-e 2025-06-01 bashad.")
        return

    priority = input("Olawiyat ra vared konid (bala, motavaset, payin): ").strip().lower()
    if priority not in ["bala", "motavaset", "payin"]:
        print("❌ Faghat mitavan 'bala', 'motavaset' ya 'payin' ra vared kard.")
        return


    task = {
        "description": description,
        "due_date": due_date,
        "priority": priority
    }

    tasks.append(task)
    print("✅ Vazife ba movafaghiat ezafe shod!")


add_task()
print(tasks)
