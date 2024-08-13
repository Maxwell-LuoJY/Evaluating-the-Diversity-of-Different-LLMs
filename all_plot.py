import matplotlib.pyplot as plt
import numpy as np

# Data
models = [
    "Claude Instant 1.2", 
    "Claude 3.5 Sonnet", 
    "GPT-3.5 Turbo", 
    "GPT-4o", 
    "Gemini Pro", 
    "Gemini 1.5 Pro Latest"
]

bert_scores = [1.25, 1.17, 1.16, 1.11, 1.19, 1.13]
ngrams_scores = [184.47, 80.38, 83.31, 68.94, 86.24, 74.92]
simcse_scores = [24.70, 17.17, 12.42, 6.94, 16.14, 14.32]
self_bleu_scores = [0.36, 0.45, 0.45, 0.49, 0.35, 0.41]

# Colors for each model pair
colors = ['#1f77b4', '#1f77b4', '#ff7f0e', '#ff7f0e', '#2ca02c', '#2ca02c']
#colors = ['#1f77b4', '#1f77b4', '#1f77b4', '#1f77b4', '#1f77b4', '#1f77b4']
# Plotting
x = np.arange(len(models))
width = 0.2

fig, ax = plt.subplots(figsize=(14, 6))

#ax.bar(x, bert_scores, width, label='BERT', color=colors)
#ax.bar(x, ngrams_scores, width, label='N-grams', color=colors)
#ax.bar(x, simcse_scores, width, label='Simcse', color=colors)
ax.bar(x, self_bleu_scores, width, label='self-BLEU', color=colors)

#ax.set_ylim(1, 1.5) 

# Labels and title
ax.set_xlabel('Models')
ax.set_ylabel('Scores')
ax.set_title('SimCSE Vendi Score for Different Models')
ax.set_xticks(x)
ax.set_xticklabels(models)
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Show plot
plt.show()