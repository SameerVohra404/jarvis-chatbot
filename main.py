from openai import OpenAI

API_KEY = "INSERT_YOUR_API_KEY_HERE"

client = OpenAI(
    api_key=API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

messages = []

def completion(message):
    global messages

    messages.append({
        "role": "user",
        "content": message
    })

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="deepseek/deepseek-r1:free"
    )

    ai_message = chat_completion.choices[0].message["content"]
    print("\nAI:", ai_message, "\n")

if __name__ == "__main__":
    user_message = input("Hi, I am Jarvis. How can I help you? ")
    completion(user_message)
