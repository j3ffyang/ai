# https://www.udemy.com/the-top-5-machine-learning-libraries-in-python/
from nltk.tokenize import sent_tokenize

para= "Thanks for taking my courses. You guys rock. Learning is fun. Please take the rest of my courses."
print(sent_tokenize(para))

from nltk.tokenize import word_tokenize

para= "Thanks for taking my courses. You guys rock. Learning is fun. Please take the rest of my courses."
print(word_tokenize(para))

from nltk.corpus import stopwords
import nltk 
nltk.download('stopwords')
print(stopwords.words("english"))
