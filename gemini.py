import requests
import genai
import json


api_key = ''
url = 'https://api.bianxieai.com/v1/chat/completions'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

data = {
    'model': 'gemini-1.5-pro-latest',
    'messages': [{'role': 'user', 'content': 'Please generate a random one-paragraph essay, remenber using characters in UTF-8 only, avoid multibyte sequence'}],
    'temperature': 1.2,
    'max_tokens':200,
}

num = 1
with open('gemini-1.5-pro-latest_temp=1.2.txt', 'a', encoding='utf-8') as f:
    for i in range(10):
        response = requests.post(url, headers=headers, json=data)
        content = response.json()['choices'][0]['message']['content']
        f.write(content)
        f.write('\n')
        print(num)
        num+=1
f.close()