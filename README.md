# AI-CHATBOT-WITH-NLP
**COMPANY**: CODETECH IT SOLUTIONS

**NAME**: KHUSHI CHAUDHARY

**INTERN ID**:CT08IHY

**DOMAIN**: PYTHON

**BATCH DURATION**: DECEMBER 30TH,2024 TO JANUARY 30TH,2025

**MENTOR NAME**: NEELA SANTOSH

**DESCRIPTION**:This Python script is a simple chatbot application that uses basic natural language processing (NLP) techniques and the spaCy library to understand and respond to user input. Below is a detailed explanation and description of the tasks it performs.
1. Purpose of the Script
The primary purpose of this script is to:

Interact with users through a conversational interface.
Understand user input by classifying it into predefined intents (e.g., greetings, goodbyes, gratitude, or default responses).
Respond appropriately using predefined responses based on the detected intent.
The chatbot serves as an example of how NLP can be applied to create conversational agents.

2. Key Components and Functionality
Imports
The script uses two libraries:

random: To randomly select a response from a list of predefined responses for each intent.
spacy: To load the English NLP model (en_core_web_sm). While the model is not actively used for advanced NLP tasks in this script, it can be further leveraged for tokenization, named entity recognition (NER), or syntactic analysis in more complex implementations.
Predefined Responses
The chatbot uses a dictionary called responses to store predefined responses for four different intents:

greeting: Responses to greetings like "Hi" or "Hello."
goodbye: Responses to farewells like "Bye" or "Goodbye."
thanks: Responses to expressions of gratitude like "Thank you" or "Thanks."
default: Generic responses when the chatbot cannot classify the user input into any specific intent.
classify_intent Function
This function determines the intent of the user's input:

Input: A string containing the user's input.
Processing:
Converts the input to lowercase to ensure case-insensitive matching.
Checks for keywords associated with each intent (e.g., "hi" or "hello" for greetings) using any() and predefined keyword lists.
Output: Returns the classified intent as a string (e.g., "greeting", "goodbye", "thanks", or "default").
generate_response Function
This function generates a response based on the classified intent:

Input: The user's input string.
Processing:
Calls the classify_intent function to determine the intent.
Randomly selects a response from the corresponding intent’s response list in the responses dictionary using random.choice.
Output: Returns the selected response as a string.
chatbot Function
This is the main loop of the chatbot:

Initialization: Displays a welcome message and instructions for exiting the chat.
Loop:
Continuously prompts the user for input using input().
Ends the loop if the user types "exit".
For all other inputs, generates and prints a response using the generate_response function.
Termination: Displays a farewell message before exiting.
3. Execution Flow
The script starts by displaying a greeting message and informing the user how to exit the chat.
The user provides input, which is processed by the classify_intent function to determine its intent.
Based on the intent, a random response is selected and displayed.
The process continues until the user types "exit," at which point the chatbot terminates.
4. Use Case and Customization
Use Case
This chatbot demonstrates how simple intent classification can create a conversational agent. It is suitable for beginner-level projects and can serve as a foundation for more advanced bots that integrate machine learning models or APIs.

Customization
Expanding Intents: Add more intents like "weather" or "help" to handle additional user queries.
Advanced NLP: Use spaCy for more complex tasks like named entity recognition (NER) or dependency parsing.
External Integration: Connect the bot to APIs (e.g., weather or news APIs) to provide dynamic responses.
Graphical Interface: Enhance usability by integrating the chatbot with a GUI or a web-based interface.
5. Practical Applications
Learning: A great starting point for understanding chatbot development.
Customer Support: Can be expanded to handle FAQs in a business setting.
Personal Assistance: Serve as a basic virtual assistant for tasks like greetings or reminders.
This code provides a solid base for chatbot development, combining simplicity with practical intent classification and response generation techniques.














