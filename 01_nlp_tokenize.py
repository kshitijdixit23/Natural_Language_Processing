import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import TreebankWordTokenizer
corpus="Fox is a clever animal. Lion is more fierceful."

sent_document= sent_tokenize(corpus) #Function
word_document=word_tokenize(corpus)  #Function

tokanizer=TreebankWordTokenizer()    #Class
print(tokanizer.tokenize(corpus))

for Sentence in sent_document:
    print(Sentence)
for Word in word_document:
    print(Word)

# word_tokanize uses TreeBankWordTokanizer under the hood.                                                           