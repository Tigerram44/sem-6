from gensim.downloader import load 
print("Loading Pre-traned Glov model(50 dimensions)...")
model=load("glove-wiki-gigaword-50")
def ewr():
    result=model.most_similar(positive=['queen','man'],negative=['king'],topn=1)
    print("\n king = man + queen =?",result[0][0])
    print("similarity:",result[0][1])

    result=model.most_similar(positive=['paris','italy'],negative=['france'],topn=1)
    print("\n paris = france + italy =?",result[0][0])
    print("similarity:",result[0][1])

    result=model.most_similar(positive=['tiger'],topn=5)
    print("\n TOP 5 WORDS SIMILAR TO 'Tiger':'")
    for word, similarity in result:
        print(word, similarity)
ewr()   