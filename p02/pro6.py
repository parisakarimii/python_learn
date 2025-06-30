flashcards = {
    "payame paris chie?": "Paris",
    "adad 2 + 2 chand ast?": "4",
    "takhtiar falsafe chist?": "sir tarik"
}

def quiz():
    score = 0
    total = len(flashcards)
    print("Azmoon shoro shod!\n")

    for question, answer in flashcards.items():
        user_answer = input(question + " ").strip().lower()
        correct_answer = answer.strip().lower()

        
        if correct_answer == "paris":
            if "paris" in user_answer:
                print("✅ Tasdigh shod!")
                score += 1
            else:
                print(f"❌ Javab eshtebah. Javabe sahih: {answer}")
        else:
      
            if user_answer == correct_answer:
                print("✅ Tasdigh shod!")
                score += 1
            else:
                print(f"❌ Javab eshtebah. Javabe sahih: {answer}")

        print()

    percentage = (score / total) * 100
    print(f"Natijeh shoma: {score} az {total} soal dorost javab dade shod.")
    print(f"Darsad natijeh: {percentage:.1f}%")

quiz()
