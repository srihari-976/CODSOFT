import random

# Define a function to greet the user
def greet_user():
    responses = ["Hello!", "Hi there!", "Hey!", "Greetings!", "hello", "Hai", "hai"]
    return random.choice(responses)

# Define a function to respond to common questions
def respond_to_question(user_input):
    user_input = user_input.lower()  # Convert user input to lowercase for case-insensitive matching

    if "how are you" in user_input:
        return "I'm just a computer program, so I don't have feelings, but I'm here to help!"

    if "what is your name" in user_input:
        return "I'm a chatbot. You can call me Jarvis."

    if "who created you" in user_input:
        return "I was created by a person named Srihari."

    if "how is the day going" in user_input:
        return "It's great today!!"

    if "can I call you Jarvis" in user_input:
        return "Of course, you can call me Jarvis."

    if "tell me an interesting fact" in user_input:
        return "Certainly! Here's an interesting fact:\nDid you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible. Honey's long shelf life is due to its low moisture content and natural acidity, which create an environment inhospitable to bacteria and microorganisms. It's one of the few foods that can truly last indefinitely if stored properly."

    if "translate 'hello' into French" in user_input:
        return "\"Hello\" translates to \"Bonjour\" in French."

    if "recommend a funny joke" in user_input:
        return "Why don't scientists trust atoms?\nBecause they make up everything! 😄"

    if "suggest a book to read" in user_input:
        return "Title: \"The Hitchhiker's Guide to the Galaxy\"\nAuthor: Douglas Adams\nThis book is a classic science fiction comedy that follows the misadventures of an unwitting human, Arthur Dent, as he is whisked away on an intergalactic journey through space and time. It's known for its witty humor and unique take on the universe. If you enjoy humorous and thought-provoking science fiction, this book is a must-read!"

    return "I'm sorry, I don't understand that question."

# Main chat loop
print("Chatbot: " + greet_user())

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    response = respond_to_question(user_input)
    print("Chatbot: " + response)
