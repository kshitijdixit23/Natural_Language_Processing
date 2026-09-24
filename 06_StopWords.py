paragraph= "The majestic old oak tree stands at the center of the quiet park, casting a deep and cool shadow over the soft green grass below. Every single day, many people from the busy neighborhood walk past its massive trunk, but only a few ever stop to truly appreciate its ancient beauty. Small brown birds build their tiny nests high up in the thick branches, while restless squirrels constantly run up and down the rough bark in search of food. When a gentle breeze blows through the valley, the leaves softly rustle, creating a peaceful melody that calms everyone nearby."


#implement stop words from "Stemming"

import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize


#tokenization
sentence = nltk.sent_tokenize(paragraph)
stemmer=PorterStemmer()


#Apply stopwords -> Apply Filter -> Apply Stemming
for i in range (len(sentence)):
   words = nltk.word_tokenize(sentence[i])  #we will get list of words "inside" the sentences.


   #now we have to see that word falls in the category of "Stopwords" or not if it does then apply "Stemming".
   words =  [stemmer.stem(word) for word in words if word not in set(stopwords.words("english"))] # If word is not found then move forward otherwise catch it & hrow it.
   sentence[i]= " ".join(words) # converting all the "list" words back into sentences.


#stopwords in ENGLISH
#print(stopwords.words("english"))
