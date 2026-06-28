print("🤖 Smart Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower().strip()

    # Greetings
    if "hello" in user or "hi" in user or "hey" in user:
        print("Bot: Hello! How can I help you today?")

    # Casual conversation
    elif "just wanna talk" in user or "want to talk" in user:
        print("Bot: Of course! I'd be happy to chat. How has your day been so far?")

    elif "how are you" in user:
        print("Bot: I'm doing well, thank you for asking. How about you?")

    elif user in ["good", "fine", "great", "awesome"]:
        print("Bot: That's wonderful to hear! What have you been working on lately?")

    elif user in ["bad", "sad", "not good"]:
        print("Bot: I'm sorry to hear that. I hope things get better soon. Would you like to talk about it?")

    # Name conversation
    elif "your name" in user or "who are you" in user:
        print("Bot: My name is SmartBot. What's your name?")

    elif "my name is" in user:
        name = user.replace("my name is", "").strip()
        print(f"Bot: Nice to meet you, {name.title()}! Are you a student or a working professional?")

    elif user == "beena":
        print("Bot: Nice to meet you, Beena! Are you a student or a working professional?")

    # Study and career
    elif "student" in user:
        print("Bot: That's great! What subject or skill are you currently learning?")

    elif "working professional" in user or "employee" in user:
        print("Bot: That's wonderful. What field do you work in?")

    elif "python" in user:
        print("Bot: Python is an excellent programming language. Are you building any projects with it?")

    elif "chatbot" in user:
        print("Bot: That's a great project! Building a chatbot helps improve programming and logic skills.")

    elif "coding" in user or "programming" in user:
        print("Bot: Coding is a valuable skill. Which programming language do you enjoy the most?")

    # Hobbies
    elif "hobby" in user or "hobbies" in user:
        print("Bot: Hobbies are a great way to relax and learn. What is your favorite hobby?")

    elif "music" in user:
        print("Bot: Music can really brighten the day. What kind of music do you enjoy?")

    elif "movie" in user:
        print("Bot: Movies are always fun. What's your favorite movie?")

    # Date and time
    elif "time" in user:
        from datetime import datetime
        current_time = datetime.now().strftime("%I:%M %p")
        print(f"Bot: The current time is {current_time}. Do you have any plans for today?")

    elif "date" in user:
        from datetime import date
        print(f"Bot: Today's date is {date.today()}. Is there anything special planned today?")

    # Weather
    elif "weather" in user:
        print("Bot: I can't check live weather information yet, but I hope it's a pleasant day where you are.")

    # Thanks
    elif "thank" in user:
        print("Bot: You're welcome! Is there anything else you'd like to discuss?")

    # Exit
    elif user == "bye":
        print("Bot: It was nice talking with you. Have a wonderful day ahead!")
        break

    # Default response
    else:
        print("Bot: That's interesting! Could you tell me more about that?")