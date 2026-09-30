import re, nltk
import pandas as pd
messages = pd.read_csv('archive\spam.csv', encoding='latin-1')
messages = messages[['v1', 'v2']]
messages.columns = ['label', 'message']

# Data Cleaning and Preprocessing - Bag of Words
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
ps=PorterStemmer()
corpus=[]
for i in range(0,len(messages)):
    review = re.sub('[^a-zA-Z]', ' ', messages['message'][i])

    review=review.lower()
    review=review.split()
    review=[ps.stem(word)for word in review if not word in stopwords.words('english')] 
    review= ' '.join(review)
    corpus.append(review)
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=2500)
X = cv.fit_transform(corpus).toarray()
print(X)
