def greet(text):
    if "hello" in text:
        return "Hello! How can I assist you today?"
    else:
        return "What are you talking about"

question = input("Whats your question? :")
greeting = greet(question)

print(f"{greeting}, be polite and ask again")
