import re, nltk
import pandas as pd
messages = pd.read_csv(r'NLP/SPAM OR HAM/archive/spam.csv', encoding='latin-1')
messages = messages[['v1', 'v2']]
messages.columns = ['label', 'message']


# Data Cleaning and Preprocessing - Bag of Words
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
ps=PorterStemmer()
stop_words=stopwords.words('english')
corpus=[]
for i in range(0,len(messages)):
   review = re.sub('[^a-zA-Z]', ' ', messages['message'][i])


   review=review.lower()
   review=review.split()
   review=[ps.stem(word)for word in review if not word in stop_words]
   review= ' '.join(review)
   corpus.append(review)
from sklearn.feature_extraction.text import CountVectorizer
#cv=CountVectorizer(max_features=100,binary=True,ngrams_range(1,1)) # UNIGRAM ONLY
#cv=CountVectorizer(max_features=300,binary=True,ngram_range=(1,2))  # UNIGRAM & BIGRAM
cv=CountVectorizer(max_features=50,binary=True,ngram_range=(2,2))  # BIGRAM & BIGRAM


X = cv.fit_transform(corpus).toarray()
print(X)
print(cv.vocabulary_)