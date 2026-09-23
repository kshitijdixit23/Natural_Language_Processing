paragraph="The old lighthouse stood as a silent sentinel on the jagged cliffs, braving decades of fierce Atlantic storms. Every evening, its brilliant beacon sliced through the dense coastal fog, offering a reliable guiding light to weary sailors navigating the treacherous, reef-filled waters below. Inside, the smooth stone walls held generations of secrets, from the quiet, isolated lives of the early keepers to the historic shipwrecks they desperately tried to prevent. Today, automated technology has completely replaced the human touch, yet the majestic structure still commands a powerful presence over the coastline. Visitors from all over the world travel down the winding, gravel path just to touch its weathered base and listen closely to the crashing waves. They often wonder about the solitary lives lived within its circular belly, imagining a time when a single flickering flame was the only thing standing between an approaching ship and absolute destruction on the rocks."
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
#print(stopwords.words('english')) # to print normal english stopwords from the NLTK 
print(sent_tokenize(paragraph))

#Apply stopwords, then Filter, then Stemming