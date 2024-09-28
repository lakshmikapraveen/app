def respond_to_user(user_input):
    """Generate a response based on user input."""
    responses = {
        "hello": "Hi there! How can I help you today?",
        "how are you?": "I'm just a program, but thanks for asking!",
        "bye": "Goodbye! Have a great day!",
    }
    return responses.get(user_input.lower(), "Sorry, I don't understand that.")

def chatbot():
    print("Welcome to the Chatbot! (type 'bye' to exit)")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        response = respond_to_user(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
