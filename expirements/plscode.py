import ollama

# Define the user prompt and system prompt
user_prompt = "what is a man, a man without love"

# Call the chat function with both prompts
response = ollama.chat(model='llama2-uncensored', messages=[
    {
        'role': 'user',
        'content': user_prompt,
    },
])

# Print the response from the model
print(response['message']['content'])

