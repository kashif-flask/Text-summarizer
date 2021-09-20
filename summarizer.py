
import gensim
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
import networkx as nx
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.tokenize.punkt import PunktSentenceTokenizer,PunktTrainer
from nltk.tokenize import word_tokenize,sent_tokenize,TreebankWordTokenizer
import math
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string
import re
#nltk.download('all')
punc=string.punctuation
stopwords = nltk.corpus.stopwords.words('english')

def convert_pdf_to_txt(path):
    
    from io import StringIO
    from pdfminer.converter import TextConverter
    from pdfminer.layout import LAParams
    from pdfminer.pdfinterp import PDFResourceManager
    from pdfminer.pdfinterp import PDFPageInterpreter
    from pdfminer.pdfpage import PDFPage
    
    rsrcmgr=PDFResourceManager()
    retstr=StringIO()
    codec='utf-8'
    laparams=LAParams()
    device=TextConverter(rsrcmgr,retstr,codec=codec,laparams=laparams)
    fp=open(path,'rb')
    interpreter=PDFPageInterpreter(rsrcmgr,device)
    password=""
    maxpages=0
    caching=True
    pagenos=set()

    for page in PDFPage.get_pages(fp,pagenos,maxpages=maxpages,password=password,caching=caching,check_extractable=True):
        interpreter.process_page(page)
                                  
    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text


print('\n')

def summarize_pdf(article_text):
    
    trainer=PunktTrainer()
    trainer.train(article_text)
    tok=PunktSentenceTokenizer(trainer.get_params())
    sentence_list = tok.tokenize(article_text)
    sentence_lists=[]
    sent_list=[]

    clean_sent=[]
    for sent in sentence_list:
            tok=TreebankWordTokenizer()
            words=tok.tokenize(sent)
            wordss=[]
            words=[ww.lower() for ww in words]
            sentence_lists.append(" ".join(words))
            for word,tag in pos_tag(words):
                if tag.startswith('NN'):
                    pos='n'
                elif tag.startswith('VB'):
                    pos='v'
                
                elif tag.startswith('RB'):
                    pos='r'
                else:
                    pos='a'
                stem=WordNetLemmatizer()
                w=stem.lemmatize(word,pos)
                if(w not in punc) & bool(re.search("[^\d]",w)):
                    wordss.append(w.lower())
            clean_sent.append(' '.join(wordss))    
            sent_list.append(wordss)
    return sent_list,clean_sent,sentence_lists,sentence_list
            
def model(sent_list,clean_sent,sentence_lists,sentence_list):
    model=KeyedVectors.load("model.bin")   
    sent_vectors=[]
    for i in clean_sent:
        if (len(i)!=0):
            v=sum([model.wv[w] if w in model.wv.vocab else np.zeros((100,)) for w in i.split()])/(len(i.split()))
        else:
            v=np.zeros((100,))
        sent_vectors.append(v)
    sim_mat=np.zeros([len(sentence_lists),len(sentence_lists)])
    for i in range(len(sentence_lists)):
        for j in range(len(sentence_lists)):
            if i!=j:
                sim_mat[i][j]=cosine_similarity(sent_vectors[i].reshape(1,100),sent_vectors[j].reshape(1,100))[0,0]
    nx_graph=nx.from_numpy_array(sim_mat)
    scores=nx.pagerank(nx_graph)
    ranked_sentences=sorted(((scores[i],s) for i,s in enumerate(sentence_lists)),reverse=True)

    summ=[j for i,j in ranked_sentences]
    return summ
"""path="C:/Users/KASHIF AI/Desktop/Text-summarizer-master/legal_doc.pdf"
text=convert_pdf_to_txt(path)
sent_list,clean_sent,sentence_lists,sentence_list= summarize_pdf(text)
summary=model(sent_list,clean_sent,sentence_lists,sentence_list)
print(summary[:10])"""

