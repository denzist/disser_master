import matplotlib.pyplot as plt

import matplotlib.ticker as ticker

# loc = ticker.MultipleLocator(base=0.1) # this locator puts ticks at regular intervals
# ax.xaxis.set_major_locator(loc)

free_prob = 0.35
prior_prob = 0.5
occ_prob = 0.7

z = 0.5

d1 = 0.05
d2 = 0.08
d3 = 0.13

x = [0., z - d1, z + d1, z + d2, z + d3, z + 0.3]
y = [free_prob, free_prob, occ_prob, occ_prob, prior_prob, prior_prob]

color = 'k'
plt.xlabel(r'$r_{cell}$' + ', ' + r'$z = 0.5$')
plt.ylabel(r'$p(r_{cell}|z)$')
plt.title('Inverse model of sonar')
plt.plot(x, y, color)
ax = plt.axes()
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.05))
plt.axis([0, z + 0.3, 0.2, 0.8])



plt.grid(True)
plt.show()