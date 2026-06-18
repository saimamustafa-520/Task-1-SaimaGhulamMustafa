from datetime import datetime

print("=" * 60)
print("🤖 Welcome to Smart AI Assistant")
print("=" * 60)

name = input("Before we begin, what's your name? ")

print(f"\nHello, {name}! Nice to meet you.")
print("Type 'help' to see all commands.")
print("Type 'bye' to exit.\n")

message_count = 0

while True:
    user = input(f"{name}: ").lower().strip()
    message_count += 1

    # Greetings
    if user in ["hi", "hello", "hey"]:
        print(f"Bot: Hello {name}! How can I help you today?")

    # About chatbot
    elif user == "your name":
        print("Bot: I am Smart AI Assistant, a rule-based chatbot built in Python.")

    elif user == "what can you do":
        print("""
Bot: I can:
✔ Answer basic questions
✔ Tell jokes
✔ Show date and time
✔ Talk about AI and Python
✔ Give study tips
✔ Motivate you
✔ Track our conversation count
        """)

    # AI Questions
    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence. It allows machines to perform tasks that usually require human intelligence.")

    elif user == "machine learning":
        print("Bot: Machine Learning is a branch of AI where computers learn patterns from data.")

    # Python Questions
    elif user == "python":
        print("Bot: Python is a powerful and beginner-friendly programming language.")

    elif user == "why learn python":
        print("Bot: Python is widely used in AI, Data Science, Automation, Web Development, and Cybersecurity.")

    # Time & Date
    elif user == "time":
        print("Bot:", datetime.now().strftime("%H:%M:%S"))

    elif user == "date":
        print("Bot:", datetime.now().strftime("%d-%m-%Y"))

    # Motivation
    elif user == "motivate me":
        print("Bot: Success comes from consistency, not perfection. Keep learning every day!")

    elif user == "i am sad":
        print("Bot: Tough days happen. Focus on one small win today—you'll feel better.")

    elif user == "i am happy":
        print("Bot: That's wonderful! Keep spreading positive energy.")

    # Study Tips
    elif user == "study tips":
        print("""
Bot:
1. Study in focused 25-minute sessions.
2. Practice coding daily.
3. Build projects.
4. Revise regularly.
5. Learn by teaching others.
        """)

    # Jokes
    elif user == "joke":
        print("Bot: Why do programmers hate nature? Too many bugs!")

    elif user == "another joke":
        print("Bot: I told my computer I needed a break. It said: No problem, I'll go to sleep.")

    # Conversation Stats
    elif user == "messages":
        print(f"Bot: We have exchanged {message_count} messages so far.")

    # Thanks
    elif user in ["thanks", "thank you"]:
        print("Bot: You're welcome! 😊")

    # Help Menu
    elif user == "help":
        print("""
================ COMMANDS ================
hello / hi / hey
your name
what can you do
what is ai
machine learning
python
why learn python
time
date
motivate me
i am sad
i am happy
study tips
joke
another joke
messages
thanks
bye
==========================================
        """)

    # Exit
    elif user == "bye":
        print(f"Bot: Goodbye {name}! We exchanged {message_count} messages today.")
        print("Bot: Have a great day! 👋")
        break

    # Unknown command
    else:
        print("Bot: Sorry, I don't understand that command. Type 'help' for options.")