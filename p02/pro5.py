flashcards = {
    "takhtiar falsafe chist?": "sir tarik",
    "adad 2 + 2 chand ast?": "4",
    "che sak mekanishium vitamor va tilooj ar heshun?": "perskesh"
}

def show_questions():
    print("\nSoalat flashcard:")
    for index, question in enumerate(flashcards.keys(), start=1):
        print(f"{index}. {question}")

def review_flashcards():
    questions = list(flashcards.keys())
    for i, question in enumerate(questions, start=1):
        print(f"\nSoal {i}: {question}")
        input("Baraye didan javab Enter bezanid...")
        print(f"Javab: {flashcards[question]}")
        if i != len(questions):
            input("Baraye raftan be soal badi Enter bezanid...")
    print("\nTamaam shod!")

def quiz():
    while True:
        show_questions()
        choice = input("\nShomare soal ra vared konid (ya 'start' baraye morur peydari, 'end' baraye payan): ")
        
        if choice.lower() == 'end':
            print("Khodahafez!")
            break
        
        if choice.lower() == 'start':
            review_flashcards()
            continue
        
        if not choice.isdigit():
            print("Lotfan yek shomare moteber vared konid.")
            continue
        
        choice = int(choice)
        questions = list(flashcards.keys())
        
        if 1 <= choice <= len(questions):
            question = questions[choice - 1]
            answer = flashcards[question]
            print(f"\nSoal: {question}")
            print(f"Javab: {answer}\n")
        else:
            print("Shomare vared shode kharej az mahdude ast.")

quiz()
