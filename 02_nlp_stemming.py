from nltk.stem import PorterStemmer

stemming=PorterStemmer()

words=["reading","writing","stuyding","racing","notably","brave"]
print(stemming.stem("congratulate"))

for word in words:
    print(word+"----->"+stemming.stem(word))