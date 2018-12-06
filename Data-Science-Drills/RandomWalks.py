# Numpy is imported, seed is set
import numpy as np
walks = []
dist = []
simulations = 2000

for i in range(simulations):
    # Initialization
    random_walk = [0]

    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        random_walk.append(step)
    walks.append(random_walk)
    dist.append(walks[-1][-1])

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Plot random_walk
for i in walks:
    plt.plot(i)
# Show the plot
plt.show()
plt.clf()

plt.hist(dist, bins=30)
#To change y ticks to percentage of the total random walks
plt.gca().set_yticklabels([f'{x/simulations*100:.2f}%' for x in plt.gca().get_yticks()])
print(dist)
plt.show()
