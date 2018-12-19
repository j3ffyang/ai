# https://www.udemy.com/introduction-to-data-science-using-python/learn/

# import urllib.request 
import requests

link= "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# f= urllib.request.urlopen(link)
f= requests.get(link)

print(f.text)
