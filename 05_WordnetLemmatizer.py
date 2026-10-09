from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
words=["running","swimming","jumping","doing","going"]
for word in words:
    print(word +"---->" +lemmatizer.lemmatize(word,pos='v'))