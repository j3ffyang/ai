# ref > https://www.thepythoncode.com/article/download-files-python

from tqdm import tqdm
import time

text = ""
for char in tqdm(["a", "b", "c", "d"]):
    time.sleep(0.25)
    text = text + char
