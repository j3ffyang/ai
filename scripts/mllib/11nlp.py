# let's tokenize some words 
# from nltk.tokenize import word_tokenize
from nltk import pos_tag, word_tokenize
# nltk.download('punkt')

wt= word_tokenize("I like Mikes course.")
print(wt)

from nltk import sent_tokenize

sentence= "I love ice cream. I also like steak."
st= sent_tokenize(sentence)
print(st)
