# find the avg heights of the male and female students. The col we need are 
# 2nd and 4th, and there's no missing data in these cols so we can use no.loadtxtself.

import numpy as np

fname = 'eg6-a-student-data.txt'
dtype1= np.dtype([('gender', '|S1'), ('height', 'f8')])
a= np.loadtxt(fname, dtype= dtype1, skiprows= 9, usecols= (1, 3))
print(a)

# to find the avg heights of the male students, we only want to index the
# records with the gender field as M, for which we can create a boolean array

m= a['gender'] == b'M'
print(m)
# m has entries that are True or False for each of the 19 valid records
# (one is commented out) according to whether the student is male or female
# So the heights of the male students can be seen
print(a['height'][m])

# therefore, the avg we need are
m_av= a['height'][m].mean()
f_av= a['height'][~m].mean()
# ~m = not m = inverse boolean array of m

print('Male avg: {:.2f} m, Female avg: {:.2f} m'.format(m_av, f_av))
print(m_av, f_av)
