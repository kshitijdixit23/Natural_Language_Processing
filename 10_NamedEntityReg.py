import nltk


sentence="The Eiffel Tower was built from 1887 to 1889 by a Fench Engineer Gustave Eiffel, whose company specialized in uilding metal frameworks and structures."
word=nltk.word_tokenize(sentence)
print(word)
posTag = nltk.pos_tag(word)
print(word)
print(nltk.ne_chunk(posTag))
