import nltk
import re
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

class Classifier():
    tfidf = TfidfVectorizer(max_features=7000)
    pickle_in = open("blog\static/blog\MODELS\corpus_tweets_train.pickle","rb")
    corpus_tweets_train = pickle.load(pickle_in)
    tfidf.fit_transform(corpus_tweets_train).toarray()
    filename = 'blog\static/blog\MODELS/twitter_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))

    def prepare_corpus(self,tweets):
        corpus_tweets = []
        size = tweets.shape[0]
        ps = PorterStemmer()
        for i in range(0,size):
            tweet = re.sub(pattern='[^a-zA-Z]',repl=' ', string=tweets['tweet'][i])

            tweet = re.sub(pattern='user' , repl='' , string = tweet)

            tweet = tweet.lower()

            words = tweet.split()

            words = [ps.stem(word) for word in words if not word in stopwords.words('english')]

            tweet = ' '.join(words)

            corpus_tweets.append(tweet)
        return corpus_tweets

    def classify(self , test_data):
        test_data = {'tweet' : [test_data]}
        test_data = pd.DataFrame.from_dict(test_data)
        corpus_test = self.prepare_corpus(test_data)
        vectors = self.tfidf.transform(corpus_test).toarray()
        answer = self.loaded_model.predict(vectors)
        return answer[0]
