# ref > https://www.thepythoncode.com/article/download-files-python

from tqdm import tqdm
import time

text = ""
for char in tqdm(["a", "b", "c", "d"]):
    time.sleep(0.25)
    text = text + char

# for i in trange(100):
#    time.sleep(0.01)

pbar = tqdm(["a", "b", "c", "d"])
for char in pbar:
    time.sleep(0.25)
    pbar.set_description("Processing %s" % char)
