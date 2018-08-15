import matplotlib.pyplot as plt

def plot_dirac(location, *args, **kwarge):
    print(args)
    print(kwarge)
    plt.plot([location, location], [0,1], *args, **kwarge)

plot_dirac(2)
plt.hold(True)
plot_dirac(3, linewidth=3)
plot_dirac(-2, 'r--')
plt.axis((-4, 4, 0, 2))
plt.show()