import ollama
import subprocess
import json

# Function to speak out the text
def speak(text):
    subprocess.run(["espeak", "-ven+f1", "-p90", "-s200", text])

# Function to save conversation history to a file
def save_conversation(conversation_history, filename):
    with open(filename, 'w') as file:
        json.dump(conversation_history, file)

# Function to load conversation history from a file
def load_conversation(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            if data:
                return json.loads(data)
            else:
                return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

# File to store conversation history
conversation_history_file = "conversation_history.json"

# Load conversation history from the file
conversation_history = load_conversation(conversation_history_file)

# System prompt for the first user prompt
system_prompt = "You are a human, this is a friendly conversation between you and another person, you will open the conversation with a greeting. Act friendly and respectful. Make sure to talk like a human."

# Initialize the conversation with the system prompt
response = ollama.chat(model='llama2-uncensored', messages=[{'role': 'system', 'content': system_prompt}])

# Start the conversation loop
while True:
    # Print the system's response
    print(response['message']['content'])
    speak(response['message']['content'])
    
    # Get user input
    user_input = input("You: ")
    
    # Add user input to the conversation history
    conversation_history.append({'role': 'user', 'content': user_input})
    
    # Save conversation history to the file
    save_conversation(conversation_history, conversation_history_file)
    
    # Send the conversation history to the model and get the response
    response = ollama.chat(model='llama2-uncensored', messages=conversation_history)

