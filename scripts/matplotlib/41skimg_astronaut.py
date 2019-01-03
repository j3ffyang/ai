# https://www.datacamp.com/community/tutorials/matplotlib-3d-volumetric-data

import matplotlib.pyplot as plt
from skimage import data

astronaut = data.astronaut()
ihc = data.immunohistochemistry()
hubble = data.hubble_deep_field()

# Initialize the subplot panels side by side
fig, ax = plt.subplots(nrows=1, ncols=3)

# Show an image in each subplot
ax[0].imshow(astronaut)
ax[0].set_title('Natural image')
ax[1].imshow(ihc)
ax[1].set_title('Microscopy image')
ax[2].imshow(hubble)
ax[2].set_title('Telescope image');

plt.show()
