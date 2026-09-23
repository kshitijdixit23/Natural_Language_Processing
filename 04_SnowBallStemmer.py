from nltk.stem import SnowballStemmer
snow_Stemmer=SnowballStemmer("english")
words=["Singing","Laughing","Goes","Does","Adversly","Protagonist","congratulate"]
for word in words:
    print(word+"---->"+snow_Stemmer.stem(word))