import re,nltk
import pandas as pd
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
messages = pd.read_csv(r'NLP/SPAM OR HAM/archive/spam.csv', encoding='latin-1')
messages = messages[['v1', 'v2']]
messages.columns = ['label', 'message']
wordlemmatizer = WordNetLemmatizer()
stop_words= stopwords.words("english")

corpus=[]
for i in range (0,len(messages)):
    review = re.sub('[^a-z A-Z]', " ", messages['message'][i])
    review = review.lower()
    review = review.split()
    review = [wordlemmatizer.lemmatize(word) for word in review if not word in stop_words]
    review =' '.join(review)
    corpus.append(review)

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf=TfidfVectorizer(max_features=10,ngram_range=(2,2))
X= tfidf.fit_transform(corpus).toarray()
print(tfidf.vocabulary_)