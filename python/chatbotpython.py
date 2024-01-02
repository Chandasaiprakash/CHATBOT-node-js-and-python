import openai

openai.api_key = ""

messages = []
system_msg = input("Assistant: What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Assistant: Your new assistant is ready!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print("\n Assistant :" + reply + "\n")
