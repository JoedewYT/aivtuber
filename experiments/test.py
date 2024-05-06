import ollama
import subprocess

def speak(text):
    subprocess.run(["espeak -en-f4 -p82 -s 190", text])

# Initialize the model
model = ollama.create_model('llama2-uncensored')

# System prompt for the first user prompt
system_prompt = "Start the conversation."

# Send the system prompt to the model and print its response
response = model.send(system_prompt)
print(response['message']['content'])
speak(response['message']['content'])

# Start the conversation loop
while True:
    # Get user input
    user_input = input("You: ")
    
    # Send the user input to the model and print its response
    response = model.send(user_input)
    print(response['message']['content'])
    speak(response['message']['content'])
