import ollama
import subprocess

def speak(text):
    subprocess.run(["espeak", "-ven+f3", "-p82", "-s190", text])

# System prompt for the first user prompt
system_prompt = "Respond to the user. and be friendly"

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
    speak(response['message']['content'])
    
    # Get user input
    user_input = input("You: ")
    
    # Send user input to the model and get the response
    response = ollama.chat(model='llama2-uncensored', messages=[
        {
            'role': 'user',
            'content': user_input,
        }
    ])

