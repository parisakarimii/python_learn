import random

flashcards = {
    "Lotfan paytakht France ra benevisid: ": "Paris",
    "2 + 2 chand ast? ": "4",
    "Nevisande Hamlet kist? ": "Shakespeare",
}

def quiz():
    score = 0
    questions = list(flashcards.items())
    random.shuffle(questions)

    for question, answer in questions:
        user_answer = input(question).strip().lower()
        correct_answer = answer.strip().lower()

        if user_answer == correct_answer:
            print("✅ Dorost!")
            score += 1
        else:
            print(f"❌ Nadorost! Javabe sahih: {answer}")

    total_questions = len(flashcards)
    print(f"\nShoma {score} az {total_questions} soal ra dorost javab dadid.")

    percentage = (score / total_questions) * 100
    print(f"Darsad natijeh: {percentage:.1f}%\n")
    if percentage == 100:
        print("🎉 Ali! Shoma hame soalha ra dorost pasokh dadid!")
    elif percentage >= 50:
        print("👍 Khob! Shoma darsad khoobi kasb kardid. Edame dahid!")
    elif percentage >= 30:
        print("🙂 Talash khoobi bud, behtar ast kami bishtar motale konid.")
    else:
        print("⚠️ Niyaz be tamrin bishtari darid. Naomid nashavid va edame dahid!")

quiz()
