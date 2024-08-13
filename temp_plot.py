import matplotlib.pyplot as plt

# Data
temperatures = [0.2, 0.8, 1.2, 1.6]
temperatures_gemini_pro = [0.2, 0.8]
temperatures_gemini_15_pro = [0.2, 0.8, 1.2, 1.6]
gpt_3_5_turbo_bert = [1.13, 1.12, 1.12, 1.16]
gpt_3_5_turbo_ngrams = [9.79, 21.65, 25.08, 29.90]
gpt_3_5_turbo_self_bleu = [0.60, 0.52, 0.49, 0.46]

gpt_4o_bert = [1.06, 1.10, 1.18, 1.49]
gpt_4o_ngrams = [12.80, 22.62, 28.88, 80.88]
gpt_4o_self_bleu = [0.60, 0.51, 0.45, 0.14]

gemini_pro_bert = [1.10, 1.83]
gemini_pro_ngrams = [15.45, 38.67]
gemini_pro_self_bleu = [0.56, 0.30]

gemini_15_pro_bert = [1.06, 1.12, 1.13, 1.15]
gemini_15_pro_ngrams = [13.00, 25.16, 30.95, 31.69]
gemini_15_pro_self_bleu = [0.52, 0.42, 0.38, 0.37]

# Plot
plt.figure(figsize=(12, 6))

#plt.plot(temperatures, gpt_3_5_turbo_bert, label='GPT-3.5', marker='o')
#plt.plot(temperatures, gpt_3_5_turbo_ngrams, label='GPT-3.5 Turbo', marker='o')
plt.plot(temperatures, gpt_3_5_turbo_self_bleu, label='GPT-3.5 Turbo', marker='o')

#plt.plot(temperatures, gpt_4o_bert, label='GPT-4o', marker='o')
#plt.plot(temperatures, gpt_4o_ngrams, label='GPT-4o', marker='o')
plt.plot(temperatures, gpt_4o_self_bleu, label='GPT-4o', marker='o')

#plt.plot(temperatures_gemini_pro, gemini_pro_bert, label='Gemini Pro', marker='o')
#plt.plot(temperatures_gemini_pro, gemini_pro_ngrams, label='Gemini Pro', marker='o')
plt.plot(temperatures_gemini_pro, gemini_pro_self_bleu, label='Gemini Pro', marker='o')

#plt.plot(temperatures_gemini_15_pro, gemini_15_pro_bert, label='Gemini 1.5 Pro', marker='o')
#plt.plot(temperatures_gemini_15_pro, gemini_15_pro_ngrams, label='Gemini 1.5 Pro', marker='o')
plt.plot(temperatures_gemini_15_pro, gemini_15_pro_self_bleu, label='Gemini 1.5 Pro', marker='o')

# Labels and title
plt.xlabel('Temperature')
plt.ylabel('Scores')
plt.title('Self-BLEU Score for Models at Different Temperatures')
plt.legend()
plt.grid(True)

# Show plot
plt.show()