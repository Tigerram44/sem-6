from gensim.downloader import load 
def rd(ems)
    pca=PCA(n_compionents=2)
    r =pca.fit_transform(ems)
    return r

def vizualize(words, e):
    plt.figure(figsize=(10,6))
    for i, word in enumerate(words):
        x,y =e[i]
        plt.scatter(x,y,marker='o',color="blue")
        plt.text(x+0.02,y+0.02,word,fontsize=12)
    plt.show()

def gsm(word)
    sw =model.most_similar(word,topn=5)
    for word, s in sw:
        print(word,s)

print("Loading Pre-traned Glov model(50 dimensions)...")
model =load("glove-wiki-gigaword-50")
words =['football','basketball','soccer','tennis','cricket','olympics','hockey','kabaddi','volleyball','shuttle']
ems =[model[word]for word in words]
e=rd(ems)
visualize(words, e)
gsm("match")