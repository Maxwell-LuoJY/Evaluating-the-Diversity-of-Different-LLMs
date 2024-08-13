from openai import OpenAI

num = 10
with open('data\gpt-4o_temp=1.2.txt','a',encoding='utf-8') as f:
    for i in range(100):
        client = OpenAI(
            api_key="",
            base_url="https://api.bianxie.ai/v1"
        )

        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": "Please generate a random one-paragraph essay, using characters in UTF-8 only",
                }
            ],
            temperature=1.2,
            max_tokens=200
        )
        f.write(completion.choices[0].message.content)
        f.write('\n')
        print(num)
        num += 1
f.close()