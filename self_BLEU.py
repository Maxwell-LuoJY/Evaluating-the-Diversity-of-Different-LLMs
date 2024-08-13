import numpy as np
import copy
from nltk.translate.bleu_score import sentence_bleu


def get_bleu_score(reference_sentence, remaining_sentences):
    lst = []
    for candidate_sentence in remaining_sentences:
        bleu = sentence_bleu([reference_sentence], candidate_sentence)
        lst.append(bleu)
    return lst


def calculate_selfBleu(sentences):
    num = 1
    bleu_scores = []
    for i in sentences:
        sentences_copy = copy.deepcopy(sentences)
        sentences_copy.remove(i)
        print(num)
        bleu = get_bleu_score(i,sentences_copy)
        bleu_scores.extend(bleu)
        num += 1
    
    return np.mean(bleu_scores)

model = 'gemini-1.5-pro-latest_temp=1.2'
file = "data\\" + model + '.txt'
with open(file,'r', encoding='utf-8') as f:
    sentences = []
    for i in range(100):
        s = f.readline().strip()
        sentences.append(s)
    
    print(model)
    print(f"{calculate_selfBleu(sentences):.02f}")
f.close()