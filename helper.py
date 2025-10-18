import numpy as np
import pandas as pd
import re
import string
import pickle

#Load the model
with open('static/model/svc_model.pkl', 'rb') as f:
    model = pickle.load(f)

#Load the vocabulary
vocab = pd.read_csv("static/model/vocabulary.txt", header = None)
tokens = vocab[0].tolist()

#Load stop word file
with open('static/model/corpora/stopwords/english', 'r') as file:
    sw = file.read().splitlines()

#Remove punctuation function
def remove_punctuation(text):
    for pun in string.punctuation:
        text = text.replace(pun, '')
    return text

from nltk.stem import PorterStemmer
ps = PorterStemmer()

def text_preprocessing(text):
    data = pd.DataFrame([text], columns=["tweet"])
    #Covert Uppercase to Lowercase
    data["tweet"] = data["tweet"].apply(lambda x: " ".join(x.lower() for x in x.split()))
    #Remove links
    data["tweet"] = data["tweet"].apply(lambda x: " ".join(re.sub(r'^https?:\/\/.*[\r\n]*', '', x, flags=re.MULTILINE) for x in x.split()))
    #Remove numbers
    data["tweet"] = data["tweet"].str.replace('\d+', '', regex = True)
    #Remove punctuation
    data["tweet"] = data["tweet"].apply(remove_punctuation)
    #Remove stopwords
    data['tweet'] = data["tweet"].apply(lambda x:" ".join(x for x in x.split() if x not in sw))
    #Stemming
    data['tweet'] = data["tweet"].apply(lambda x:" ".join(ps.stem(x) for x in x.split()))

    return data["tweet"]

def vectorizer(ds):
    vectorized_lst = []
    for sen in ds:
        sen_lst = np.zeros(len(tokens))
        for i in range(len(tokens)):
            if tokens[i] in sen.split():
                sen_lst[i] = 1
        vectorized_lst.append(sen_lst)
    vectorized_lst_new = np.asarray(vectorized_lst, dtype=np.float32)
    return vectorized_lst_new

def get_prediction(vectorizered_text):
    prediction = model.predict(vectorizered_text)
    if prediction == 1:
        return 'Negative'
    else:
        return 'Positive'
