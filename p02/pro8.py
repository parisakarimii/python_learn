import json
import os

flashcards = {}

def save_flashcards():
    with open("flashcards.json", "w") as file:
        json.dump(flashcards, file)


def load_flashcards():
    global flashcards
    if os.path.exists("flashcards.json"):
        with open("flashcards.json", "r") as file:
            flashcards = json.load(file)
    else:
        flashcards = {}


def add_flashcard():
    question = input("Soal ra vared konid: ")
    answer = input("Javabe soal ra vared konid: ")
    flashcards[question] = answer
    save_flashcards()
    print("✅ Flashcard ba movafaghiat ezafe shod!")

def delete_flashcard():
    if not flashcards:
        print("⚠️ Hich flashcardi baraye hazf vojood nadarad!")
        return

    print("Flashcard-ha:")
    for i, question in enumerate(flashcards.keys(), 1):
        print(f"{i}. {question}")

    choice = input("Shomare soal ke mikhahid hazf konid ra vared konid: ")
    if choice.isdigit():
        choice_num = int(choice)
        if 1 <= choice_num <= len(flashcards):
            question_to_delete = list(flashcards.keys())[choice_num - 1]
            del flashcards[question_to_delete]
            save_flashcards()
            print(f"✅ Flashcard '{question_to_delete}' hazf shod!")
        else:
            print("⚠️ Entekhab shoma kharj az range mojood ast.")
    else:
        print("⚠️ Lotfan yek shomare sahih vared konid.")


def review_flashcards():
    if not flashcards:
        print("⚠️ Hich flashcardi baraye moroor vojood nadarad!")
        return

    for question, answer in flashcards.items():
        print(f"Soal: {question}")
        user_answer = input("Javabe shoma: ")
        if user_answer.strip().lower() == answer.strip().lower():
            print("✅ Javabe dorost!")
        else:
            print(f"❌ Javabe eshtebah. Javabe dorost: {answer}")
        print("-" * 30)

def show_menu():
    print("\n=== Flashcard Menu ===")
    print("1. Ezafe kardan flashcard")
    print("2. Hazf kardan flashcard")
    print("3. Moroor flashcard-ha")
    print("4. Khoroji")
    choice = input("Entekhab konid (1-4): ")
    return choice

def main():
    load_flashcards()
    while True:
        choice = show_menu()
        if choice == '1':
            add_flashcard()
        elif choice == '2':
            delete_flashcard()
        elif choice == '3':
            review_flashcards()
        elif choice == '4':
            print("Khodahafez!")
            break
        else:
            print("Lotfan yek gozine dorost vared konid.")

if __name__ == "__main__":
    main()
