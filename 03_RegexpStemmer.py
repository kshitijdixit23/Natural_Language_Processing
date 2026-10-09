from nltk.stem import RegexpStemmer
reg_Stemmer=RegexpStemmer('ing$|e$|s$|able$',min=4)
words=["running","parliament","ablity","disable","mangoes","trees"]
for word in words:
    print(word + "--->"+reg_Stemmer.stem(word))