from openai import OpenAI

client = OpenAI(
    api_key="put your key",
    base_url="https://openrouter.ai/api/v1"
)

response = client.chat.completions.create(
    model="deepseek/deepseek-r1",
    messages=[
        {
            "role": "user",
            "content": "who is Ashfaq vishu?"
        }
    ]
)

print(response.choices[0].message.content)
print(response)




