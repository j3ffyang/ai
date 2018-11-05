import pandas as pd
import matplotlib.pyplot as plt

population = pd.read_csv('world-population.csv', index_col=0)
population.plot()
plt.show()

# plot = population.plot(title = 'World Population', lw = 2, colormap = 'jet', marker = '.', markersize=10)
plot = population.plot(title='World Population', lw=2, colormap='jet', marker='.', markersize=10)

plot.set_xlabel("Year")
plot.set_ylabel("Population")

# saving the file
plt.savefig('population.png')
