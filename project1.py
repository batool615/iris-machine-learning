dict = {
    "hello": "hello! how can i help you?",
    "hi": "hi there!",
    "how are you": "i'm doing great. how about you?",
    "i'm fine": "that's good to hear!",
    "i'm not feeling well": "i'm sorry to hear that. hope you feel better soon.",
    "what is your name": "i'm bot.",
    "thanks": "you're welcome!"
}

print("Welcome to the chatbot! You can ask me questions or say hello.")
print("Type 'exit' or 'bye' to quit.\n")

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "exit" or user_input == "bye":
        print("Bot: Goodbye!")
        break

    reply = dict.get(user_input, "Sorry, I don't understand.")
    print("Bot:", reply)