# https://scipython.com/book/chapter-6-numpy/examples/the-stroop-effect/
# in an experiment to investigate the Stroop Effect, a group of students were
# timed reading out 25 randomly ordered color names, first in blank ink and then
# in a color other than the one they name (eg. the word 'red' in blue ink)

import numpy as np

# read in the data from stroop.txt, indetifying missing values and
# replacing them with NaN
data= np.genfromtxt('stroop.txt', skip_header= 1,
                    dtype= [('student', 'u8'), ('gender', 'S1'),
                            ('black', 'f8'), ('colour', 'f8')],
                    delimiter= ',',
                    missing_values= 'X')
nwords= 25

# remove invalie rows from data set
filtered_data= data[np.isfinite(data['black']) & np.isfinite(data['colour'])]

# extract rows by gender (M/F) and word color (black/ color) and nomalize
# to time taken per word
fb= filtered_data['black'][filtered_data['gender']==b'F']/ nwords
mb= filtered_data['black'][filtered_data['gender']==b'M']/ nwords
fc= filtered_data['colour'][filtered_data['gender']==b'F']/ nwords
mc= filtered_data['colour'][filtered_data['gender']==b'M']/ nwords

# produce stat: mean and standard deviation by gender and word color
mu_fb, sig_fb = np.mean(fb), np.std(fb)
mu_fc, sig_fc = np.mean(fc), np.std(fc)
mu_mb, sig_mb = np.mean(mb), np.std(mb)
mu_mc, sig_mc = np.mean(mc), np.std(mc)

print('Mean and (standard deviation) times per word (sec)')
print('gender |    black      |    colour     | difference')
print('   F   | {:4.3f} ({:4.3f}) | {:4.3f} ({:4.3f}) |   {:4.3f}'
                    .format(mu_fb, sig_fb, mu_fc, sig_fc, mu_fc - mu_fb))
print('   M   | {:4.3f} ({:4.3f}) | {:4.3f} ({:4.3f}) |   {:4.3f}'
                    .format(mu_mb, sig_mb, mu_mc, sig_mc, mu_mc - mu_mb))
