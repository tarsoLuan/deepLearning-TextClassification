import nltk
import numpy as np
from nltk.stem.snowball import SnowballStemmer

# nltk.download('punkt')
stemmer = SnowballStemmer("portuguese")

def tokenize(sentence):
    return nltk.word_tokenize(sentence ,language='portuguese')

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenize_sentence, all_words):
    tokenize_sentence = [stem(w) for w in tokenize_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)

    for idx, w in enumerate(all_words):
        if w in tokenize_sentence:
            bag[idx] = '1.0'
    
    return bag
