def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    
    elif "how are you" in user_input:
        return "I'm just a program, but thanks for asking! How about you?"
    
    elif "what is your name" in user_input:
        return "I am a simple rule-based chatbot created to help you."
    
    elif "help" in user_input:
        return "Sure! What do you need help with?"
    
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day!"
    
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

def start_chat():
    print("Welcome to the chatbot! Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['exit', 'bye']:
            print(chatbot_response(user_input))
            break
        
        response = chatbot_response(user_input)
        print("Chatbot:", response)
        
start_chat()
