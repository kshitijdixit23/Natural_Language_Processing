paragraph="The majestic old oak tree stands at the center of the quiet park, casting a deep and cool shadow over the soft green grass below. Every single day, many people from the busy neighborhood walk past its massive trunk, but only a few ever stop to truly appreciate its ancient beauty. Small brown birds build their tiny nests high up in the thick branches, while restless squirrels constantly run up and down the rough bark in search of food. When a gentle breeze blows through the valley, the leaves softly rustle, creating a peaceful melody that calms everyone nearby."
import nltk
from nltk.stem import SnowballStemmer
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#tokenize -> stemming -> stopwords 
tokenizer=sent_tokenize(paragraph)
stemmer=SnowballStemmer('english')

for i in range (len(tokenizer)):
    words=word_tokenize(tokenizer[i])
    words=[stemmer.stem(word) for word in words if word.lower() not in set(stopwords.words("english"))]
    tokenizer[i]= " ".join(words)

print(tokenizer)


