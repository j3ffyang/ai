# ref > https://www.thepythoncode.com/article/access-wikipedia-python

import wikipedia

# print the summary of what python is 
print(wikipedia.summary("Python Programming Language"))

result = wikipedia.search("Neural network")
print(result)

page = wikipedia.page(result[0])
print(page)

title = page.title
categories = page.categories
content = page.content
links = page.links 
references = page.references
summary = page.summary

# print info 
print("Page content:\n", content, "\n")
print("Page title:", title, "\n")
print("Categories:", categories, "\n")
print("Links:", links, "\n")
print("References:", references, "\n")
print("Summary:", summary, "\n")
