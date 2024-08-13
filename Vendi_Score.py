from vendi_score import text_utils

model = 'gemini-1.5-pro-latest_temp=1.2'
file = "data\\" + model + '.txt'

def main():
    with open(file, 'r',encoding='utf-8') as f:
        sents = []
        for i in range(100):
            s = f.readline().strip()
            sents.append(s)

        ngram_vs = text_utils.ngram_vendi_score(sents, ns=[1, 2])
        bert_vs = text_utils.embedding_vendi_score(sents, model_path="bert-base-uncased")
        #simcse_vs = text_utils.embedding_vendi_score(sents, model_path="princeton-nlp/unsup-simcse-bert-base-uncased")
        print(f"{model} N-grams: {ngram_vs:.02f}")
        print(f"{model} Bert: {bert_vs:.02f}")
        #print(f"{model} Simcse: {simcse_vs:.02f}")

if __name__ == "__main__":
    main()