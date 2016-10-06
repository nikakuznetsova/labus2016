import random
import matplotlib.pyplot as plt

random.seed(0)
n = 100000
values = [random.normalvariate(0, 1) for i in range(n)]
plt.hist(values, bins=100)
plt.show()