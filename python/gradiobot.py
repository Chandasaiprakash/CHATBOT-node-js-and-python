import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a software developer"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "WTF ChatBot")

demo.launch(share=True)