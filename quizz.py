def ask_question(question, options, correct_answer):
    """Ask a question and return True if the answer is correct."""
    print(f"\n{question}")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    
    try:
        answer = int(input("Your answer (1-4): "))
        if options[answer - 1] == correct_answer:
            print("Correct!")
            return True
        else:
            print("Incorrect.")
            return False
    except (ValueError, IndexError):
        print("Invalid input. Please enter a number between 1 and 4.")
        return False

def quiz_app():
    print("Welcome to the Simple Quiz Application!")
    
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "answer": "Paris"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["3", "4", "5", "6"],
            "answer": "4"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Venus"],
            "answer": "Mars"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["Harper Lee", "Mark Twain", "Ernest Hemingway", "F. Scott Fitzgerald"],
            "answer": "Harper Lee"
        },
    ]

    score = 0
    
    for q in questions:
        if ask_question(q["question"], q["options"], q["answer"]):
            score += 1

    print(f"\nYour total score: {score}/{len(questions)}")
    print("Thank you for playing!")

if __name__ == "__main__":
    quiz_app()
