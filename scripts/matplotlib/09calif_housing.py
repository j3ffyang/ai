# https://realpython.com/python-matplotlib-guide/ > search cal_housing

from io import BytesIO
import tarfile
from urllib.request import urlopen
import numpy as np

url= 'http://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.tgz'
b= BytesIO(urlopen(url).read())
fpath= 'CaliforniaHousing/cal_housing.data'

with tarfile.open(mode='r', fileobj=b) as archive:
    housing= np.loadtxt(archive.extractfile(fpath), delimiter=',')

y= housing[:, -1]
pop, age= housing[:, [4, 7]].T 

def add_titlebox(ax, text):
    ax.text(.55, .8, text,
            horizontalalignment='center',
            transform= ax.transAxes,
            bbox= dict(facecolor='while', alpha=0.6),
            fontsize= 12.5)
    return ax 

