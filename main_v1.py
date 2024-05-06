import ollama
import subprocess

#def speak(text):
#    subprocess.run(["espeak", "-ven+f1", "-p83", "-s190", text])

# Initialize an empty list to store the conversation history
conversation_history = []

# System prompt for the first user prompt
system_prompt = "You are a human, this is a friendly conversation between you and another person, you will open the conversation with a greeting. Act friendly and respectful. Make sure to talk like a human."

# Initialize the conversation with the system prompt
response = ollama.chat(model='llama2-uncensored', messages=[
    {
        'role': 'system',
        'content': system_prompt,
    }
])

# Start the conversation loop
while True:
    # Print the system's response
    print(response['message']['content'])
#    speak(response['message']['content'])
    
    # Get user input
    user_input = input("You: ")
    
    # Add user input to the conversation history
    conversation_history.append({
        'role': 'user',
        'content': user_input,
    })
    
    # Send the conversation history to the model and get the response
    response = ollama.chat(model='llama2-uncensored', messages=conversation_history)
