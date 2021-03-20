def azureml_main(dataset, stop_words):
  import os
  import pandas as pd
  import string
  import nltk
  from nltk.stem.porter import PorterStemmer
 dataset.columns = ['sentiment', 'tweets']
 tweets = dataset['tweets'].tolist()
 sp = string.punctuation
 tweets = list(map(lambda t: ''.join(["" if c.isdigit() else c for c     in t]), tweets))
 tweets = list(map(lambda t: ''.join(["" if c in sp else c for c in t]), tweets))
 tweets = list(map(str.lower, tweets))
 porter_stemmer = PorterStemmer()
 temp = [tweet.split() for tweet in tweets] ## Split tweets into tokens
 tweets = list(map(lambda t: ' '.join([porter_stemmer.stem(word) for   word in t.split()]), tweets))
 stop_words = [w for w in stop_words.words if w in  stop_words.words.unique() ]
 tweets = list(map(lambda t: ' '.join([word for word in t.split() if word not in set(stop_words)]), tweets))
 dataset['sentiment'] = [1 if s == 4 else -1 for s in   dataset['sentiment']]
 return dataset,
