def create_flashcard(flashcards):
    """Create a new flashcard."""
    question = input("Enter the flashcard question: ")
    answer = input("Enter the flashcard answer: ")
    flashcards[question] = answer
    print("Flashcard added.\n")

def study_flashcards(flashcards):
    """Study the flashcards."""
    for question, answer in flashcards.items():
        input(f"Question: {question}\nPress Enter to see the answer...")
        print(f"Answer: {answer}\n")

def flashcard_app():
    flashcards = {}
    
    print("Welcome to the Flashcard Quiz App!")
    
    while True:
        print("1. Create Flashcard")
        print("2. Study Flashcards")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            create_flashcard(flashcards)
        elif choice == '2':
            study_flashcards(flashcards)
        elif choice == '3':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid option, please try again.\n")

if __name__ == "__main__":
    flashcard_app()
