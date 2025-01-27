import random
import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

# Predefined responses
responses = {
    "greeting": [
        "Hello! How can I assist you today?",
        "Hi there! What can I help you with?",
        "Hey! Need any assistance?"
    ],
    "goodbye": [
        "Goodbye! Have a great day!",
        "See you later!",
        "Bye! Take care!"
    ],
    "thanks": [
        "You're welcome!",
        "Happy to help!",
        "Anytime!"
    ],
    "default": [
        "I'm not sure how to respond to that.",
        "Can you please elaborate?",
        "Sorry, I didn't understand that."
    ]
}

# Function to classify user input
def classify_intent(text):
    text = text.lower()
    if any(greet in text for greet in ["hi", "hello", "hey"]):
        return "greeting"
    elif any(bye in text for bye in ["bye", "goodbye", "see you"]):
        return "goodbye"
    elif any(thank in text for thank in ["thank", "thanks"]):
        return "thanks"
    else:
        return "default"

# Function to generate response
def generate_response(user_input):
    intent = classify_intent(user_input)
    return random.choice(responses[intent])

# Main chatbot loop
def chatbot():
    print("Chatbot: Hello! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = generate_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
