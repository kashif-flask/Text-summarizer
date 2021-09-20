from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models import KeyedVectors
glove2word2vec('glove.6B.100d.txt','glove.6B.100d.txt.word2vec') #'glove.6B.100d.txt this file need to be downloaded from glove official site' 
model=KeyedVectors.load_word2vec_format('glove.6B.100d.txt.word2vec',binary=False)
model.save("model.bin")
