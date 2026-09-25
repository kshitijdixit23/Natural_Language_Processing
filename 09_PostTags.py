paragraph="The majestic old oak tree stands at the center of the quiet park, casting a deep and cool shadow over the soft green grass below. Every single day, many people from the busy neighborhood walk past its massive trunk, but only a few ever stop to truly appreciate its ancient beauty. Small brown birds build their tiny nests high up in the thick branches, while restless squirrels constantly run up and down the rough bark in search of food. When a gentle breeze blows through the valley, the leaves softly rustle, creating a peaceful melody that calms everyone nearby."

import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from nltk.tag import PerceptronTagger

tokenizer= sent_tokenize(paragraph)
for i in range(len(tokenizer)):
    words=word_tokenize(tokenizer[i])
    words=[ word for word in words if word.lower() not in set(stopwords.words('english'))]
    pos_tag = nltk.pos_tag(words)
print(pos_tag)



'''
The program is working as follows...
1. It is converting the paragraph into sentence then to words.
2. After "words convertion" it applies "stopwords to those words" by comparing with the english sentences.
3. At last step it prints the "stopwords with their respective "Parts of Speech""
'''