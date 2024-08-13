import requests
import pandas as pd

def get_embeddings(text):
    api_key = ''
    url = 'https://api.bianxieai.com/v1/embeddings'
    data = {
        "input": text,
        "model": "text-embedding-ada-002",
        "encoding_format": "float"
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json=data)
    js = response.json()
    return js['data'][0]['embedding']

def txt_to_csv(model_name):
    with open(model_name + '.txt','r') as f_in:
        for i in range(700):
            l = []
            tmp = []
            s = f_in.readline().strip('\n')
            tmp.append(s)
            tmp.append(get_embeddings(s))
            l.append(tmp)
            df = pd.DataFrame(l,columns=['Paragraph','Embeddings'])
            df.to_csv(model_name + ".csv", mode='a', index=False, header=False)
            print(i+1)
    f_in.close()

txt_to_csv('claude-instant-1.2')