import requests


api_key = ''
url = 'https://api.bianxieai.com/v1/chat/completions'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

data = {
    'model': 'claude-2.0',
    'messages': [{'role': 'user', 'content': 'Please generate a random one-paragraph essay, give it directly without "Here is a randomized one-paragraph essay", remenber using characters in UTF-8 only.'}],
    'temperature': 0.2,
    'max_tokens':200,
}

with open('claude-2.0_temp=0.2.txt', 'a', encoding='utf-8') as f:
    num = 1
    for i in range(10):
        response = requests.post(url, headers=headers, json=data)
        js = response.json()
        print(js)
        content = js['choices'][0]['message']['content']
        f.write(content)
        f.write('\n')
        print(num)
        num+=1
f.close()
