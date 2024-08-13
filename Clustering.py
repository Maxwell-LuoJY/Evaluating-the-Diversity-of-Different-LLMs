import numpy as np
import pandas as pd
from ast import literal_eval
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import matplotlib
import matplotlib.pyplot as plt
from openai import OpenAI   

def sumerize(n_clusters, df, rev_per_cluster, colors):
    client = OpenAI(
    api_key="",
    base_url="https://api.bianxieai.com/v1"
    )

    for i in range(n_clusters):
        print(f"Cluster {i} (visualized in {colors[i]}) Theme:", end=" ")

        paragraphs = "\n".join(
            df[df.Cluster == i]
            .paragraph
            .sample(rev_per_cluster, random_state=42)
            .values
        )

        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": f'What do the following paragraphs have in common?\n\nparagraphs:\n"""\n{paragraphs}\n"""\n\nTheme:',
                }
            ]
        )
        print(completion.choices[0].message.content.replace("\n", ""))

        sample_cluster_rows = df[df.Cluster == i].sample(rev_per_cluster, random_state=42)
        print(f"Here are {rev_per_cluster} samples of the paragraphs in this cluster:")
        for j in range(rev_per_cluster):
            print(str(j+1) + '.' + sample_cluster_rows.paragraph.str[:70].values[j])
        print("-" * 100)

datafile_path = "data\gemini-pro.csv"

df = pd.read_csv(datafile_path, encoding='latin-1')
df["embedding"] = df.embedding.apply(literal_eval).apply(np.array)
matrix = np.vstack(df.embedding.values)

n_clusters = 8
colors = ["blue", "orange", "green", "red", "purple", "brown", "pink", "gray"]

kmeans = KMeans(n_clusters=n_clusters, init="k-means++", random_state=42)
kmeans.fit(matrix)
labels = kmeans.labels_
df["Cluster"] = labels

#sumerize(n_clusters=n_clusters, df=df, rev_per_cluster=5, colors=colors)

tsne = TSNE(n_components=2, perplexity=15, random_state=42, init="random", learning_rate=200)
vis_dims2 = tsne.fit_transform(matrix)

x = [x for x, y in vis_dims2]
y = [y for x, y in vis_dims2]

for category, color in enumerate(colors):
    xs = np.array(x)[df.Cluster == category]
    ys = np.array(y)[df.Cluster == category]
    plt.scatter(xs, ys, color=color, alpha=0.3)

    avg_x = xs.mean()
    avg_y = ys.mean()

    plt.scatter(avg_x, avg_y, marker="x", color=color, s=100)
plt.title(f"Clusters identified visualized in language 2d using t-SNE\nNo. of clusters = {n_clusters}")
plt.show()
